def obsah_obdelniku():
    a = int(input("Zadej velikost strany a v cm: "))
    b = int(input("Zadej velikost strany b v cm: "))
    if a > 0 and b > 0:
        obsah = a * b
        print(f"Obsah obdélníku o stranách {a} a {b} je {obsah}")
    else:
        print("Špatné hodnoty. Zkuste znovu.")
        obsah_obdelniku()

obsah_obdelniku()
