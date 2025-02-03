#5 warna

warna_resistor = {
    "hitam": 0,
    "coklat": 1,
    "merah": 2,
    "oranye": 3,
    "kuning": 4,
    "hijau": 5,
    "biru": 6,
    "ungu": 7,
    "abu-abu": 8,
    "putih": 9
}

toleransi_resistor = {
    "perak": "±10%",
    "emas": "±5%",
    "coklat": "±1%",
    "merah": "±2%",
    "hijau": "±0.5%",
    "biru": "±0.25%",
    "ungu": "±0.1%",
}

multiplier_resistor = {
    "perak": 0.01,
    "emas": 0.1,
    "hitam": 1,
    "coklat": 10,
    "merah": 100,
    "oranye": 1000,
    "kuning": 10000,
    "hijau": 100000,
    "biru": 1000000,
    "ungu": 10000000
}

def hitung_resistor(gelang1, gelang2, gelang3, gelang4, gelang5):
    try:
        nilai1 = warna_resistor[gelang1]
        nilai2 = warna_resistor[gelang2]
        nilai3 = warna_resistor[gelang3]
        multiplier = multiplier_resistor[gelang4]
        toleransi = toleransi_resistor[gelang5]

        resistansi = (nilai1 * 100 + nilai2 * 10 + nilai3) * multiplier

        print(f"\nNilai Resistor: {resistansi} Ohm")
        print(f"Toleransi: {toleransi}")
    except KeyError:
        print("Warna yang dimasukkan tidak valid.")

print("Program Perhitungan Warna Resistor")
print("=================================")
print("Masukkan warna gelang resistor (gunakan huruf kecil):")
gelang1 = input("Gelang 1: ")
gelang2 = input("Gelang 2: ")
gelang3 = input("Gelang 3: ")
gelang4 = input("Gelang 4 (Multiplier): ")
gelang5 = input("Gelang 5 (Toleransi): ")

hitung_resistor(gelang1, gelang2, gelang3, gelang4, gelang5)
