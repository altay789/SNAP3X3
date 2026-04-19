import random
import os



liste=[1,2,3,4,5,6,7,0,8]
hedef=[1,2,3,4,5,6,7,8,0]
hamle_sayisi=0 


while True:


    while True:
        random.shuffle(liste)
        s = [x for x in liste if x != 0]
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]>s[j]:
                    count=count+1

        if count%2==0:
            break



    while liste != hedef:
        os.system("cls" if os.name == "nt" else "clear")
        s = [x for x in liste if x != 0]
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] > s[j]:
                    count = count + 1
        print("inversion:", count)
        
        
        print("\n\n")
        for i in range(9):
            if liste[i] == 0:
                print("[]", end=" ")
            else:
                print(liste[i], end=" ")
            if (i+1) % 3 == 0:
                print()
        bos = liste.index(0)
        satir = bos // 3
        sutun = bos % 3
        tus = input("w,a,s,d ???")
        hamle_sayisi+=1
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
            print("Geçersiz tuş!")
            continue
        if 0 <= yeni_satir <= 2 and 0 <= yeni_sutun <= 2:
            yeni_index = yeni_satir * 3 + yeni_sutun
            temp = liste[bos]
            liste[bos] = liste[yeni_index]
            liste[yeni_index] = temp
        else:
            print("O yöne gidemezsin!")

    print("Tebrikler kazandin!")
    print(f"Hamle sayisi: {hamle_sayisi}")

    print("Tekrar oynamak isterim/1\nbitir/2")
    secim=int(input("seciminizi giriniz:"))
    if secim==1:
        continue
    else:
        break
    
