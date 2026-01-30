import sys
import os
import json
import tkinter as tk
import customtkinter as ctk

# ===== RESOURCE PATH =====
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ===== CONFIG GLOBAL =====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BG_MAIN = "#0B0F19"
BG_CARD = "#111827"
GOLD = "#C8AA6E"
GOLD_LIGHT = "#E6D8A3"
BLUE = "#1E3A8A"

# ===== DADOS =====
def carregar_counters():
    try:
        caminho = resource_path("data/lolcounters.json")

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return dados
    except Exception as e:
        print("Erro ao carregar os dados dos counters:", e)
        return {}
counters = carregar_counters()

# ===== TOOLTIP =====
class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tip = None

    def show(self, text):
        if self.tip or not text:
            return

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tip = tk.Toplevel(self.widget)
        self.tip.overrideredirect(True)
        self.tip.configure(bg=BG_CARD)

        label = tk.Label(
            self.tip,
            text=text,
            bg=BG_CARD,
            fg=GOLD_LIGHT,
            padx=10,
            pady=5,
            font=("Segoe UI", 10)
        )
        label.pack()

        self.tip.geometry(f"+{x}+{y}")

    def hide(self, event=None):
        if self.tip:
            self.tip.destroy()
            self.tip = None

# ===== FUNÇÕES =====
def buscar_campeao(nome_digitado):
    nome_digitado = nome_digitado.lower().strip()
    list_resultado.delete(0, "end")

    for counter in counters:
        nome_json = counter["Campeão"].split("\n")[0].lower()
        print( nome_json, nome_digitado )

        if nome_json == nome_digitado:
            lista_counters = counter.get("Counters", [])
            filtrar_lane(lista_counters)
            return
    return list_resultado.insert("end", "Campeão não encontrado.")

def filtrar_lane(lista_counters):
    lane_selecionada = combo_lane.get()
    lista_counters_filtrada = []
    for counter in lista_counters:
        if counter.get("Lane") == lane_selecionada:
            lista_counters_filtrada.append(counter)
    mostrar_counters(lista_counters_filtrada)


def mostrar_counters(lista_counters_filtrada):
    list_resultado.delete(0, "end")
    for counter in lista_counters_filtrada:
        nome = counter["Campeão"]
        winrate = counter["Win Rate"]

        texto = f"{nome} - Win Rate: {winrate}%"

        list_resultado.insert("end", texto)


def atualizar_autocomplete(event=None):
    texto = entry_campeao.get().lower()
    list_campeoes.delete(0, "end")

    for ITEM in counters:
        nome = ITEM["Campeão"].split("\n")[0]
        if texto in nome.lower():
            list_campeoes.insert("end", nome)

def selecionar_campeao(event):
    try:
        selecionado = list_campeoes.get(list_campeoes.curselection())
        entry_campeao.delete(0, "end")
        entry_campeao.insert(0, selecionado)
        atualizar_lanes(selecionado)
    except:
        pass

def atualizar_lanes(campeao):
    lanes = []
    for item in counters:
        if item["Campeão"].split("\n")[0] == campeao:  # Comparar os dados do campeão selecionado
            for counter in item.get("Counters", []): # Procurar no JSON os Counters
                lane = counter.get("Lane") # e extrair as lanes disponíveis
                if lane and lane not in lanes:
                    lanes.append(lane)
    combo_lane.configure(values=lanes)
    combo_lane.set(lanes[0] if lanes else "Nenhuma Lane")

# ===== JANELA =====
app = ctk.CTk()
app.iconbitmap(resource_path("icon.ico"))
app.title("LoL Counters")
app.geometry("540x620")
app.configure(fg_color=BG_MAIN)
app.resizable(False, False)

# ===== TÍTULO =====
titulo = ctk.CTkLabel(
    app,
    text="League of Legends – Counters",
    text_color=GOLD,
    font=ctk.CTkFont(size=22, weight="bold")
)
titulo.pack(pady=20)

# ===== FRAME BUSCA =====
frame_busca = ctk.CTkFrame(app, fg_color=BG_CARD)
frame_busca.pack(padx=20, pady=10, fill="x")

entry_campeao = ctk.CTkEntry(
    frame_busca,
    placeholder_text="Digite o nome do campeão",
    text_color=GOLD_LIGHT,
    fg_color=BG_MAIN,
    border_color=GOLD
)
entry_campeao.pack(padx=10, pady=10, fill="x")
entry_campeao.bind("<KeyRelease>", atualizar_autocomplete)

# Tooltip
tooltip = ToolTip(entry_campeao)
tooltip_texto = tk.StringVar()

entry_campeao.bind("<Enter>", lambda e: tooltip.show(tooltip_texto.get()))
entry_campeao.bind("<Leave>", tooltip.hide)

# ===== LISTA AUTOCOMPLETE =====
list_campeoes = tk.Listbox(
    frame_busca,
    height=5,
    bg=BG_MAIN,
    fg=GOLD_LIGHT,
    selectbackground=BLUE,
    highlightthickness=0,
    borderwidth=0
)
list_campeoes.pack(padx=10, pady=(0, 10), fill="x")
list_campeoes.bind("<<ListboxSelect>>", selecionar_campeao)

# ===== FRAME LANE =====
frame_lane = ctk.CTkFrame(app, fg_color=BG_CARD)
frame_lane.pack(padx=20, pady=10, fill="x")

combo_lane = ctk.CTkOptionMenu(
    frame_lane,
    values=[],
    fg_color=BG_MAIN,
    button_color=BLUE,
    text_color=GOLD_LIGHT
)
combo_lane.pack(padx=10, pady=10, fill="x")

# ===== BOTÃO =====
btn_buscar = ctk.CTkButton(
    app,
    text="Buscar Counters",
    fg_color=BLUE,
    hover_color=GOLD,
    text_color="white",
    command=lambda: buscar_campeao(entry_campeao.get())
)
btn_buscar.pack(pady=15)

# ===== RESULTADO =====
frame_resultado = ctk.CTkFrame(app, fg_color=BG_CARD)
frame_resultado.pack(padx=20, pady=10, fill="both", expand=True)

label_resultado = ctk.CTkLabel(
    frame_resultado,
    text="Counters",
    text_color=GOLD,
    font=ctk.CTkFont(size=16, weight="bold")
)
label_resultado.pack(pady=10)

list_resultado = tk.Listbox(
    frame_resultado,
    bg=BG_MAIN,
    fg=GOLD_LIGHT,
    selectbackground=BLUE,
    highlightthickness=0,
    borderwidth=0
)
list_resultado.pack(padx=10, pady=10, fill="both", expand=True)

app.mainloop()