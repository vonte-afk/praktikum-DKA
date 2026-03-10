# input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# menghitung nilai akhir
nilai_akhir = (tugas * 0.20) + (uts * 0.35) + (uas * 0.45)

# output
print("\n===== HASIL NILAI MAHASISWA =====")
print("Nama Mahasiswa :", nama)
print("Nilai Tugas    :", tugas)
print("Nilai UTS      :", uts)
print("Nilai UAS      :", uas)
print("Nilai Akhir    :", nilai_akhir)