#bu kod tkinter da direkt fonksiyonlarla çağırabilsin diye fonksiyonlara ayrılmış halidir.
#burada tusları input olarak almadık cunku bunun gibi özellikleri tkinter da alıcaz burada sadece fonksiyonlar var.
#...



import random

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
         
    