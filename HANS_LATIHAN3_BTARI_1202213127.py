import os
os.system("cls")

sifat_wakhid= 'wibu'
sifatcalonjodoh= input('Masukkan Sifat Calon Jodoh: ')
def pasutricocoklogi(sifat_wakhid,sifatcalonjodoh):
    if sifat_wakhid==sifatcalonjodoh:
        print('Wakhid dan Jodoh cocok')
    if sifat_wakhid!=sifatcalonjodoh:
        print('Wakhid dan Jodoh tidak cocok')

pasutricocoklogi(sifat_wakhid,sifatcalonjodoh)