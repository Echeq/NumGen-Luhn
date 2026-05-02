import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

def algoritmo_luhn(numero):
    suma = 0
    for i, d in enumerate(reversed(numero)):
        d = int(d) * (2 if i % 2 == 0 else 1)
        if d > 9: d -= 9
        suma += d
    return suma % 10 == 0

def identificar_marca(bin_code):
    if bin_code.startswith("4"): return "Visa"
    if bin_code[:2] in ["51","52","53","54","55"]: return "Mastercard"
    if bin_code[:2] in ["34","37"]: return "American Express"
    return "Aleatorio"

def formatear_numero(numero):
    return " ".join([numero[i:i+4] for i in range(0, len(numero), 4)])

def generar_tarjeta_completa(bin_base):
    while True:
        bin_proc = "".join([str(random.randrange(0, 10)) if c == "X" else c for c in bin_base])
        dif = 15 - len(bin_proc)
        if dif > 0: bin_proc += "".join([str(random.randrange(0, 10)) for _ in range(dif)])
        elif dif < 0: bin_proc = bin_proc[:15]
        for ch in range(10):
            test = bin_proc + str(ch)
            if algoritmo_luhn(test): return test

def generar_cvv_random():
    return f"{random.randrange(0, 1000):03d}"

class TarjetaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador Luhn - Educativo")
        self.root.geometry("420x450")
        self.root.configure(bg="#f0f0f0")

        main = ttk.Frame(root, padding="12")
        main.pack(fill=tk.BOTH, expand=True)
        ttk.Label(main, text="Generador de Tarjetas Ficticias", font=("Arial", 11, "bold")).pack(pady=(0, 8))

        cfg = ttk.LabelFrame(main, text="Configuracion", padding="10")
        cfg.pack(fill=tk.X, pady=(0, 8))

        ttk.Label(cfg, text="BIN (IIN):").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.bin_var = tk.StringVar(value="4")
        ttk.Entry(cfg, textvariable=self.bin_var, width=25).grid(row=0, column=1, sticky=tk.W, padx=(8, 0), pady=3)
        ttk.Label(cfg, text="(X=aleatorio)").grid(row=0, column=2, sticky=tk.W, padx=(5, 0))

        ttk.Label(cfg, text="Fecha:").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.mes_var = tk.StringVar(value="12")
        self.mes_combo = ttk.Combobox(cfg, textvariable=self.mes_var, width=5, state="readonly")
        self.mes_combo["values"] = [f"{i:02d}" for i in range(1, 13)]
        self.mes_combo.current(11)
        self.mes_combo.grid(row=1, column=1, sticky=tk.W, padx=(8, 0), pady=3)
        ttk.Label(cfg, text="/").grid(row=1, column=1, padx=(50, 0), sticky=tk.W)

        self.ano_var = tk.StringVar()
        self.ano_combo = ttk.Combobox(cfg, textvariable=self.ano_var, width=5, state="readonly")
        anos = [str(datetime.now().year + i)[-2:] for i in range(10)]
        self.ano_combo["values"] = anos
        self.ano_combo.current(0)
        self.ano_combo.grid(row=1, column=1, sticky=tk.W, padx=(75, 0), pady=3)

        ttk.Label(cfg, text="CVV:").grid(row=2, column=0, sticky=tk.W, pady=3)
        self.cvv_var = tk.StringVar()
        self.cvv_entry = ttk.Entry(cfg, textvariable=self.cvv_var, width=18)
        self.cvv_entry.grid(row=2, column=1, sticky=tk.W, padx=(8, 0), pady=3)
        self.cvv_entry.insert(0, "XXX")
        self.cvv_entry.bind("<FocusIn>", lambda e: self.cvv_entry.delete(0, tk.END))
        self.cvv_entry.bind("<FocusOut>", self._ph_cvv)

        ttk.Label(cfg, text="Cantidad:").grid(row=3, column=0, sticky=tk.W, pady=3)
        self.cant_var = tk.StringVar(value="1")
        ttk.Entry(cfg, textvariable=self.cant_var, width=18).grid(row=3, column=1, sticky=tk.W, padx=(8, 0), pady=3)
        ttk.Button(cfg, text="GENERAR", command=self._generar).grid(row=4, column=0, columnspan=2, pady=10)

        res = ttk.LabelFrame(main, text="Resultados", padding="10")
        res.pack(fill=tk.BOTH, expand=True)
        scroll = ttk.Scrollbar(res, orient=tk.VERTICAL)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt = tk.Text(res, height=10, width=42, font=("Courier", 9), yscrollcommand=scroll.set, state=tk.DISABLED)
        self.txt.pack(fill=tk.BOTH, expand=True)
        scroll.config(command=self.txt.yview)

        ttk.Label(main, text="Solo con fines educativos", font=("Arial", 7), foreground="gray").pack(pady=(5, 0))
        btns = ttk.Frame(main)
        btns.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(btns, text="Limpiar", command=self._limpiar).pack(side=tk.LEFT, padx=2)
        ttk.Button(btns, text="Minimizar", command=self.root.iconify).pack(side=tk.LEFT, padx=2)
        ttk.Button(btns, text="Copiar", command=self._copiar).pack(side=tk.LEFT, padx=2)

    def _err(self, msg):
        self.txt.config(state=tk.NORMAL)
        self.txt.delete(1.0, tk.END)
        self.txt.insert(tk.END, msg + "\n")
        self.txt.config(state=tk.DISABLED)

    def _ph_cvv(self, e):
        if not self.cvv_var.get(): self.cvv_entry.insert(0, "XXX")

    def _generar(self):
        self.txt.config(state=tk.NORMAL)
        self.txt.delete(1.0, tk.END)
        self.txt.config(state=tk.DISABLED)
        try:
            b = self.bin_var.get().strip().upper()
            if not b or not all(c.isdigit() or c == "X" for c in b):
                self._err("BIN invalido (solo numeros o X)"); return

            tmp = b.replace("X", "0")[:15]
            marca = identificar_marca(tmp) if len(tmp) >= 2 else "Aleatorio"

            c = self.cant_var.get().strip()
            if not c.isdigit():
                self._err("Cantidad invalida (solo numeros)"); return
            cant = max(1, min(int(c), 100))

            fecha = f"{self.mes_var.get()}/{self.ano_var.get()}"

            cvv = self.cvv_var.get().strip().upper()
            if cvv == "" or cvv == "XXX":
                rnd_cvv = True
            else:
                if "X" in cvv or not cvv.isdigit() or len(cvv) < 3:
                    self._err("CVV invalido: use 3 digitos, XXX, o deje vacio"); return
                rnd_cvv = False

            self.txt.config(state=tk.NORMAL)
            self.txt.insert(tk.END, f"--- BIN: {b} | {marca} ---\n\n")
            for _ in range(cant):
                num = generar_tarjeta_completa(b)
                cvv_o = generar_cvv_random() if rnd_cvv else cvv
                self.txt.insert(tk.END, f"Numero: {formatear_numero(num)}\n")
                self.txt.insert(tk.END, f"  Fecha: {fecha} | CVV: {cvv_o}\n\n")
            self.txt.see(tk.END)
            self.txt.config(state=tk.DISABLED)
        except Exception as e:
            self.txt.config(state=tk.NORMAL)
            self.txt.insert(tk.END, f"Error: {e}\n")
            self.txt.config(state=tk.DISABLED)

    def _limpiar(self):
        self.txt.config(state=tk.NORMAL)
        self.txt.delete(1.0, tk.END)
        self.txt.config(state=tk.DISABLED)

    def _copiar(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.txt.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    TarjetaGUI(root)
    root.mainloop()