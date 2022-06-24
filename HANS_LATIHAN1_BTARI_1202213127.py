import os
os.system("cls")
#menghitung volume kubus
sisi= float(int(input('Masukkan sisi : ')))
volume = lambda sisi:sisi**3

print(f"Volume kubus dengan sisi {sisi} adalah {volume(sisi)}")