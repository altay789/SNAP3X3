import tkinter as tk
import random

liste = [1,2,3,4,5,6,7,0,8]
hedef = [1,2,3,4,5,6,7,8,0]
hamle_sayisi = 0

pencere = tk.Tk()
pencere.title("8 Puzzle")

butonlar = []

def inversion_kontrol(liste):
    s = [x for x in liste if x != 0]
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] > s[j]:
                count += 1
    return count % 2 == 0

def karistir():
    global liste
    while True:
        random.shuffle(liste)
        if inversion_kontrol(liste):
            break
    guncelle()

def guncelle():
    for i in range(9):
        if liste[i] == 0:
            butonlar[i].config(text="", bg="lightgray")
        else:
            butonlar[i].config(text=str(liste[i]), bg="white")

def hareket(i):
    global hamle_sayisi

    bos = liste.index(0)

    # komşu mu kontrolü
    komsular = []
    satir = bos // 3
    sutun = bos % 3

    if satir > 0: komsular.append(bos - 3)
    if satir < 2: komsular.append(bos + 3)
    if sutun > 0: komsular.append(bos - 1)
    if sutun < 2: komsular.append(bos + 1)

    if i in komsular:
        liste[bos], liste[i] = liste[i], liste[bos]
        hamle_sayisi += 1
        guncelle()
        kontrol()

def kontrol():
    if liste == hedef:
        sonuc_label.config(text=f"Kazandın! Hamle: {hamle_sayisi}")

# BUTONLARI OLUŞTUR
for i in range(9):
    btn = tk.Button(pencere, text="", width=6, height=3,
                    command=lambda i=i: hareket(i))
    btn.grid(row=i//3, column=i%3)
    butonlar.append(btn)

# ALT KISIM
karistir_btn = tk.Button(pencere, text="Karıştır", command=karistir)
karistir_btn.grid(row=3, column=0, columnspan=3, sticky="we")

sonuc_label = tk.Label(pencere, text="")
sonuc_label.grid(row=4, column=0, columnspan=3)

karistir()
guncelle()

pencere.mainloop()
