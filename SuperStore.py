from tabulate import tabulate
import datetime as dt

class Transaction():
  '''
  Class Transaction() merupakan class untuk menyimpan method yang akan digunakan untuk melakukan perintah.
    di dalam class Transaction terdapat beberapa method, yaitu:
      - add_item()
      - update_name()
      - update_qty()
      - update_price()
      - delete_item()
      - reset()
      -check_order()
  '''
  Chart = {}
  Total = 0

  def add_item(self, item_name, item_qty, item_price):
    '''
    add_item() merupakan function untuk menambahkan item ke dalam keranjang belanja

    Parameter:
    ----------
    item_name: str
        merukapan nama barang yang akan dibeli.
    item_qty: int
        merupakan jumlah barang yang akan dibeli.
    item_price: int
        merupakan harga barang yang akan dibeli.
    '''
    self.item_name = item_name
    self.item_qty = item_qty
    self.item_price = item_price
    self.Chart.update({item_name: [item_qty, item_price]})

  def update_name(self, old_name, new_name):
    '''
    update_name() merupakan function untuk mengubah nama barang yang sudah ada
    di dalam keranjang belanja.

    Parameter:
    ----------
    old_name: str
      merupakan nama barang yang sudah ada di keranjang.
    new_name: str
      merupakan nama barang yang baru.
    '''
    self.Chart[new_name] = self.Chart.pop(old_name)
    print(f'{old_name} berhasil diubah menjadi {new_name}.')

  def update_qty(self, item_name, new_qty):
    '''
    update_qty() merupakan function untuk mengubah jumlah barang yang ingin dibeli

    Parameter:
    ----------
    item_name: str
      merupakan nama barang yang sudah ada di keranjang.
    new_qty: int
      merupakan jumalah barang yang terbaru yang ingin dimasukan ke dalam keranjang.
    '''
    self.Chart[item_name][0] = new_qty
    print(f'Jumlah {item_name} berhasil diubah menjadi {new_qty}.')

  def update_price(self, item_name, new_price):
    '''
    update_price() adalah function untuk mengubah harga barang yang sudah ada di keranjang,
    apa bila barang tersebut tidak ada, maka akan menampilkan error.

    Parameter:
    ----------
    item_name: str
      merupakan nama barang yang sudah ada di keranjang.
    new_price: int
      merupakan harga barang terbaru yang ingin dimasukan ke dalam keranjang sesuai dengan nama barang.
    '''
    self.Chart[item_name][1] = new_price
    print(f'Harga {item_name} berhasil diubah menjadi {new_price}.')

  def delete_item(self, item_name):
    '''
    Function delete_item() merupakan function untuk menghapus nama barang, jumlah barang, dan harga barang,
    Parameter yang harus dimasukan hanya 1.

    Parameter:
    ----------
    item_name: str
      merupakan nama barang yang sudah ada di keranjang.
    '''
    self.Chart.pop(item_name)
    print(f'{item_name} berhasil dihapus.')

  def reset(self):
    '''
    reset() merupakan function untuk menghapus keseluruhan barang yang ada di keranjang.
    '''
    self.Chart = {}
    self.Total = 0
    print(f'Order berhasil dibatalkan.')

  def check_order(self):
    '''
    Function untuk menampilkan keranjang belanja terupdate beserta total diskon.
    Apabila total belanja lebih dari Rp200.000 akan mendapatkan diskon 5%,
    apabila total belanja lebih dari Rp300.000 akan mendapatkan diskon 8%, dan
    apabila total belanja lebih dari Rp500.000 akan mendapatkan diskon 10%.
    '''
    disc_5 = 0.05
    disc_8 = 0.08
    disc_10 = 0.1

    # untuk menyimpan header yang akan dipanggil saat looping struk belanja agar header tidak terprint terus menerus
    header = ['Nama Barang', 'Total Harga']
    table = [header]

    if not self.Chart:
      print('Keranjang Anda kosong.')
      return

    print('Keranjang belanja Anda:\n')
    self.Total = 0
    for index, (item_name, item_info) in enumerate(self.Chart.items()):
      qty = item_info[0]
      price = item_info[1]
      subtotal = qty * price
      self.Total += subtotal
      table.append([f'-{item_name}\n  {qty} x {price:,}', f'Rp {subtotal:,}'])

    if self.Total > 500_000:
      diskon = self.Total * disc_10
    elif self.Total > 300_000:
      diskon = self.Total * disc_8
    elif self.Total > 200_000:
      diskon = self.Total * disc_5
    else:
      diskon = 0

    table.append(['=' * 8, '=' * 8])
    table.append(['Subtotal', f'Rp {self.Total:,}'])
    table.append(['Diskon', f'Rp {int(diskon):,}'])
    table.append(['Total', f'Rp {int(self.Total - diskon):,}'])
    print(tabulate(table, headers='firstrow'))
    return diskon

class Runner():
  '''
  Class Runner() adalah sebuah class untuk menjalankan programnya, tujuannya agar di file utama tidak terdapat pengulangan kode yang tidak perlu.
  '''
  open_message = 'Welcome to SuperStore, '

  def __init__(self, name):
    self.name = name
    self.transID = name + '-' + dt.datetime.now().strftime('%y%m%d')
    self.transaction = Transaction()

  def welcome(self):
    '''
    method ini hanya untuk menampilkan pesan saat uuser baru pertama kali menjalankan kodenya.
    '''
    print('=' * (len(self.open_message) + len(self.transID) + 2))
    print(f'{self.open_message} {self.transID.title()}!')
    print('=' * (len(self.open_message) + len(self.transID) + 2))

  def input_item(self):
    '''
    input_item() akan melakukan perulangan untuk melakukan penambahan item.
    Apabila customer input 'y' maka customer akan melakukan input order kembali,
    Apabila customer input 'n' maka customer akan diarahkan ke step selanjutnya, dan
    Apabila customer tidak input 'y' maupun 'n', maka akan melakukan perulangan sampai customer input 'y' dan 'n'.
    '''
    while True:
      items = input('Masukan nama barang: ').title()
      try:
        qty = int(input('Masukan jumlah barang yang ingin dibeli: '))
        price = int(input('Masukan harga barang: '))
        self.transaction.add_item(items, qty, price)
        self.transaction.check_order()
        while True:
          ans = input('Apakah ingin menambah order? (y/n) ')
          if ans.lower() == 'n':
            break
          elif ans.lower()== 'y':
            break
          else:
            print('Jawaban tidak valid, silahkan masukan "y/n"')

        if ans.lower() == 'n':
          break
      except ValueError:
        print(f'Jumlah barang dan/atau harga barang harus berupa angka')

  def get_diskon(self):
    '''
    method get_diskon() hanya untuk menyimpan jumlah diskon agar bisa dipanggil saat ingin melakukan pembayaran ke kasir.
    '''
    return self.transaction.check_order()

  def input_choice(self):
    '''
    input_choice() merupakan method yang akan dijalankan setetelah user selesai input barang belanjaan, dan akan menampilkan 6 pilihan menu berikut:
    0. Melanjutkan ke pembayaran.
    1. Ubah nama barang.
    2. Ubah jumlah barang.
    3. Ubah harga.
    4. Hapus barang, jumlah & harga sekaligus.
    5. Tambah barang belanjaan.
    6. Batalkan transaksi.
    '''
    items_unavailable = 'Nama barang yang Anda masukkan tidak ada di keranjang belanja.'

    while True:
      print('\nApakah ada yang ingin Anda ubah?\n')
      print('  0. Melanjutkan ke pembayaran.')
      print('  1. Ubah nama barang.')
      print('  2. Ubah jumlah barang.')
      print('  3. Ubah harga.')
      print('  4. Hapus barang, jumlah & harga sekaligus.')
      print('  5. Tambah barang belanjaan.')
      print('  6. Batalkan transaksi.\n')

      try:
        answer = int(input('Silahkan masukan angka yang sesuai dengan pilihan: '))
        if answer == 6:
          self.transaction.reset()
          break
        elif answer == 1:
          while True:
            old_name1 = input('Masukan nama barang yang ingin diubah: ').title()
            if old_name1 in self.transaction.Chart:
              new_name1 = input('Masukan nama barang yang baru: ').title()
              self.transaction.update_name(old_name1, new_name1)
              self.transaction.check_order()
              break
            else:
              print(items_unavailable)
        elif answer == 2:
          while True:
            old_name1 = input('Masukan nama barang yang ingin diubah: ').title()
            if old_name1 in self.transaction.Chart:
              new_qty1 = int(input('Masukan jumlah barang: '))
              self.transaction.update_qty(old_name1, new_qty1)
              self.transaction.check_order()
              break
            else:
              print(items_unavailable)
        elif answer == 3:
          while True:
            old_name1 = input('Masukan nama barang yang ingin diubah: ').title()
            if old_name1 in self.transaction.Chart:
              new_price1 = int(input('Masukan harga barang: '))
              self.transaction.update_price(old_name1, new_price1)
              self.transaction.check_order()
              break
            else:
              print(items_unavailable)
        elif answer == 4:
          while True:
            old_name1 = input('Masukan nama barang yang ingin dihapus: ').title()
            if old_name1 in self.transaction.Chart:
              self.transaction.delete_item(old_name1)
              self.transaction.check_order()
              break
            else:
              print(items_unavailable)
        elif answer == 5:
          self.input_item()
        else:
          payment = f'Silahkan ke kasir untuk melakukan pembayaran sejumlah Rp {int(self.transaction.Total - self.get_diskon()):,}.'
          print('=' * len(payment))
          print(payment)
          print('Terima kasih sudah berbelanja di SuperStore!')
          break
      except ValueError:
        print('Apa yang Anda masukkan tidak ada di pilihan.')