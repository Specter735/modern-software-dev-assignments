# /tes-kode
**Description:** Menjalankan unit tests (pytest) untuk backend dan merangkum hasilnya.

**Intent:** 1. Jalankan perintah terminal: `pytest backend/tests/ -q --maxfail=1`
2. Jika ada tes yang gagal (FAILED), baca log error-nya, dan berikan saya 3 poin singkat tentang file mana yang rusak dan apa solusinya.
3. Jika semua tes berhasil (PASSED), berikan pesan "Semua sistem backend aman!".

**Output:** Ringkasan hasil testing yang mudah dibaca.