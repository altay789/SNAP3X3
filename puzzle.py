import tkinter as tk
from mantik import gorsel_hazirla, inversion_kontrol
import random
from mantik import en_kisa_yol
import time



# --- BAŞLANGIÇ AYARLARI ---
liste = [1, 2, 3, 4, 5, 6, 7, 0, 8]
hedef = [1, 2, 3, 4, 5, 6, 7, 8, 0]
hamle_sayisi = 0
butonlar = []
baslangic_zamani = 0
def guncelle():
    for i in range(9):
        val = liste[i]

        if gorsel_parcalari:

            butonlar[i].config(image=gorsel_parcalari[val], text="")

            if val == 0:
                butonlar[i].config(state="disabled", bd=0, highlightthickness=0)
            else:
                renk = "#82E0AA" if val == hedef[i] else "#F1948A"
                butonlar[i].config(bg=renk, state="normal", bd=0, highlightthickness=2)
        else:
            butonlar[i].config(text=str(val) if val != 0 else "", font=("Arial", 18))


def hareket(i):
    global hamle_sayisi
    bos = liste.index(0)
    # Satır/Sütun farkından komşu kontrolü
    if abs(bos // 3 - i // 3) + abs(bos % 3 - i % 3) == 1:
        liste[bos], liste[i] = liste[i], liste[bos]
        hamle_sayisi += 1
        guncelle()

        if liste == hedef:
            sure = time.time() - baslangic_zamani
            sonuc_label.config(text=f"Kazandın! Hamle: {hamle_sayisi} Süre: {int(sure)} saniye", fg="green")




def karistir():
    global baslangic_zamani
    baslangic_zamani = time.time()
    global hamle_sayisi
    hamle_sayisi = 0
    sonuc_label.config(text="")
    while True:
        random.shuffle(liste)
        if inversion_kontrol(liste) and liste != hedef:
            break
    guncelle()
    kalan = en_kisa_yol(liste)
    kalan_label.config(text=f"En kısa yol: {kalan} hamle")


# --- ARAYÜZ ---
pencere = tk.Tk()
pencere.title("Snap3X3 - Görsel Puzzle")
pencere.geometry("450x600")
pencere.config(bg="#18182F")

gorsel_parcalari = gorsel_hazirla("gorsel1.jpg")

oyun_alani = tk.Frame(pencere, bg="#292054")
oyun_alani.pack(pady=20)
baslik_label = tk.Label(pencere, text="", font=("Segoe UI Black", 28, "bold"), bg="#1A1C29", fg="#F4D35E")
baslik_label.pack(pady=10)

hedef_metin = "SNAP 3X3"


def harf_harf_yaz(indeks=0):
    if indeks < len(hedef_metin):
        mevcut_metin = baslik_label.cget("text")
        baslik_label.config(text=mevcut_metin + hedef_metin[indeks])

        pencere.after(150, harf_harf_yaz, indeks + 1)


harf_harf_yaz()

for i in range(9):
    btn = tk.Button(oyun_alani, width=100, height=100, command=lambda x=i: hareket(x))
    btn.grid(row=i // 3, column=i % 3, padx=1, pady=1)
    butonlar.append(btn)

karistir_btn = tk.Button(pencere, text="↻ Oyunu Karıştır", command=karistir,
                         bg="#EE964B", fg="white", font=("Montserrat", 12, "bold"), relief="flat")
karistir_btn.pack(pady=10)

sonuc_label = tk.Label(pencere, text="", bg="#18182F", font=("Arial", 12, "bold"))
sonuc_label.pack()
kalan_label = tk.Label(pencere, text="", bg="#18182F", fg="white", font=("Arial", 12))
kalan_label.pack()

guncelle()
pencere.mainloop()
