import candra125
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matriks A")
for baris in A:
    print(baris)
print("\nMatriks B")
for baris in B:
    print(baris)

print("\nHasil Perkalian A x B")
hasil_kali = candra125.perkalian_matriks(A, B)
for baris in hasil_kali:
    print(baris)
    
print("\nTranspose Matriks A")
hasil_transpose = candra125.transpose_matriks(A)
for baris in hasil_transpose:
    print(baris)