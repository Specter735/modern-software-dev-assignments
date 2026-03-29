# Week 6 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Abdurrahman Gilang Harjuna \
SUNet ID: 2310817110004 \
Citations: **TODO**

This assignment took me about 1 1/2 hours to do. 


## Brief findings overview 
> Hasil pemindaian dari Semgrep menggunakan konfigurasi default dan secrets, ditemukan 6 celah keamana SAST berstatus blocking dan 0 kebocoran password secrets. Temuannya mencakup SQL Injection, OS Command Injection, dan XXS. Saya memilih untuk menangani dan memperbaiki 3 celah saja.

## Fix #1
a. File and line(s)
> backend/app/routers/notes.py baris ke 72 dan 80

b. Rule/category Semgrep flagged
> python.sqlalchemy.security.audit.avoid-sqlalchemy-text

c. Brief risk description
> SQL Injection terjadi karena penggunaan format f-string secara langsung didalam fungsi teks pada SQL Alchemy

d. Your change (short code diff or explanation, AI coding tool usage)
> Saya memperbaikinya secara manual, menghapus f-string dan mengganti variabel '%{q}%' dengan parameter pengikat/bind parameter bernama :search. Saya juga meneruskan input dari pengguna secara aman pada saat eksekusi kode dengan menggunakan db.execute(sql, {"search": f"%{q}%"}).

e. Why this mitigates the issue
> Dengan menggunakan queri berparameter sistem database akan memperlakukan tesk yang dimasukkan oleh pengguna murni sebagai data literal/teks biasa, bukan sebagai perintah instruksi SQL, agar menetralkan dari SQL Injection.

## Fix #2
a. File and line(s)
> backend/app/routers/notes.py baris ke 108-115


b. Rule/category Semgrep flagged
> python.lang.security.audit.subprocess-shell-true

c. Brief risk description
> Celah OS Command Injection terjadi karena parameter shell=true saat menjalahkan perintah subprocess.run. jika penyerang bisa mengontrol teks pada variabel cmd maka mereka dapat menyisipkan perintah terminal tambahan untuk mengambil alih atau merusak server secara langsung misal dengan karakter ; dan &&.

d. Your change (short code diff or explanation, AI coding tool usage)
> Saya mengubah parameter shell=true menjadi shell=false, karena berubah menjadi false maka mewajibkan perintah ditulis dalam bentuk list bukan string teks tunggal. Saya juga mengimpor modul bawaan shlex dan menggunakan safe_cmd = shlex.split(cmd) untuk memecah teks perintah secara aman sebelum mengeksekusinya di subprocess.run(safe_cmd, ...).

e. Why this mitigates the issue
> shell=false akan mencegah sistem operasi untuk membuka proses terminal perantara, sehingga karakter khusus terminal tidak bisa berfungsi seperti |, >, dan &&. shlex.split(cmd) memastikan perintah dipecah dengan aman menjadi sebuah array sehingga sistem hanya akan menjalankan perintah utama tanpa mengeksekusi perintah tambahan dari penyerang.

## Fix #3
a. File and line(s)
> frontend/app.js baris ke 14

b. Rule/category Semgrep flagged
> javascript.browser.security.insecure-document-method

c. Brief risk description
> Celah kemanan XSS/Cross Site Scripting terjadi karena penggunaan innerHTML untuk memasukkan data dari pengguna secara langsung kedalam halaman webnya. penyerang tersebut bisa mengirimkan catatan kode javascript jahat yang akan tereksekusi secara otomatis diperangkat pengguna lain yang membuka halaman web tersebut. 

d. Your change (short code diff or explanation, AI coding tool usage)
> Saya menghapus bagian innerHTML dan saya bangun elemen DOM tersebut secara manual dan aman menggunakan document.createElement('strong') dan memasukkan teks judulnya menggunakan strong.textContent = n.title; lalu untuk catatannua ditambah menggunakan fungsi document.createTextNode().

e. Why this mitigates the issue
> textContent dan metode createTextNode secara otomatis melakukan pembersihan/satinization pada data yang masuk. Kedua fungsi ini memaksa browser untuk menganggap semua input dari pengguna hanya sebagai teks statis saja. jika ada tag HTML atau script yang berbahaya disisipkan, browser hanya akan menampilkan sebagai teks biasa di layar tanpa eksekusi.