# def tambah(bil1, bil2):
#     return bil1 + bil2

# print(tambah(2,3))

# def love(cowo, cewe):
#     return cowo+ " love " +cewe

# print(love("william", "sherlock"))

# print(2+(8-1)*5)

# i = 0  #deklarasi variabel
# while i < 5: #kondisi
#     print("luna") #program/perintah
#     i += 2 #iterasi


# nama = "gfuhjvht"

# for i in nama:
#     print(i)

# import ascii_magic as AsciiArt

# art = AsciiArt.from_image("totoro.png")
# art.to_terminal(columns=120)

import turtle

# # Membuat objek turtle
# t = turtle.Turtle()
# t.speed(0)  # Set kecepatan menjadi maksimum

# # Mengubah warna pengisi dan garis
# t.color('red', 'red')

# # Mengatur posisi awal
# t.penup()
# t.goto(0, -200)
# t.pendown()

# # Memulai menggambar
# t.begin_fill()

# # Menggambar setengah lingkaran atas
# t.left(140)
# t.forward(224)
# for i in range(200):
#     t.right(1)
#     t.forward(2)

# # Memutar ke bawah
# t.left(120)
# for i in range(200):
#     t.right(1)
#     t.forward(2)

# # Mengakhiri pengisian warna
# t.end_fill()

# # Menutup jendela turtle saat di-klik
# turtle.done()

import turtle

# Membuat objek turtle
t = turtle.Turtle()
t.speed(0)  # Set kecepatan menjadi maksimum

# Mengubah warna pengisi dan garis
t.color('red', 'red')

# Mengatur posisi awal
t.penup()
t.goto(0, -200)
t.pendown()

# Memulai menggambar
t.begin_fill()

# Menggambar setengah lingkaran atas
t.circle(200, 180)

# Membuat tali hati
t.goto(0, 0)

# Menggambar setengah lingkaran bawah
t.circle(-200, 180)

# Mengakhiri pengisian warna
t.end_fill()

# Menutup jendela turtle saat di-klik
turtle.done()