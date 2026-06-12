# candra125.py
def perkalian_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            jumlah = 0
            for k in range(len(B)):
                jumlah += A[i][k] * B[k][j]
            baris.append(jumlah)
        hasil.append(baris)
    return hasil

def transpose_matriks(A):
    hasil = []
    for j in range(len(A[0])):
        baris = []
        for i in range(len(A)):
            baris.append(A[i][j])
        hasil.append(baris)
    return hasil