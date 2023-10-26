import heapq

# Data Jadwal Mata Kuliah
schedule_data = {
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

# Inisialisasi Simpul Awal
initial_schedule = []
cost = 0
for course in sks_data:
    cost += sks_data[course]
frontier = [(cost, initial_schedule)]

# Fungsi untuk memeriksa apakah jadwal memenuhi semua ketentuan
def is_valid_schedule(schedule):
    for day in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]:
        day_schedule = [item[2] for item in schedule if item[0] == day]
        if len(day_schedule) != len(set(day_schedule)):
            return False
    return True

# Fungsi untuk menghitung biaya (total SKS) dari jadwal
def calculate_cost(schedule):
    total_cost = 0
    for item in schedule:
        total_cost += sks_data[item[2]]
    return total_cost

# Implementasi algoritma A* Search
def a_star_search():
    while frontier:
        cost, schedule = heapq.heappop(frontier)
        if is_valid_schedule(schedule):
            return schedule  # Jadwal valid ditemukan

        for course, time_slots in schedule_data.items():
            for day, time in time_slots:
                if course not in [item[2] for item in schedule]:
                    new_schedule = schedule + [(day, time, course)]
                    new_cost = calculate_cost(new_schedule)
                    heapq.heappush(frontier, (new_cost, new_schedule))

    return None  # Tidak ada jadwal yang memenuhi semua ketentuan

# Menjalankan algoritma A* Search
result = a_star_search()

if result:
    print("Jadwal yang memenuhi semua ketentuan:")
    for day, time, course in result:
        print(f"{course} pada {day} pukul {time}")
else:
    print("Tidak ada jadwal yang memenuhi semua ketentuan.")
