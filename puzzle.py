import tkinter as tk
from fonksiyon import gorsel_hazirla, inversion_kontrol, en_kisa_yol
import random
import time

# --- PENCERE ---
pencere = tk.Tk()
pencere.title("Snap3X3 - Görsel Puzzle")
pencere.geometry("450x600")
pencere.config(bg="#18182F")

# --- DEĞİŞKENLER ---
liste = [1, 2, 3, 4, 5, 6, 7, 0, 8]
hedef = [1, 2, 3, 4, 5, 6, 7, 8, 0]
hamle_sayisi = 0
baslangic_zamani = 0
rekor = None

butonlar = []
gorsel_parcalari = []

# --- LABEL'lar ---
rekor_label = tk.Label(pencere, text="Rekor: -", bg="#18182F", fg="gold", font=("Arial", 12, "bold"))
rekor_label.pack()

sonuc_label = tk.Label(pencere, text="", bg="#18182F", font=("Arial", 12, "bold"))
sonuc_label.pack()

kalan_label = tk.Label(pencere, text="", bg="#18182F", fg="white", font=("Arial", 12))
kalan_label.pack()

# --- BAŞLIK ---
baslik_label = tk.Label(pencere, text="", font=("Segoe UI Black", 28, "bold"), bg="#1A1C29", fg="#F4D35E")
baslik_label.pack(pady=10)

hedef_metin = "SNAP 3X3"

def harf_harf_yaz(indeks=0):
    if indeks < len(hedef_metin):
        mevcut = baslik_label.cget("text")
        baslik_label.config(text=mevcut + hedef_metin[indeks])
        pencere.after(150, harf_harf_yaz, indeks + 1)

harf_harf_yaz()

# --- OYUN ALANI ---
oyun_alani = tk.Frame(pencere, bg="#292054")
oyun_alani.pack(pady=20)

for i in range(9):
    btn = tk.Button(oyun_alani, width=100, height=100, command=lambda x=i: hareket(x))
    btn.grid(row=i // 3, column=i % 3, padx=1, pady=1)
    butonlar.append(btn)

# --- FONKSİYONLAR ---

def guncelle():
    for i in range(9):
        val = liste[i]

        if gorsel_parcalari:
            butonlar[i].config(image=gorsel_parcalari[val], text="")
            butonlar[i].image = gorsel_parcalari[val]  # 🔥 ÖNEMLİ

            if val == 0:
                butonlar[i].config(state="disabled", bd=0)
            else:
                butonlar[i].config(state="normal", bd=1)

        else:
            butonlar[i].config(text=str(val) if val != 0 else "", font=("Arial", 18))


def hareket(i):
    global hamle_sayisi, rekor

    bos = liste.index(0)

    if abs(bos // 3 - i // 3) + abs(bos % 3 - i % 3) == 1:
        liste[bos], liste[i] = liste[i], liste[bos]
        hamle_sayisi += 1
        guncelle()

        if liste == hedef:
            sure = time.time() - baslangic_zamani

            # 🔥 REKOR KONTROLÜ
            if rekor is None or hamle_sayisi < rekor:
                rekor = hamle_sayisi

            rekor_label.config(text=f"Rekor: {rekor} hamle")

            sonuc_label.config(
                text=f"Kazandın! Hamle: {hamle_sayisi} Süre: {int(sure)} saniye",
                fg="green"
            )


def karistir():
    global hamle_sayisi, baslangic_zamani

    hamle_sayisi = 0
    baslangic_zamani = time.time()
    sonuc_label.config(text="")

    while True:
        random.shuffle(liste)
        if inversion_kontrol(liste) and liste != hedef:
            break

    guncelle()

    kalan = en_kisa_yol(liste)
    kalan_label.config(text=f"En kısa yol: {kalan} hamle")


# --- GÖRSEL ---
gorsel_parcalari = gorsel_hazirla("gorsel1.jpg")

# --- BUTON ---
karistir_btn = tk.Button(
    pencere,
    text="↻ Oyunu Karıştır",
    command=karistir,
    bg="#EE964B",
    fg="white",
    font=("Montserrat", 12, "bold")
)
karistir_btn.pack(pady=10)

# --- BAŞLAT ---
guncelle()
pencere.mainloop()
