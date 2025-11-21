# file handling: navigate dan move (belom ke bagian copy atau rename atau remove)
# file organizing lesson

import os #library operating system agar python bisa config isi penyimpanan komputer
import time #library waktu
import shutil #library Shell Utilities, gunanya agar bisa menggunakan command seperti command di shell linux (CLI)

# print(os.getcwd())  #artinya OperatingSystem.GetCurrentWorkingDirectory
                    #yaitu directory folder saat ini

# os.chdir('/home/icedtea/Downloads/folder tes') #pindah ke directory folder "folder tes"
# time.sleep(0.5) #tunggu 0.5 detik, berkat library waktu

# print(os.getcwd()) #print directory apakah work
# print(os.listdir())    #sama seperti command 'ls' di CLI, dalam format 'list' python
                        #yaitu list isi folder directory saat ini


# <----- KODE DIATAS (kecuali import library) HANYA UNTUK TES ----->







# <----- MULAI PROJECT ----->

# Mengikuti Tutorial Alex The Analyst:
#  butuh docs library os sama shutils cik biar bisa tau semua command libnya,
#  tapi saat ini kuliat dari tutorial dulu (lebih susah tau apa aja commandnya karena ya cuman dari tutorial simple)
# tujuan: 1. apakah ada folder di directory saat ini, jika tidak maka buat folder baru
#         2. cek setiap file dan cari tahu tipe file nya, LALU pindahkan ke folder yang sesuai (biar rapi)

# <--- VARIABEL AWAL --->
path = os.getcwd() #ini variable shortcutku untuk os.getcwd() yaitu untuk tau sedang di path mana
# List nama folder tujuan untuk pengorganisasian file.
# Menggunakan penamaan snake_case (folder_names) untuk konsistensi.
fldrnames = [
    'Folder Media',
    'Folder Dokumen & Kode',
    'Folder Lainnya'
]

# Tuple untuk Tipe File Media (Gambar, Video, Audio).
medtuple = (
    ".png", ".jpeg", ".jpg", ".webp", ".tiff", ".tif", ".bmp", ".raw", ".heif", ".heic",
    ".gif", ".apng", ".avif",
    ".svg", ".eps", ".ai", ".psd", ".pdf", ".cdr",
    ".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv",
    ".mp3", ".wav", ".aac", ".flac", ".ogg",
)

# Tuple untuk Tipe File Dokumen, Kode Sumber, dan Arsip.
doccodetuple = (
    ".txt", ".py", ".html", ".js", ".css", ".ts", ".cpp", ".c", ".h", ".java",
    ".sh", ".bat", ".php", ".rb", ".go", ".swift",
    ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".odt", ".ods", ".odp",
    ".json", ".xml", ".csv", ".yml", ".ini", ".cfg",
    ".zip", ".rar", ".7z", ".tar", ".gz",
)


print() #dekorasi
print("--<{Filetype Organizer}>--") #dekorasi
print(f"Anda sedang berada di directory --< {path} >--") #bilang sedang di path mana
print("Mau sortir folder apa? (misal: /home/icedtea/Downloads/folder tes/)") #dekorasi
usrpath = input("Silakan masukkan path: ") #variabel input path dari user
os.chdir(usrpath) #PENTING untuk memindahkan script python ke path input user
print(f"Oke, anda sedang berada di path --< {path} >--") #konfirmasi path
print() #dekorasi

FGpath = os.path.join(usrpath, fldrnames[0]) #path folder gambar
FTpath = os.path.join(usrpath, fldrnames[1]) #path folder teks
FLpath = os.path.join(usrpath, fldrnames[2]) #path folder file lainnya
Flist = [FGpath, FTpath, FLpath] #list path folder

# <--- LOOP PENGECEKAN APAKAH SUDAH ADA FOLDER SORTIR FILETYPE --->
for urutannama in range(0, 3): #loop berapa kali berdasarkan range(0,3) yang artinya 3 kali (0 tak termasuk karena dalam list 0 juga tak termasuk)
    print(f"Apakah sudah ada folder bernama '{fldrnames[urutannama]}'?") #dekorasi
    
    if not os.path.exists(os.path.join(usrpath, fldrnames[urutannama])): #CEK Jika TAK ADA folder bernama {isi list fldrnames} pada directory saat ini, maka
        print(f"{os.path.exists(os.path.join(usrpath, fldrnames[urutannama]))}, membuat folder sekarang.") #print False berdasarkan tidak adanya folder2 baru ku
        os.makedirs((os.path.join(usrpath, fldrnames[urutannama]))) #membuat folder baruku, [urutannama] yaitu urutan loop keberapa dalam list fldrnames ku
    
    else: # Jika ADA folder bernama {isi list fldrnames} pada directory saat ini, maka
        print(os.path.exists(os.path.join(usrpath, fldrnames[urutannama]))) #print True berdasarkan adanya folder2 baru ku ini

print() #dekorasi
print() #dekorasi
print("Memulai perpindahan file..") #dekorasi

for file in os.listdir(): #loop berapa kali berdasarkan SEMUA file dalam list dir kita ini
    filepath = os.path.join(usrpath, file) #path untuk setiap file di os.listdir(), agar memindahkan gampang (/home/Downloads/ tak bakal ada jika tak pakai path)
    
    if file.endswith(medtuple): #jika filenya berakhir dengan tipe file gambar, maka lakukan kode berikut
        print(f"Mencoba memindah file gambar:") #bilang bahwa akan memindahkan file gambar
        print(f"└{file}") #beri tahu nama filenya apa
        shutil.move(filepath, FGpath) #memindahkan file yang berakhir dengan tipe file gambar, ke path folder gambar
    
    elif file.endswith(doccodetuple): #jika filenya berakhir dengan tipe file teks, maka lakukan kode berikut
        print(f"Mencoba memindah file teks:") #bilang bahwa akan memindahkan file teks
        print(f"└{file}") #beri tahu nama filenya apa
        shutil.move(filepath, FTpath) #memindahkan file yang berakhir dengan tipe file teks, ke path folder teks
    
    elif filepath not in Flist: #jika filenya tidak di list path folder maka lakukan kode berikut
        print(f"Mencoba memindah file tak dikenal:") #bilang bahwa akan memindahkan file tak dikenal
        print(f"└{file}") #beri tahu nama filenya apa
        shutil.move(filepath, FLpath) #memindahkan file yang tak dikenal, ke path folder lainnya
    
    else: #jika bertemu dengan folder di Flist maka lakukan kode berikut
        continue #continue = skip bagian kode ini

print() #dekorasi
print("Semua file berhasil dipindahkan ke folder yang sesuai.") #dekorasi