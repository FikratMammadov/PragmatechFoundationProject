mehsullar = []


class Mehsul():
    def __init__(self, _ad, _qiymet, _miqdar):
        self.ad = _ad
        self.qiymet = _qiymet
        self.miqdar = _miqdar
        mehsullar.append(self)

    def melumatGoster(self):
        print(f'{self.ad} | {self.qiymet} | {self.miqdar}' )
    


def istehsalEt():
    ad = input('Mehsulun adi: ')
    qiymet = int(input("Mehsulun qiymeti: "))
    miqdar = int(input("Mehsulun miqdari: "))
    mehsul = Mehsul(ad, qiymet, miqdar)


for say in range(5):
    istehsalEt()

def melumatlariGoster():
    for mehsul in mehsullar:
        mehsul.melumatGoster()

emr=input('Mehsullari gormek isteyirsizmi? Yes/No ')

if emr=='Yes':
    melumatlariGoster()

 
def qiymetCemi():
    cem=0
    for mehsul in mehsullar:
        cem+=mehsul.qiymet
    print(cem)

qiymetCemi()
