from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .db import init_db
from .routers import action_items, notes

BASE_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = BASE_DIR / "frontend"

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting API Initializing SQLite Database...")
    init_db()
    yield
    print("Shutting down API...")

app = FastAPI(
    title="Action Item Extractor API",
    description="A smart tool to extract tasks from notes using Regular Expressions and Local LLM (Ollama).",
    version="1.0.0",
    lifespan=lifespan
)

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def index() -> str:
    html_path = FRONTEND_DIR / "index.html"
    return html_path.read_text(encoding="utf-8")

app.include_router(notes.router)
app.include_router(action_items.router)