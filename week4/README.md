# Panduan Proyek (Week 4 Starter App)
Ini adalah aplikasi Developer's Command Center menggunakan FastAPI (Backend) dan HTML/JS statis (Frontend).

## Struktur Direktori
- `backend/`: Berisi aplikasi FastAPI (`main.py`, `routers`, `models`, dll).
- `frontend/`: File UI statis.
- `data/`: Folder untuk database SQLite (`seed.sql`).
- `docs/`: Dokumen tugas.

## Aturan Utama untuk Claude (AI):
1. **Testing:** Selalu jalankan `pytest backend/tests/` setelah melakukan perubahan kode. Jangan gunakan `make test` jika command `make` tidak tersedia di Windows, gunakan langsung `pytest`.
2. **Keamanan:** Jangan pernah menghapus file database `.db` secara permanen tanpa persetujuan pengguna.
3. **Gaya Penulisan:** Gunakan bahasa Python yang modern (Python 3.10+) dan pastikan menggunakan format JSON yang valid saat membuat endpoint API baru.
4. **Alur Kerja (Workflow):** Jika diminta menambahkan fitur baru, ikuti urutan ini: Tulis Test -> Tulis Kode -> Jalankan Test -> Perbaiki jika gagal.