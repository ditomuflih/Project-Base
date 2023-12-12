import heapq
import random

class ScheduleNode:
    def __init__(self, day, class_name, start_time, end_time):
        self.day = day
        self.class_name = class_name
        self.start_time = start_time
        self.end_time = end_time

    def __lt__(self, other):
        # Comparison for the priority queue
        return self.end_time < other.end_time
    
def is_valid_schedule(schedule, current):
    # Check if the current class can be added to the schedule without overlapping
    overlapping_classes = [c for c in schedule[current.day] if not (current.end_time <= c.start_time or current.start_time >= c.end_time)]
    return not overlapping_classes

def find_schedule(classes):
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']
    schedule = {day: [] for day in days}
    heap = []

    selected_classes = set()

    for cls in classes:
        while True:
            random_class = random.choice(classes[cls])
            class_name = cls + ' ' + random_class[0]

            # Ensure each class is selected only once
            if class_name not in selected_classes:
                selected_classes.add(class_name)
                break

        heapq.heappush(heap, ScheduleNode(random_class[1], class_name, random_class[2], random_class[3]))

    while heap:
        current = heapq.heappop(heap)
        if is_valid_schedule(schedule, current):
            schedule[current.day].append(current)

    return schedule

def print_schedule(schedule):
    for day in schedule:
        print(day)
        if not schedule[day]:
            print("Hari ini kosong.")
        else:
            for cls in schedule[day]:
                print(f"{cls.class_name} Jam {cls.start_time}-{cls.end_time}")
        print()

# Jadwal untuk setiap mata kuliah
classes = {
    'Jaringan Komputer': [
        ('A', 'Senin', '15:30', '17:09'),
        ('B', 'Senin', '16:20', '18:09'),
        ('C', 'Senin', '10:20', '11:59'),
        ('D', 'Rabu', '16:20', '18:09'),
        ('E', 'Rabu', '15:30', '17:09'),
        ('F', 'Rabu', '10:20', '11:59'),
        ('G', 'Selasa', '09:30', '11:09'),
    ],
    'Basis Data': [
        ('A', 'Senin', '9:30', '11:09'),
        ('B', 'Selasa', '15:30', '17:09'),
        ('C', 'Senin', '12:50', '14:29'),
        ('D', 'Rabu', '10:20', '11:59'),
        ('E', 'Rabu', '07:00', '08:39'),
        ('F', 'Selasa', '12:50', '14:29'),
        ('G', 'Rabu', '10:20', '11:59'),
    ],
    'Desain dan Analisis Algoritma': [
        ('A', 'Jumat', '08:40', '10:19'),
        ('B', 'Senin', '07:50', '09:29'),
        ('C', 'Selasa', '13:40', '15:19'),
        ('D', 'Jumat', '07:50', '09:29'),
        ('E', 'Kamis', '15:30', '17:09'),
        ('F', 'Selasa', '15:30', '17:09'),
        ('G', 'Rabu', '07:00', '08:39'),
    ],
    'Kecerdasan Buatan': [
        ('A', 'Senin', '07:00', '08:39'),
        ('B', 'Rabu', '09:30', '11:09'),
        ('C', 'Kamis', '07:00', '08:39'),
        ('D', 'Rabu', '13:40', '15:19'),
        ('E', 'Rabu', '12:50', '14:29'),
        ('F', 'Rabu', '12:50', '14:29'),
        ('G', 'Kamis', '14:30', '16:19'),
    ],
    'Metode Numerik': [
        ('A', 'Rabu', '09:30', '11:09'),
        ('B', 'Jumat', '07:00', '08:39'),
        ('C', 'Senin', '14:30', '16:19'),
        ('D', 'Kamis', '14:30', '16:19'),
        ('E', 'Selasa', '07:00', '08:39'),
        ('F', 'Kamis', '07:00', '08:39'),
        ('G', 'Senin', '09:30', '11:09'),
    ],
     'Interaksi Manusia dan Komputer': [
        ('A', 'Rabu', '08:30', '11:09'),
        ('B', 'Jumat', '07:00', '08:39'),
        ('C', 'Senin', '14:30', '16:19'),
        ('D', 'Kamis', '14:30', '16:19'),
        ('E', 'Selasa', '07:00', '08:39'),
        ('F', 'Kamis', '07:00', '08:39'),
        ('G', 'Senin', '09:30', '11:09'),
    ]
}

# Cari dan cetak jadwal yang optimal
optimal_schedule = find_schedule(classes)
print_schedule(optimal_schedule)
