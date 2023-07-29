N = int(input())

if N < 2 and N > 20:
    print("Invalid Input")
else:
    angka = []
    for i in range(N):
        inputan = input()
        angka.append(int(inputan))
    kpk = angka[0]
    i = 1
    while i < len(angka):
        if kpk % angka[i] != 0:
            kpk += angka[0]
            i = 1
        else:
            i += 1
    print(kpk)
