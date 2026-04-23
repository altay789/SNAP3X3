import tkinter as tk
from PIL import Image, ImageTk
import random

# --- BAŞLANGIÇ AYARLARI ---
liste = [1, 2, 3, 4, 5, 6, 7, 0, 8]
hedef = [1, 2, 3, 4, 5, 6, 7, 8, 0]
hamle_sayisi = 0
butonlar = []

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
                    
                    bos_resim = Image.new('RGB', (100, 100), color='#292054')
                    parcalar[0] = ImageTk.PhotoImage(bos_resim)
                    continue
                kutu = (j*genislik, i*genislik, (j+1)*genislik, (i+1)*genislik)
                kesik = img.crop(kutu)
                parcalar[sayi] = ImageTk.PhotoImage(kesik)
        return parcalar
    except Exception as e:
        print("Hata: Resim bulunamadı.", e)
        return None

# --- OYUN MANTIĞI ---
def inversion_kontrol(test_list):
    s = [x for x in test_list if x != 0]
    count = sum(1 for i in range(len(s)) for j in range(i+1, len(s)) if s[i] > s[j])
    return count % 2 == 0

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
    if abs(bos//3 - i//3) + abs(bos%3 - i%3) == 1:
        liste[bos], liste[i] = liste[i], liste[bos]
        hamle_sayisi += 1
        guncelle()
        if liste == hedef:
            sonuc_label.config(text=f"Kazandın! Hamle: {hamle_sayisi}", fg="green")

def karistir():
    global hamle_sayisi
    hamle_sayisi = 0
    sonuc_label.config(text="")
    while True:
        random.shuffle(liste)
        if inversion_kontrol(liste) and liste != hedef:
            break
    guncelle()

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
    btn.grid(row=i//3, column=i%3, padx=1, pady=1)
    butonlar.append(btn)

karistir_btn = tk.Button(pencere, text="↻ Oyunu Karıştır", command=karistir, 
                         bg="#EE964B", fg="white", font=("Montserrat", 12, "bold"), relief="flat")
karistir_btn.pack(pady=10)

sonuc_label = tk.Label(pencere, text="", bg="#18182F", font=("Arial", 12, "bold"))
sonuc_label.pack()

guncelle()
pencere.mainloop()
