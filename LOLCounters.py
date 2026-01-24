import sys
import os
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
counters = {
    "Aatrox": {"Top": ["Irelia", "Darius", "Ornn", "Jax", "Yasuo", "Malphite", "Vayne"]},
    "Ahri": {"Mid": ["Yasuo", "Ekko", "Diana", "Irelia", "Kassadin", "Galio"]},
    "Akali": {"Mid": ["Kassadin", "Galio", "Annie", "Veigar", "Akshan", "Vex", "Twisted Fate"]},
    "Ambessa": {
        "Top": ["Pantheon", "Jayce", "Darius", "Garen", "Singed"],
        "Jg": ["Shyvana", "Kha'Zix", "Wukong", "Viego", "Fiddlesticks", "Warwick"]
    },
    "Amumu": {"Top": ["Shyvana", "Lee Sin", "Vi", "Warwick", "Kha'Zix", "Volibear", "Olaf"]},
    "Annie": {"Mid": ["Kassadin", "Brand", "Orianna", "Fizz", "Veigar", "Lux"]},
    "Ashe": {"Adc": ["Caitlyn", "Draven", "Jhin", "Tristana", "Ezreal", "Lucian"]},
    "Aurelion Sol": {"Mid": ["Fizz", "Zed", "Yasuo", "Lux", "Katarina", "Karma", "Galio"]},
    "Blitzcrank": {"Sup": ["Leona", "Alistar", "Morgana", "Thresh", "Braum", "Rakan"]},
    "Brand": {
        "Mid": ["Fizz", "Galio", "Lux", "Zed", "Corki", "Ekko"],
        "Sup": ["Maokai", "Pyke", "Nautilus", "Blitzcrank", "Morgana", "Braum"]
    },
    "Braum": {"Sup": ["Morgana", "Leona", "Soraka", "Alistar", "Karma", "Vayne", "Senna"]},
    "Caitlyn": {"Adc": ["Jhin", "Ezreal", "Nilah", "Twitch", "Jinx", "Draven"]},
    "Camille": {"Top": ["Renekton", "Darius", "Fiora", "Riven", "Nasus", "Shen"]},
    "Corki": {
        "Mid": ["Zed", "Fizz", "Lux", "Ahri", "Brand", "Syndra"],
        "Adc": ["Caitlyn", "Draven", "Ashe", "Varus", "Lucian", "Sivir"]
    },
    "Darius": {
        "Top": ["Vayne", "Ornn", "Kayle", "Jayce", "Urgot"],
        "Jg": ["Wukong", "Nunu", "Master Yi", "Ekko", "Evelynn", "Viego"]
    },
    "Diana": {
        "Mid": ["Kayle", "Fizz", "Pantheon", "Gragas", "Ekko", "Jayce"],
        "Jg": ["Fizz", "Jax", "Pantheon", "Tryndamere", "Kayle", "Ekko"]
    },
    "Dr. Mundo": {
        "Top": ["Darius", "Aatrox", "Vayne", "Gwen", "Fiora", "Camille", "Gragas"],
        "Jg": ["Gragas", "Xin Zhao", "Kayn", "Viego", "Lillia", "Ekko"]
    },
    "Draven": {"Adc": ["Senna", "Jhin", "Ashe", "Nilah", "Ziggs"]},
    "Ekko": {
        "Mid": ["Kassadin", "Galio", "Swain", "Irelia", "Yasuo", "Akali"],
        "Jg": ["Kha'Zix", "Rengar", "Amumu", "Vi", "Nunu", "Talon"]
    },
    "Evelynn": {"Jg": ["Kha'Zix", "Xin Zhao", "Lee Sin", "Master Yi", "Rengar", "Fiddlesticks"]},
    "Ezreal": {"Adc": ["Nilah", "Vayne", "Draven", "Tristana", "Kalista"]},
    "Fiddlesticks": {"Jg": ["Shyvana", "Vi", "Amumu", "Ekko", "Xin Zhao", "Dr. Mundo"]},
    "Fiora": {"Top": ["Warwick", "Vayne", "Pantheon", "Darius", "Renekton", "Malphite"]},
    "Fizz": {
        "Mid": ["Diana", "Kassadin", "Annie", "Lux", "Yasuo", "Galio"],
        "Jg": ["Lee Sin", "Vi", "Rengar", "Kha'Zix", "Evelynn", "Graves"]
    },
    "Galio": {
        "Mid": ["Yasuo", "Swain", "Orianna", "Ahri", "Vex", "Syndra"],
        "Sup": ["Alistar", "Lulu", "Janna", "Braum", "Zyra", "Lux"]
    },
    "Garen": {"Top": ["Darius", "Camille", "Kayle", "Fiora", "Shen", "Ornn", "Vayne"]},
    "Gnar": {"Top": ["Irelia", "Darius", "Olaf", "Renekton", "Nasus", "Camille"]},
    "Gragas": {
        "Top": ["Pantheon", "Aatrox", "Jax", "Darius", "Kennen", "Garen"],
        "Jg": ["Lee Sin", "Rengar", "Kha'Zix", "Viego", "Evelynn", "Diana"]
    },
    "Graves": {"Jg": ["Evelynn", "Vi", "Rengar", "Kha'Zix", "Rammus", "Fiddlesticks"]},
    "Gwen": {"Top": ["Fiora", "Jax", "Riven", "Darius", "Nasus", "Tryndamere"]},
    "Hecarim": {"Jg": ["Master Yi", "Evelynn", "Warwick", "Vi", "Jarvan IV", "Graves"]},
    "Heimerdinger": {"Mid": ["Zoe", "Veigar", "Ekko", "Syndra", "Lux", "Zed"]},
    "Irelia": {
        "Mid": ["Ekko", "Zoe", "Vex", "Annie", "Yasuo", "Syndra"],
        "Top": ["Garen", "Darius", "Renekton", "Malphite", "Nasus", "Sett"]
    },
    "Janna": {"Sup": ["Nami", "Blitzcrank", "Lux", "Sona", "Soraka", "Senna"]},
    "Jarvan IV": {"Jg": ["Vi", "Lee Sin", "Xin Zhao", "Nunu", "Ekko", "Gwen"]},
    "Jax": {
        "Top": ["Renekton", "Garen", "Pantheon", "Urgot", "Dr. Mundo", "Singed", "Gragas"],
        "Jg": ["Kha'Zix", "Kayn", "Rammus", "Fiddlesticks", "Evelynn", "Lillia"]
    },
    "Jayce": {
        "Top": ["Olaf", "Renekton", "Fiora", "Wukong", "Pantheon", "Urgot"],
        "Mid": ["Brand", "Annie", "Galio", "Zoe", "Diana", "Vex"]
    },
    "Jhin": {"Adc": ["Lucian", "Vayne", "Tristana", "Nilah", "Twitch", "Jinx"]},
    "Jinx": {"Adc": ["Draven", "Tristana", "Xayah", "Twitch", "Nilah", "Senna"]},
    "Kai'Sa": {"Adc": ["Vayne", "Xayah", "Ezreal", "Sivir", "Lucian", "Caitlyn"]},
    "Kalista": {"Adc": ["Nilah", "Xayah", "Lucian", "Twitch", "Ashe", "Zeri"]},
    "Karma": {
        "Sup": ["Sona", "Lulu", "Blitzcrank", "Zyra", "Rakan", "Morgana"],
        "Mid": ["Veigar", "Lux", "Orianna", "Ahri", "Yasuo", "Ekko"]
    },
    "Kassadin": {"Mid": ["Zed", "Yasuo", "Riven", "Yone", "Ekko", "Jayce"]},
    "Katarina": {"Mid": ["Fizz", "Kayle", "Yasuo", "Pantheon", "Annie", "Ahri", "Galio"]},
    "Kayle": {
        "Top": ["Pantheon", "Riven", "Jax", "Wukong", "Jayce", "Yone"],
        "Mid": ["Annie", "Orianna", "Ziggs", "Syndra", "Zoe", "Twisted Fate"]
    },
    "Kayn": {"Jg": ["Vi", "Rengar", "Shyvana", "Evelynn", "Master Yi", "Xin Zhao"]},
    "Kennen": {
        "Top": ["Nasus", "Irelia", "Dr. Mundo", "Olaf", "Vladimir", "Kayle"],
        "Mid": ["Diana", "Ahir", "Vladimir", "Annie", "Galio", "Brand"]
    },
    "Kha'Zix": {"Jg": ["Rengar", "Vi", "Lee Sin", "Volibear", "Warwick", "Rammus"]},
    "Kindred": {"Jg": ["Lee Sin", "Gragas", "Master Yi", "Evelynn", "Kha'Zix", "Vi"]},
    "Lee Sin": {"Jg": ["Rammus", "Wukong", "Fiddlesticks", "Warwick", "Graves"]},
    "Leona": {"Sup": ["Morgana", "Alistar", "Janna", "Karma", "Braum", "Thresh"]},
    "Lillia": {"Jg": ["Rengar", "Ekko", "Diana", "Master Yi", "Evelynn", "Jarvan IV"]},
    "Lissandra": {"Mid": ["Vex", "Lux", "Malphite", "Kassadin", "Varus", "Galio"]},
    "Lucian": {
        "Adc": ["Vayne", "Ashe", "Nilah", "Caitlyn", "Twitch", "Tristana"],
        "Mid": ["Brand", "Galio", "Annie", "Aurelion Sol", "Fizz", "Yasuo"]
    },
    "Lulu": {"Sup": ["Sona", "Soraka", "Blitzcrank", "Rakan", "Karma", "Leona"]},
    "Lux": {
        "Mid": ["Fizz", "Kassadin", "Ahri", "Yasuo", "Karma", "Yone"],
        "Sup": ["Sona", "Blitzcrank", "Soraka", "Nautilus", "Zyra", "Leona"]
    },
    "Master Yi": {"Jg": ["Rammus", "Vi", "Amumu", "Kha'Zix", "Warwick", "Kayn"]},
    "Malphite": {
        "Top": ["Fiora", "Olaf", "Darius", "Garen", "Shen", "Dr. Mundo"],
        "Mid": ["Diana", "Annie", "Morgana", "Fizz", "Ekko", "Kassadin"],
        "Sup": ["Morgana", "Sona", "Senna", "Rakan", "Thresh", "Nautilus"]
    },
    "Maokai": {
        "Sup": ["Braum", "Alistar", "Janna", "Thresh", "Lulu", "Zyra"],
        "Jg": ["Rammus", "Warwick", "Jarvan IV", "Nunu", "Rengar", "Lillia"],
        "Top": ["Garen", "Dr. Mundo", "Nasus", "Sett", "Camille", "Fiora"]
    },
    "Milio": {"Sup": ["Blitzcrank", "Thresh", "Pyke", "Nautilus", "Senna", "Lux"]},
    "Miss Fortune": {"Adc": ["Tristana", "Draven", "Caitlyn", "Lucian", "Senna", "Vayne"]},
    "Mordekaiser": {
        "Top": ["Olaf", "Fiora", "Warwick", "Riven", "Jax", "Gwen"],
        "Jg": ["Master Yi", "Warwick", "Lillia", "Ekko", "Pantheon", "Gragas"]
    },
    "Morgana": {
        "Sup": ["Karma", "Janna", "Sona", "Soraka", "Yuumi", "Lulu"],
        "Mid": ["Fizz", "Zed", "Katarina", "Seraphine", "Tristana", "Lissandra"],
        "Jg": ["Zed", "Fizz", "Olaf", "Amumu", "Rengar", "Ambessa"]
    },
    "Nami": {"Sup": ["Lulu", "Blitzcrank", "Morgana", "Leona", "Alistar", "Sona"]},
    "Nasus": {"Top": ["Darius", "Teemo", "Pantheon", "Volibear", "Olaf", "Garen", "Camille", "Gwen"]},
    "Nautilus": ["Morgana", "Janna", "Alistar", "Rakan", "Seraphine", "Lulu"],
    "Nilah": {
        "Top": ["Pantheon", "Teemo", "Malphite", "Vayne", "Jayce", "Yone"],
        "Adc": ["Caitlyn", "Jhin", "Ezreal", "Kalista", "Lucian", "Vayne"]
    },
    "Nunu": {"Jg": ["Lee Sin", "Vi", "Kha'Zix", "Diana", "Evelynn", "Gragas"]},
    "Olaf": {
        "Jg": ["Gragas", "Jarvan IV", "Warwick", "Rengar", "Fiddlesticks", "Master Yi"],
        "Top": ["Volibear", "Jax", "Kayle", "Sett", "Riven"]
    },
    "Orianna": {"Mid": ["Diana", "Gragas", "Ziggs", "Ahri", "Zed", "Syndra"]},
    "Ornn": {"Top": ["Fiora", "Shen", "Olaf", "Camille", "Vayne", "Gwen"]},
    "Pantheon": {
        "Jg": ["Rammus", "Vi", "Diana", "Rengar", "Shyvana", "Dr. Mundo"],
        "Top": ["Fiora", "Malphite", "Camile", "Olaf", "Shen", "Jayce"],
        "Mid": ["Orianna", "Ahri", "Zoe", "Syndra", "Jayce", "Swain"]
    },
    "Pyke": {"Sup": ["Leona", "Nautilus", "Rakan", "Blitzcrank", "Maokai", "Braum"]},
    "Rakan": {"Sup": ["Lulu", "Leona", "Janna", "Alistar", "Karma", "Milio"]},
    "Rammus": {"Jg": ["Fiddlesticks", "Evelynn", "Lillia", "Amumu", "Nunu", "Shyvana"]},
    "Renekton": {"Top": ["Vayne", "Garen", "Olaf", "Kayle", "Teemo", "Pantheon"]},
    "Rengar": {"Jg": ["Rammus", "Amumu", "Jarvan IV", "Warwick", "Master Yi", "Vi"]},
    "Riven": {"Top": ["Ornn", "Shen", "Sett", "Urgot", "Renekton", "Garen"]},
    "Rumble": {"Top": ["Garen", "Jayce", "Sion", "Shen", "Camille", "Tryndamere"]},
    "Samira": {"Adc": ["Draven", "Miss Fortune", "Senna", "Nilah", "Jinx", "Xayah"]},
    "Senna": {
        "Sup": ["Blitzcrank", "Rakan", "Leona", "Thresh", "Braum", "Nautilus"],
        "Adc": ["Caitlyn", "Jhin", "Ezreal", "Kalista", "Lucian", "Vayne"]
    },
    "Seraphine": {
        "Sup": ["Sona", "Soraka", "Janna", "Senna", "Pyke", "Milio"],
        "Mid": ["Fizz", "Ziggs", "Irelia", "Katarina", "Kayle", "Zed"]
    },
    "Sett": {"Top": ["Malphite", "Renekton", "Garen", "Pantheon", "Singed", "Volibear"]},
    "Shen": {"Top": ["Darius", "Teemo", "Sett", "Kayle", "Olaf", "Gwen"]},
    "Shyvana": {"Jg": ["Vi", "Lee Sin", "Kha'Zix", "Gragas", "Volibear", "Gwen"]},
    "Singed": {"Top": ["Kennen", "Riven", "Fiora", "Urgot", "Warwick", "Darius"]},
    "Sion": {
        "Top": ["Pantheon", "Aatrox", "Garen", "Nasus", "Darius", "Riven", "Jax"],
        "Jg": ["Warwick", "Ambessa", "Gwen", "Vi", "Kindred"]
    },
    "Sivir": {"Adc": ["Jhin", "Jinx", "Kai'Sa", "Miss Fortune", "Ashe"]},
    "Sona": {"Sup": ["Blitzcrank", "Leona", "Thresh", "Nautilus", "Zyra", "Alistar"]},
    "Soraka": {"Sup": ["Blitzcrank", "Thresh", "Leona", "Pyke", "Nautilus", "Alistar"]},
    "Swain": {
        "Mid": ["Ahri", "Jayce", "Akshan", "Fizz", "Yone", "Galio"],
        "Sup": ["Brand", "Lux", "Lulu", "Morgana", "Janna", "Zyra"]
    },
    "Syndra": {"Mid": ["Kassadin", "Fizz", "Lux", "Yasuo", "Kayle", "Talon"]},
    "Talon": {
        "Mid": ["Ekko", "Vex", "Veigar", "Fizz", "Kassadin", "Katarina"],
        "Jg": ["Rammus", "Xin Zhao", "Amumu", "Diana", "Fiddlesticks", "Vi"]
    },
    "Teemo": {
        "Top": ["Pantheon", "Jayce", "Ornn", "Malphite", "Riven", "Irelia"],
        "Mid": ["Fizz", "Lux", "Karma", "Galio", "Zoe", "Vex"]
    },
    "Thresh": {"Sup": ["Lulu", "Morgana", "Janna", "Nami", "Zyra", "Seraphine"]},
    "Tristana": {"Adc": ["Draven", "Sivir", "Lucian", "Jinx", "Caitlyn", "Nilah"]},
    "Tryndamere": {
        "Top": ["Malphite", "Teemo", "Darius", "Renekton", "Sett"],
        "Jg": ["Fizz", "Kayle", "Ekko", "Gragas", "Warwick"]
    },
    "Twisted Fate": {"Mid": ["Fizz", "Diana", "Ahri", "Yasuo", "Veigar", "Zed"]},
    "Twitch": {
        "Adc": ["Jhin", "Tristana", "Kai'Sa", "Draven", "Xayah", "Samira"],
        "Jg": ["Vi", "Kha'Zix", "Rengar", "Evelynn", "Lee Sin", "Kayn"]
    },
    "Urgot": {"Top": ["Dr. Mundo", "Kayle", "Teemo", "Olaf", "Garen", "Ornn"]},
    "Varus": {
        "Adc": ["Twitch", "Jinx", "Miss Fortune", "Sivir", "Samira", "Jhin"],
        "Mid": ["Annie", "Zoe", "Jayce", "Yasuo", "Katarina", "Yone"]
    },
    "Vayne": {
        "Adc": ["Caitlyn", "Draven", "Varus", "Ashe", "Tristana", "Nilah"],
        "Top": ["Pantheon", "Teemo", "Malphite", "Yone", "Jayce", "Vladimir"]
    },
    "Veigar": {"Mid": ["Zed", "Katarina", "Diana", "Zoe", "Jayce", "Ekko"]},
    "Vex": {"Mid": ["Pantheon", "Galio", "Veigar", "Kassadin", "Katarina", "Kayle"]},
    "Vi": {"Jg": ["Lee Sin", "Xin Zhao", "Warwick", "Diana", "Volibear", "Olaf"]},
    "Viego": {"Jg": ["Rammus", "Evelynn", "Warwick", "Vi", "Ekko", "Amumu"]},
    "Viktor": {"Mid": ["Ekko", "Fizz", "Zed", "Kassadin", "Yasuo", "Akali"]},
    "Vladimir": {
        "Mid": ["Fizz", "Kassadin", "Ahri", "Orianna", "Ziggs"],
        "Top": ["Kennen", "Camille", "Irelia", "Riven", "Darius", "Yone", "Nasus", "Aatrox"]
    },
    "Volibear": {
        "Top": ["Jayce", "Vayne", "Teemo", "Fiora", "Darius", "Kayle"],
        "Jg": ["Wukong", "Master Yi", "Amumu", "Rengar", "Lillia", "Fiddlesticks"]
    },
    "Warwick": {
        "Jg": ["Evelynn", "Nunu", "Rengar", "Maokai", "Rammus", "Vi"],
        "Top": ["Kayle", "Olaf", "Urgot", "Singed", "Darius", "Nasus"]
    },
    "Wukong": {
        "Jg": ["Lee Sin", "Amumu", "Jarvan IV", "Evelynn", "Vi", "Shyvana"],
        "Top": ["Ornn", "Darius", "Garen", "Nasus", "Olaf", "Volibear"]
    },
    "Xayah": {"Adc": ["Miss Fortune", "Tristana", "Varus", "Caitlyn", "Draven"]},
    "Xin Zhao": {"Jg": ["Malphite", "Rammus", "Lee Sin", "Evelynn", "Ekko", "Master Yi"]},
    "Yasuo": {
        "Mid": ["Fizz", "Renekton", "Annie", "Vex", "Vladimir", "Swain"],
        "Top": ["Renekton", "Nasus", "Tryndamere", "Garen", "Camille", "Darius"]
    },
    "Yone": {
        "Top": ["Pantheon", "Urgot", "Riven", "Fiora", "Garen", "Sett"],
        "Mid": ["Annie", "Zed", "Fizz", "Ahri", "Veigar", "Talon"]
    },
    "Yuumi": {"Sup": ["Leona", "Alistar", "Rakan", "Blitzcrank", "Soraka", "Sona"]},
    "Zeri": {"Adc": ["Draven", "Tristana", "Jhin", "Caitlyn", "Vayne", "Samira"]},
    "Zed": {
        "Mid": ["Fizz", "Ekko", "Vladimir", "Ahri", "Kayle", "Galio"],
        "Jg": ["Rammus", "Amumu", "Kindred", "Rengar", "Kayn", "Master Yi"]
    },
    "Ziggs": {"Mid": ["Kayle", "Talon", "Brand", "Ekko", "Annie", "Garen"]},
    "Zoe": {"Mid": ["Veigar", "Ahri", "Kassadin", "Twisted Fate", "Akali", "Zed"]},
    "Zyra": {
        "Sup": ["Janna", "Sona", "Thresh", "Morgana", "Alistar", "Soraka"],
        "Mid": ["Ziggs", "Heimerdinger", "Lux", "Syndra", "Katarina", "Zed"]
    }
}

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
def atualizar_autocomplete(event=None):
    texto = entry_campeao.get().lower()
    list_campeoes.delete(0, "end")

    for nome in counters:
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
    lanes = list(counters[campeao].keys())
    combo_lane.configure(values=lanes)
    combo_lane.set(lanes[0])


def buscar_counters():
    campeao = entry_campeao.get()
    lane = combo_lane.get()

    list_resultado.delete(0, "end")

    if campeao in counters and lane in counters[campeao]:
        for c in counters[campeao][lane]:
            list_resultado.insert("end", c)

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
    command=buscar_counters
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