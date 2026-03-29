# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Abdurrahman Gilang Harjuna \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature
Prompt: 
```text
I need to implement the `extract_action_items_llm(notes: str) -> list[str]` function in `week2/app/services/extract.py`. Please use the official `ollama` Python client to send the `notes` to a local model (e.g., 'llama3.1:8b' or 'mistral-nemo'). Crucially, enforce Structured Outputs so the model strictly returns a JSON array of strings representing the action items. Do not include any markdown formatting or extra prose in the response, just the raw JSON list.
``` 

Generated Code Snippets:
File: week2/app/services/extract.py
Lines: (Di bagian paling bawah file, sekitar baris 65 - 105)
Added `ActionItemsSchema` class using Pydantic.
Added `extract_action_items_llm()` function implementing the Ollama chat call with structured JSON formatting and fallback logic.

### Exercise 2: Add Unit Tests
Prompt: 
```text
Please write robust unit tests for the new `extract_action_items_llm` function inside `week2/tests/test_extract.py`. The tests should cover various edge cases, including: standard bulleted lists, keyword-prefixed lines (like 'todo:' or 'action:'), imperative sentences hidden in paragraphs, and completely empty or non-actionable inputs. Use `pytest` and mock the `chat` function from `ollama` so the tests run quickly without needing the actual LLM running locally.
``` 

Generated Code Snippets:
File: week2/tests/test_extract.py
Lines: (Di bagian paling bawah file)
Added multiple test functions using `pytest` and `unittest.mock.patch` to simulate LLM JSON responses:
- `test_extract_action_items_llm_bullet_lists`
- `test_extract_action_items_llm_keywords`
- `test_extract_action_items_llm_empty_input`

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```text
Please refactor `week2/app/main.py` to meet modern FastAPI standards. Specifically, fix the app lifecycle by removing the global `init_db()` call and replacing it with an `@asynccontextmanager` lifespan function. Also, clean up the configuration by centralizing the directory path definitions (for the frontend and static files) at the top of the file to avoid repetition. Add proper metadata to the FastAPI instance.
``` 

Generated/Modified Code Snippets:
File: week2/app/main.py
Lines: Entire file replaced.
- Implemented `lifespan` context manager for safe `init_db()` execution.
- Centralized `BASE_DIR` and `FRONTEND_DIR` path definitions.
- Added API metadata (title, description, version) to the `FastAPI()` instance.


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```text
I need to expose the LLM extraction feature and a way to list all notes.
1. In `week2/app/routers/action_items.py`, create a new POST endpoint `/api/extract-llm` that receives a `NoteRequest` and returns a list of action items using the `extract_action_items_llm` function.
2. In `week2/app/routers/notes.py`, create a new GET endpoint `/api/notes` that retrieves all notes from the database.
3. Update the frontend (`week2/frontend/index.html` or the relevant JS file) to include two new buttons: "Extract LLM" (calling `/api/extract-llm`) and "List Notes" (calling `/api/notes` and displaying the results).
``` 

Generated Code Snippets:
File: week2/app/routers/action_items.py
Lines: (At the bottom of the file)
Added `@router.post("/extract-llm")` endpoint.

File: week2/app/routers/notes.py
Lines: (At the bottom of the file)
Added `@router.get("/")` endpoint to retrieve all notes.

File: week2/frontend/index.html
Lines: (Inside the form and results area)
Added "Extract LLM" and "List Notes" buttons, along with their corresponding JavaScript event listeners to handle API calls and DOM updates.


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 