from pathlib import Path
from threading import Thread

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

ROOT = Path(__file__).resolve().parent
ASSET = ROOT / "assets" / "aftab.jpg"

GOLD = (1.0, 0.72, 0.08, 1)
RED = (0.92, 0.05, 0.08, 1)
DARK = (0.025, 0.025, 0.035, 1)
CARD = (0.055, 0.055, 0.07, 1)
WHITE = (0.95, 0.95, 0.95, 1)
MUTED = (0.62, 0.62, 0.68, 1)
GREEN = (0.15, 0.85, 0.4, 1)


class Card(Button):
    def __init__(self, title, subtitle, icon, callback, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)
        self.size_hint_y = None
        self.height = 92
        self.text = f"{icon}   {title}\n{subtitle}"
        self.halign = "left"
        self.valign = "middle"
        self.padding = (18, 0)
        self.color = WHITE
        self.font_size = "15sp"
        self.bind(on_release=callback)
        with self.canvas.before:
            Color(*CARD)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[16])
            Color(*RED)
            self.edge = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 16), width=1.0)
        self.bind(pos=self._sync, size=self._sync)

    def _sync(self, *_):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.edge.rounded_rectangle = (self.x, self.y, self.width, self.height, 16)


class AftabApp(App):
    title = "AFTAB MODZ"

    def build(self):
        Window.clearcolor = DARK
        root = BoxLayout(orientation="vertical", padding=12, spacing=10)

        # Header
        header = BoxLayout(size_hint_y=None, height=120, spacing=12)
        portrait = Image(source=str(ASSET), size_hint_x=None, width=105, allow_stretch=True, keep_ratio=True)
        header.add_widget(portrait)

        titles = BoxLayout(orientation="vertical", padding=(0, 8))
        titles.add_widget(Label(text="AFTAB MODZ", color=GOLD, bold=True, font_size="27sp", halign="left", valign="middle"))
        titles.add_widget(Label(text="AFTAB AHMAD VIP MOD", color=WHITE, font_size="14sp", halign="left", valign="middle"))
        titles.add_widget(Label(text="PAK TOOL SUITE  •  PREMIUM EDITION", color=RED, font_size="11sp", halign="left", valign="middle"))
        header.add_widget(titles)
        root.add_widget(header)

        status = Label(text="●  READY TO WORK     •     ANDROID", color=GREEN, size_hint_y=None, height=28, font_size="12sp")
        root.add_widget(status)

        scroll = ScrollView(do_scroll_x=False)
        menu = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        menu.bind(minimum_height=menu.setter("height"))

        items = [
            ("📦", "UNPACK PAK", "Extract files from PAK", self.not_ready),
            ("💉", "INJECT / EDIT", "Modify or add files", self.not_ready),
            ("🔨", "FULL REBUILD", "Rebuild complete PAK", self.not_ready),
            ("📁", "REPACK TO PATH", "Save to custom path", self.not_ready),
            ("🔐", "PROTECT PAK", "SM4 encryption / protection", self.not_ready),
            ("🗑", "DELETE TEMP", "Clean temporary workspace", self.not_ready),
        ]
        for icon, title, sub, cb in items:
            menu.add_widget(Card(title, sub, icon, cb))
        scroll.add_widget(menu)
        root.add_widget(scroll)

        bottom = BoxLayout(size_hint_y=None, height=52, spacing=8)
        for text in ("⌂  HOME", "☷  LOGS", "⚙  SETTINGS", "ⓘ  ABOUT"):
            b = Button(text=text, background_normal="", background_color=(0.06, 0.06, 0.08, 1), color=GOLD, font_size="11sp")
            b.bind(on_release=lambda *_args, t=text: self.info(t))
            bottom.add_widget(b)
        root.add_widget(bottom)
        return root

    def info(self, title):
        Label(text=f"{title}\n\nAndroid GUI layer is ready.\nPAK engine integration comes next.", color=WHITE, halign="center")
        p = Popup(title="AFTAB MODZ", content=Label(text=f"{title}\n\nUI build is ready.\nNext phase: connect tool.py engine.", color=WHITE, halign="center"), size_hint=(.82, .42))
        p.open()

    def not_ready(self, *_):
        content = BoxLayout(orientation="vertical", spacing=12, padding=14)
        content.add_widget(Label(text="ENGINE INTEGRATION", color=GOLD, font_size="18sp", bold=True))
        content.add_widget(Label(text="The Android GUI is ready.\nThe existing tool.py PAK engine will be connected in the next build phase.\n\nThis keeps the original PAK logic instead of rewriting it.", color=WHITE, halign="center"))
        bar = ProgressBar(max=100, value=100, size_hint_y=None, height=8)
        content.add_widget(bar)
        b = Button(text="OK", size_hint_y=None, height=46, background_normal="", background_color=RED)
        content.add_widget(b)
        p = Popup(title="AFTAB MODZ", content=content, size_hint=(.88, .52))
        b.bind(on_release=p.dismiss)
        p.open()


if __name__ == "__main__":
    AftabApp().run()
