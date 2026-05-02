import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime
import os

translations = {
    "en": {
        "title": "NumGen - Card Generator",
        "header": "NumGen - Card Generator",
        "warn": "FOR EDUCATIONAL USE ONLY - Illegal use prohibited",
        "config": "Configuration",
        "bin": "BIN:",
        "date": "Date:",
        "cvv": "CVV:",
        "qty": "Quantity:",
        "generate": "GENERATE",
        "results": "Results",
        "clear": "Clear",
        "minimize": "Minimize",
        "copy": "Copy",
        "export": "Export",
        "err_bin": "BIN invalid (numbers or X only)",
        "err_bin_luhn": "ERROR BIN INVALID",
        "err_qty": "Invalid quantity (numbers only)",
        "err_cvv": "CVV invalid: use 3 digits, XXX, or leave empty",
        "error": "Error",
        "brand": "Random",
        "lang": "Language",
        "about": "About",
        "exported": "Exported",
    },
    "es": {
        "title": "NumGen - Generador de Tarjetas",
        "header": "NumGen - Generador de Tarjetas",
        "warn": "SOLO PARA USO EDUCACIONAL - Uso ilicito prohibido",
        "config": "Configuracion",
        "bin": "BIN:",
        "date": "Fecha:",
        "cvv": "CVV:",
        "qty": "Cantidad:",
        "generate": "GENERAR",
        "results": "Resultados",
        "clear": "Limpiar",
        "minimize": "Minimizar",
        "copy": "Copiar",
        "export": "Exportar",
        "err_bin": "BIN invalido (solo numeros o X)",
        "err_bin_luhn": "ERROR BIN NO VALIDO",
        "err_qty": "Cantidad invalida (solo numeros)",
        "err_cvv": "CVV invalido: use 3 digitos, XXX, o deje vacio",
        "error": "Error",
        "brand": "Aleatorio",
        "lang": "Idioma",
        "about": "Acerca de",
        "exported": "Exportado",
    },
    "pt": {
        "title": "NumGen - Gerador de Cartoes",
        "header": "NumGen - Gerador de Cartoes",
        "warn": "APENAS PARA USO EDUCACIONAL - Uso ilegal proibido",
        "config": "Configuracao",
        "bin": "BIN:",
        "date": "Data:",
        "cvv": "CVV:",
        "qty": "Quantidade:",
        "generate": "GERAR",
        "results": "Resultados",
        "clear": "Limpar",
        "minimize": "Minimizar",
        "copy": "Copiar",
        "export": "Exportar",
        "err_bin": "BIN invalido (apenas numeros ou X)",
        "err_bin_luhn": "ERRO BIN INVALIDO",
        "err_qty": "Quantidade invalida (apenas numeros)",
        "err_cvv": "CVV invalido: use 3 digitos, XXX, ou deixe vazio",
        "error": "Erro",
        "brand": "Aleatorio",
        "lang": "Idioma",
        "about": "Sobre",
        "exported": "Exportado",
    },
    "ru": {
        "title": "NumGen - Генератор Карт",
        "header": "NumGen - Генератор Карт",
        "warn": "ТОЛЬКО ДЛЯ ОБРАЗОВАНИЯ - Незаконное использование запрещено",
        "config": "Конфигурация",
        "bin": "BIN:",
        "date": "Дата:",
        "cvv": "CVV:",
        "qty": "Количество:",
        "generate": "СОЗДАТЬ",
        "results": "Результаты",
        "clear": "Очистить",
        "minimize": "Свернуть",
        "copy": "Копировать",
        "export": "Экспорт",
        "err_bin": "BIN недействителен (только цифры или X)",
        "err_bin_luhn": "ОШИБКА BIN НЕДЕЙСТВИТЕЛЕН",
        "err_qty": "Неверное количество (только цифры)",
        "err_cvv": "CVV недействителен: используйте 3 цифры, XXX, или оставьте пустым",
        "error": "Ошибка",
        "brand": "Случайный",
        "lang": "Язык",
        "about": "О программе",
        "exported": "Экспортировано",
    },
    "zh": {
        "title": "NumGen - 卡片生成器",
        "header": "NumGen - 卡片生成器",
        "warn": "仅供教育用途 - 禁止非法使用",
        "config": "配置",
        "bin": "BIN:",
        "date": "日期:",
        "cvv": "CVV:",
        "qty": "数量:",
        "generate": "生成",
        "results": "结果",
        "clear": "清除",
        "minimize": "最小化",
        "copy": "复制",
        "export": "导出",
        "err_bin": "BIN无效（仅数字或X）",
        "err_bin_luhn": "错误 BIN无效",
        "err_qty": "数量无效（仅数字）",
        "err_cvv": "CVV无效：请使用3位数字、XXX、或留空",
        "error": "错误",
        "brand": "随机",
        "lang": "语言",
        "about": "关于",
        "exported": "已导出",
    },
}

def algoritmo_luhn(numero):
    suma = 0
    for i, d in enumerate(reversed(numero)):
        d = int(d) * (2 if i % 2 == 0 else 1)
        if d > 9: d -= 9
        suma += d
    return suma % 10 == 0

def identificar_marca(bin_code):
    first = bin_code[0] if bin_code else ""
    if first == "3": return "American Express"
    if first == "4": return "Visa"
    if first == "5": return "Mastercard"
    if first == "6": return "Discover"
    if bin_code[:2] in ["51","52","53","54","55"]: return "Mastercard"
    if bin_code[:2] in ["34","37"]: return "American Express"
    return "Random"

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
        self.lang = "en"
        self.t = translations["en"]
        self._build_ui()

    def _build_ui(self):
        self.root.title(self.t["title"])
        self.root.geometry("430x480")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        lang_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=self.t["lang"], menu=lang_menu)
        lang_menu.add_command(label="English", command=lambda: self._set_lang("en"))
        lang_menu.add_command(label="Espanol", command=lambda: self._set_lang("es"))
        lang_menu.add_command(label="Portugues", command=lambda: self._set_lang("pt"))
        lang_menu.add_command(label="Ruskiy", command=lambda: self._set_lang("ru"))
        lang_menu.add_command(label="Zhongwen", command=lambda: self._set_lang("zh"))

        about_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=self.t["about"], menu=about_menu)
        about_menu.add_command(label=self.t["about"], command=self._show_about)

        main = ttk.Frame(self.root, padding="10")
        main.pack(fill=tk.BOTH, expand=True)
        ttk.Label(main, text=self.t["header"], font=("Arial", 12, "bold")).pack(pady=(0, 5))
        ttk.Label(main, text=self.t["warn"], font=("Arial", 7), foreground="red").pack(pady=(0, 5))

        cfg = ttk.LabelFrame(main, text=self.t["config"], padding="10")
        cfg.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(cfg, text=self.t["bin"]).grid(row=0, column=0, sticky=tk.W, pady=4)
        self.bin_var = tk.StringVar(value="4000XXXXXXXXXXXX")
        ttk.Entry(cfg, textvariable=self.bin_var, width=25).grid(row=0, column=1, columnspan=2, sticky=tk.W, padx=(8, 0), pady=4)

        ttk.Label(cfg, text=self.t["date"]).grid(row=1, column=0, sticky=tk.W, pady=4)
        self.mes_var = tk.StringVar(value="RND")
        self.mes_combo = ttk.Combobox(cfg, textvariable=self.mes_var, width=4, state="readonly")
        self.mes_combo["values"] = ["RND"] + [f"{i:02d}" for i in range(1, 13)]
        self.mes_combo.current(0)
        self.mes_combo.grid(row=1, column=1, sticky=tk.W, padx=(8, 0), pady=4)

        self.ano_var = tk.StringVar(value="RND")
        self.ano_combo = ttk.Combobox(cfg, textvariable=self.ano_var, width=4, state="readonly")
        anos = [str(datetime.now().year + i)[-2:] for i in range(10)]
        self.ano_combo["values"] = ["RND"] + anos
        self.ano_combo.current(0)
        self.ano_combo.grid(row=1, column=2, sticky=tk.W, padx=(5, 0), pady=4)

        ttk.Label(cfg, text=self.t["cvv"]).grid(row=2, column=0, sticky=tk.W, pady=4)
        self.cvv_var = tk.StringVar()
        self.cvv_entry = ttk.Entry(cfg, textvariable=self.cvv_var, width=18)
        self.cvv_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=(8, 0), pady=4)
        self.cvv_entry.insert(0, "XXX")
        self.cvv_entry.bind("<FocusIn>", lambda e: self.cvv_entry.delete(0, tk.END))
        self.cvv_entry.bind("<FocusOut>", self._ph_cvv)

        ttk.Label(cfg, text=self.t["qty"]).grid(row=3, column=0, sticky=tk.W, pady=4)
        self.cant_var = tk.StringVar(value="1")
        ttk.Entry(cfg, textvariable=self.cant_var, width=18).grid(row=3, column=1, columnspan=2, sticky=tk.W, padx=(8, 0), pady=4)

        btn_frame = ttk.Frame(cfg)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=12)
        self.btn_generate = ttk.Button(btn_frame, text=self.t["generate"], command=self._generar)
        self.btn_generate.pack(side=tk.LEFT, padx=2)
        self.btn_export = ttk.Button(btn_frame, text=self.t["export"], command=self._export, state=tk.DISABLED)
        self.btn_export.pack(side=tk.LEFT, padx=2)

        res = ttk.LabelFrame(main, text=self.t["results"], padding="8")
        res.pack(fill=tk.BOTH, expand=True)

        scroll = ttk.Scrollbar(res, orient=tk.VERTICAL)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt = tk.Text(res, height=12, width=42, font=("Courier", 9), yscrollcommand=scroll.set, state=tk.DISABLED)
        self.txt.pack(fill=tk.BOTH, expand=True)
        scroll.config(command=self.txt.yview)
        self.txt.bind("<Double-Button-1>", self._on_double_click)

        btns = ttk.Frame(main)
        btns.pack(fill=tk.X, pady=(8, 0))
        ttk.Button(btns, text=self.t["clear"], command=self._limpiar).pack(side=tk.LEFT, padx=2)
        ttk.Button(btns, text=self.t["minimize"], command=self.root.iconify).pack(side=tk.LEFT, padx=2)
        ttk.Button(btns, text=self.t["copy"], command=self._copiar).pack(side=tk.LEFT, padx=2)

    def _set_lang(self, lang):
        self.lang = lang
        self.t = translations[lang]
        for widget in self.root.winfo_children():
            widget.destroy()
        self._build_ui()

    def _show_about(self):
        about_win = tk.Toplevel(self.root)
        about_win.title(self.t["about"])
        about_win.geometry("400x280")
        about_win.resizable(False, False)

        ttk.Label(about_win, text="NumGen", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(about_win, text="Card Generator with Luhn Validation", font=("Arial", 10)).pack()

        info = f"""Created by: Elvis Enrique Chen Qiu (Echeq)

GitHub: github.com/Echeq
LinkedIn: linkedin.com/in/echeq/

This is open source software - 2026

DISCLAIMER:
This software is for EDUCATIONAL purposes only.
It is ILLEGAL to use for:
- Fraudulent activities
- Real credit cards
- Any illicit purpose

Using this software for illegal activities
is strictly prohibited."""
        ttk.Label(about_win, text=info, justify=tk.CENTER).pack(pady=20)
        ttk.Button(about_win, text="OK", command=about_win.destroy).pack(pady=10)

    def _err(self, msg):
        self.txt.config(state=tk.NORMAL)
        self.txt.delete(1.0, tk.END)
        self.txt.insert(tk.END, msg + "\n")
        self.txt.config(state=tk.DISABLED)

    def _ph_cvv(self, e):
        if not self.cvv_var.get(): self.cvv_entry.insert(0, "XXX")

    def _on_double_click(self, event):
        self.txt.config(state=tk.NORMAL)
        self.txt.tag_remove(tk.SEL, "1.0", tk.END)
        try:
            pos = self.txt.index("@%s,%s" % (event.x, event.y))
            line_start = self.txt.index("%s linestart" % pos)
            line_end = self.txt.index("%s lineend" % pos)
            line = self.txt.get(line_start, line_end)
            bin_part = line.split("|")[0]
            bin_start = line_start
            bin_end = line_start + "+%dc" % len(bin_part)
            self.txt.tag_add(tk.SEL, bin_start, bin_end)
            self.txt.mark_set(tk.INSERT, bin_start)
            self.txt.see(bin_start)
        except:
            pass
        self.txt.config(state=tk.DISABLED)

    def _generar(self):
        self.txt.config(state=tk.NORMAL)
        self.txt.delete(1.0, tk.END)
        self.txt.config(state=tk.DISABLED)
        try:
            b = self.bin_var.get().strip().upper()
            if not b or not all(c.isdigit() or c == "X" for c in b) or "-" in b:
                self._err(self.t["err_bin"]); return

            if "X" not in b:
                dif = 16 - len(b)
                if dif > 0:
                    b = b + "X" * dif

            tmp = b.replace("X", "0")[:15]
            if "X" not in b and tmp and not algoritmo_luhn(tmp + "0"):
                self._err(self.t["err_bin_luhn"]); return
            marca = identificar_marca(tmp) if len(tmp) >= 2 else self.t["brand"]

            c = self.cant_var.get().strip()
            if not c.isdigit() or "-" in c:
                self._err(self.t["err_qty"]); return
            cant = max(1, min(int(c), 999999999))

            mes = self.mes_var.get()
            ano = self.ano_var.get()
            if mes == "RND":
                mes = f"{random.randrange(1, 13):02d}"
            if ano == "RND":
                ano = str(random.randrange(int(datetime.now().year), int(datetime.now().year) + 10))[-2:]

            cvv = self.cvv_var.get().strip().upper()
            if cvv == "" or cvv == "XXX":
                rnd_cvv = True
            else:
                if "X" in cvv or not cvv.isdigit() or len(cvv) != 3 or "-" in cvv:
                    self._err(self.t["err_cvv"]); return
                rnd_cvv = False

            self.txt.config(state=tk.NORMAL)
            self.txt.insert(tk.END, f"--- BIN: {b} | {marca} ---\n\n")
            for _ in range(cant):
                num = generar_tarjeta_completa(b)
                cvv_o = generar_cvv_random() if rnd_cvv else cvv
                self.txt.insert(tk.END, f"{num}|{mes}|20{ano}|{cvv_o}\n")
            self.txt.see(tk.END)
            self.txt.config(state=tk.DISABLED)
            self.btn_export.config(state=tk.NORMAL)
        except Exception as e:
            self.txt.config(state=tk.NORMAL)
            self.txt.insert(tk.END, f"{self.t['error']}: {e}\n")
            self.txt.config(state=tk.DISABLED)

    def _limpiar(self):
        self.txt.config(state=tk.NORMAL)
        self.txt.delete(1.0, tk.END)
        self.txt.config(state=tk.DISABLED)
        self.btn_export.config(state=tk.DISABLED)

    def _copiar(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.txt.get(1.0, tk.END))

    def _export(self):
        content = self.txt.get(1.0, tk.END).strip()
        if not content:
            return
        lines = content.split("\n")
        bin_used = ""
        output_lines = []
        for line in lines:
            if "|" in line and not line.startswith("---"):
                parts = line.split("|")
                if len(parts) >= 4:
                    output_lines.append(line)
                    if not bin_used:
                        bin_used = parts[0]
        if not output_lines:
            return
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        now = datetime.now()
        fecha = now.strftime("%Y%m%d")
        hora = now.strftime("%H%M%S")
        bin_name = bin_used[:4] if bin_used else "BIN"
        filename = f"{bin_name}_{fecha}_{hora}.txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            f.write("\n".join(output_lines))
        self._err(self.t["exported"] + f" to output/{filename}")

if __name__ == "__main__":
    root = tk.Tk()
    TarjetaGUI(root)
    root.mainloop()