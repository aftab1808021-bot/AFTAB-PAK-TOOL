from pathlib import Path
import shutil
import threading
import traceback

from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

import tool_core as engine

GOLD = (1.0, 0.72, 0.08, 1)
GOLD2 = (0.98, 0.86, 0.35, 1)
BG = (0.018, 0.022, 0.028, 1)
CARD = (0.045, 0.052, 0.065, 1)
CARD2 = (0.065, 0.074, 0.09, 1)
WHITE = (0.94, 0.95, 0.97, 1)
MUTED = (0.57, 0.61, 0.68, 1)
GREEN = (0.18, 0.92, 0.48, 1)
RED = (1.0, 0.25, 0.28, 1)

KV = r'''
#:import dp kivy.metrics.dp
#:import rgba kivy.utils.get_color_from_hex

<GoldButton@Button>:
    background_normal: ''
    background_down: ''
    background_color: rgba('#1A1608') if self.state == 'normal' else rgba('#3A2B08')
    color: rgba('#F7F7F7')
    bold: True
    font_size: '13sp'
    border: 0,0,0,0

<DarkButton@Button>:
    background_normal: ''
    background_down: ''
    background_color: rgba('#10151D') if self.state == 'normal' else rgba('#1B222D')
    color: rgba('#E8EBF0')
    font_size: '12sp'
    border: 0,0,0,0

<Root>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: rgba('#05070A')
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        size_hint_y: None
        height: dp(64)
        padding: dp(12), dp(8)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: rgba('#080B10')
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'AFTAB MODZ'
            color: rgba('#FFC52B')
            font_size: '22sp'
            bold: True
            halign: 'left'
            valign: 'middle'
            text_size: self.size
        Label:
            text: 'PAK TOOL  •  Android Edition'
            color: rgba('#89919E')
            font_size: '10sp'
            size_hint_x: .85
            halign: 'right'
            valign: 'middle'
            text_size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(12), dp(10)
        spacing: dp(9)
        ScrollView:
            id: scroll
            bar_width: dp(3)
            do_scroll_x: False
            GridLayout:
                id: content
                cols: 1
                spacing: dp(9)
                padding: 0, 0, 0, dp(12)
                size_hint_y: None
                height: self.minimum_height
    BoxLayout:
        size_hint_y: None
        height: dp(58)
        spacing: dp(5)
        padding: dp(5), dp(5)
        canvas.before:
            Color:
                rgba: rgba('#080B10')
            Rectangle:
                pos: self.pos
                size: self.size
        GoldButton:
            text: 'HOME'
            on_release: root.show_home()
        DarkButton:
            text: 'FILES'
            on_release: root.show_files()
        DarkButton:
            text: 'LOGS'
            on_release: root.show_logs()
        DarkButton:
            text: 'SETTINGS'
            on_release: root.show_settings()
'''

Builder.load_string(KV)


def panel(**kwargs):
    box = BoxLayout(orientation='vertical', padding=dp(13), spacing=dp(8), **kwargs)
    with box.canvas.before:
        from kivy.graphics import Color, RoundedRectangle
        Color(*CARD)
        rect = RoundedRectangle(pos=box.pos, size=box.size, radius=[dp(13)])
    def sync(*_):
        rect.pos = box.pos
        rect.size = box.size
    box.bind(pos=sync, size=sync)
    return box


def title(text, size=16):
    return Label(text=text, color=GOLD2, font_size=f'{size}sp', bold=True,
                 size_hint_y=None, height=dp(size+10), halign='left', valign='middle', text_size=(None, None))


def small(text, color=MUTED, size=11):
    return Label(text=text, color=color, font_size=f'{size}sp', halign='left', valign='middle',
                 text_size=(None, None), size_hint_y=None, height=dp(size+9))


class ActionCard(Button):
    def __init__(self, action, icon, heading, desc, **kwargs):
        super().__init__(**kwargs)
        self.action = action
        self.text = f'{icon}\n{heading}\n{desc}'
        self.markup = True
        self.font_size = '12sp'
        self.bold = True
        self.color = WHITE
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0.075, 0.065, 0.025, 1)
        self.bind(on_release=lambda *_: App.get_running_app().root.choose_pak(self.action))


class Root(BoxLayout):
    status = StringProperty('Ready')
    selected_pak = StringProperty('None')
    progress = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base = Path(App.get_running_app().user_data_dir)
        engine.ensure_directories(self.base)
        self.pak_path = None
        self.edit_path = self.base / 'PAK TOOL' / 'EDIT'
        self.logs = []
        self.current_page = 'home'
        Clock.schedule_once(lambda *_: self.show_home(), 0.15)

    def add_log(self, text):
        self.logs.append(text)

    @mainthread
    def set_status(self, text):
        self.status = text
        self._refresh_status()

    def _clear(self):
        self.ids.content.clear_widgets()

    def _refresh_status(self):
        # Home status is rebuilt only when Home is visible.
        if self.current_page == 'home':
            self.show_home()

    def show_home(self):
        self.current_page = 'home'
        self._clear()
        hero = panel(size_hint_y=None, height=dp(150))
        row = BoxLayout(spacing=dp(12))
        photo = Image(source=str(Path(__file__).with_name('aftab_profile.jpg')), allow_stretch=True, keep_ratio=True, size_hint_x=.33)
        row.add_widget(photo)
        info = BoxLayout(orientation='vertical', spacing=dp(3))
        info.add_widget(Label(text='AFTAB MODZ', color=GOLD, font_size='24sp', bold=True, halign='left', text_size=(None, None), size_hint_y=None, height=dp(35)))
        info.add_widget(small('PAK TOOL  •  ANDROID EDITION', WHITE, 10))
        info.add_widget(small('MOD  •  EDIT  •  REPACK  •  PROTECT', MUTED, 10))
        status_color = GREEN if not self.status.startswith('ERROR') else RED
        info.add_widget(small(('● ' if status_color == GREEN else '● ') + self.status.split('\n')[0], status_color, 11))
        row.add_widget(info)
        hero.add_widget(row)
        self.ids.content.add_widget(hero)

        sel = panel(size_hint_y=None, height=dp(92))
        sel.add_widget(title('SELECTED PAK', 12))
        sel.add_widget(small(self.selected_pak if self.pak_path else 'No PAK selected', WHITE, 12))
        b = GoldButton(text='SELECT PAK FILE', size_hint_y=None, height=dp(40))
        b.bind(on_release=lambda *_: self.choose_pak('unpack'))
        sel.add_widget(b)
        self.ids.content.add_widget(sel)

        grid = GridLayout(cols=2, spacing=dp(8), size_hint_y=None, height=dp(282))
        cards = [
            ('unpack', '01', 'UNPACK PAK', 'Extract files from PAK'),
            ('inject', '02', 'INJECT / EDIT', 'Modify files inside PAK'),
            ('repack', '03', 'FULL REBUILD', 'Rebuild complete PAK'),
            ('target', '04', 'REPACK TO PATH', 'Repack to target path'),
            ('protect', '05', 'PROTECT PAK', 'Protect / encrypt PAK'),
        ]
        for action, num, head, desc in cards:
            grid.add_widget(ActionCard(action, num, head, desc))
        delete = ActionCard('delete', '06', 'DELETE WORK', 'Clear temporary folders')
        grid.add_widget(delete)
        self.ids.content.add_widget(grid)

        foot = panel(size_hint_y=None, height=dp(76))
        foot.add_widget(title('WORKSPACE', 11))
        foot.add_widget(small(str(self.base / 'PAK TOOL'), MUTED, 9))
        self.ids.content.add_widget(foot)

    def show_files(self):
        self.current_page = 'files'
        self._clear()
        p = self.base / 'PAK TOOL' / 'PAK'
        p.mkdir(parents=True, exist_ok=True)
        box = panel(size_hint_y=None, height=dp(92 + max(1, len(list(p.glob('*.pak')))) * 62))
        box.add_widget(title('PAK FILES', 18))
        files = sorted(p.glob('*.pak'))
        if not files:
            box.add_widget(small('No .pak files yet. Put a PAK inside the PAK TOOL/PAK folder.', MUTED, 11))
        else:
            for f in files:
                b = DarkButton(text=f'{f.name}  •  {f.stat().st_size/1024/1024:.1f} MB', size_hint_y=None, height=dp(52))
                b.bind(on_release=lambda btn, path=f: self.select_existing(path))
                box.add_widget(b)
        self.ids.content.add_widget(box)

    def select_existing(self, path):
        self.pak_path = Path(path)
        self.selected_pak = self.pak_path.name
        self.status = 'PAK selected'
        self.show_home()

    def show_logs(self):
        self.current_page = 'logs'
        self._clear()
        box = panel(size_hint_y=None, height=dp(430))
        box.add_widget(title('OPERATION LOGS', 18))
        text = '\n'.join(self.logs[-80:]) if self.logs else 'No operations logged yet.'
        ti = TextInput(text=text, readonly=True, multiline=True, background_color=(.02,.025,.03,1), foreground_color=WHITE, cursor_color=GOLD, font_size='10sp')
        box.add_widget(ti)
        clear = GoldButton(text='CLEAR LOGS', size_hint_y=None, height=dp(42))
        clear.bind(on_release=lambda *_: self.clear_logs())
        box.add_widget(clear)
        self.ids.content.add_widget(box)

    def clear_logs(self):
        self.logs.clear()
        self.show_logs()

    def show_settings(self):
        self.current_page = 'settings'
        self._clear()
        box = panel(size_hint_y=None, height=dp(360))
        box.add_widget(title('SETTINGS', 18))
        box.add_widget(small('Appearance', GOLD2, 11))
        box.add_widget(small('Theme: Dark Premium', WHITE, 12))
        box.add_widget(small('Accent: AFTAB Gold', WHITE, 12))
        box.add_widget(small('Engine', GOLD2, 11))
        box.add_widget(small('Pure Python SM4 on Android', WHITE, 12))
        box.add_widget(small('Temporary work: ' + str(self.base), MUTED, 9))
        box.add_widget(small('About', GOLD2, 11))
        box.add_widget(small('AFTAB MODZ PAK TOOL\nAndroid Edition', WHITE, 12))
        box.add_widget(small('Premium UI • PAK engine retained', MUTED, 10))
        self.ids.content.add_widget(box)

    def choose_pak(self, mode):
        if mode == 'delete':
            self.delete_work()
            return
        self._file_popup(mode)

    def _file_popup(self, mode):
        folder = self.base / 'PAK TOOL' / 'PAK'
        folder.mkdir(parents=True, exist_ok=True)
        files = sorted(folder.glob('*.pak'))
        box = BoxLayout(orientation='vertical', spacing=dp(7), padding=dp(9))
        if not files:
            box.add_widget(Label(text='No .pak files found.\n\nCopy your PAK into:\n' + str(folder), color=WHITE))
        else:
            for f in files:
                b = DarkButton(text=f'{f.name}\n{f.stat().st_size/1024/1024:.1f} MB', size_hint_y=None, height=dp(58))
                b.bind(on_release=lambda btn, p=f: self._run_mode(mode, p))
                box.add_widget(b)
        close = DarkButton(text='CLOSE', size_hint_y=None, height=dp(44))
        box.add_widget(close)
        pop = Popup(title='SELECT PAK', content=box, size_hint=(.94, .78), separator_color=GOLD)
        close.bind(on_release=pop.dismiss)
        self._popup = pop
        pop.open()

    def _run_mode(self, mode, pak_path):
        if hasattr(self, '_popup'):
            self._popup.dismiss()
        self.pak_path = Path(pak_path)
        self.selected_pak = self.pak_path.name
        if mode == 'unpack':
            self._confirm_operation('UNPACK PAK', 'Extract this PAK into the workspace?', mode)
        elif mode == 'inject':
            self._confirm_operation('INJECT / EDIT', 'Use files from PAK TOOL/EDIT?', mode)
        elif mode == 'repack':
            self._confirm_operation('FULL REBUILD', 'Rebuild the PAK from PAK TOOL/EDIT?', mode)
        elif mode == 'protect':
            self._confirm_operation('PROTECT PAK', 'Create a protected copy in RESULT?', mode)
        elif mode == 'target':
            self._ask_target()

    def _confirm_operation(self, heading, message, mode):
        box = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(12))
        box.add_widget(Label(text=message, color=WHITE))
        buttons = BoxLayout(size_hint_y=None, height=dp(44), spacing=dp(8))
        no = DarkButton(text='CANCEL')
        yes = GoldButton(text='CONTINUE')
        buttons.add_widget(no); buttons.add_widget(yes)
        box.add_widget(buttons)
        pop = Popup(title=heading, content=box, size_hint=(.88, .32), separator_color=GOLD)
        no.bind(on_release=pop.dismiss)
        yes.bind(on_release=lambda *_: (pop.dismiss(), self.start_worker(mode)))
        pop.open()

    def start_worker(self, mode):
        self.add_log(f'[{mode.upper()}] Starting: {self.selected_pak}')
        self.current_page = 'home'
        self.show_home()
        threading.Thread(target=self._worker, args=(mode,), daemon=True).start()

    def select_edit_folder(self):
        self.edit_path.mkdir(parents=True, exist_ok=True)
        self.set_status('EDIT folder: ' + str(self.edit_path))

    def clear_selection(self):
        self.pak_path = None
        self.selected_pak = 'None'
        self.set_status('Ready')

    def _worker(self, mode):
        try:
            if not self.pak_path:
                raise ValueError('Select a PAK first.')
            pak = engine.TencentPakFile(self.pak_path)
            result_dir = self.base / 'PAK TOOL' / 'RESULT'
            result_dir.mkdir(parents=True, exist_ok=True)
            out = result_dir / self.pak_path.name
            self.set_status(f'{mode.upper()} running…')
            self.add_log(f'Opening PAK: {self.pak_path.name}')
            if mode == 'unpack':
                out_dir = self.base / 'UNPACK' / self.pak_path.stem
                pak.dump(out_dir)
                engine.dump_unpacking_log(pak, out_dir / f'Debug_{self.pak_path.stem}.log')
                self.add_log(f'UNPACK complete: {out_dir}')
                self.set_status(f'UNPACK complete\n{out_dir}')
            elif mode == 'inject':
                if not any(self.edit_path.rglob('*')):
                    raise ValueError('PAK TOOL/EDIT is empty.')
                edited, added = engine.inject_edit_files(pak, self.edit_path, out, protect_new=True, sm4_type=47)
                self.add_log(f'Injection complete: edited={edited}, added={added}')
                self.set_status(f'INJECT complete — edited {edited}, added {added}\n{out}')
            elif mode == 'repack':
                if not any(self.edit_path.rglob('*')):
                    raise ValueError('PAK TOOL/EDIT is empty.')
                count = engine.repack_pak_file_full(pak, self.edit_path, out)
                self.add_log(f'REPACK complete: {count} files')
                self.set_status(f'REPACK complete — {count} files\n{out}')
            elif mode == 'protect':
                protected, skipped = engine.protect_pak_file(pak, out, sm4_type=47)
                self.add_log(f'PROTECT complete: protected={protected}, skipped={skipped}')
                self.set_status(f'PROTECT complete — protected {protected}, skipped {skipped}\n{out}')
        except Exception as exc:
            self.add_log('ERROR: ' + str(exc))
            self.set_status('ERROR: ' + str(exc))
            traceback.print_exc()

    def _ask_target(self):
        box = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(8))
        field = TextInput(hint_text='Content/Lua/GameLua/Mod/BRMod', multiline=False, foreground_color=WHITE, background_color=CARD2)
        box.add_widget(field)
        btn = GoldButton(text='START REPACK', size_hint_y=None, height=dp(44))
        box.add_widget(btn)
        popup = Popup(title='TARGET PAK PATH', content=box, size_hint=(.9, .35), separator_color=GOLD)
        def go(*_):
            target = field.text.strip().replace('\\', '/').strip('/')
            popup.dismiss()
            if not target:
                self.set_status('Target path is required.')
                return
            threading.Thread(target=self._target_worker, args=(target,), daemon=True).start()
        btn.bind(on_release=go)
        popup.open()

    def _target_worker(self, target):
        try:
            pak = engine.TencentPakFile(self.pak_path)
            out = self.base / 'PAK TOOL' / 'RESULT' / self.pak_path.name
            count = engine.repack_pak_file_full(pak, self.edit_path, out, target, force_add=True)
            self.add_log(f'TARGET REPACK complete: {count} files -> {target}')
            self.set_status(f'REPACK complete — {count} files → {target}\n{out}')
        except Exception as exc:
            self.add_log('ERROR: ' + str(exc))
            self.set_status('ERROR: ' + str(exc))

    def delete_work(self):
        for name in ('UNPACK', 'REPACK'):
            p = self.base / name
            if p.exists():
                shutil.rmtree(p)
            p.mkdir(parents=True, exist_ok=True)
        self.add_log('Temporary UNPACK/REPACK folders cleared.')
        self.set_status('Temporary folders cleared.')


class AftabPakApp(App):
    title = 'AFTAB MODZ PAK TOOL'
    def build(self):
        return Root()


if __name__ == '__main__':
    AftabPakApp().run()
