
import tkinter as tk
from tkinter import simpledialog, messagebox

# Kullanıoı Verileri
class Antrenman:
    def __init__(self, isim, aciklama):
        self.isim = isim
        self.aciklama = aciklama

class Takip:
    def __init__(self, tarih, antrenman, notlar):
        self.tarih = tarih
        self.antrenman = antrenman
        self.notlar = notlar

class Sporcu:
    def __init__(self, isim, brans):
        self.isim = isim
        self.brans = brans
        self.antrenmanlar = []
        self.takipler = []

    def antrenman_ekle(self, antrenman):
        self.antrenmanlar.append(antrenman)

    def takip_ekle(self, takip):
        self.takipler.append(takip)

    def rapor_ver(self):
        if not self.takipler:
            return "Henüz takip yok."
        rapor = ""
        for t in self.takipler:
            rapor += f"{t.tarih} - {t.antrenman.isim}: {t.notlar}\n"
        return rapor

# Uygulama arayüzü 
class Uygulama:
    def __init__(self, pencere):
        self.sporcular = {}
        self.pencere = pencere
        self.pencere.title("Spor Takip Sistemi")

        self.cerceve = tk.Frame(pencere, padx=15, pady=15)
        self.cerceve.pack()

        tk.Button(self.cerceve, text="Sporcu Ekle", width=25, command=self.sporcu_ekle).pack(pady=3)
        tk.Button(self.cerceve, text="Antrenman Ekle", width=25, command=self.antrenman_ekle).pack(pady=3)
        tk.Button(self.cerceve, text="Takip Ekle", width=25, command=self.takip_ekle).pack(pady=3)
        tk.Button(self.cerceve, text="Rapor Göster", width=25, command=self.rapor_goster).pack(pady=3)
        tk.Button(self.cerceve, text="Çık", width=25, command=pencere.quit).pack(pady=3)

    def sporcu_ekle(self):
        isim = simpledialog.askstring("Sporcu", "Sporcunun adı:")
        if not isim:
            return
        if isim in self.sporcular:
            messagebox.showerror("Hata", "Bu sporcu zaten var.")
            return
        brans = simpledialog.askstring("Branş", "Spor dalı:")
        self.sporcular[isim] = Sporcu(isim, brans)
        messagebox.showinfo("Tamam", f"{isim} eklendi.")

    def antrenman_ekle(self):
        isim = simpledialog.askstring("Sporcu", "Sporcunun adı:")
        if isim not in self.sporcular:
            messagebox.showerror("Hata", "Sporcu yok.")
            return
        ant_ad = simpledialog.askstring("Antrenman", "Antrenman adı:")
        aciklama = simpledialog.askstring("Açıklama", "Kısa açıklama:")
        yeni_ant = Antrenman(ant_ad, aciklama)
        self.sporcular[isim].antrenman_ekle(yeni_ant)
        messagebox.showinfo("Tamam", "Antrenman eklendi.")

    def takip_ekle(self):
        isim = simpledialog.askstring("Sporcu", "Sporcunun adı:")
        if isim not in self.sporcular:
            messagebox.showerror("Hata", "Sporcu yok.")
            return

        sp = self.sporcular[isim]
        if not sp.antrenmanlar:
            messagebox.showwarning("Uyarı", "Önce antrenman girin.")
            return

        tarih = simpledialog.askstring("Tarih", "Tarih (örnek: 25.04.2025)")
        ant_liste = "\n".join([f"{i}: {a.isim}" for i, a in enumerate(sp.antrenmanlar)])
        secim = simpledialog.askinteger("Antrenman Seç", f"Antrenman numarası:\n{ant_liste}")
        if secim is None or secim >= len(sp.antrenmanlar):
            messagebox.showerror("Hata", "Geçersiz.")
            return

        notlar = simpledialog.askstring("Not", "Kısa yorum:")
        takip = Takip(tarih, sp.antrenmanlar[secim], notlar)
        sp.takip_ekle(takip)
        messagebox.showinfo("Tamam", "Takip eklendi.")

    def rapor_goster(self):
        isim = simpledialog.askstring("Sporcu", "Sporcunun adı:")
        if isim not in self.sporcular:
            messagebox.showerror("Hata", "Sporcu yok.")
            return
        rapor = self.sporcular[isim].rapor_ver()
        messagebox.showinfo("Rapor", rapor)

#    Uygulamayı Başlatabilirsiniz
if __name__ == "__main__":
    pencere = tk.Tk()
    app = Uygulama(pencere)
    pencere.mainloop()
