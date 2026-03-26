# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _create(client, description: str) -> dict:
    """Create an action item and return its data dict."""
    r = client.post("/action-items/", json={"description": description})
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["ok"] is True
    return body["data"]


# ---------------------------------------------------------------------------
# Existing behaviour (updated for envelope format)
# ---------------------------------------------------------------------------

def test_create_and_complete_action_item(client):
    item = _create(client, "Ship it")
    assert item["completed"] is False

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["completed"] is True

    r = client.get("/action-items/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) == 1


# ---------------------------------------------------------------------------
# GET /action-items?completed= filter
# ---------------------------------------------------------------------------

def test_list_items_no_filter_returns_all(client):
    _create(client, "Task A")
    _create(client, "Task B")

    r = client.get("/action-items/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) == 2


def test_list_items_filter_by_completed(client):
    a = _create(client, "Task A")
    b = _create(client, "Task B")
    _create(client, "Task C")

    # complete A and B
    client.put(f"/action-items/{a['id']}/complete")
    client.put(f"/action-items/{b['id']}/complete")

    r = client.get("/action-items/?completed=true")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) == 2
    assert all(item["completed"] for item in body["data"])


def test_list_items_filter_by_incomplete(client):
    a = _create(client, "Task A")
    _create(client, "Task B")

    client.put(f"/action-items/{a['id']}/complete")

    r = client.get("/action-items/?completed=false")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) == 1
    assert body["data"][0]["completed"] is False


# ---------------------------------------------------------------------------
# POST /action-items/bulk-complete
# ---------------------------------------------------------------------------

def test_bulk_complete_marks_all_completed(client):
    a = _create(client, "Task A")
    b = _create(client, "Task B")
    c = _create(client, "Task C")

    r = client.post("/action-items/bulk-complete", json={"ids": [a["id"], b["id"]]})
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) == 2
    assert all(item["completed"] for item in body["data"])

    # third item must remain incomplete
    r = client.get("/action-items/?completed=false")
    incomplete = r.json()["data"]
    assert len(incomplete) == 1
    assert incomplete[0]["id"] == c["id"]


def test_bulk_complete_idempotent(client):
    """Completing already-completed items should succeed without error."""
    a = _create(client, "Task A")
    b = _create(client, "Task B")

    client.post("/action-items/bulk-complete", json={"ids": [a["id"], b["id"]]})

    r = client.post("/action-items/bulk-complete", json={"ids": [a["id"], b["id"]]})
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert all(item["completed"] for item in body["data"])


def test_bulk_complete_not_found_returns_error_envelope(client):
    """A missing ID must return 404 with error envelope; valid items stay incomplete."""
    a = _create(client, "Task A")

    r = client.post("/action-items/bulk-complete", json={"ids": [a["id"], 9999]})
    assert r.status_code == 404
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "NOT_FOUND"
    assert "9999" in body["error"]["message"]

    # Task A must NOT have been marked complete (transactional safety)
    r = client.get("/action-items/?completed=false")
    ids = [item["id"] for item in r.json()["data"]]
    assert a["id"] in ids


# ---------------------------------------------------------------------------
# Error cases for existing endpoints
# ---------------------------------------------------------------------------

def test_complete_item_not_found_returns_error_envelope(client):
    r = client.put("/action-items/9999/complete")
    assert r.status_code == 404
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "NOT_FOUND"
