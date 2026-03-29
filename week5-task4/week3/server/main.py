import os
import httpx
from mcp.server.fastmcp import FastMCP

# 1. Inisialisasi Server MCP
mcp = FastMCP("TMDB_Movie_Server")

# Mengambil Token dari Environment Variable (Keamanan)
TMDB_TOKEN = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_headers():
    return {
        "Authorization": f"Bearer {TMDB_TOKEN}",
        "accept": "application/json"
    }

# TOOL 1 Search Movies
@mcp.tool()
async def search_movies(query: str) -> str:
    """Mencari film berdasarkan judul (keyword). Mengembalikan daftar film beserta ID-nya."""
    if not TMDB_TOKEN:
        return "Error: TMDB_API_KEY belum di-set di environment variables."
    
    url = f"{BASE_URL}/search/movie"
    params = {"query": query, "language": "en-US", "page": 1}
    
    async with httpx.AsyncClient() as client:
        try:
            # Menggunakan timeout 10 detik sebagai praktik ketahanan (resilience)
            response = await client.get(url, headers=get_headers(), params=params, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            
            results = data.get("results", [])
            if not results:
                return f"Tidak ditemukan film dengan kata kunci: '{query}'"
            
            # Memformat hasil agar mudah dibaca oleh AI (hanya ambil 5 teratas)
            output = f"Ditemukan {len(results)} hasil untuk '{query}':\n\n"
            for movie in results[:5]: 
                output += f"- {movie['title']} (ID: {movie['id']})\n  Rilis: {movie.get('release_date', 'N/A')} | Rating: {movie.get('vote_average', 'N/A')}/10\n  Overview: {movie.get('overview', '')[:100]}...\n\n"
            return output
        
        except httpx.HTTPStatusError as e:
            return f"API Error: TMDB merespons dengan status {e.response.status_code}"
        except Exception as e:
            return f"Terjadi kesalahan saat menghubungi API TMDB: {str(e)}"

# TOOL 2 Get Movie Details
@mcp.tool()
async def get_movie_details(movie_id: int) -> str:
    """Mengambil detail spesifik dari sebuah film menggunakan movie_id (ID TMDB)."""
    if not TMDB_TOKEN:
        return "Error: TMDB_API_KEY belum di-set di environment variables."
    
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"language": "en-US"}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=get_headers(), params=params, timeout=10.0)
            if response.status_code == 404:
                return f"Film dengan ID {movie_id} tidak ditemukan di database TMDB."
            response.raise_for_status()
            movie = response.json()
            
            genres = ", ".join([g["name"] for g in movie.get("genres", [])])
            
            output = f"🎥 Detail Film: {movie.get('title')}\n"
            output += f"Tagline: {movie.get('tagline', '-')}\n"
            output += f"Genre: {genres}\n"
            output += f"Durasi: {movie.get('runtime', 0)} menit\n"
            output += f"Status: {movie.get('status', 'Unknown')}\n"
            output += f"Rating: {movie.get('vote_average')}/10 (dari {movie.get('vote_count')} suara)\n\n"
            output += f"Sinopsis:\n{movie.get('overview')}"
            
            return output
            
        except httpx.HTTPStatusError as e:
            return f"API Error: TMDB merespons dengan status {e.response.status_code}"
        except Exception as e:
            return f"Terjadi kesalahan saat menghubungi API TMDB: {str(e)}"

if __name__ == "__main__":
    # Menjalankan server dalam mode STDIO (Standar untuk Claude Desktop / Cursor)
    mcp.run(transport='stdio')