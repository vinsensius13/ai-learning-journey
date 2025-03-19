# Menulis ke file
with open("data.txt", "w") as file:
    file.write("Ini adalah file pertama saya!\n")

# Membaca file
with open("data.txt", "r") as file:
    print("Isi file:", file.read())
