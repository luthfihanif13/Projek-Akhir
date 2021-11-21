#Program Ojekonline syariah

def login():
  print('login Pejuang PA')
  while True:
    username = input('username : ')
    passw = input('password : ')
    if username == 'Luthfi' and passw == '082' or username == 'Adit' and passw == 'unsend' or username == 'puput' and passw == 'sibukmc' :
        print('---------------------------------')
        print('-------Ojek Online Syariah-------')
        print('--Membantu Antum dalam Berpergian--')
        print('------Aman,Nyaman,Terpercaya------')
        print('---------------------------------')
        break
    else:
        print('silahkan antum memasukkan password/username dengan benar!')
        continue  

def motor():
    pilihan = input('motor')
    motor[pilihan]

def mobil():
    pilihan = input('mobil')
    mobil[pilihan]


def kendaraan():
  while True:
    print('kendaraan')
    print('1. Motor\n2. Mobil')
    pilihan = input('masukan pilihan: ')
    if pilihan == '1':
        motor()
        print('\nAntum memilih motor')
        input()
    elif pilihan == '2':
        mobil()
        print('\nAntum memilih mobil')
        input()
        break


penjemputan = {
  'lokasi': ['Ahmad yani', 'Sentosa', 'Pasar segiri', 'Slamet riyadi', 'Dr sutomo', 'Pramuka', 'Perjuangan', 'Wahid hasyim', 'Bengkuring', 'Kusuma bangsa', 'Palaran', 'Air putih', 'Air hitam', 'Juanda', 'Cendana', 'Loa bakung', 'Lempake', 'Remaja', 'Segiri', 'Makroman']
}

tujuan = {
  'lokasi': ['Ahmad yani', 'Sentosa', 'Pasar segiri', 'Slamet riyadi', 'Dr sutomo', 'Pramuka', 'Perjuangan', 'Wahid hasyim', 'Bengkuring', 'Kusuma bangsa', 'Palaran', 'Air putih', 'Air hitam', 'Juanda', 'Cendana', 'Loa bakung', 'Lempake', 'Remaja', 'Segiri', 'Makroman']
}


def list_jalanan_penjemputan():
    penjemputan
    for key, value in penjemputan.items():
      print(key, value)


def tambah():
    input_baru = input('masukan nama jalan: ')
    penjemputan[input_baru]

def update():
    input_baru = input('update nama jalan: ')
    penjemputan[input_baru]

def hapus():
    del penjemputan [input('menghapus jalan: ')]


def list_jalanan_tujuan():
    tujuan
    for key, value in tujuan.items():
      print(key, value)


def tambah_tujuan():
    input_baru = input('masukan nama jalan: ')
    tujuan[input_baru]

def update_tujuan():
    input_baru = input('update nama jalan: ')
    tujuan[input_baru]

def hapus_tujuan():
    del tujuan [input('menghapus jalan: ')]


def main_menu():
    while True:
        print('menu')
        print('==============')
        print('1. List jalanan')
        print('2. Menambahkan lokasi penjemputan')
        print('3. Mengupdate lokasi penjemputan')
        print('4. Menghapus lokasi penjemputan')
        print('5. Menambahkan lokasi tujuan')
        print('6. Mengupdate lokasi tujuan')
        print('7. Menghapus lokasi tujaun')
        print('8. Keluar dari program ')
        pilih = input('Masukan pilihan: ')
        if pilih == '1':
            list_jalanan_penjemputan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '2':
            tambah()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '3':
            update()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '4':
            hapus()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '5':
            tambah_tujuan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '6':
            update_tujuan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '7':
            hapus_tujuan()
            print("\n")
            input("Tekan Enter untuk kembali...")
        elif pilih == '8':
            print('Antum telah keluar')
            break
        
def ikhwan():
    pilihan = input('Ikhwan')
    ikhwan[pilihan]

def akhwat():
    pilihan = input('Akhwat')
    akhwat[pilihan]

def driver():
  while True:
    print('kendaraan')
    print('1. Ikhwan\n2. Akhwat')
    pilihan = input('masukan pilihan: ')
    if pilihan == '1':
        ikhwan()
        print('\nAntum memilih pengemudi Ikhwan')
        input()
    elif pilihan == '2':
        akhwat()
        print('\nAntum memilih pengemudi Akhwat')
        input()
        break

harga_km_motor = 5000
harga_km_mobil = 12000
harga = 0


def gopay():
    pilihan = input('Gopay')
    gopay[pilihan]

def tunai():
    pilihan = input('Tunai')
    tunai[pilihan]

    while True:
            jarak_km = int(input('Masukkan jarak tempuh: '))
            bayar = int(input('jumlah nominal uang = Rp '))
            print ('Silahkan Antum Perika Inputan')



total= jarak_km * bayar
def pembayaran():
  while True:
      print('mau bayar pakai apa: ')
      print('1. Gopay\n2. Tunai')
      pilihan = input('masukan pilihan: ')
      if pilihan == '1':
        gopay()
        print('\nAntum memilih membayar dengan gopay')
        input()
      elif pilihan == '2':
        tunai()
        print('\nAntum memilih membayar dengan tunai')
        input()
        break


while True:
      bayar=int(input('jumlah nominal uang = Rp '))
      if total <= bayar:
        kembalian= (bayar-total)
        print('Uang kembalian = ', 'Rp', kembalian)
        

