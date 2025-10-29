# 2. Pola piramid (menggunakan nested loop)
print("\n2. Pola piramid:")
for i in range(1, 6):
    # Cetak spasi di depan
    for j in range(5 - i):
        print(" ", end="")
    # Cetak bintang
    for j in range(2 * i - 1):
        print("*", end="")
    print()