# Week 3: TMDB Movie MCP Server

This is a local Model Context Protocol (MCP) server that wraps the external **The Movie Database (TMDB) API**. It runs over STDIO transport and allows any MCP-compatible AI client to search for movies and retrieve detailed movie information.

## Features (MCP Tools)
This server exposes the following tools:
1. `search_movies`: Search for movies by a keyword/title. Returns a list of matching movies, their release dates, ratings, and TMDB IDs.
2. `get_movie_details`: Retrieves comprehensive details for a specific movie using its TMDB ID (includes genres, runtime, status, and full overview).

## Resilience & Security
- **Authentication:** Uses API Key authorization via Bearer token (aligned with best practices). The token is never hardcoded and is injected via environment variables.
- **Resilience:** Implements a 10-second timeout for all HTTP requests to prevent hanging. Includes graceful error handling for HTTP failures (e.g., `raise_for_status()`) and empty search results.

## Setup & Run Instructions

### Prerequisites
- Python 3.10+
- [Poetry](https://python-poetry.org/)
- A free API Read Access Token from [TMDB](https://www.themoviedb.org/settings/api).

### Installation
Navigate to the project root and install the dependencies:
```bash
poetry add mcp httpx