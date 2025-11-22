print()
print("=== lowbudget calc ===")
print("calc is short for calculator*")

value = input("masukkan perhitungan: ") # input dari user

output = [] # hasil akhir
isisementara = [] # potongan saat ini
tipesekarang = None # tipe potongan saat ini ('digit' atau 'non')

for character in value: # iterasi setiap karakter dalam input
    if character.isdigit(): # cek apakah karakter adalah digit
        tipebaru = 'digit' # tipe baru adalah 'digit'
    else: # jika bukan digit
        tipebaru = 'nondigit' # tipe baru adalah 'nondigit'
    
    if tipebaru != tipesekarang: # KALO tipe baru BUKAN tipe sekarang maka
        if isisementara != []: # KALO potongan sekarang ADA ISINYA
            output.append(isisementara) # TAMBAHIN potongan sekarang ke hasil akhir
        isisementara = [] # RESET potongan sekarang
        tipesekarang = tipebaru # TIPE BARU JADI TIPESEKARANG

    isisementara.append(character) # tambahkan karakter ke potongan saat ini

if isisementara != []: # setelah iterasi, KALO potongan sekarang ADA ISINYA
    output.append(isisementara) # TAMBAHIN potongan sekarang ke hasil akhir

hasil = ["".join(isisementara) for isisementara in output] # gabungkan karakter dalam setiap potongan menjadi string
print(hasil) # cetak hasil akhir

hasil[0] = int(hasil[0]) # konversi potongan pertama dalam hasil menjadi integer
hasil[1] = str(hasil[1]) # konversi potongan kedua dalam hasil menjadi string
hasil[2] = int(hasil[2]) # konversi potongan ketiga dalam hasil menjadi integer

print(hasil[0]) # cetak potongan pertama
print(hasil[1]) # cetak potongan kedua
print(hasil[2]) # cetak potongan ketiga

