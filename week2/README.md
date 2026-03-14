# Action Item Extractor API

A modern FastAPI project for extracting actionable tasks from free-form notes using both regular expressions and local LLMs (Ollama). Built for rapid prototyping, learning, and practical automation.

---

## Overview

This app converts notes into structured action items, supporting:
- **Regex-based extraction** for bullet points, checkboxes, and keywords
- **LLM-based extraction** using Ollama for advanced task detection
- **SQLite** for persistent storage of notes and action items
- **REST API** for integration and automation
- **Frontend** served via FastAPI static files

---

## Setup & Run Instructions

### 1. Environment Setup
- Python 3.10+ recommended
- Install dependencies:

```bash
poetry install
```

### 2. Start the API Server

```bash
poetry run uvicorn week2.app.main:app --reload
```

- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the frontend
- API docs available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### Notes
- `GET /notes` — List all notes
- `POST /notes` — Create a new note `{ content: str }`
- `GET /notes/{note_id}` — Retrieve a single note

### Action Items
- `POST /action-items/extract` — Extract action items from text (regex)
  - Payload: `{ text: str, save_note?: bool }`
- `POST /action-items/extract-llm` — Extract action items using LLM (Ollama)
  - Payload: `{ text: str, save_note?: bool }`
- `GET /action-items` — List all action items
- `POST /action-items/{action_item_id}/done` — Mark action item as done

---

## Pytest Instructions

- Run all tests:

```bash
pytest week2/tests/
```

- Tests cover:
  - Regex extraction logic
  - LLM extraction (mocked)
  - Database operations

---

## Project Structure

```
week2/
  app/
    main.py         # FastAPI app entry point
    db.py           # SQLite database logic
    routers/
      action_items.py
      notes.py
    services/
      extract.py    # Extraction logic (regex & LLM)
  tests/
    test_extract.py # Pytest unit tests
  frontend/
    index.html      # Simple UI
```

---

## Credits

- Built for Stanford CS146S: Modern Software Development
- Author: Abdurrahman Gilang Harjuna

---

## License

MIT License
