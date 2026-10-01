# 1. Array
mahasiswa = ["Andi", "Budi", "Citra", "Deni"]

print("Data mahasiswa:")
for nama in mahasiswa:
    print(nama)


# 2. Stack untuk fitur Undo
stack_undo = []

stack_undo.append("Tambah data Andi")
stack_undo.append("Tambah data Budi")
stack_undo.append("Edit data Citra")

print("\nUndo:")
print(stack_undo.pop())


# 3. Queue untuk sistem antrean
from collections import deque

queue = deque()

queue.append("Mahasiswa A")
queue.append("Mahasiswa B")
queue.append("Mahasiswa C")

print("\nAntrean:")
print(queue.popleft())


# 4. Hash Table untuk pencarian berdasarkan key
data_mahasiswa = {
    "23001": "Andi",
    "23002": "Budi",
    "23003": "Citra"
}

nim = "23002"

print("\nPencarian berdasarkan NIM:")
print(data_mahasiswa[nim])