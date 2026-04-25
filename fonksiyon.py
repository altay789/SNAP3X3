from PIL import Image, ImageTk
import heapq
hedef=[1,2,3,4,5,6,7,8,0]


def gorsel_hazirla(yol):

    try:
        img = Image.open(yol)
        img = img.resize((300, 300))

        parcalar = [None] * 9
        genislik = 100

        for i in range(3):
            for j in range(3):
                sayi = i * 3 + j + 1
                if sayi == 9:
                    # Sağ alt köşe (boşluk) için düz renkli bir resim oluşturuyoruz
                    bos_resim = Image.new('RGB', (100, 100), color='#292054')
                    parcalar[0] = ImageTk.PhotoImage(bos_resim)
                    continue

                # Resmi kesme işlemi (sol, üst, sağ, alt)
                kutu = (j * genislik, i * genislik, (j + 1) * genislik, (i + 1) * genislik)
                kesik = img.crop(kutu)
                parcalar[sayi] = ImageTk.PhotoImage(kesik)

        return parcalar
    except Exception as e:
        print("Hata: Resim bulunamadı.", e)
        return None


def inversion_kontrol(test_list):

    s = [x for x in test_list if x != 0]
    count = sum(1 for i in range(len(s)) for j in range(i + 1, len(s)) if s[i] > s[j])
    return count % 2 == 0

def manhattan(liste):
    toplam=0
    for i, val in enumerate(liste):
        if val==0:
            continue
        hedef_index=val-1
        suan_satir=i//3  #satiri veririr.
        suan_sutun=i%3   #sütunu verir.
        hedef_satir=hedef_index//3
        hedef_sutun=hedef_index%3
        toplam+=abs(hedef_satir - suan_satir) + abs(hedef_sutun - suan_sutun)
    return toplam

def en_kisa_yol(liste):
    kuyruk = [(manhattan(liste), 0, tuple(liste))]
    ziyaret = {}
    
    while kuyruk:
        f, g, durum = heapq.heappop(kuyruk)
        
        if list(durum) == hedef:
            return g
        
        if durum in ziyaret:
            continue
        ziyaret[durum] = g
        
        bos = durum.index(0)
        satir, sutun = bos // 3, bos % 3
        
        for ds, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            ys, yc = satir+ds, sutun+dc
            if 0 <= ys < 3 and 0 <= yc < 3:
                yi = ys*3+yc
                lst = list(durum)
                lst[bos], lst[yi] = lst[yi], lst[bos]
                komsu = tuple(lst)
                yeni_g = g + 1
                yeni_f = yeni_g + manhattan(komsu)
                heapq.heappush(kuyruk, (yeni_f, yeni_g, komsu))
    
    return None
