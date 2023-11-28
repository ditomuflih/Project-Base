import heapq
from datetime import datetime, timedelta

# Data kelas
matakuliah_data = {
    "Pancasila": [
        "Senin 08:00 - 10:00", "Selasa 10:00 - 12:00",
        "Rabu 14:00 - 16:00", "Kamis 08:00 - 10:00",
        "Jumat 10:00 - 12:00", "Sabtu 08:00 - 10:00"
    ],
    "Kecerdasan Buatan": [
        "Senin 14:00 - 16:00", "Selasa 08:00 - 10:00",
        "Rabu 10:00 - 12:00", "Kamis 14:00 - 16:00",
        "Jumat 08:00 - 10:00", "Sabtu 10:00 - 12:00"
    ],
    "Etika Profesi": [
        "Senin 10:00 - 12:00", "Selasa 14:00 - 16:00",
        "Rabu 08:00 - 10:00", "Kamis 10:00 - 12:00",
        "Jumat 14:00 - 16:00", "Sabtu 14:00 - 16:00"
    ],
    "Basis Data": [
        "Senin 08:00 - 10:00", "Selasa 10:00 - 12:00",
        "Rabu 14:00 - 16:00", "Kamis 08:00 - 10:00",
        "Jumat 10:00 - 12:00", "Sabtu 08:00 - 10:00"
    ],
    "Jaringan Komputer": [
        "Senin 14:00 - 16:00", "Selasa 08:00 - 10:00",
        "Rabu 10:00 - 12:00", "Kamis 14:00 - 16:00",
        "Jumat 08:00 - 10:00", "Sabtu 10:00 - 12:00"
    ],
    "Metode Numerik": [
        "Senin 08:00 - 10:00", "Selasa 10:00 - 12:00",
        "Rabu 14:00 - 16:00", "Kamis 08:00 - 10:00",
        "Jumat 10:00 - 12:00", "Sabtu 08:00 - 10:00"
    ],
    "Interaksi Manusia dan Komputer": [
        "Senin 14:00 - 16:00", "Selasa 08:00 - 10:00",
        "Rabu 10:00 - 12:00", "Kamis 14:00 - 16:00",
        "Jumat 08:00 - 10:00", "Sabtu 10:00 - 12:00"
    ],
    "Desain dan Analisis Algoritma": [
        "Senin 08:00 - 10:00", "Selasa 10:00 - 12:00",
        "Rabu 14:00 - 16:00", "Kamis 08:00 - 10:00",
        "Jumat 10:00 - 12:00", "Sabtu 08:00 - 10:00"
    ]
}

# Data SKS Mata Kuliah
sks_data = {
    "Pancasila": 2,
    "Kecerdasan Buatan": 3,
    "Etika Profesi": 2,
    "Basis Data": 3,
    "Jaringan Komputer": 2,
    "Metode Numerik": 3,
    "Interaksi Manusia dan Komputer": 3,
    "Desain dan Analisis Algoritma": 3
}

# Jumlah Mahasiswa
jumlah_mahasiswa = {
    "Pancasila": 30,
    "Kecerdasan Buatan": 40,
    "Etika Profesi": 30,
    "Basis Data": 40,
    "Jaringan Komputer": 40,
    "Metode Numerik": 40,
    "Interaksi Manusia dan Komputer": 40,
    "Desain dan Analisis Algoritma": 40
}


# Fungsi untuk menghitung nilai konflik
def hitung_nilai_konflik(slot_waktu, matakuliah, jadwal):
    # Implementasi rumus nilai konflik (sesuai dengan keterangan)
    # Misalnya, kita asumsikan bahwa constraint ruangan dan waktu dosen tidak diberikan pada contoh ini.
    n1 = 0.1  # Constraint ruangan (contoh: 0.1)
    n2 = 0.45  # Constraint waktu dosen (contoh: 0.45)
    n3 = 0.45 if len(jadwal[slot_waktu]) > 1 else 0  # Tipe kelas (contoh: 0.45 atau 0)
    cd = 1  # Banyak constraint waktu/sks matakuliah (contoh: 1)

    nilai_konflik = n1 + n2 + n3
    return nilai_konflik

# Fungsi untuk menghitung nilai kualitas slot waktu (H dalam A*)
def hitung_kualitas_slot_waktu(slot_waktu, matakuliah, jadwal):
    # Implementasi rumus nilai kualitas slot waktu (sesuai dengan keterangan)
    # Misalnya, kita asumsikan bahwa P1, P2, dan P3 tidak diberikan pada contoh ini.
    p1 = 0.4  # Contoh nilai P1
    p2 = 0.35  # Contoh nilai P2
    p3 = 0.25  # Contoh nilai P3

    kualitas_slot_waktu = p1 + p2 + p3
    return kualitas_slot_waktu

# Fungsi A* Search untuk mencari slot waktu terbaik
def a_star_search(matakuliah, sks, jumlah_mahasiswa):
    jadwal = {}  # Dictionary untuk menyimpan jadwal
    for slot in matakuliah_data[matakuliah]:
        jadwal[slot] = []

    # Fungsi untuk menghitung biaya total (F dalam A*)
    def hitung_biaya_total(slot_waktu):
        g = len(jadwal[slot_waktu]) * sks
        h = hitung_kualitas_slot_waktu(slot_waktu, matakuliah, jadwal)
        return g + h

    # Heap priority queue untuk menyimpan slot waktu yang akan diekspansi
    open_list = [(0, matakuliah_data[matakuliah][0])]  # (biaya, slot_waktu)
    
    while open_list:
        biaya, current_slot = heapq.heappop(open_list)

        # Jika slot waktu memiliki kapasitas cukup
        if len(jadwal[current_slot]) + jumlah_mahasiswa <= 60:
            jadwal[current_slot].append(matakuliah)

            # Jika semua SKS terpenuhi, kembalikan jadwal
            if sum(sks_data[m] for m in matakuliah_data) == sum(len(jadwal[slot]) * sks_data[m] for m in matakuliah_data):
                return jadwal

            # Ekspansi ke slot waktu berikutnya
            for next_slot in matakuliah_data[matakuliah]:
                heapq.heappush(open_list, (hitung_biaya_total(next_slot), next_slot))

    # Jika tidak ditemukan jadwal yang memenuhi semua constraint
    return None

# Uji coba untuk semua mata kuliah
for matakuliah_uji_coba in matakuliah_data.keys():
    sks_uji_coba = sks_data[matakuliah_uji_coba]
    jumlah_mahasiswa_uji_coba = jumlah_mahasiswa[matakuliah_uji_coba]

    hasil_jadwal = a_star_search(matakuliah_uji_coba, sks_uji_coba, jumlah_mahasiswa_uji_coba)

    # Tampilkan hasil jadwal
    print(f"Jadwal untuk {matakuliah_uji_coba}:")
    for slot, matkul in hasil_jadwal.items():
        print(f"{slot}: {matkul}")
