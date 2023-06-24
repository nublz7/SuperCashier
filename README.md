# PROJECT SIMPLE SUPER CASHIER

## _Background_
Ini merupakan program kasir _self-service_ menggunakan Python yang bertujuan untuk mempermudah serta mempercepat proses belanja serta proses pembayaran.
Secara garis besar, program ini akan mempermudah untuk melakukan penambahan barang, mengubah jumlah barang, mengubah harga barang, serta ada fitur diskon yang sudah otomatis apa bila customer mencapai total belanja sejumlah nominal tertentu.

## _Objective_
  1. Membuat sistem kasir self-service dengan fitur untuk mentambahkan barang (nama barang, jumlah, harga).
  2. Mempermudah pelanggan untuk melakukan transanksi, walaupun pelanggan belum sampai di toko.
  3. Mempercepat proses di kasir, sehingga tidak terjadi antrian yang panjang.

## _Requirement_
  1. Menggunakan _Object Oriented Programing_ (OOP).
  2. Menerapkan prinsip Clean Code (PEP8).
  3. Membuat docstring di setiap fucntion dan/atau class yang ada.
  4. Terdapat `try-error`, `branching` di dalam code.
  5. Menggunakan library `tabulate` untuk membuat struk belanja.
  6. Menggunakan library `datetime` untuk membuat id pelanggan.

## Alur Program/_Flowchart_
![Flowchart](https://github.com/nublz7/SuperCashier/assets/134612964/2ae9768e-c055-44fa-bdd7-bfa43cec588e)

## _Test Case_
### Test 1
Pada case pertama berikut, customer ingin membeli 2 Ayam Goreng seharga @20,000 dan 3 Pasta Gigi seharga @15,000

![test1](https://github.com/nublz7/SuperCashier/assets/134612964/cc990189-cbab-4cd1-b9a5-5603c8152322)

### Test 2
Case 2 berikut ternyata customer salah membeli item Pasta Gigi, sehingga harus menghapus nama barang beserta jumlah dan harganya.

![test2](https://github.com/nublz7/SuperCashier/assets/134612964/dc1d08bd-c7ad-418d-986e-3f5f6f14f439)

### Test 3
Pada case ini, customer ingin menghapus semua barang belanjaan yang ada di keranjang.

![test3](https://github.com/nublz7/SuperCashier/assets/134612964/a00cf036-dcd6-4a3e-b319-faf274906ba3)

### Test 4
Setelah menghapus semua belanjaan di keranjang, customer membeli lagi barang-barang berikut dan langsung ingin membayarnya ke kasir.
  - 2 Ayam Goreng @20,000
  - 3 Pasta Gigi @15,000
  - 1 Mainan Mobil @200,000
  - 5 Mie Instan @3,000

![test4](https://github.com/nublz7/SuperCashier/assets/134612964/7683718c-aa95-426e-9e09-3441e0819d4f)

## Kesimpulan
Program berikut masih sangat amat sederhana, sehingga masih banyak ruang untuk improvisasi, seperti:
  - UI yang menarik.
  - UX yang memudahkan untuk semua kelompok umur.
  - Dapat melakukan export dari total belanjaan ke dalam file seperti `.csv` agar customer mudah saat melakukan pengecekan di rumah.
