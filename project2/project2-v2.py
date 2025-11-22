print()
print("=== lowbudget calc ===")
print("calc is short for calculator*")

plusoperators = ["add", "+", "ad", "tambah", "tambahi", "ditambah", "tambahin", "plus"]
suboperators = ["sub", "-", "minus", "kurang", "dikurangi", "kurangin", "min", "subtract", "subtractedby"]
muloperators = ["mul", "*", "multiply", "x", "kali", "dikali", 'dikalikan', "dikaliin", "multipliedby"]


stopbruh = ""

#LOOP UTAMA!
while stopbruh != "stop":

    output = [] # hasil akhir
    isisementara = [] # potongan saat ini
    tipesekarang = None # tipe potongan saat ini ('digit' atau 'non')

    value = input("masukkan perhitungan: ") # input dari user

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
                                # print(hasil) # cetak hasil akhir DEBUGGING

    # LOOP ubah semua digit dalam hasil menjadi integer
    temphasil = [] # list hasil sementara
    for chunk in hasil:
        if chunk.isdigit():
            temphasil.append(int(chunk)) # Convert and append to the new list
        else:
            temphasil.append(chunk)     # Keep the original value
    hasil = temphasil # Replace the old list with the new one


    # calculator

    if hasil[0] == '-' and type(hasil[1]) == int:
        hasil[1] = hasil[1]-hasil[1]*2
        del hasil[0]
                                # print("berhasil mengubah -angka jadi int beneran") DEBUGGING

                                # print(hasil) DEBUGGING
    hasilakhir = 0

    if hasil[1] in plusoperators and type(hasil[0]) == int and type(hasil[2]) == int:
        hasilakhir = hasilakhir + hasil[0] + hasil[2]
    elif hasil[1] in suboperators and type(hasil[0]) == int and type(hasil[2]) == int:
        hasilakhir = hasilakhir + hasil[0] - hasil[2]
    elif hasil[1] in muloperators and type(hasil[0]) == int and type(hasil[2]) == int:
        hasilakhir = hasilakhir + hasil[0] * hasil[2]
    else:
        continue #kalo yang ditengah bukan operator ya skip aja

    

    print(f"hasil anda: {hasilakhir}")
    