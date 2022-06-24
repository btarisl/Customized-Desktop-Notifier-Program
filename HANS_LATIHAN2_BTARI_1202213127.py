import os
os.system("cls")
print('='*14+' Rekomendasi Tempat Wisata di Indonesia '+'='*14)
class Kotawisata:
    def __init__(self, namakota,julukan,tempatwisata) :
        self.namakota = namakota
        self.julukan =julukan
        self.tempatwisata= tempatwisata

    def print_info(self):
        print (f'Nama Daerah \t: {self.namakota}')
        print (f'Julukan \t: {self.julukan}\Tempat Wisata \t: {self.tempatwisata}')
    
if __name__ == '__main__':
    kotanya = Kotawisata('Bandung','Kota Kembang','Dago Dream Park')
    kotanya.print_info()
    print()

if __name__ == '__main__':
    kotanya = Kotawisata('Bogor','Kota Hujan','Telaga Warna')
    kotanya.print_info()
    print()

if __name__ == '__main__':
    kotanya = Kotawisata('Yogyakarta','Kota Pelajar','Candi Pramabanan')
    kotanya.print_info()
    print()