from typing import List, Tuple

def merge_sort(data_barang: List[Tuple[str, int]]) -> List[Tuple[str, int]]:

    if len(data_barang) <= 1:
        return data_barang

    # Membagi data barang menjadi dua sub-array
    middle = len(data_barang) // 2
    kiri = merge_sort(data_barang[:middle])
    kanan = merge_sort(data_barang[middle:])

    # Menggabungkan sub-array yang telah terurut
    return merge(kiri, kanan)

def merge(kiri: List[Tuple[str, int]], kanan: List[Tuple[str, int]]) -> List[Tuple[str, int]]:

    result = []
    i = 0
    j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i][1] <= kanan[j][1]:  # Bandingkan berdasarkan harga
            result.append(kiri[i])
            i += 1
        else:
            result.append(kanan[j])
            j += 1

    # Menambahkan elemen yang tersisa
    result += kiri[i:]
    result += kanan[j:]

    return result

def custom_comparison(a: Tuple[str, int], b: Tuple[str, int]) -> bool:

    if a[1] == b[1]:  # Jika harga sama, urutkan berdasarkan nama
        return a[0] <= b[0]
    else:
        return a[1] <= b[1]

# Contoh penggunaan dengan data yang lebih lengkap
data_barang = [
    ("Laptop", 8800000),
    ("Smartphone", 2599000),
    ("Television", 1155000),
    ("Headphone", 1769000),
    ("Kulkas", 1500000),
    ("Air Conditioner", 3250000),
    ("Kompor Listrik", 999000),
    ("Rice Cooker", 2199000),
    ("Mesin Cuci", 3499000),
    ("Microwave", 1499000),
]

# Urutkan data 
print("========================================================")
print("TUGAS BESAR KELOMPOK DUA TEKNIK INFORMATIKA SEMESTER DUA")
print("ALGORITMA MERGE SORT UNTUK MENGURUTKAN DATA HARGA BARANG")
print("========================================================")
print()

print("--------------------------")
print("DATA SEBELUM DI URUTKAN : ")
print("--------------------------")
print(data_barang)
print("--------------------------------------------------------------------------------------------------------------")
print()

data_barang_terurut = merge_sort(data_barang)
print("--------------------------")
print("DATA SETELAH DI URUTKAN : ")
print("--------------------------")
print(data_barang_terurut)
print("--------------------------------------------------------------------------------------------------------------")
print()