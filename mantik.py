#bu kod tkinter da direkt fonksiyonlarla çağırabilsin diye fonksiyonlara ayrılmış halidir.
#burada tusları input olarak almadık cunku bunun gibi özellikleri tkinter da alıcaz burada sadece fonksiyonlar var.
#...



import random
import heapq
import time

hedef=[1,2,3,4,5,6,7,8,0]
liste=[1,2,3,4,5,6,7,8,0]


def karistir(liste):
   
    while True:
        random.shuffle(liste)
        s = [x for x in liste if x != 0]
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]>s[j]:
                    count=count+1

        if count%2==0:
            return liste

def inversion(liste):
    s=[x for x in liste if x != 0]
    count=0 
    for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]>s[j]:
                    count=count+1
    return count                
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
def hareket_ettirme(liste,tus):
    bos = liste.index(0)
    satir=bos//3
    sutun=bos%3
    if tus == "w":
            yeni_satir = satir + 1
            yeni_sutun = sutun
    elif tus == "a":
            yeni_sutun = sutun + 1
            yeni_satir = satir
    elif tus == "s":
            yeni_satir = satir - 1
            yeni_sutun = sutun
    elif tus == "d":
            yeni_sutun = sutun - 1
            yeni_satir = satir
    else:
         return liste        
    if 0<=yeni_satir<=2 and 0<=yeni_sutun<=2:
         
        yeni_index = yeni_satir * 3 + yeni_sutun
        temp = liste[bos]
        liste[bos] = liste[yeni_index]
        liste[yeni_index] = temp
        return liste
         
    
