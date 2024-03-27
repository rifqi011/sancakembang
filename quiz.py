import random

kunci = random.randint(1, 10)

jawaban = input("Pilihlah angka acak (1-10): ")

if jawaban == kunci:
    print("benar")
else:
    print("salah")