jezyk = "Pythona"
pytanie = "Czy lubisz %s" % jezyk
print(pytanie)

wersja = 3.8

print("Używam wersji Pythona: %i" % wersja)
print("Używam wersji Pythona: %f" % wersja)
print("Używam wersji Pythona: %.1f" % wersja)
print("Używam wersji Pythona: %.f" % wersja)

print("Lubię %(jezyk)s" % {"jezyk": "Jave"})

print(f"Lubię {jezyk}")
print("Lubię {0} i {1}".format("Pythona", "Jave"))
