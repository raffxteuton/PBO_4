import tkinter as tk
import math

class Silinder(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.label_jari_jari = tk.Label(self, text="Masukkan Jari-jari")
        self.label_jari_jari.grid(row=0, column=0, sticky=tk.W)

        self.entry_jari_jari = tk.Entry(self)
        self.entry_jari_jari.grid(row=0, column=1, sticky=tk.W)

        self.label_tinggi = tk.Label(self, text="Masukkan Tinggi")
        self.label_tinggi.grid(row=1, column=0, sticky=tk.W)

        self.entry_tinggi = tk.Entry(self)
        self.entry_tinggi.grid(row=1, column=1, sticky=tk.W)

        self.button_hitung = tk.Button(self, text="Hitung", command=self.hitung)
        self.button_hitung.grid(row=2, column=0, sticky=tk.W)

        self.label_luas_permukaan = tk.Label(self, text="Luas Permukaan")
        self.label_luas_permukaan.grid(row=2, column=1, sticky=tk.W)

        self.label_luas_permukaan_hasil = tk.Label(self)
        self.label_luas_permukaan_hasil.grid(row=2, column=2, sticky=tk.W)

        self.label_volume = tk.Label(self, text="Volume")
        self.label_volume.grid(row=3, column=1, sticky=tk.W)

        self.label_volume_hasil = tk.Label(self)
        self.label_volume_hasil.grid(row=3, column=2, sticky=tk.W)

    def hitung(self):
        jari_jari = float(self.entry_jari_jari.get())
        tinggi = float(self.entry_tinggi.get())

        # Rumus luas permukaan silinder
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

        # Rumus volume silinder
        volume = math.pi * jari_jari ** 2 * tinggi

        # Mengatur label hasil perhitungan
        self.label_luas_permukaan_hasil.config(text=luas_permukaan)
        self.label_volume_hasil.config(text=volume)


root = tk.Tk()
app = Silinder(root)
app.pack()
root.mainloop()
