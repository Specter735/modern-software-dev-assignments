# Week 5 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Abdurrahman Gilang Harjuna \
SUNet ID: 2310817110004 \
Citations: **TODO**

This assignment took me about 3 hours to do. 


## YOUR RESPONSES
### Automation A: Warp Drive saved prompts, rules, MCP servers

a. Design of each automation, including goals, inputs/outputs, steps
> Goals: Memaksa AI agar selalu mengembalikan respon API sesuai dengan standar JSON Envelope yng sudah ditentukan
input/Ouputnya: input berupa perintah pembuatan/modifikasi endpoint FastAPI didirektori backendoutput berupa kode FastAPI dan Pydantic Scemas yang secara otomatis menggunakan format pada sukses dan error
Steps: membuat saved prompt diwarp drive dengan judul FastAPI Standard Envelope Formatter yang berisi instruksi ketat/rule mengenai struktur response JSON yang wajib digunakan setiap kali AI memanipulasi Endpoint.

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before: saya harus mengetik ulang instruksi format envelope berulang kali setiap meminta AI membuat Endpoint baru karna terlewat atau menghasilkan format yang tidak konsisten
After: aturan format tersimpan secata global di warp. AI secata otomatis mengaplikasikan standar respon ini tanpa perlu diinstruksikan ulang didalam kolom chat, ini sangat menghemat waktu dalam promptingnya.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> Saya  menggunakan otonomi partial local agent untuk keamanan agar AI tidak sembarangan merusak codebase utamanya. saya melakukan supervisi secara manual pada setiap plan yang diajukan AI dan menekan tombol Approve sebelum AI diizinkan untuk membaca, menulis file dan menjalankan perintah diterminal.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> rule ini diaplikasikan secara  universal kesemua agent AI yang saya jalankan bersamaan pada part B.

e. How you used the automation (what pain point it resolves or accelerates)
> otomatisasi ini menyelesaikan pain point berupa prompt fatigue yaitu kelelahan dalam prompt panjang dan human error yaitu lupa untuk memberikan syarat formatnya karena itu pengembangan backend menjadi lebih cepat dan konsisten.



### Automation B: Multi‑agent workflows in Warp 

a. Design of each automation, including goals, inputs/outputs, steps
> Goal: menyelesaikan 2 taks yaitu task 2 dan task 4 secara bersamaan menggunakan 2 agent AI yang berbeda tanpa menimbulkan konflik kodenya. 
Steps:
1. Membuat 2 git worktree terpisah week5-task2 dan week5-task4 untuk mengisolasi environtment kerja.
2. Mmebuka 2 Tab Terminal yang berbeda di warp
3. Menjalankan 1 lokal agent di masing masing tab prompt spesifik untuk masing masing task.
4. mengawasi dan menyetujui eksekusi dari kedua agent secara bergantian atau otomatis, lalu mengerjakan merge kembali ke branch setelah keduanya selesai

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before: mengerjakan task2 dan task4 harus dilakukan secara sekuensial. jika task 2 sedang berjalan atau debug maka untuk task4 harus menunggu yang membuat pengerjaan menjadi lebih lambat/bottleneck.
After: kedua task diselesaikan secara bersamaan/pararel. agen 1 menulis dan melakukan testing untuk task2, agent 2 memikirkan logika bulk complete pada task4 pada waktu yang bersamaan. waktu pengerjaan menjadi lebih cepat. 

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> saya menggunakan partial autonomi, saya yang bertindak untuk berpidah pindah tab setiap kali agen ingin memodifikasi file atau menjalankan pytest dan klik approve.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> Roles: agent 1 fokus pada endpoint pencarian dan paginasi task 2 dan agent 2 fokus pada endpoint filter bulk update task 4
coordination strategy: penggunaan gir worktree ini untuk mencegah file yang sama oleh 2 agen yang berbeda diwaktu yang bersamaan.
wins: efesiensi waktu karena agen 1 berhasil mengerjakan tugasnya tanpa mengganggu agen 2

e. How you used the automation (what pain point it resolves or accelerates)
> workflow ini menyelesaikan masalah bottleneck dalam pengembangan perangkat lunak dari pada membiarkan resource menganggur saat satu fitur di uji, sebaiknya melakukan multitasking pada agen tersebut.


### (Optional) Automation C: Any Additional Automations
a. Design of each automation, including goals, inputs/outputs, steps
> TODO

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> TODO

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> TODO

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> TODO

e. How you used the automation (what pain point it resolves or accelerates)
> TODO

