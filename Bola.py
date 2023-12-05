import tkinter as tk
import math

class Bola(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.label_jari_jari = tk.Label(self, text="Masukkan Jari-jari")
        self.label_jari_jari.grid(row=0, column=0, sticky=tk.W)

        self.entry_jari_jari = tk.Entry(self)
        self.entry_jari_jari.grid(row=0, column=1, sticky=tk.W)

        self.button_hitung = tk.Button(self, text="Hitung", command=self.hitung)
        self.button_hitung.grid(row=1, column=0, sticky=tk.W)

        self.label_volume = tk.Label(self, text="Volume")
        self.label_volume.grid(row=1, column=1, sticky=tk.W)

        self.label_volume_hasil = tk.Label(self)
        self.label_volume_hasil.grid(row=1, column=2, sticky=tk.W)

        self.label_luas_permukaan = tk.Label(self, text="Luas Permukaan")
        self.label_luas_permukaan.grid(row=2, column=1, sticky=tk.W)

        self.label_luas_permukaan_hasil = tk.Label(self)
        self.label_luas_permukaan_hasil.grid(row=2, column=2, sticky=tk.W)

    def hitung(self):
        jari_jari = float(self.entry_jari_jari.get())

        # Rumus volume bola
        volume = (4 / 3) * math.pi * jari_jari ** 3

        # Rumus luas permukaan bola
        luas_permukaan = 4 * math.pi * jari_jari ** 2

        # Mengatur label hasil perhitungan
        self.label_volume_hasil.config(text=volume)
        self.label_luas_permukaan_hasil.config(text=luas_permukaan)


root = tk.Tk()
app = Bola(root)
app.pack()
root.mainloop()
