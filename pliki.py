PATH = r"F:\szkolenie_luty01\nowy2.txt"
# uchwyt = open("dane.txt","r", encoding="utf-8")
# uchwyt2 = open(r"F:\szkolenie_luty01\nowy.txt","w")
# uchwyt2 = open(PATH, "r")
# uchwyt2.write("Zapis do pliku, został dokonany!")
# dane = uchwyt2.read(1024)
# print(dane)
# uchwyt2.close()

try:
    with open(PATH, "r") as uchwyt3:
        for linia in uchwyt3:
            print(linia, end="")
except IOError:
    print("Plik nie istnieje, lub zła nazwa!")


