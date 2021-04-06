#Titus Kurniawan Sandy Purwanto
#I0320102
#kelas c

print('-----Program Penghitung Rata-rata-----')

print('================')
x = float(input('Input banyaknya nilai : '))
nilai = []
i = 1
while i <= x:
    score = float(input("Masukkan nilai anda : "))
    nilai.append(score)
    i = i + 1

rata2_nilai = sum(nilai)/x
print("Nilai rata-rata anda adalah ", rata2_nilai)