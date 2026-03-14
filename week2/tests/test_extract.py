import os
import pytest
from unittest.mock import patch, MagicMock

from ..app.services.extract import extract_action_items, extract_action_items_llm

def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items

# TODO 2: Unit Tests for LLM Extraction
@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_bullet_lists(mock_chat):
    # simulasi balasan dari ollama
    mock_response = MagicMock()
    mock_response.message.content = '{"items": ["Review PR", "Update documentation"]}'
    mock_chat.return_value = mock_response

    # exsekusi fungsi ysng dibuat tadi
    text = "Notes:\n- Review PR\n- Update documentation"
    items = extract_action_items_llm(text)

    # validasi
    assert len(items) == 2
    assert "Review PR" in items
    assert "Update documentation" in items
    mock_chat.assert_called_once() # memanggil LLM

@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_keywords(mock_chat):
    mock_response = MagicMock()
    mock_response.message.content = '{"items": ["Fix login bug", "Email client"]}'
    mock_chat.return_value = mock_response

    text = "TODO: Fix login bug\nACTION: Email client\nJust a normal sentence."
    items = extract_action_items_llm(text)

    assert len(items) == 2
    assert "Fix login bug" in items

@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_empty_input(mock_chat):
    # fungsi harus langsung mengembalikan list kosong tanpa panggil LLM jika imputannya kososng
    text = "   \n  "
    items = extract_action_items_llm(text)
    
    assert items == []
    mock_chat.assert_not_called()

@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_fallback_on_error(mock_chat):
    # simulasi otomatis fallback ke fungsi regex jika ollama error atau mati
    mock_chat.side_effect = Exception("Ollama connection refused")
    
    text = "- [ ] This is a fallback test"
    items = extract_action_items_llm(text)
    
    assert "This is a fallback test" in items