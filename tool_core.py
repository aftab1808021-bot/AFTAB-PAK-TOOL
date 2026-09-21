import itertools as it
import math
import struct
import shutil
import os
import sys
import uuid
import hashlib
import platform
import subprocess
import requests
import base64
import zlib
import ctypes
from dataclasses import dataclass
from functools import lru_cache
from pathlib import PurePath, Path
from typing import List, Dict, Tuple, Optional, Any
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.table import Table
from rich import print as rprint
from rich.markup import escape
from rich.text import Text
from rich.align import Align
from rich.console import Group
from rich.box import HEAVY_EDGE, ROUNDED, DOUBLE_EDGE, HEAVY
from datetime import datetime
import pytz
import gmalg
from Crypto.Cipher import AES
from Crypto.Cipher.AES import MODE_CBC
from Crypto.Hash import SHA1
from Crypto.Util.Padding import unpad
from zstandard import ZstdDecompressor, ZstdCompressionDict, DICT_TYPE_AUTO, ZstdCompressor

console = Console()

# ═══════════════════════════════════════════════════════════════════════════
#  🎩  @AFTAB MODZ  —  GODFATHER LUXE THEME  🎩
# ═══════════════════════════════════════════════════════════════════════════

GOLD       = "#FFD700"
DEEP_GOLD  = "#B8860B"
LIGHT_GOLD = "#FFEC8B"
CREAM      = "#FFF8DC"
CRIMSON    = "#DC143C"
EMERALD    = "#50C878"

# ─────────────────────────────  BANNER  ─────────────────────────────

def print_banner():
    """Premium cyber-HUD banner tuned for Termux/mobile terminals."""
    os.system('cls' if os.name == 'nt' else 'clear')

    width = min(max(getattr(console, "width", 80), 58), 86)

    # Compact block logo: large enough to feel premium, small enough for phones.
    logo_lines = [
        " █████╗ ███████╗████████╗ █████╗ ██████╗ ",
        "██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗",
        "███████║█████╗     ██║   ███████║██████╔╝",
        "██╔══██║██╔══╝     ██║   ██╔══██║██╔══██╗",
        "██║  ██║███████╗   ██║   ██║  ██║██████╔╝",
        "╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ",
    ]

    logo = Group(*[
        Align.center(Text(line, style=f"bold {LIGHT_GOLD}"))
        for line in logo_lines
    ])

    sub = Text()
    sub.append("◆ ", style=GOLD)
    sub.append("AFTAB AHMAD VIP MOD", style=f"bold {CREAM}")
    sub.append(" ◆", style=GOLD)

    feature = Text()
    feature.append("LOCK", style=DEEP_GOLD)
    feature.append("  UNPACK", style=CREAM)
    feature.append("   │   ", style=GOLD)
    feature.append("INJECT", style=DEEP_GOLD)
    feature.append("   │   ", style=GOLD)
    feature.append("REPACK", style=DEEP_GOLD)
    feature.append("   │   ", style=GOLD)
    feature.append("PROTECT", style=DEEP_GOLD)

    status = Text()
    status.append("● ONLINE", style=f"bold {EMERALD}")
    status.append("  •  ", style=GOLD)
    status.append("TERMUX EDITION", style=f"bold {LIGHT_GOLD}")
    status.append("  •  ", style=GOLD)
    status.append(get_indian_time() + " IST", style=CREAM)

    footer = Text("★  PAK TOOL SUITE — PREMIUM EDITION  ★", style=f"bold {CRIMSON}")

    header = Group(
        logo,
        Text(""),
        Align.center(sub),
        Align.center(feature),
        Align.center(status),
        Text(""),
        Align.center(footer),
    )

    console.print(
        Panel(
            header,
            title="[bold #FFD700]╣ AFTAB MODZ ╠[/bold #FFD700]",
            subtitle="[dim]V4.6 • POWERED FOR TERMUX[/dim]",
            border_style=GOLD,
            box=DOUBLE_EDGE,
            padding=(0, 1),
            expand=True,
            width=width,
        )
    )


def get_indian_time():
    tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


def safe_input(prompt: str = '') -> str:
    try:
        return input(prompt)
    except (EOFError, RuntimeError):
        try:
            if sys.platform != 'win32':
                with open('/dev/tty', 'r') as tty:
                    sys.stderr.write(prompt)
                    sys.stderr.flush()
                    return tty.readline().rstrip('\n')
            else:
                with open('CON', 'r') as con:
                    sys.stderr.write(prompt)
                    sys.stderr.flush()
                    return con.readline().rstrip('\r\n')
        except Exception:
            return ''
    except Exception:
        return ''


def human_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f'{size:.2f} {unit}'
        size /= 1024.0
    return f'{size:.2f} PB'


# ═══════════════════════════════════════════════════════════════════════════
#  🎩  MENU  —  GODFATHER LUXE
# ═══════════════════════════════════════════════════════════════════════════

def print_menu():
    """Premium single-column HUD menu; optimized for narrow Termux screens."""
    width = min(max(getattr(console, "width", 80), 58), 86)

    rows = [
        ("01", "📦", "UNPACK PAK", "Extract files from PAK"),
        ("02", "💉", "INJECT / EDIT", "Modify or add files"),
        ("03", "🔨", "FULL REBUILD", "Rebuild complete PAK"),
        ("04", "📁", "REPACK TO PATH", "Save to custom path"),
        ("05", "🔐", "PROTECT PAK", "SM4 encryption / protection"),
        ("06", "🗑", "DELETE FOLDER", "Remove temporary files"),
        ("00", "🚪", "EXIT", "Close the tool"),
    ]

    lines = []
    for num, icon, title, desc in rows:
        line = Text()
        line.append("  ", style=GOLD)
        line.append(f"{num}", style=f"bold {LIGHT_GOLD}")
        line.append("  ", style=GOLD)
        line.append(icon + " ", style=DEEP_GOLD)
        line.append(f"{title:<17}", style=f"bold {CREAM}")
        line.append(" │ ", style=GOLD)
        line.append(desc, style=LIGHT_GOLD)
        line.append("  ›", style=f"bold {GOLD}")
        lines.append(line)

    content = Group(*[Align.left(x) for x in lines])

    console.print(
        Panel(
            content,
            title="[bold #FFEC8B]◆  MAIN MENU  ◆[/bold #FFEC8B]",
            border_style=GOLD,
            box=ROUNDED,
            padding=(1, 1),
            expand=True,
            width=width,
        )
    )

    prompt = Text()
    prompt.append("  ⌁ ", style=GOLD)
    prompt.append("YOUR COMMAND, BOSS", style=f"bold {LIGHT_GOLD}")
    prompt.append("   [1-6 / 0] › ", style=CREAM)
    console.print(
        Panel(
            prompt,
            border_style=DEEP_GOLD,
            box=HEAVY_EDGE,
            padding=(0, 1),
            width=width,
        ),
        end="",
    )


def print_menu_tip():
    console.print()
    width = min(max(getattr(console, "width", 80), 56), 92)
    console.print(
        Panel(
            Text.assemble(
                ("💡 TIP  ", f"bold {DEEP_GOLD}"),
                ("Drop files in PAK TOOL/EDIT keeping their in-pak path, then use ", CREAM),
                ("[2]", f"bold {LIGHT_GOLD}"),
                (" to inject them all at once.", CREAM),
            ),
            border_style=DEEP_GOLD,
            box=HEAVY_EDGE,
            padding=(0, 1),
            width=width,
        )
    )


# ═══════════════════════════════════════════════════════════════════════════
#  🎩  STYLED PANELS  (Rich-markup safe)
# ═══════════════════════════════════════════════════════════════════════════

def _strip_markup_len(s: str) -> int:
    """Approximate visible width: strip rich tags (rough)."""
    out = []
    i = 0
    while i < len(s):
        if s[i] == '[':
            j = s.find(']', i)
            if j != -1:
                i = j + 1
                continue
        out.append(s[i])
        i += 1
    return len(out)


def _panel_line(color: str, inner_markup: str, width: int = 74) -> str:
    visible = _strip_markup_len(inner_markup)
    pad = " " * max(0, width - visible)
    return f"[{color}]║[/{color}]{inner_markup}{pad}[{color}]║[/{color}]"


def panel_success(title: str, body: str):
    console.print()
    console.print(f"[{EMERALD}]╔══════════════════════════════════════════════════════════════════════════╗[/{EMERALD}]")
    console.print(_panel_line(EMERALD, f"[{LIGHT_GOLD}]  ✅ {escape(title)}[/{LIGHT_GOLD}]"))
    for line in body.split("\n"):
        console.print(_panel_line(EMERALD, f"[{CREAM}]    {escape(line)}[/{CREAM}]"))
    console.print(f"[{EMERALD}]╚══════════════════════════════════════════════════════════════════════════╝[/{EMERALD}]")
    console.print()


def panel_error(title: str, body: str):
    console.print()
    console.print(f"[{CRIMSON}]╔══════════════════════════════════════════════════════════════════════════╗[/{CRIMSON}]")
    console.print(_panel_line(CRIMSON, f"[{LIGHT_GOLD}]  ❌ {escape(title)}[/{LIGHT_GOLD}]"))
    for line in body.split("\n"):
        console.print(_panel_line(CRIMSON, f"[{CREAM}]    {escape(line)}[/{CREAM}]"))
    console.print(f"[{CRIMSON}]╚══════════════════════════════════════════════════════════════════════════╝[/{CRIMSON}]")
    console.print()


def panel_warn(title: str, body: str):
    console.print()
    console.print(f"[{GOLD}]╔══════════════════════════════════════════════════════════════════════════╗[/{GOLD}]")
    console.print(_panel_line(GOLD, f"[{LIGHT_GOLD}]  ⚠  {escape(title)}[/{LIGHT_GOLD}]"))
    for line in body.split("\n"):
        console.print(_panel_line(GOLD, f"[{CREAM}]    {escape(line)}[/{CREAM}]"))
    console.print(f"[{GOLD}]╚══════════════════════════════════════════════════════════════════════════╝[/{GOLD}]")
    console.print()


def section_header(icon: str, title: str):
    console.print()
    console.print(f"[{GOLD}]╭───────────────────────────── {icon}  [bold {LIGHT_GOLD}]{escape(title)}[/bold {LIGHT_GOLD}]  {icon} ─────────────────────────────╮[/{GOLD}]")


def section_footer():
    console.print(f"[{GOLD}]╰──────────────────────────────────────────────────────────────────────────╯[/{GOLD}]")


# ═══════════════════════════════════════════════════════════════════════════
#  SIMPLE BLOCK DISPLAY
# ═══════════════════════════════════════════════════════════════════════════

class SimpleBlockDisplay:
    def __init__(self, total_files: int, pak_name: str):
        self.total_files = total_files
        self.pak_name = pak_name
        self.processed_files = 0
        self.current_file = ""
        self.current_file_idx = 0
        self.all_blocks = []
        self.total_fitted = 0
        self.total_skipped = 0

    def start_file(self, file_name: str, total_blocks: int):
        self.current_file_idx += 1
        self.current_file = file_name
        self.current_blocks = []
        self.current_total_blocks = total_blocks
        self.current_fitted = 0
        self.current_skipped = 0

        console.print()
        console.print(f"[{GOLD}]┌─────────────────────────────────────────────────────────────[/{GOLD}]")
        console.print(f"[{GOLD}]│[/] [{LIGHT_GOLD}][{self.current_file_idx}/{self.total_files}][/] [{CREAM}]{escape(file_name)}[/{CREAM}] [{DEEP_GOLD}]({total_blocks} blocks)[/{DEEP_GOLD}]")
        console.print(f"[{GOLD}]├─────────────────────────────────────────────────────────────[/{GOLD}]")

    def add_block(self, block_idx: int, block_size: int, fitted: bool, compression_ratio: float = None):
        size_mb = block_size / (1024 * 1024)
        if fitted:
            self.current_fitted += 1
            self.total_fitted += 1
            ratio_str = f" [{compression_ratio:.1%}]" if compression_ratio else ""
            status = f"[{EMERALD}]✓ FITTED{ratio_str}[/{EMERALD}]"
        else:
            self.current_skipped += 1
            self.total_skipped += 1
            status = f"[{CRIMSON}]✗ SKIPPED[/{CRIMSON}]"
        console.print(f"[{GOLD}]│[/]    Block {block_idx:3d}: {size_mb:>7.2f} MB  →  {status}")
        self.current_blocks.append({'fitted': fitted})

    def finish_file(self):
        total_blocks = len(self.current_blocks)
        if total_blocks > 0:
            if self.current_fitted == total_blocks:
                status = f"[{EMERALD}]✓ ALL FITTED[/{EMERALD}]"
            elif self.current_fitted > 0:
                status = f"[{LIGHT_GOLD}]✓ {self.current_fitted}/{total_blocks} FITTED[/{LIGHT_GOLD}]"
            else:
                status = f"[{CRIMSON}]✗ ALL SKIPPED[/{CRIMSON}]"
        else:
            status = f"[{EMERALD}]✓ DONE[/{EMERALD}]"
        console.print(f"[{GOLD}]└─────────────────────────────────────────────────────────────[/{GOLD}]")
        console.print(f"  [{DEEP_GOLD}]Result:[/{DEEP_GOLD}] {status}")
        self.processed_files += 1
        self.all_blocks.extend(self.current_blocks)

    def final_summary(self):
        total_blocks = len(self.all_blocks)
        console.print()
        console.print(f"[{GOLD}]╔═════════════════════════════════════════════════════════════════╗[/{GOLD}]")
        console.print(f"[{GOLD}]║[/] [bold {LIGHT_GOLD}]🎩 REPACK SUMMARY[/bold {LIGHT_GOLD}]")
        console.print(f"[{GOLD}]║[/]")
        console.print(f"[{GOLD}]║[/]   Total Files:   [{LIGHT_GOLD}]{self.processed_files}[/{LIGHT_GOLD}]")
        console.print(f"[{GOLD}]║[/]   Total Blocks:  [{LIGHT_GOLD}]{total_blocks}[/{LIGHT_GOLD}]")
        console.print(f"[{GOLD}]║[/]   Fitted Blocks: [{EMERALD}]{self.total_fitted}[/{EMERALD}]")
        console.print(f"[{GOLD}]║[/]   Skipped Blocks:[{CRIMSON}]{self.total_skipped}[/{CRIMSON}]")
        if total_blocks > 0:
            success_rate = (self.total_fitted / total_blocks) * 100
            console.print(f"[{GOLD}]║[/]   Success Rate:  [{LIGHT_GOLD}]{success_rate:.1f}%[/{LIGHT_GOLD}]")
        console.print(f"[{GOLD}]╚═════════════════════════════════════════════════════════════════╝[/{GOLD}]")


# ═══════════════════════════════════════════════════════════════════════════
#  ORIGINAL CLASSES (UNCHANGED LOGIC)
# ═══════════════════════════════════════════════════════════════════════════

ZUC_KEY = bytes.fromhex('01010101010101010101010101010101')
ZUC_IV = bytes.fromhex('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

RSA_MOD_1 = bytes.fromhex('CBE8B9F2504050EF9831B719E9A6249A6D238505ADE909BDE78C180DED6072A0C3347B8AF4780E1F212D952D82D4BF7F233C1ECA499E1F9D9A85B4FAD759F54BABC1666C5DE411EA9E4B2374425DD6C6F54333BBC8F2610FE6063E4D0D6C21A671A8F7C3740555E5DC06D4E1691C456DB4116C0C012BF7B206E8311AAAEC689952BF804EF638F09D5822B4117B114208F14DEB459E80CB770E5B0D7978E21F5E6CED4999D3583108221A7AB28B960277ADB5690A332784019D9C195BE4EA9EA0A09459010F236465DE0D59C3EF7324E954E1118D93EE19F299760C2CDB963CE87973EA5ECC9BBE81C27D4C7C8572AC07E9BCEAC9BD72AB7A56A3C0AD736ABCE4')
RSA_MOD_2 = bytes.fromhex('7F58E8A39A4DA4E87357DDD650EAA16D3B5CE95B213D1030A662566444796A78A84AE9AC3DBFFDE7F41094896696835DAF13B89E6EC2B84963B1B1BAF7151DA245C3FBFAE2A6AE18B2684D03F9229DE2C91440F2A3A3BCDE1E5680C16722A88039C73560D5D43F4B6562C2EEA5B1D926D86B51108A2643C70FB74D6442CE3A08339B8FD8F660AE88129B7AB8C46F2FA58124485CCCB1E987B05A6DA65A01858ED3F89905449AE42BB07290FCB9994BF22E26610BCABB9804783A3B9587917F3D97316EDDA15C5E13F79066407B55A93B291B68A4AC42A98D6E35FED84B14A792D154E62028DDAD20FC301951E5924BE9AD62FB719DD94CC30CAB871BEC4377A8')

SIMPLE1_DECRYPT_KEY = 121
SIMPLE2_DECRYPT_KEY = bytes.fromhex('E55B4ED1')
SIMPLE2_BLOCK_SIZE = 16

SM4_SECRET_4 = 'eb691efea914241317a8'
SM4_SECRET_2 = 'Q0hVTKey$as*1ZFlQCiA'
SM4_SECRET_NEW = [
    'xG2qW5lP7lV2iN5fN5pG', 'xT1cJ6dL5wC0kK1rB4dK', 'qC4jS5bZ6fL5xE6nD4zA',
    'gD4jQ2aL3bS3lC3xT0iW', 'xU1yQ8wE9zY3gZ3bT5aE', 'uQ3cO2dX7xY4xU7gH7iS',
    'gW1fR0jK6wQ4oN0oK1kZ', 'aJ4pV7iZ7pU4wP2aC2cZ', 'cX6jT3cM2oT3vK0kJ1qN',
    'iT2vS0cS6yT6cZ1sE1lO', 'hM1pH9iY8wM9hT4lN5uJ', 'kG6bC8jK0fL0dE4sH4mL',
    'dB6lB3vE0eZ8wM8rI0aC', 'tP7sP7nI9rA2vQ4cV5yQ', 'aT0cL1yN4pT3sZ7eM2vY',
    'uV6fU8fC9zN3mP5dH8mN', 'rT6aQ6oZ1yM0gO5tO1aN', 'jU5bH7lQ0fM9hK2kI0oF',
    'iQ0eM0mJ7uT0kV6kL5zY',
]

EM_SIMPLE1 = 1
EM_SIMPLE2 = 16
EM_SM4_2 = 2
EM_SM4_4 = 4
EM_SM4_NEW_BASE = 31
EM_SM4_NEW_MASK = ~EM_SM4_NEW_BASE
EM_UNKNOWN_17 = 17

CM_NONE = 0
CM_ZLIB = 1
CM_ZSTD = 6
CM_ZSTD_DICT = 8
CM_MASK = 15


class SM4:
    _S_BOX = bytes([
        52, 102, 37, 116, 137, 120, 228, 169, 90, 65, 188, 122, 214, 22, 33, 35,
        77, 97, 218, 148, 155, 223, 19, 60, 105, 58, 49, 10, 95, 215, 153, 149,
        241, 174, 114, 61, 7, 96, 36, 182, 152, 238, 196, 162, 45, 136, 221, 141,
        4, 234, 187, 17, 202, 62, 93, 161, 246, 63, 176, 151, 128, 71, 43, 166,
        230, 247, 217, 177, 89, 192, 124, 190, 84, 40, 183, 126, 79, 248, 67, 110,
        160, 80, 14, 245, 144, 184, 251, 163, 123, 98, 25, 70, 3, 42, 185, 143,
        159, 119, 180, 91, 131, 135, 8, 235, 226, 30, 66, 240, 15, 232, 113, 106,
        117, 173, 85, 31, 181, 171, 51, 250, 127, 21, 189, 133, 216, 6, 104, 179,
        82, 48, 72, 11, 0, 237, 239, 178, 87, 142, 231, 108, 213, 229, 46, 83,
        130, 5, 249, 129, 244, 86, 191, 140, 75, 227, 219, 74, 145, 76, 44, 211,
        64, 41, 78, 32, 20, 54, 121, 9, 111, 209, 55, 224, 57, 12, 138, 146,
        56, 18, 53, 109, 225, 253, 147, 154, 23, 212, 201, 156, 107, 132, 38, 157,
        175, 118, 193, 158, 208, 150, 197, 203, 233, 115, 73, 210, 205, 100, 195, 199,
        1, 125, 243, 172, 252, 222, 164, 68, 50, 27, 194, 186, 28, 2, 198, 39,
        69, 139, 242, 24, 167, 16, 81, 29, 200, 207, 99, 255, 47, 13, 88, 206,
        101, 165, 220, 26, 59, 134, 254, 34, 92, 168, 94, 103, 170, 236, 112, 204
    ])
    _FK = [1184304796, 1270900830, 1493524870, 3164752158]
    _CK = [964907, 973793155, 2654690407, 2916866751, 2071233739, 1226140771, 3348805095, 2045549823,
           388349611, 800627875, 612403927, 3721562911, 1195432523, 3150178931, 612053223, 2445162591,
           67183755, 1174197155, 1393249511, 3331183455, 3822152747, 1332317203, 1804781383, 1990130463,
           1282653851, 3376591251, 2910902311, 925872959, 332098219, 735840931, 396665415, 3588844719]

    @staticmethod
    def ROL32(x, n):
        return (x << n) & 0xFFFFFFFF | (x >> (32 - n))

    @staticmethod
    def _BS(X):
        return (SM4._S_BOX[X >> 24 & 255] << 24 | SM4._S_BOX[X >> 16 & 255] << 16 |
                SM4._S_BOX[X >> 8 & 255] << 8 | SM4._S_BOX[X & 255])

    @staticmethod
    def _T0(X):
        X = SM4._BS(X)
        return X ^ SM4.ROL32(X, 2) ^ SM4.ROL32(X, 10) ^ SM4.ROL32(X, 18) ^ SM4.ROL32(X, 24)

    @staticmethod
    def _T1(X):
        X = SM4._BS(X)
        return X ^ SM4.ROL32(X, 13) ^ SM4.ROL32(X, 23)

    @staticmethod
    def _key_expand(key: bytes, rkey: list):
        K0 = int.from_bytes(key[0:4], 'big') ^ SM4._FK[0]
        K1 = int.from_bytes(key[4:8], 'big') ^ SM4._FK[1]
        K2 = int.from_bytes(key[8:12], 'big') ^ SM4._FK[2]
        K3 = int.from_bytes(key[12:16], 'big') ^ SM4._FK[3]
        for i in range(0, 32, 4):
            K0 = K0 ^ SM4._T1(K1 ^ K2 ^ K3 ^ SM4._CK[i]); rkey[i] = K0
            K1 = K1 ^ SM4._T1(K2 ^ K3 ^ K0 ^ SM4._CK[i + 1]); rkey[i + 1] = K1
            K2 = K2 ^ SM4._T1(K3 ^ K0 ^ K1 ^ SM4._CK[i + 2]); rkey[i + 2] = K2
            K3 = K3 ^ SM4._T1(K0 ^ K1 ^ K2 ^ SM4._CK[i + 3]); rkey[i + 3] = K3

    @classmethod
    def key_length(cls):
        return 16

    @classmethod
    def block_length(cls):
        return 16

    def __init__(self, key: bytes):
        if len(key) != self.key_length():
            raise ValueError(f'Key must be {self.key_length()} bytes')
        self._key = key
        self._rkey = [0] * 32
        SM4._key_expand(self._key, self._rkey)
        self._block_buffer = bytearray()
        if not hasattr(SM4, '_T_TABLES'):
            SM4._T_TABLES = SM4._make_t_tables()

    def encrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise ValueError(f'Block must be {self.block_length()} bytes')
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], 'big'); X1 = int.from_bytes(block[4:8], 'big')
        X2 = int.from_bytes(block[8:12], 'big'); X3 = int.from_bytes(block[12:16], 'big')
        for i in range(0, 32, 4):
            X0 = X0 ^ SM4._T0(X1 ^ X2 ^ X3 ^ RK[i])
            X1 = X1 ^ SM4._T0(X2 ^ X3 ^ X0 ^ RK[i + 1])
            X2 = X2 ^ SM4._T0(X3 ^ X0 ^ X1 ^ RK[i + 2])
            X3 = X3 ^ SM4._T0(X0 ^ X1 ^ X2 ^ RK[i + 3])
        BUFFER = self._block_buffer; BUFFER.clear()
        BUFFER.extend(X3.to_bytes(4, 'big')); BUFFER.extend(X2.to_bytes(4, 'big'))
        BUFFER.extend(X1.to_bytes(4, 'big')); BUFFER.extend(X0.to_bytes(4, 'big'))
        return bytes(BUFFER)

    def decrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise ValueError(f'Block must be {self.block_length()} bytes')
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], 'big'); X1 = int.from_bytes(block[4:8], 'big')
        X2 = int.from_bytes(block[8:12], 'big'); X3 = int.from_bytes(block[12:16], 'big')
        for i in range(0, 32, 4):
            X0 = X0 ^ SM4._T0(X1 ^ X2 ^ X3 ^ RK[31 - i])
            X1 = X1 ^ SM4._T0(X2 ^ X3 ^ X0 ^ RK[30 - i])
            X2 = X2 ^ SM4._T0(X3 ^ X0 ^ X1 ^ RK[29 - i])
            X3 = X3 ^ SM4._T0(X0 ^ X1 ^ X2 ^ RK[28 - i])
        BUFFER = self._block_buffer; BUFFER.clear()
        BUFFER.extend(X3.to_bytes(4, 'big')); BUFFER.extend(X2.to_bytes(4, 'big'))
        BUFFER.extend(X1.to_bytes(4, 'big')); BUFFER.extend(X0.to_bytes(4, 'big'))
        return bytes(BUFFER)

    @classmethod
    def _make_t_tables(cls):
        S = cls._S_BOX
        def rol(x, n): return (x << n) & 0xFFFFFFFF | (x >> (32 - n))
        def L(y): return y ^ rol(y, 2) ^ rol(y, 10) ^ rol(y, 18) ^ rol(y, 24)
        T0 = [0] * 256; T1 = [0] * 256; T2 = [0] * 256; T3 = [0] * 256
        for i in range(256):
            s = S[i]
            T0[i] = L(s << 24); T1[i] = L(s << 16); T2[i] = L(s << 8); T3[i] = L(s)
        return (T0, T1, T2, T3)

    def _bulk(self, data: bytes, rk) -> bytes:
        n = len(data); out = bytearray(n)
        T0, T1, T2, T3 = self._T_TABLES
        unpack_from = struct.unpack_from; pack_into = struct.pack_into
        idx = 0
        while idx < n:
            X0, X1, X2, X3 = unpack_from('>IIII', data, idx)
            for i in range(0, 32, 4):
                t = X1 ^ X2 ^ X3 ^ rk[i]
                X0 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
                t = X2 ^ X3 ^ X0 ^ rk[i + 1]
                X1 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
                t = X3 ^ X0 ^ X1 ^ rk[i + 2]
                X2 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
                t = X0 ^ X1 ^ X2 ^ rk[i + 3]
                X3 ^= T0[t >> 24] ^ T1[t >> 16 & 255] ^ T2[t >> 8 & 255] ^ T3[t & 255]
            pack_into('>IIII', out, idx, X3, X2, X1, X0)
            idx += 16
        return bytes(out)

    def encrypt_bulk(self, data: bytes) -> bytes:
        lib = _load_fast_sm4()
        if lib is not None:
            data = bytes(data); n = len(data)
            inbuf = ctypes.create_string_buffer(data); outbuf = ctypes.create_string_buffer(n)
            lib.sm4_ecb(ctypes.create_string_buffer(self._key), inbuf, outbuf, n, 1)
            return outbuf.raw
        return self._bulk(data, self._rkey)

    def decrypt_bulk(self, data: bytes) -> bytes:
        lib = _load_fast_sm4()
        if lib is not None:
            data = bytes(data); n = len(data)
            inbuf = ctypes.create_string_buffer(data); outbuf = ctypes.create_string_buffer(n)
            lib.sm4_ecb(ctypes.create_string_buffer(self._key), inbuf, outbuf, n, 0)
            return outbuf.raw
        return self._bulk(data, self._rkey[::-1])


_FAST_SM4_LIB = None
_FAST_SM4_TRIED = False


def _sm4_c_source() -> str:
    sbox = SM4._S_BOX; fk = SM4._FK; ck = SM4._CK
    L = []
    L.append('// auto-generated fast SM4 (GB/T 32907-2016) from tool.py constants')
    L.append('#include <stdint.h>'); L.append('#include <stddef.h>'); L.append('')
    L.append('static const uint8_t SBOX[256] = { ' + ', '.join(str(x) for x in sbox) + ' };')
    L.append('static const uint32_t FK[4] = { ' + ', '.join(hex(x) for x in fk) + ' };')
    L.append('static const uint32_t CK[32] = { ' + ', '.join(hex(x) for x in ck) + ' };')
    L.append('')
    L.append('static inline uint32_t rotl(uint32_t x, int n){ return (x << n) | (x >> (32 - n)); }')
    L.append('static inline uint32_t load_be(const uint8_t* p){ return ((uint32_t)p[0]<<24)|((uint32_t)p[1]<<16)|((uint32_t)p[2]<<8)|(uint32_t)p[3]; }')
    L.append('static inline void store_be(uint8_t* p, uint32_t v){ p[0]=(uint8_t)(v>>24); p[1]=(uint8_t)(v>>16); p[2]=(uint8_t)(v>>8); p[3]=(uint8_t)v; }')
    L.append('static inline uint32_t sb(uint32_t x){ return ((uint32_t)SBOX[(x>>24)&0xff]<<24)|((uint32_t)SBOX[(x>>16)&0xff]<<16)|((uint32_t)SBOX[(x>>8)&0xff]<<8)|(uint32_t)SBOX[x&0xff]; }')
    L.append('static inline uint32_t t0(uint32_t x){ x = sb(x); return x ^ rotl(x,2) ^ rotl(x,10) ^ rotl(x,18) ^ rotl(x,24); }')
    L.append('static inline uint32_t t1(uint32_t x){ x = sb(x); return x ^ rotl(x,13) ^ rotl(x,23); }')
    L.append('')
    L.append('static void expand(const uint8_t* key, uint32_t rk[32]){')
    L.append('    uint32_t k0 = load_be(key) ^ FK[0];')
    L.append('    uint32_t k1 = load_be(key+4) ^ FK[1];')
    L.append('    uint32_t k2 = load_be(key+8) ^ FK[2];')
    L.append('    uint32_t k3 = load_be(key+12) ^ FK[3];')
    L.append('    for (int i = 0; i < 32; i++){')
    L.append('        k0 ^= t1(k1 ^ k2 ^ k3 ^ CK[i]); rk[i] = k0;')
    L.append('        k1 ^= t1(k2 ^ k3 ^ k0 ^ CK[++i]); rk[i] = k1;')
    L.append('        k2 ^= t1(k3 ^ k0 ^ k1 ^ CK[++i]); rk[i] = k2;')
    L.append('        k3 ^= t1(k0 ^ k1 ^ k2 ^ CK[++i]); rk[i] = k3;')
    L.append('    }'); L.append('}')
    L.append('')
    L.append('static void crypt_block(const uint8_t* in, uint8_t* out, const uint32_t* rk){')
    L.append('    uint32_t x0 = load_be(in); uint32_t x1 = load_be(in+4);')
    L.append('    uint32_t x2 = load_be(in+8); uint32_t x3 = load_be(in+12);')
    L.append('    for (int i = 0; i < 32; i += 4){')
    L.append('        x0 ^= t0(x1 ^ x2 ^ x3 ^ rk[i]);')
    L.append('        x1 ^= t0(x2 ^ x3 ^ x0 ^ rk[i+1]);')
    L.append('        x2 ^= t0(x3 ^ x0 ^ x1 ^ rk[i+2]);')
    L.append('        x3 ^= t0(x0 ^ x1 ^ x2 ^ rk[i+3]);')
    L.append('    }')
    L.append('    store_be(out, x3); store_be(out+4, x2); store_be(out+8, x1); store_be(out+12, x0);')
    L.append('}')
    L.append('')
    L.append('void sm4_ecb(const uint8_t* key, const uint8_t* in, uint8_t* out, size_t len, int encrypt){')
    L.append('    uint32_t rk[32]; expand(key, rk);')
    L.append('    if (!encrypt){')
    L.append('        for (int i = 0; i < 16; i++){ uint32_t tmp = rk[i]; rk[i] = rk[31-i]; rk[31-i] = tmp; }')
    L.append('    }')
    L.append('    for (size_t off = 0; off < len; off += 16){ crypt_block(in + off, out + off, rk); }')
    L.append('}')
    return '\n'.join(L)


def _load_fast_sm4():
    global _FAST_SM4_LIB, _FAST_SM4_TRIED
    if _FAST_SM4_TRIED:
        return _FAST_SM4_LIB
    _FAST_SM4_TRIED = True
    # Android APKs should not compile native C code at runtime.
    # The pure-Python SM4 implementation below remains the fallback.
    if sys.platform == "android" or os.environ.get("ANDROID_ARGUMENT"):
        return None
    try:
        tool_dir = Path(__file__).resolve().parent
        src_path = tool_dir / 'sm4_fast.c'; so_path = tool_dir / 'sm4_fast.so'
        c_src = _sm4_c_source()
        if not src_path.exists():
            src_path.write_text(c_src)
        if src_path.read_text() != c_src:
            src_path.write_text(c_src)
        recompile = (not so_path.exists()) or (so_path.stat().st_mtime < src_path.stat().st_mtime)
        if recompile:
            for cc in ('gcc', 'cc', 'clang'):
                try:
                    r = subprocess.run([cc, '-O2', '-shared', '-fPIC', str(src_path), '-o', str(so_path)],
                                       capture_output=True, timeout=120)
                    if r.returncode == 0 and so_path.exists():
                        break
                except Exception:
                    continue
        if not so_path.exists():
            return None
        lib = ctypes.CDLL(str(so_path))
        lib.sm4_ecb.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
        lib.sm4_ecb.restype = None
        _FAST_SM4_LIB = lib
        return lib
    except Exception:
        return None


class Misc:
    @staticmethod
    def pad_to_n(data: bytes, n: int) -> bytes:
        assert n > 0
        padding = n - len(data) % n
        if padding == n:
            return data
        return data + b'\x00' * padding

    @staticmethod
    def align_up(x: int, n: int) -> int:
        return (x + n - 1) // n * n


class Reader:
    def __init__(self, buffer, cursor=0):
        self._buffer = buffer; self._cursor = cursor

    def u1(self, move_cursor=True): return self.unpack('B', move_cursor=move_cursor)[0]
    def u4(self, move_cursor=True): return self.unpack('<I', move_cursor=move_cursor)[0]
    def u8(self, move_cursor=True): return self.unpack('<Q', move_cursor=move_cursor)[0]
    def i1(self, move_cursor=True): return self.unpack('b', move_cursor=move_cursor)[0]
    def i4(self, move_cursor=True): return self.unpack('<i', move_cursor=move_cursor)[0]
    def i8(self, move_cursor=True): return self.unpack('<q', move_cursor=move_cursor)[0]
    def s(self, n: int, move_cursor=True): return self.unpack(f'{n}s', move_cursor=move_cursor)[0]

    def unpack(self, f: str, offset=0, move_cursor=True):
        x = struct.unpack_from(f, self._buffer, self._cursor + offset)
        if move_cursor:
            self._cursor += struct.calcsize(f)
        return x

    def string(self, move_cursor=True):
        length = self.i4(move_cursor=move_cursor)
        if length == 0:
            return str()
        assert length > 0
        offset = 0 if move_cursor else 4
        return self.unpack(f'{length}s', offset=offset, move_cursor=move_cursor)[0].rstrip(b'\x00').decode()


class PakInfo:
    def __init__(self, buffer, keystream: List[int]):
        def decrypt_index_encrypted(x): return (x ^ keystream[3]) & 255
        def decrypt_magic(x): return x ^ keystream[2]
        def decrypt_index_hash(x):
            key = struct.pack('<5I', *keystream[4:][:5])
            assert len(x) == len(key)
            return bytes((a ^ b for a, b in zip(x, key)))
        def decrypt_index_size(x): return x ^ (keystream[10] << 32 | keystream[11])
        def decrypt_index_offset(x): return x ^ (keystream[0] << 32 | keystream[1])
        reader = Reader(buffer[-PakInfo._mem_size((-1)):])
        self.index_encrypted = decrypt_index_encrypted(reader.u1()) == 1
        self.magic = decrypt_magic(reader.u4())
        self.version = reader.u4()
        self.index_hash = decrypt_index_hash(reader.s(20)) if self.version >= 6 else bytes()
        self.index_size = decrypt_index_size(reader.u8())
        self.index_offset = decrypt_index_offset(reader.u8())
        if self.version <= 3:
            self.index_encrypted = False

    @staticmethod
    def _mem_size(_): return 45


class TencentPakInfo(PakInfo):
    def __init__(self, buffer, keystream: List[int]):
        def decrypt_unk(x):
            key = struct.pack('<8I', *keystream[7:][:8])
            assert len(x) == len(key)
            return bytes((a ^ b for a, b in zip(x, key)))
        def decrypt_stem_hash(x): return x ^ keystream[8]
        def decrypt_unk_hash(x): return x ^ keystream[9]
        super().__init__(buffer, keystream)
        reader = Reader(buffer[-TencentPakInfo._mem_size(self.version):])
        self.unk1 = decrypt_unk(reader.s(32)) if self.version >= 7 else bytes()
        self.packed_key = reader.s(256) if self.version >= 8 else bytes()
        self.packed_iv = reader.s(256) if self.version >= 8 else bytes()
        self.packed_index_hash = reader.s(256) if self.version >= 8 else bytes()
        self.stem_hash = decrypt_stem_hash(reader.u4()) if self.version >= 9 else 0
        self.unk2 = decrypt_unk_hash(reader.u4()) if self.version >= 9 else 0
        self.content_org_hash = reader.s(20) if self.version >= 12 else bytes()

    @staticmethod
    def _mem_size(version: int) -> int:
        s7 = 32 if version >= 7 else 0
        s8 = 768 if version >= 8 else 0
        s9 = 8 if version >= 9 else 0
        s12 = 20 if version >= 12 else 0
        return PakInfo._mem_size(version) + s7 + s8 + s9 + s12


class PakCompressedBlock:
    def __init__(self, reader: Reader):
        self.start = reader.u8(); self.end = reader.u8()


@dataclass
class TencentPakEntry:
    def __init__(self, reader: Reader, version: int):
        self.content_hash = reader.s(20)
        if version <= 1:
            _ = reader.u8()
        self.offset = reader.u8()
        self.uncompressed_size = reader.u8()
        self.compression_method = reader.u4() & CM_MASK
        self.size = reader.u8()
        self.unk1 = reader.u1() if version >= 5 else 0
        self.unk2 = reader.s(20) if version >= 5 else bytes()
        if self.compression_method != 0 and version >= 3:
            self.compressed_blocks = [PakCompressedBlock(reader) for _ in range(reader.u4())]
        else:
            self.compressed_blocks = []
        self.compression_block_size = reader.u4() if version >= 4 else 0
        self.encrypted = reader.u1() == 1 if version >= 4 else False
        self.encryption_method = reader.u4() if version >= 12 else 0
        self.index_new_sep = reader.u4() if version >= 12 else 0


class PakCrypto:
    class _LCG:
        def __init__(self, seed):
            self.state = seed

        def next(self):
            MASK_32 = 4294967295
            MSB_1 = 2147483648

            def wrap(x):
                x &= MASK_32
                if not x & MSB_1:
                    return x
                return (x + MSB_1 & MASK_32) - MSB_1

            x1 = wrap(1103515245 * self.state)
            self.state = wrap(x1 + 12345)
            x2 = wrap(x1 + 77880) if self.state < 0 else self.state
            return (x2 >> 16 & MASK_32) % 32767

    @staticmethod
    def zuc_keystream() -> List[int]:
        zuc = gmalg.ZUC(ZUC_KEY, ZUC_IV)
        return [struct.unpack('>I', zuc.generate())[0] for _ in range(16)]

    @staticmethod
    def _xorxor(buffer, x):
        return bytes((buffer[i] ^ x[i % len(x)] for i in range(len(buffer))))

    @staticmethod
    def _hashhash(buffer, n):
        result = bytes()
        for i in range(math.ceil(n / SHA1.digest_size)):
            result += SHA1.new(buffer).digest()
        if len(result) >= n:
            return result[:n]
        return result + b'\x00' * (n - len(result))

    @staticmethod
    def _meowmeow(buffer):
        def unpad(x):
            skip = 1 + next((i for i in range(len(x)) if x[i] != 0))
            return x[skip:]

        if len(buffer) < 43:
            return bytes()
        x1 = buffer[1:][:SHA1.digest_size]
        x2 = buffer[SHA1.digest_size + 1:]
        x1 = PakCrypto._xorxor(x1, PakCrypto._hashhash(x2, len(x1)))
        x2 = PakCrypto._xorxor(x2, PakCrypto._hashhash(x1, len(x2)))
        part1, m = (x2[:SHA1.digest_size], x2[SHA1.digest_size:])
        if part1 != SHA1.new(b'\x00' * SHA1.digest_size).digest():
            return bytes()
        return unpad(m)

    @staticmethod
    def rsa_extract(signature, modulus):
        c = int.from_bytes(signature, 'little')
        n = int.from_bytes(modulus, 'little')
        e = 65537
        m = pow(c, e, n).to_bytes(256, 'little').rstrip(b'\x00')
        return PakCrypto._meowmeow(Misc.pad_to_n(m, 4))

    @staticmethod
    def _decrypt_simple1(ciphertext):
        return bytes((x ^ SIMPLE1_DECRYPT_KEY for x in ciphertext))

    @staticmethod
    def _decrypt_simple2(ciphertext):
        class RollingKey:
            def __init__(self, initial_value):
                self._value = initial_value

            def update(self, x):
                self._value ^= x
                return self._value

        assert len(ciphertext) % SIMPLE2_BLOCK_SIZE == 0
        initial_key, = struct.unpack('<I', SIMPLE2_DECRYPT_KEY)
        rolling_key = RollingKey(initial_key)
        plaintext = (struct.pack('<I', rolling_key.update(x)) for x in
                     struct.unpack(f'<{len(ciphertext) // 4}I', ciphertext))
        return bytes(it.chain.from_iterable(plaintext))

    @staticmethod
    @lru_cache(maxsize=1)
    def _derive_sm4_key(file_path: PurePath, encryption_method: int) -> bytes:
        part1 = file_path.stem.lower()
        if encryption_method == EM_SM4_2:
            secret = SM4_SECRET_2
        else:
            if encryption_method == EM_SM4_4:
                secret = SM4_SECRET_4
            else:
                index = (encryption_method - EM_SM4_NEW_BASE) % len(SM4_SECRET_NEW)
                secret = f'{SM4_SECRET_NEW[index]}{encryption_method}'
        return SHA1.new(str(part1 + secret).encode()).digest()[:SM4.key_length()]

    @staticmethod
    @lru_cache(maxsize=1)
    def _sm4_context_for_key(key):
        return SM4(key)

    @staticmethod
    def _decrypt_sm4(ciphertext, file_path, encryption_method):
        assert len(ciphertext) % SM4.block_length() == 0
        key = PakCrypto._derive_sm4_key(file_path, encryption_method)
        sm4 = PakCrypto._sm4_context_for_key(key)
        return sm4.decrypt_bulk(ciphertext)

    @staticmethod
    def decrypt_index(ciphertext, pak_info):
        if pak_info.version > 7:
            key = PakCrypto.rsa_extract(pak_info.packed_key, RSA_MOD_1)
            iv = PakCrypto.rsa_extract(pak_info.packed_iv, RSA_MOD_1)
            assert len(key) == 32 and len(iv) == 32
            aes = AES.new(key, MODE_CBC, iv[:16])
            return unpad(aes.decrypt(ciphertext), AES.block_size)
        return bytes(PakCrypto._decrypt_simple1(ciphertext))

    @staticmethod
    def _is_simple1_method(em): return em == EM_SIMPLE1

    @staticmethod
    def _is_simple2_method(em): return em == EM_SIMPLE2 or em == 17

    @staticmethod
    def _is_sm4_method(em): return em == EM_SM4_2 or em == EM_SM4_4 or em & EM_SM4_NEW_MASK != 0

    @staticmethod
    def align_encrypted_content_size(n, em):
        if PakCrypto._is_simple2_method(em):
            return Misc.align_up(n, SIMPLE2_BLOCK_SIZE)
        if PakCrypto._is_sm4_method(em):
            return Misc.align_up(n, SM4.block_length())
        return n

    @staticmethod
    def decrypt_block(ciphertext, file, encryption_method):
        if PakCrypto._is_simple1_method(encryption_method):
            return PakCrypto._decrypt_simple1(ciphertext)
        if PakCrypto._is_simple2_method(encryption_method):
            return PakCrypto._decrypt_simple2(ciphertext)
        if PakCrypto._is_sm4_method(encryption_method):
            return PakCrypto._decrypt_sm4(ciphertext, file, encryption_method)
        raise ValueError(f'Unknown encryption method: {encryption_method}')

    @staticmethod
    @lru_cache(maxsize=33)
    def generate_block_indices(n, encryption_method):
        if not PakCrypto._is_sm4_method(encryption_method):
            return list(range(n))
        permutation = []
        lcg = PakCrypto._LCG(n)
        while len(permutation) != n:
            x = lcg.next() % n
            if x not in permutation:
                permutation.append(x)
        inverse = [0] * len(permutation)
        for i, x in enumerate(permutation):
            inverse[x] = i
        return inverse


class PakCompression:
    @staticmethod
    @lru_cache(maxsize=33)
    def _zstd_decompressor(dict):
        return ZstdDecompressor(dict)

    @staticmethod
    def zstd_dictionary(dict_data):
        return ZstdCompressionDict(dict_data, DICT_TYPE_AUTO)

    @staticmethod
    def decompress_block(block, dict, compression_method):
        if compression_method == CM_ZLIB:
            try:
                return zlib.decompress(block)
            except zlib.error:
                return block
        if compression_method == CM_ZSTD or compression_method == CM_ZSTD_DICT:
            if compression_method != CM_ZSTD_DICT:
                dict = None
            return PakCompression._zstd_decompressor(dict).decompress(block)
        raise ValueError(f'Unknown compression method: {compression_method}')


class TencentPakFile:
    def __init__(self, file_path, is_od=False):
        self._file_path = file_path
        with open(file_path, 'rb') as file:
            self._file_content = memoryview(file.read())
        self._is_od = is_od
        self._mount_point = PurePath()
        self._is_zstd_with_dict = 'zsdic' in str(self._file_path)
        self._zstd_dict = None
        self._zstd_dict_entry = None
        self._files = []
        self._index = {}
        self._pak_info = TencentPakInfo(self._file_content, PakCrypto.zuc_keystream())
        self._verify_stem_hash()
        self._tencent_load_index()

    def _get_method_str(self, method_int, is_encryption):
        if is_encryption:
            if PakCrypto._is_simple1_method(method_int): return "SIMPLE1"
            if PakCrypto._is_simple2_method(method_int): return "SIMPLE2"
            if PakCrypto._is_sm4_method(method_int): return f"SM4 (Type {method_int})"
            return "NONE" if method_int == 0 else "UNKNOWN"
        else:
            if method_int == CM_NONE: return "NONE"
            if method_int == CM_ZLIB: return "ZLIB"
            if method_int == CM_ZSTD: return "ZSTD"
            if method_int == CM_ZSTD_DICT: return "ZSTD_DICT"
            return "UNKNOWN"

    def _verify_stem_hash(self):
        if not self._is_od and self._pak_info.version >= 9:
            try:
                assert self._pak_info.stem_hash == zlib.crc32(self._file_path.stem.encode('utf-32le'))
            except AssertionError:
                panel_warn("Stem Hash Mismatch",
                           "PAK filename differs from original stem.\nRename back to match before game use.")

    def _tencent_load_index(self):
        index_data = self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size]
        if self._pak_info.index_encrypted:
            index_data = PakCrypto.decrypt_index(index_data, self._pak_info)
        self._verify_index_hash(index_data)
        self._load_index(index_data)

    def _verify_index_hash(self, index_data):
        expected_hash = self._pak_info.index_hash
        if not self._is_od and self._pak_info.version >= 8:
            if expected_hash != PakCrypto.rsa_extract(self._pak_info.packed_index_hash, RSA_MOD_2):
                panel_warn("Index Hash Mismatch", "Rebuilt PAK — stale RSA blob, ignored.")
        assert expected_hash == SHA1.new(index_data).digest()

    @staticmethod
    def _construct_mount_point(mount_point):
        result = PurePath()
        for part in PurePath(mount_point).parts:
            if part != '..':
                result /= part
        return result

    def _peek_content(self, offset, size, encryption_method):
        size = PakCrypto.align_encrypted_content_size(size, encryption_method)
        return self._file_content[offset:][:size]

    def _peek_block_content(self, block, encryption_method):
        size = PakCrypto.align_encrypted_content_size(block.end - block.start, encryption_method)
        return self._file_content[block.start:][:size]

    def _construct_zstd_dict(self, dict_entry):
        assert not self._zstd_dict
        assert not dict_entry.encrypted
        assert dict_entry.compression_method == CM_NONE
        reader = Reader(self._peek_content(dict_entry.offset, dict_entry.size, 0))
        dict_size = reader.u8()
        _ = reader.u4()
        assert dict_size == reader.u4()
        dict_data = reader.s(dict_size)
        self._zstd_dict = PakCompression.zstd_dictionary(dict_data)

    def _load_index(self, index_data):
        if self._pak_info.version <= 10:
            raise ValueError(f'Unsupported version: {self._pak_info.version}')
        reader = Reader(index_data)
        self._mount_point = self._construct_mount_point(reader.string())
        self._files = [TencentPakEntry(reader, self._pak_info.version) for _ in range(reader.u4())]
        for _ in range(reader.u8()):
            dir_path = PurePath(reader.string())
            e = {reader.string(): self._files[~reader.i4()] for _ in range(reader.u8())}
            if self._is_zstd_with_dict and dir_path.name == 'zstddic':
                assert len(e) == 1
                self._zstd_dict_entry = e[[*e.keys()][0]]
                self._construct_zstd_dict(self._zstd_dict_entry)
            else:
                self._index.update({PurePath(dir_path): e})

    def _write_to_disk(self, file_path, entry):
        encryption_method = entry.encryption_method
        compression_method = entry.compression_method
        enc_str = self._get_method_str(encryption_method, True)
        comp_str = self._get_method_str(compression_method, False)
        console.print(f"[{GOLD}]  ✓[/{GOLD}] [{CREAM}]{escape(file_path.name)}[/{CREAM}] [{DEEP_GOLD}][{comp_str}/{enc_str}][/{DEEP_GOLD}]")
        with open(file_path, 'wb') as file:
            if compression_method == CM_NONE:
                data = self._peek_content(entry.offset, entry.size, encryption_method)
                if entry.encrypted:
                    data = PakCrypto.decrypt_block(data, file_path, encryption_method)
                file.write(data[:entry.uncompressed_size])
                return
            try:
                for x in PakCrypto.generate_block_indices(len(entry.compressed_blocks), encryption_method):
                    data = self._peek_block_content(entry.compressed_blocks[x], encryption_method)
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(data, file_path, encryption_method)
                    data = PakCompression.decompress_block(data, self._zstd_dict, compression_method)
                    file.write(data)
            except Exception as exc:
                file.seek(0); file.truncate()
                raw = bytearray()
                for blk in entry.compressed_blocks:
                    raw += self._peek_block_content(blk, encryption_method)
                file.write(raw)
                console.print(f"[{CRIMSON}]  ![/{CRIMSON}] [{CREAM}]Raw dump for undecryptable file[/{CREAM}] [{LIGHT_GOLD}]{escape(file_path.name)}[/{LIGHT_GOLD}]")

    def dump(self, out_path):
        out_path = out_path / self._mount_point
        out_path.mkdir(parents=True, exist_ok=True)
        total_files = sum(len(d) for d in self._index.values())
        with Progress(
            SpinnerColumn(style=GOLD),
            TextColumn(f"[bold {LIGHT_GOLD}][UNPACK][/bold {LIGHT_GOLD}] {{task.description}}"),
            BarColumn(bar_width=None, complete_style=GOLD, finished_style=EMERALD),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task(f"[{CREAM}]Extracting files...[/{CREAM}]", total=total_files)
            for dir_path, dir_content in self._index.items():
                current_out_path = out_path / dir_path
                current_out_path.mkdir(parents=True, exist_ok=True)
                for file_name, entry in dir_content.items():
                    self._write_to_disk(current_out_path / file_name, entry)
                    progress.update(task, advance=1)


def dump_unpacking_log(pak_file, output_log_path):
    with open(output_log_path, 'w', encoding='utf-8') as log_file:
        log_file.write('=' * 80 + '\n')
        log_file.write('@AFTAB MODZ  —  PAK UNPACKING DEBUG LOG\n')
        log_file.write('=' * 80 + '\n\n')
        log_file.write(f'PAK File: {pak_file._file_path}\n')
        log_file.write(f'PAK Info Version: {pak_file._pak_info.version}\n')
        log_file.write(f'Mount Point: {pak_file._mount_point}\n')
        log_file.write('-' * 80 + '\n\n')
        file_count = 0
        for dir_path, files in pak_file._index.items():
            for file_name, entry in files.items():
                file_count += 1
                full_path = str(PurePath(dir_path) / file_name).replace('\\', '/')
                log_file.write(f'\n[{file_count}] {full_path}\n')
                log_file.write(f'  Uncompressed Size: {entry.uncompressed_size:,} bytes\n')
                log_file.write(f'  Compressed Size: {entry.size:,} bytes\n')
                log_file.write(f'  Compression Method: {entry.compression_method}\n')
                log_file.write(f'  Encryption Method: {entry.encryption_method}\n')
                log_file.write(f'  Compressed Blocks: {len(entry.compressed_blocks)}\n')
                if entry.compressed_blocks:
                    for i, blk in enumerate(entry.compressed_blocks):
                        log_file.write(f'    Block {i}: Offset={blk.start:,} Size={blk.end - blk.start:,} bytes\n')
        log_file.write('\n' + '=' * 80 + '\nEND OF LOG\n' + '=' * 80 + '\n')
    console.print(f"[{EMERALD}]  ✅ Debug log saved:[/{EMERALD}] [{CREAM}]{output_log_path}[/{CREAM}]")


def _zstd_add_skippable_padding(data: bytes, pad_len: int) -> bytes:
    if pad_len <= 0:
        return data
    out = bytearray(data)
    while pad_len > 0:
        frame_len = min(max(pad_len - 8, 0), 1048576)
        out += b'P*M\x18'
        out += struct.pack('<I', frame_len)
        out += b'\x00' * frame_len
        pad_len -= 8 + frame_len
    return bytes(out)


def _encrypt_plaintext(plaintext, pak_relative_path, encryption_method):
    if PakCrypto._is_simple1_method(encryption_method):
        return bytes((b ^ SIMPLE1_DECRYPT_KEY for b in plaintext))
    if PakCrypto._is_simple2_method(encryption_method):
        pad = -len(plaintext) % SIMPLE2_BLOCK_SIZE
        plaintext += b'\x00' * pad
        key, = struct.unpack('<I', SIMPLE2_DECRYPT_KEY)
        rolling = key
        out = []
        for x, in struct.iter_unpack('<I', plaintext):
            c = rolling ^ x
            out.append(c)
            rolling ^= c
        return struct.pack(f'<{len(out)}I', *out)
    if PakCrypto._is_sm4_method(encryption_method):
        key = PakCrypto._derive_sm4_key(pak_relative_path, encryption_method)
        sm4 = PakCrypto._sm4_context_for_key(key)
        pad_len = -len(plaintext) % 16
        if pad_len > 0:
            plaintext += b'\x00' * pad_len
        return sm4.encrypt_bulk(plaintext)
    return plaintext


# ═══════════════════════════════════════════════════════════════════════════
#  REPACK FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def _repack_uncompressed(outfh, pak_file, entry, pak_relative_path, new_data):
    enc_method = entry.encryption_method
    target_size = entry.size
    enc_region = PakCrypto.align_encrypted_content_size(target_size, enc_method) if entry.encrypted else target_size
    plaintext = new_data[:enc_region]
    if entry.encrypted:
        a = PakCrypto.align_encrypted_content_size(len(plaintext), enc_method)
        plaintext += b'\x00' * (a - len(plaintext))
        cipher = _encrypt_plaintext(plaintext, pak_relative_path, enc_method)
        outfh.seek(entry.offset)
        outfh.write(cipher)
        with open(pak_file._file_path, 'rb') as src:
            src.seek(entry.offset + len(cipher))
            outfh.write(src.read(enc_region - len(cipher)))
    else:
        outfh.seek(entry.offset)
        outfh.write(plaintext)
        with open(pak_file._file_path, 'rb') as src:
            src.seek(entry.offset + len(plaintext))
            outfh.write(src.read(target_size - len(plaintext)))


def _best_compress(chunk, cm, zstd_dict=None, fast=False):
    if cm == CM_ZLIB:
        return zlib.compress(chunk, 1 if fast else 9)
    if cm in (CM_ZSTD, CM_ZSTD_DICT):
        zd = zstd_dict if cm == CM_ZSTD_DICT else None
        levels = [6, 3, 1] if fast else [22, 19, 16, 13, 10, 7, 4, 1]
        for lvl in levels:
            try:
                return ZstdCompressor(level=lvl, dict_data=zd, threads=1).compress(chunk)
            except Exception:
                continue
    return chunk


def _pw_string(s):
    if not s:
        return struct.pack('<i', 0)
    b = s.encode('utf-8') + b'\x00'
    return struct.pack('<i', len(b)) + b


def _pw_entry(e, v):
    w = bytearray(e.content_hash)
    w += struct.pack('<Q', e.offset)
    w += struct.pack('<Q', e.uncompressed_size)
    w += struct.pack('<I', e.compression_method)
    w += struct.pack('<Q', e.size)
    if v >= 5:
        w += bytes([e.unk1])
        w += e.unk2
    if e.compression_method != CM_NONE and v >= 3:
        w += struct.pack('<I', len(e.compressed_blocks))
        for b in e.compressed_blocks:
            w += struct.pack('<QQ', b.start, b.end)
    if v >= 4:
        w += struct.pack('<I', e.compression_block_size)
        w += bytes([1 if e.encrypted else 0])
    if v >= 12:
        w += struct.pack('<II', e.encryption_method, e.index_new_sep)
    return bytes(w)


def _get_all_dirs_and_mp(pak_file):
    raw = bytes(pak_file._file_content[pak_file._pak_info.index_offset:][:pak_file._pak_info.index_size])
    if pak_file._pak_info.index_encrypted:
        raw = PakCrypto.decrypt_index(raw, pak_file._pak_info)
    r = Reader(raw)
    mp = r.string()
    num_files = r.u4()
    for _ in range(num_files):
        TencentPakEntry(r, pak_file._pak_info.version)
    dirs = {}
    for _ in range(r.u8()):
        dp = r.string()
        cnt = r.u8()
        dirs[dp] = {r.string(): pak_file._files[~r.i4()] for _ in range(cnt)}
    return mp, dirs


def repack_pak_file_full(pak_file, edited_root, output_path, target_path=None, force_add=False):
    import copy as _cp
    section_header("🔨", "FULL PAK REBUILD")
    if target_path:
        console.print(f"[{GOLD}]│[/{GOLD}]  [{LIGHT_GOLD}]🎯 Target path:[/{LIGHT_GOLD}] [{CREAM}]{escape(target_path)}[/{CREAM}]")
    section_footer()

    edit_files = [p for p in Path(edited_root).rglob('*') if p.is_file()]
    if not edit_files:
        panel_error("No Files Found", "EDIT folder is empty!")
        return 0

    console.print(f"[{GOLD}]  📁 Found[/{GOLD}] [{LIGHT_GOLD}]{len(edit_files)}[/{LIGHT_GOLD}] [{GOLD}]files in EDIT folder[/{GOLD}]")

    version = pak_file._pak_info.version
    keystream = PakCrypto.zuc_keystream()
    orig_fc = pak_file._file_content

    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)

    if target_path and force_add:
        target_path = target_path.replace('\\', '/')
        matched_dir = None
        for existing_dir in all_dirs.keys():
            if existing_dir.strip('/').lower() == target_path.strip('/').lower():
                matched_dir = existing_dir
                break
        if matched_dir:
            target_path = matched_dir
        else:
            target_path = target_path.strip('/') + '/'

    pak_name_map = {}
    for dir_path, files in pak_file._index.items():
        for name, entry in files.items():
            full_path = str(PurePath(dir_path) / name).replace('\\', '/')
            pak_name_map.setdefault(name.lower(), []).append((full_path, entry))

    edited = {}
    for p in edit_files:
        fl = p.name.lower()
        found_match = False
        if fl in pak_name_map:
            cands = pak_name_map[fl]
            if target_path:
                target_candidates = [(fp, e) for fp, e in cands if target_path.strip('/') in fp]
                if target_candidates:
                    sz = p.stat().st_size
                    sm = [(fp, e) for fp, e in target_candidates if e.uncompressed_size == sz]
                    fp, ent = sm[0] if sm else target_candidates[0]
                    edited[fp] = (p, ent)
                    found_match = True
            if not found_match:
                sz = p.stat().st_size
                sm = [(fp, e) for fp, e in cands if e.uncompressed_size == sz]
                fp, ent = sm[0] if sm else cands[0]
                if target_path:
                    new_fp = f"{target_path.rstrip('/')}/{p.name}"
                    edited[new_fp] = (p, ent)
                else:
                    edited[fp] = (p, ent)
                found_match = True
        if not found_match:
            stem = p.stem.lower()
            ext = p.suffix.lower()
            for dir_path, files in pak_file._index.items():
                for name, entry in files.items():
                    if Path(name).stem.lower() == stem and Path(name).suffix.lower() == ext:
                        full_path = str(PurePath(dir_path) / name).replace('\\', '/')
                        if target_path:
                            new_fp = f"{target_path.rstrip('/')}/{p.name}"
                            edited[new_fp] = (p, entry)
                        else:
                            edited[full_path] = (p, entry)
                        found_match = True
                        break
                if found_match:
                    break
        if not found_match and force_add and target_path:
            template_entry = None
            for dir_path, files in pak_file._index.items():
                for name, entry in files.items():
                    if Path(name).suffix.lower() == p.suffix.lower():
                        template_entry = entry
                        break
                if template_entry:
                    break
            if not template_entry:
                for dir_path, files in pak_file._index.items():
                    for name, entry in files.items():
                        template_entry = entry
                        break
                    if template_entry:
                        break
            if template_entry:
                new_fp = f"{target_path.rstrip('/')}/{p.name}"
                edited[new_fp] = (p, template_entry)

    if not edited:
        panel_error("No Files to Repack", "Could not match any files.")
        return 0

    console.print(f"[{GOLD}]  📁 Files to repack:[/{GOLD}] [{LIGHT_GOLD}]{len(edited)}[/{LIGHT_GOLD}]")

    new_files = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}
    edited_paths = {fp: p for fp, (p, _) in edited.items()}

    out_buf = bytearray()
    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry), None)
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne

            em = old_entry.encryption_method
            cm = old_entry.compression_method
            if full_path in edited_paths:
                p, template = edited[full_path]
                new_raw = p.read_bytes()
                pak_rel = PurePath(full_path)
                ne.content_hash = SHA1.new(new_raw).digest()
                ne.uncompressed_size = len(new_raw)
                ne.compression_method = template.compression_method if template else cm
                ne.encryption_method = template.encryption_method if template else em
                ne.encrypted = template.encrypted if template else old_entry.encrypted
                ne.unk1 = template.unk1 if template else old_entry.unk1
                if template and target_path:
                    full_path_str = mp_str + full_path
                    ne.unk2 = SHA1.new(full_path_str.lower().encode('utf-8')).digest()
                else:
                    ne.unk2 = template.unk2 if template else old_entry.unk2
                ne.index_new_sep = template.index_new_sep if template else old_entry.index_new_sep

                if ne.compression_method == CM_NONE:
                    cipher = (_encrypt_plaintext(new_raw, pak_rel, ne.encryption_method)
                              if ne.encrypted else new_raw)
                    ne.offset = len(out_buf)
                    ne.size = len(new_raw)
                    ne.uncompressed_size = len(new_raw)
                    out_buf += cipher
                else:
                    cs = (template.compression_block_size if template and template.compression_block_size > 0
                          else old_entry.compression_block_size if old_entry.compression_block_size > 0
                          else 65536)
                    chunks = [new_raw[i:i + cs] for i in range(0, len(new_raw), cs)]
                    new_blks = []
                    for chunk in chunks:
                        compressed = _best_compress(chunk, ne.compression_method, pak_file._zstd_dict)
                        cipher = (_encrypt_plaintext(compressed, pak_rel, ne.encryption_method)
                                  if ne.encrypted else compressed)
                        blk = PakCompressedBlock.__new__(PakCompressedBlock)
                        blk.start = len(out_buf)
                        blk.end = blk.start + len(cipher)
                        out_buf += cipher
                        new_blks.append(blk)
                    ne.compressed_blocks = new_blks
                    ne.offset = new_blks[0].start if new_blks else len(out_buf)
                    ne.size = sum(b.end - b.start for b in new_blks)
                    ne.uncompressed_size = len(new_raw)
                console.print(f"[{EMERALD}]  ✓ Processed:[/{EMERALD}] [{CREAM}]{escape(full_path)}[/{CREAM}]")
            else:
                if cm == CM_NONE:
                    read_sz = (PakCrypto.align_encrypted_content_size(old_entry.size, em)
                               if old_entry.encrypted else old_entry.size)
                    ne.offset = len(out_buf)
                    out_buf += bytes(orig_fc[old_entry.offset: old_entry.offset + read_sz])
                elif old_entry.compressed_blocks:
                    new_blks = []
                    for ob in old_entry.compressed_blocks:
                        unc = ob.end - ob.start
                        enc = (PakCrypto.align_encrypted_content_size(unc, em)
                               if old_entry.encrypted else unc)
                        nb = PakCompressedBlock.__new__(PakCompressedBlock)
                        nb.start = len(out_buf)
                        nb.end = nb.start + unc
                        out_buf += bytes(orig_fc[ob.start: ob.start + enc])
                        new_blks.append(nb)
                    ne.compressed_blocks = new_blks
                    ne.offset = new_blks[0].start

    if target_path and force_add:
        for fp, (p, template) in edited.items():
            already = False
            for dp_str, dir_files in all_dirs.items():
                for name, entry in dir_files.items():
                    if str(PurePath(dp_str) / name).replace('\\', '/') == fp:
                        already = True
                        break
                if already:
                    break
            if already:
                continue
            ne = _cp.copy(template)
            new_raw = p.read_bytes()
            pak_rel = PurePath(fp)
            ne.content_hash = SHA1.new(new_raw).digest()
            ne.uncompressed_size = len(new_raw)
            ne.compression_method = template.compression_method
            ne.encryption_method = template.encryption_method
            ne.encrypted = template.encrypted
            ne.unk1 = template.unk1
            full_path_str = mp_str + fp
            ne.unk2 = SHA1.new(full_path_str.lower().encode('utf-8')).digest()
            ne.index_new_sep = template.index_new_sep
            if ne.compression_method == CM_NONE:
                cipher = (_encrypt_plaintext(new_raw, pak_rel, ne.encryption_method)
                          if ne.encrypted else new_raw)
                ne.offset = len(out_buf)
                ne.size = len(new_raw)
                ne.uncompressed_size = len(new_raw)
                out_buf += cipher
            else:
                cs = template.compression_block_size if template.compression_block_size > 0 else 65536
                chunks = [new_raw[i:i + cs] for i in range(0, len(new_raw), cs)]
                new_blks = []
                for chunk in chunks:
                    compressed = _best_compress(chunk, ne.compression_method, pak_file._zstd_dict)
                    cipher = (_encrypt_plaintext(compressed, pak_rel, ne.encryption_method)
                              if ne.encrypted else compressed)
                    blk = PakCompressedBlock.__new__(PakCompressedBlock)
                    blk.start = len(out_buf)
                    blk.end = blk.start + len(cipher)
                    out_buf += cipher
                    new_blks.append(blk)
                ne.compressed_blocks = new_blks
                ne.offset = new_blks[0].start if new_blks else len(out_buf)
                ne.size = sum(b.end - b.start for b in new_blks)
                ne.uncompressed_size = len(new_raw)
            new_files.append(ne)
            if target_path not in all_dirs:
                all_dirs[target_path] = {}
            all_dirs[target_path][p.name] = ne
            console.print(f"[{EMERALD}]  ✓ Added new:[/{EMERALD}] [{CREAM}]{escape(fp)}[/{CREAM}]")

    _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path)
    return len(edited)


# ═══════════════════════════════════════════════════════════════════════════
#  MULTI-FILE INJECT + PROTECT
# ═══════════════════════════════════════════════════════════════════════════

def _normalize_dir_key(path_str):
    s = str(path_str).replace('\\', '/').strip('/')
    return (s + '/') if s else ''


def _find_existing_dir(all_dirs, want_dir):
    want = _normalize_dir_key(want_dir).strip('/').lower()
    if not want:
        return ''
    for k in all_dirs:
        if k.strip('/').lower() == want:
            return k
    best = None
    for k in all_dirs:
        key = k.strip('/').lower()
        if key and want.endswith('/' + key):
            if best is None or len(key) > len(best):
                best = k
    return best


def _strip_mount_prefix(pak_file, rel_dir):
    mp = str(pak_file._mount_point).replace('\\', '/').strip('/')
    rd = str(rel_dir).replace('\\', '/').strip('/')
    if mp and (rd.lower() == mp.lower() or rd.lower().startswith(mp.lower() + '/')):
        return rd[len(mp):].lstrip('/')
    return rd


def _pick_template(pak_file, all_dirs, target_dir, file_name):
    ext = Path(file_name).suffix.lower()
    if target_dir in all_dirs:
        for name, e in all_dirs[target_dir].items():
            if Path(name).suffix.lower() == ext:
                return e
    for dp, files in all_dirs.items():
        for name, e in files.items():
            if Path(name).suffix.lower() == ext:
                return e
    for dp, files in all_dirs.items():
        for name, e in files.items():
            return e
    return pak_file._files[0] if pak_file._files else None


def _default_compression(pak_file):
    cm_counter = {}
    for e in pak_file._files:
        cm = e.compression_method
        if cm in (CM_ZLIB, CM_ZSTD, CM_ZSTD_DICT):
            cm_counter[cm] = cm_counter.get(cm, 0) + 1
    if pak_file._is_zstd_with_dict and cm_counter.get(CM_ZSTD_DICT, 0):
        return CM_ZSTD_DICT
    if cm_counter.get(CM_ZSTD, 0):
        return CM_ZSTD
    if cm_counter.get(CM_ZSTD_DICT, 0):
        return CM_ZSTD
    return CM_ZLIB


def _write_entry_content(out_buf, ne, plaintext, pak_rel, zstd_dict, fast=False):
    if ne.compression_method == CM_NONE:
        cipher = (_encrypt_plaintext(plaintext, pak_rel, ne.encryption_method)
                  if ne.encrypted else plaintext)
        ne.offset = len(out_buf)
        ne.size = len(plaintext)
        ne.uncompressed_size = len(plaintext)
        out_buf += cipher
        return
    cs = ne.compression_block_size if ne.compression_block_size > 0 else 65536
    chunks = [plaintext[i:i + cs] for i in range(0, len(plaintext), cs)]
    if not chunks:
        ne.compressed_blocks = []
        ne.offset = len(out_buf)
        ne.size = 0
        ne.uncompressed_size = 0
        return
    n = len(chunks)
    inv = PakCrypto.generate_block_indices(n, ne.encryption_method) if ne.encrypted else list(range(n))
    file_order = [0] * n
    for j in range(n):
        file_order[inv[j]] = j
    new_blks = [None] * n
    for k in range(n):
        chunk = chunks[file_order[k]]
        compressed = _best_compress(chunk, ne.compression_method, zstd_dict, fast=fast)
        cipher = (_encrypt_plaintext(compressed, pak_rel, ne.encryption_method)
                  if ne.encrypted else compressed)
        blk = PakCompressedBlock.__new__(PakCompressedBlock)
        blk.start = len(out_buf)
        blk.end = blk.start + len(cipher)
        out_buf += cipher
        new_blks[k] = blk
    ne.compressed_blocks = new_blks
    ne.offset = new_blks[0].start
    ne.size = sum(b.end - b.start for b in new_blks)
    ne.uncompressed_size = len(plaintext)


def _extract_entry_plaintext(pak_file, entry, full_path):
    em = entry.encryption_method
    cm = entry.compression_method
    path = PurePath(full_path)
    if cm == CM_NONE:
        data = pak_file._peek_content(entry.offset, entry.size, em)
        if entry.encrypted:
            data = PakCrypto.decrypt_block(data, path, em)
        return bytes(data[:entry.uncompressed_size])
    out = bytearray()
    for x in PakCrypto.generate_block_indices(len(entry.compressed_blocks), em):
        data = pak_file._peek_block_content(entry.compressed_blocks[x], em)
        if entry.encrypted:
            data = PakCrypto.decrypt_block(data, path, em)
        out += PakCompression.decompress_block(data, pak_file._zstd_dict, cm)
    return bytes(out)


def _copy_original_content(out_buf, pak_file, ne, old_entry):
    em = old_entry.encryption_method
    if old_entry.compression_method == CM_NONE:
        read_sz = (PakCrypto.align_encrypted_content_size(old_entry.size, em)
                   if old_entry.encrypted else old_entry.size)
        ne.offset = len(out_buf)
        out_buf += bytes(pak_file._file_content[old_entry.offset: old_entry.offset + read_sz])
    elif old_entry.compressed_blocks:
        new_blks = []
        for ob in old_entry.compressed_blocks:
            unc = ob.end - ob.start
            enc = (PakCrypto.align_encrypted_content_size(unc, em)
                   if old_entry.encrypted else unc)
            nb = PakCompressedBlock.__new__(PakCompressedBlock)
            nb.start = len(out_buf)
            nb.end = nb.start + unc
            out_buf += bytes(pak_file._file_content[ob.start: ob.start + enc])
            new_blks.append(nb)
        ne.compressed_blocks = new_blks
        ne.offset = new_blks[0].start
    ne.encryption_method = old_entry.encryption_method
    ne.encrypted = old_entry.encrypted


def _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path):
    version = pak_file._pak_info.version
    keystream = PakCrypto.zuc_keystream()
    eidx = {id(new_files[i]): i for i in range(len(new_files))}
    old_id_to_new_idx = {id(pak_file._files[i]): i for i in range(len(pak_file._files))}
    idx = bytearray(_pw_string(mp_str))
    idx += struct.pack('<I', len(new_files))
    for ne in new_files:
        idx += _pw_entry(ne, version)
    idx += struct.pack('<Q', len(all_dirs))
    for dp_str, dir_files in all_dirs.items():
        idx += _pw_string(dp_str)
        idx += struct.pack('<Q', len(dir_files))
        for name, old_e in dir_files.items():
            idx += _pw_string(name)
            found_idx = eidx.get(id(old_e))
            if found_idx is None:
                found_idx = old_id_to_new_idx.get(id(old_e))
            if found_idx is None:
                copy_of = next((k for k, v in old_to_new.items() if v is old_e), None)
                if copy_of is not None:
                    found_idx = eidx.get(id(old_to_new[copy_of]))
            if found_idx is None:
                for i, e in enumerate(new_files):
                    if e.offset == old_e.offset and e.size == old_e.size:
                        found_idx = i
                        break
            idx += struct.pack('<i', ~found_idx if found_idx is not None else -1)
    index_plain = bytes(idx)
    new_sha1 = SHA1.new(index_plain).digest()
    if pak_file._pak_info.index_encrypted:
        key = PakCrypto.rsa_extract(pak_file._pak_info.packed_key, RSA_MOD_1)
        iv = PakCrypto.rsa_extract(pak_file._pak_info.packed_iv, RSA_MOD_1)
        aes = AES.new(key, MODE_CBC, iv[:16])
        pad = (-len(index_plain)) % AES.block_size or AES.block_size
        index_bytes = aes.encrypt(index_plain + bytes([pad] * pad))
    else:
        index_bytes = index_plain
    new_idx_offset = len(out_buf)
    new_idx_size = len(index_bytes)
    out_buf += index_bytes
    footer_sz = TencentPakInfo._mem_size(version)
    new_footer = bytearray(pak_file._file_content[-footer_sz:])
    h_key = struct.pack('<5I', *keystream[4:9])
    new_footer[-36:-16] = bytes(a ^ b for a, b in zip(new_sha1, h_key))
    new_footer[-16:-8] = ((new_idx_size ^ (keystream[10] << 32 | keystream[11])).to_bytes(8, 'little'))
    new_footer[-8:] = ((new_idx_offset ^ (keystream[0] << 32 | keystream[1])).to_bytes(8, 'little'))
    out_buf += new_footer
    with open(output_path, 'wb') as f:
        f.write(out_buf)


def inject_edit_files(pak_file, edit_root, output_path, protect_new=False, sm4_type=47):
    import copy as _cp
    version = pak_file._pak_info.version
    if version < 12:
        raise ValueError(f'Unsupported pak version: {version} (need >= 12)')
    edit_files = [p for p in Path(edit_root).rglob('*') if p.is_file()]
    if not edit_files:
        raise ValueError(f'No files found in EDIT folder: {edit_root}')
    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)
    injections = {}
    for p in edit_files:
        rel = p.relative_to(edit_root)
        parts = rel.parts
        file_name = parts[-1]
        rel_dir = '/'.join(parts[:-1]).replace('\\', '/')
        rel_dir = _strip_mount_prefix(pak_file, rel_dir)
        target_dir = _find_existing_dir(all_dirs, rel_dir) if rel_dir.strip('/') else ''
        if target_dir is None:
            target_dir = _normalize_dir_key(rel_dir)
        existing = None
        if target_dir in all_dirs:
            for name, e in list(all_dirs[target_dir].items()):
                if name.lower() == file_name.lower():
                    existing = (name, e)
                    break
        if existing:
            full_path = target_dir + existing[0]
            injections[full_path] = (p, existing[1], False)
        else:
            full_path = target_dir + file_name
            template = _pick_template(pak_file, all_dirs, target_dir, file_name)
            injections[full_path] = (p, template, True)
        console.print(f"[{GOLD}]  ●[/{GOLD}] [{CREAM}]{escape(full_path)}[/{CREAM}] [{DEEP_GOLD}]({'replace' if existing else 'add new'})[/{DEEP_GOLD}]")

    new_files = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}
    out_buf = bytearray()
    edited_count = 0
    new_count = 0
    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry), None)
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne
            if full_path in injections:
                p, template, is_new = injections[full_path]
                new_raw = p.read_bytes()
                pak_rel = PurePath(full_path)
                ne.content_hash = SHA1.new(new_raw).digest()
                ne.uncompressed_size = len(new_raw)
                if is_new:
                    ne.compression_method = _default_compression(pak_file)
                    if protect_new:
                        ne.encryption_method = sm4_type
                        ne.encrypted = True
                    else:
                        ne.encryption_method = template.encryption_method if template else 0
                        ne.encrypted = template.encrypted if template else False
                    ne.unk1 = template.unk1 if template else 0
                    ne.compression_block_size = (template.compression_block_size if template
                                                 and template.compression_block_size > 0 else 65536)
                    ne.index_new_sep = template.index_new_sep if template else 0
                    new_count += 1
                else:
                    ne.compression_method = old_entry.compression_method
                    if protect_new:
                        ne.encryption_method = sm4_type
                        ne.encrypted = True
                    else:
                        ne.encryption_method = old_entry.encryption_method
                        ne.encrypted = old_entry.encrypted
                    ne.unk1 = old_entry.unk1
                    ne.compression_block_size = (old_entry.compression_block_size
                                                 if old_entry.compression_block_size > 0 else 65536)
                    ne.index_new_sep = old_entry.index_new_sep
                    edited_count += 1
                ne.unk2 = SHA1.new((mp_str + full_path).lower().encode('utf-8')).digest()
                _write_entry_content(out_buf, ne, new_raw, pak_rel, pak_file._zstd_dict)
                console.print(f"[{EMERALD}]  ✓ {'Edited' if not is_new else 'Added'}:[/{EMERALD}] "
                              f"[{CREAM}]{escape(full_path)}[/{CREAM}] [{DEEP_GOLD}]({len(new_raw):,} B)[/{DEEP_GOLD}]")
            else:
                _copy_original_content(out_buf, pak_file, ne, old_entry)

    for full_path, (p, template, is_new) in injections.items():
        if not is_new:
            continue
        already = False
        for dp_str, dir_files in all_dirs.items():
            for name, entry in dir_files.items():
                if str(PurePath(dp_str) / name).replace('\\', '/') == full_path:
                    already = True
                    break
            if already:
                break
        if already:
            continue
        ne = _cp.copy(template) if template else None
        if ne is None:
            ne = TencentPakEntry(Reader(b''), version)
            ne.compression_method = CM_NONE
            ne.encrypted = False
        else:
            ne.compressed_blocks = [_cp.copy(b) for b in template.compressed_blocks]
        new_raw = p.read_bytes()
        pak_rel = PurePath(full_path)
        ne.content_hash = SHA1.new(new_raw).digest()
        ne.uncompressed_size = len(new_raw)
        ne.compression_method = _default_compression(pak_file)
        if protect_new:
            ne.encryption_method = sm4_type
            ne.encrypted = True
        else:
            ne.encryption_method = template.encryption_method if template else 0
            ne.encrypted = template.encrypted if template else False
        ne.unk1 = template.unk1 if template else 0
        ne.compression_block_size = (template.compression_block_size if template
                                     and template.compression_block_size > 0 else 65536)
        ne.index_new_sep = template.index_new_sep if template else 0
        ne.unk2 = SHA1.new((mp_str + full_path).lower().encode('utf-8')).digest()
        _write_entry_content(out_buf, ne, new_raw, pak_rel, pak_file._zstd_dict)
        new_files.append(ne)
        old_to_new[id(ne)] = ne
        dp_key = full_path.rsplit('/', 1)[0] + '/' if '/' in full_path else ''
        all_dirs.setdefault(dp_key, {})[full_path.rsplit('/', 1)[-1]] = ne
        new_count += 1
        console.print(f"[{EMERALD}]  ✓ Added:[/{EMERALD}] [{CREAM}]{escape(full_path)}[/{CREAM}] "
                      f"[{DEEP_GOLD}]({len(new_raw):,} B)[/{DEEP_GOLD}]")

    _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path)
    return edited_count, new_count


def protect_pak_file(pak_file, output_path, sm4_type=47):
    import copy as _cp
    version = pak_file._pak_info.version
    if version < 12:
        raise ValueError(f'Unsupported pak version: {version} (need >= 12)')
    mp_str, all_dirs = _get_all_dirs_and_mp(pak_file)
    new_files = []
    for e in pak_file._files:
        ne = _cp.copy(e)
        ne.compressed_blocks = [_cp.copy(b) for b in e.compressed_blocks]
        new_files.append(ne)
    old_to_new = {id(pak_file._files[i]): new_files[i] for i in range(len(pak_file._files))}
    out_buf = bytearray()
    protected = 0
    skipped = 0
    for dp_str, dir_files in list(all_dirs.items()):
        for name, old_entry in list(dir_files.items()):
            full_path = str(PurePath(dp_str) / name).replace('\\', '/')
            ne = old_to_new.get(id(old_entry), None)
            if ne is None:
                ne = _cp.copy(old_entry)
                ne.compressed_blocks = [_cp.copy(b) for b in old_entry.compressed_blocks]
                new_files.append(ne)
                old_to_new[id(old_entry)] = ne
            is_marker = (old_entry.compression_method == CM_NONE and old_entry.size == 0)
            is_zdict = (pak_file._zstd_dict_entry is not None and old_entry is pak_file._zstd_dict_entry)
            if is_marker or is_zdict:
                _copy_original_content(out_buf, pak_file, ne, old_entry)
                skipped += 1
                continue
            try:
                plaintext = _extract_entry_plaintext(pak_file, old_entry, full_path)
            except Exception:
                _copy_original_content(out_buf, pak_file, ne, old_entry)
                skipped += 1
                console.print(f"[{CRIMSON}]  ! Skipped undecryptable:[/{CRIMSON}] [{CREAM}]{escape(full_path)}[/{CREAM}]")
                continue
            ne.compression_method = old_entry.compression_method
            if ne.compression_method == CM_NONE:
                ne.compression_method = CM_ZLIB
            ne.encryption_method = sm4_type
            ne.encrypted = True
            ne.unk1 = old_entry.unk1
            ne.unk2 = old_entry.unk2
            ne.index_new_sep = old_entry.index_new_sep
            ne.compression_block_size = (old_entry.compression_block_size
                                         if old_entry.compression_block_size > 0 else 65536)
            _write_entry_content(out_buf, ne, plaintext, PurePath(full_path), pak_file._zstd_dict, fast=True)
            protected += 1
            if protected <= 12 or protected % 250 == 0:
                console.print(f"[{GOLD}]  🔒[/{GOLD}] [{LIGHT_GOLD}]Re-encrypted:[/{LIGHT_GOLD}] "
                              f"[{CREAM}]{escape(full_path)}[/{CREAM}] [{DEEP_GOLD}]({len(plaintext):,} B)[/{DEEP_GOLD}]")
    _write_pak_index_footer(pak_file, mp_str, all_dirs, new_files, old_to_new, out_buf, output_path)
    return protected, skipped


# ═══════════════════════════════════════════════════════════════════════════
#  ORIGINAL REPACK (OPTION 2 legacy)
# ═══════════════════════════════════════════════════════════════════════════

def _repack_compressed_with_display(outfh, pak_file, entry, pak_relative_path, new_data, repack_dir, display):
    blocks = entry.compressed_blocks
    enc_method = entry.encryption_method
    comp_method = entry.compression_method
    order = PakCrypto.generate_block_indices(len(blocks), enc_method)
    if len(new_data) != entry.uncompressed_size:
        if len(new_data) < entry.uncompressed_size:
            new_data = new_data.ljust(entry.uncompressed_size, b'\x00')
        else:
            new_data = new_data[:entry.uncompressed_size]
    if len(blocks) > 1:
        if entry.compression_block_size > 0:
            chunk_size = entry.compression_block_size
        else:
            block_sizes = [blk.end - blk.start for blk in blocks]
            total_block_size = sum(block_sizes)
            avg_block_size = total_block_size / len(blocks)
            avg_compression_ratio = total_block_size / entry.uncompressed_size if entry.uncompressed_size > 0 else 1
            chunk_size = int(avg_block_size / avg_compression_ratio) if avg_compression_ratio > 0 else 65536
        ptr = 0
        for logical_i, phys_i in enumerate(order):
            blk = blocks[phys_i]
            target_size = blk.end - blk.start
            chunk_len = min(chunk_size, len(new_data) - ptr)
            if chunk_len <= 0:
                break
            chunk = new_data[ptr:ptr + chunk_len]
            ptr += chunk_len
            with open(pak_file._file_path, 'rb') as src:
                src.seek(blk.start)
                original_compressed = src.read(target_size)
            compressed_ok = False
            new_compressed = None
            zstd_dict = pak_file._zstd_dict if comp_method == CM_ZSTD_DICT else None
            if comp_method in (CM_ZSTD, CM_ZSTD_DICT):
                for level in [22, 19, 16, 13, 10, 7, 4, 1]:
                    c = ZstdCompressor(level=level, dict_data=zstd_dict, threads=1)
                    new_compressed = c.compress(chunk)
                    if len(new_compressed) <= target_size:
                        compressed_ok = True
                        break
            elif comp_method == CM_ZLIB:
                new_compressed = zlib.compress(chunk, zlib.Z_BEST_COMPRESSION)
                if len(new_compressed) <= target_size:
                    compressed_ok = True
            if not compressed_ok:
                outfh.seek(blk.start)
                outfh.write(original_compressed)
                display.add_block(logical_i, target_size, False)
                continue
            if entry.encrypted:
                if PakCrypto._is_sm4_method(enc_method):
                    pad_len = -len(new_compressed) % 16
                    if pad_len > 0:
                        new_compressed += b'\x00' * pad_len
                new_compressed = _encrypt_plaintext(new_compressed, pak_relative_path, enc_method)
            if len(new_compressed) > target_size:
                outfh.seek(blk.start)
                outfh.write(original_compressed)
                display.add_block(logical_i, target_size, False)
            else:
                outfh.seek(blk.start)
                outfh.write(new_compressed)
                if len(new_compressed) < target_size:
                    outfh.write(b'\x00' * (target_size - len(new_compressed)))
                ratio = len(new_compressed) / len(chunk) if len(chunk) > 0 else 1
                display.add_block(logical_i, target_size, True, ratio)
    else:
        if not blocks:
            return
        blk = blocks[0]
        target_size = blk.end - blk.start
        with open(pak_file._file_path, 'rb') as src:
            src.seek(blk.start)
            original_compressed = src.read(target_size)
        compressed_ok = False
        new_compressed = None
        zstd_dict = pak_file._zstd_dict if comp_method == CM_ZSTD_DICT else None
        if comp_method in (CM_ZSTD, CM_ZSTD_DICT):
            for level in [22, 19, 16, 13, 10, 7, 4, 1]:
                c = ZstdCompressor(level=level, dict_data=zstd_dict, threads=1)
                new_compressed = c.compress(new_data)
                if len(new_compressed) <= target_size:
                    compressed_ok = True
                    break
        elif comp_method == CM_ZLIB:
            new_compressed = zlib.compress(new_data, zlib.Z_BEST_COMPRESSION)
            if len(new_compressed) <= target_size:
                compressed_ok = True
        if not compressed_ok:
            outfh.seek(blk.start)
            outfh.write(original_compressed)
            display.add_block(0, target_size, False)
            return
        if entry.encrypted:
            if PakCrypto._is_sm4_method(enc_method):
                pad_len = -len(new_compressed) % 16
                if pad_len > 0:
                    new_compressed += b'\x00' * pad_len
            new_compressed = _encrypt_plaintext(new_compressed, pak_relative_path, enc_method)
        if len(new_compressed) > target_size:
            outfh.seek(blk.start)
            outfh.write(original_compressed)
            display.add_block(0, target_size, False)
        else:
            outfh.seek(blk.start)
            outfh.write(new_compressed)
            if len(new_compressed) < target_size:
                outfh.write(b'\x00' * (target_size - len(new_compressed)))
            ratio = len(new_compressed) / len(new_data) if len(new_data) > 0 else 1
            display.add_block(0, target_size, True, ratio)


def smart_resolve_by_fingerprint(filename, repack_file, candidates):
    repack_size = repack_file.stat().st_size
    size_matches = [(path, entry) for path, entry in candidates if entry.uncompressed_size == repack_size]
    if len(size_matches) == 1:
        return size_matches[0]
    if not size_matches:
        return None

    def fingerprint(e):
        return (e.uncompressed_size, e.size, e.compression_method, len(e.compressed_blocks), e.compression_block_size)

    base_fp = fingerprint(size_matches[0][1])
    final_matches = [(path, entry) for path, entry in size_matches if fingerprint(entry) == base_fp]
    if len(final_matches) == 1:
        return final_matches[0]
    return None


def repack_pak_file_with_block_display(pak_file, edited_root, output_path):
    shutil.copy2(pak_file._file_path, output_path)
    pak_name_map = {}
    for dir_path, files in pak_file._index.items():
        for name, entry in files.items():
            full_path = str(PurePath(dir_path) / name).replace('\\', '/')
            key = name.lower()
            pak_name_map.setdefault(key, []).append((full_path, entry))
    edited = {}
    for p in edited_root.rglob('*'):
        if not p.is_file():
            continue
        fname_lower = p.name.lower()
        if fname_lower in pak_name_map:
            candidates = pak_name_map[fname_lower]
            if len(candidates) == 1:
                full_path, entry = candidates[0]
                edited[full_path] = (p, entry)
            else:
                resolved = smart_resolve_by_fingerprint(filename=p.name, repack_file=p, candidates=candidates)
                if resolved:
                    full_path, entry = resolved
                    edited[full_path] = (p, entry)
        else:
            stem = p.stem.lower()
            ext = p.suffix.lower()
            for dir_path, files in pak_file._index.items():
                for name, entry in files.items():
                    if Path(name).stem.lower() == stem and Path(name).suffix.lower() == ext:
                        full_path = str(PurePath(dir_path) / name).replace('\\', '/')
                        edited[full_path] = (p, entry)
                        break
    if not edited:
        panel_error("No Files to Repack", "Could not match any files.")
        return
    total_files = len(edited)
    display = SimpleBlockDisplay(total_files, pak_file._file_path.name)
    with open(output_path, 'r+b') as outfh:
        for full_path, (p, entry) in edited.items():
            file_name = p.name
            total_blocks = len(entry.compressed_blocks) if entry.compressed_blocks else 1
            display.start_file(file_name, total_blocks)
            new_data = p.read_bytes()
            pak_rel = PurePath(full_path)
            if entry.compression_method == CM_NONE:
                _repack_uncompressed(outfh, pak_file, entry, pak_rel, new_data)
                display.add_block(0, len(new_data), True)
            else:
                _repack_compressed_with_display(outfh, pak_file, entry, pak_rel, new_data, edited_root, display)
            display.finish_file()
    display.final_summary()


def detect_repack_mode(pak_path):
    name = pak_path.name.lower()
    if name == 'mini_obb.pak':
        return 'MINI_OBB'
    if 'zsdic' in name:
        return 'OBBZSDIC'
    if 'game' in name or 'patch' in name:
        return 'GAMEPATCH'
    return 'OBBZSDIC'


def repack_mini_obb(pak, repack_dir, output_pak):
    console.print(f"[{GOLD}]🧩 Repack Mode:[/{GOLD}] [{LIGHT_GOLD}]MINI_OBB[/{LIGHT_GOLD}]")
    pak._is_zstd_with_dict = False
    pak._zstd_dict = None
    repack_pak_file_with_block_display(pak_file=pak, edited_root=repack_dir, output_path=output_pak)


def repack_obbzsdic(pak, repack_dir, output_pak):
    console.print(f"[{GOLD}]🧩 Repack Mode:[/{GOLD}] [{LIGHT_GOLD}]OBBZSDIC[/{LIGHT_GOLD}]")
    repack_pak_file_with_block_display(pak_file=pak, edited_root=repack_dir, output_path=output_pak)


def repack_gamepatch(pak, repack_dir, output_pak):
    console.print(f"[{GOLD}]🧩 Repack Mode:[/{GOLD}] [{LIGHT_GOLD}]GAMEPATCH[/{LIGHT_GOLD}]")
    pak._is_zstd_with_dict = False
    pak._zstd_dict = None
    repack_pak_file_with_block_display(pak_file=pak, edited_root=repack_dir, output_path=output_pak)


def ensure_directories(base_dir):
    (base_dir / "PAK").mkdir(parents=True, exist_ok=True)
    (base_dir / "UNPACK").mkdir(parents=True, exist_ok=True)
    (base_dir / "REPACK").mkdir(parents=True, exist_ok=True)
    (base_dir / "RESULT").mkdir(parents=True, exist_ok=True)
    pak_tool_dir = base_dir / "PAK TOOL"
    (pak_tool_dir / "EDIT").mkdir(parents=True, exist_ok=True)
    (pak_tool_dir / "UNPACK").mkdir(parents=True, exist_ok=True)
    (pak_tool_dir / "RESULT").mkdir(parents=True, exist_ok=True)
    (pak_tool_dir / "PAK").mkdir(parents=True, exist_ok=True)


def delete_folder(data_path):
    folders = []
    for item in data_path.iterdir():
        if item.is_dir() and item.name not in ['PAK', 'UNPACK', 'REPACK', 'RESULT', 'PAK TOOL']:
            folders.append(item)
    if not folders:
        panel_warn("No Folders", "Nothing to delete.")
        return
    console.print()
    console.print(f"[{GOLD}]╭────────────────────── 📁 AVAILABLE FOLDERS ──────────────────────╮[/{GOLD}]")
    for i, folder in enumerate(folders, 1):
        folder_size = 0
        for root, dirs, files in os.walk(folder):
            for file in files:
                fp = os.path.join(root, file)
                if os.path.isfile(fp):
                    folder_size += os.path.getsize(fp)
        name = folder.name[:42]
        pad = " " * max(0, 42 - len(name))
        console.print(f"[{GOLD}]│[/{GOLD}]  [{LIGHT_GOLD}][{i}][/{LIGHT_GOLD}]  [{CREAM}]{escape(name)}[/{CREAM}]{pad}[{DEEP_GOLD}]{human_size(folder_size):>12}[/{DEEP_GOLD}]  [{GOLD}]│[/{GOLD}]")
    console.print(f"[{GOLD}]╰──────────────────────────────────────────────────────────────────╯[/{GOLD}]")
    try:
        choice = int(console.input(f"\n[{LIGHT_GOLD}]  ➤ Select folder number (1-{len(folders)}): [/{LIGHT_GOLD}]"))
        if 1 <= choice <= len(folders):
            selected_folder = folders[choice - 1]
            confirm = safe_input(f"[{LIGHT_GOLD}]  ➤ Delete {selected_folder.name}? (yes/no): [/{LIGHT_GOLD}]").strip().lower()
            if confirm == 'yes':
                shutil.rmtree(selected_folder)
                panel_success("Deleted", f"Folder removed: {selected_folder.name}")
            else:
                panel_warn("Cancelled", "No folder deleted.")
        else:
            panel_error("Invalid", "Number out of range.")
    except ValueError:
        panel_error("Invalid Input", "Please enter a number.")


def display_file_selector(title, folder_path, file_pattern="*.pak"):
    files = list(folder_path.glob(file_pattern))
    if not files:
        panel_error("No Files Found", f"No {file_pattern} files in {folder_path}")
        return None, None
    console.print()
    console.print(f"[{GOLD}]╭─────────────────────── {escape(title)} ───────────────────────╮[/{GOLD}]")
    console.print(f"[{GOLD}]│[/{GOLD}]  [{DEEP_GOLD}]#   File Name                                        Size[/{DEEP_GOLD}]  [{GOLD}]│[/{GOLD}]")
    console.print(f"[{GOLD}]├─────────────────────────────────────────────────────────┤[/{GOLD}]")
    for i, f in enumerate(files, 1):
        size_mb = f.stat().st_size / (1024 * 1024)
        name_display = f.name[:44]
        pad = " " * max(0, 44 - len(name_display))
        console.print(f"[{GOLD}]│[/{GOLD}]  [{LIGHT_GOLD}][{i:2d}][/{LIGHT_GOLD}] [{CREAM}]{escape(name_display)}[/{CREAM}]{pad}[{DEEP_GOLD}]{size_mb:>8.2f} MB[/{DEEP_GOLD}]  [{GOLD}]│[/{GOLD}]")
    console.print(f"[{GOLD}]╰─────────────────────────────────────────────────────────╯[/{GOLD}]")
    try:
        idx = int(console.input(f"\n[{LIGHT_GOLD}]  ➤ Select file number (1-{len(files)}): [/{LIGHT_GOLD}]")) - 1
        if idx < 0 or idx >= len(files):
            panel_error("Invalid", "Number out of range.")
            return None, None
        return files[idx], files
    except ValueError:
        panel_error("Invalid Input", "Please enter a number.")
        return None, None


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN MENU
# ═══════════════════════════════════════════════════════════════════════════

def main_menu():
    if getattr(sys, 'frozen', False):
        data_path = Path(sys.executable).parent
    else:
        data_path = Path(__file__).parent
    ensure_directories(data_path)
    while True:
        print_banner()
        print_menu()
        print_menu_tip()
        choice = safe_input('').strip()

        if choice == '1':
            pak_dir = data_path / "PAK"
            if not pak_dir.exists():
                panel_error("Missing Folder", f"PAK folder not found: {pak_dir}")
                safe_input('\n  Press Enter...')
                continue
            pak_file, _ = display_file_selector("📂 AVAILABLE .PAK FILES TO UNPACK", pak_dir)
            if not pak_file:
                safe_input('\n  Press Enter...')
                continue
            try:
                section_header("🚀", f"UNPACKING {pak_file.name}")
                pak = TencentPakFile(pak_file)
                unpack_path = data_path / "UNPACK" / pak_file.stem
                repack_path = data_path / "REPACK" / pak_file.stem
                pak.dump(unpack_path)
                log_path = unpack_path / f'Debug_{pak_file.stem}.log'
                dump_unpacking_log(pak, log_path)
                for dir_path, _ in pak._index.items():
                    current_repack_path = repack_path / pak._mount_point / dir_path
                    current_repack_path.mkdir(parents=True, exist_ok=True)
                section_footer()
                panel_success("UNPACK COMPLETE", f"Extracted to: {unpack_path}")
            except Exception as e:
                panel_error("Unpack Failed", escape(str(e)))
            safe_input('\n  Press Enter...')

        elif choice == '2':
            pak_tool_dir = data_path / "PAK TOOL"
            pak_dir = pak_tool_dir / "PAK"
            edit_dir = pak_tool_dir / "EDIT"
            result_dir = pak_tool_dir / "RESULT"
            if not pak_dir.exists():
                panel_error("Missing Folder", f"PAK TOOL/PAK not found: {pak_dir}")
                safe_input('\n  Press Enter...')
                continue
            pak_file, _ = display_file_selector("💉 AVAILABLE .PAK FILES TO INJECT INTO", pak_dir)
            if not pak_file:
                safe_input('\n  Press Enter...')
                continue
            if not edit_dir.exists() or not any(edit_dir.iterdir()):
                panel_error("No Files in EDIT", "Place files in PAK TOOL/EDIT keeping in-pak path.")
                safe_input('\n  Press Enter...')
                continue
            console.print()
            console.print(f"[{GOLD}]╭──────────────── 🔐 ENCRYPTION CHOICE ────────────────╮[/{GOLD}]")
            console.print(f"[{GOLD}]│[/{GOLD}]  [{CREAM}]YES = game-native SM4 encryption (recommended)[/{CREAM}]  [{GOLD}]│[/{GOLD}]")
            console.print(f"[{GOLD}]╰──────────────────────────────────────────────────────╯[/{GOLD}]")
            enc_choice = safe_input(f"[{LIGHT_GOLD}]  ➤ Encrypt injected files? (Y/n): [/{LIGHT_GOLD}]").strip().lower()
            protect_new = enc_choice not in ('n', 'no')
            try:
                section_header("🚀", f"INJECTING INTO {pak_file.name}")
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name
                edited, added = inject_edit_files(pak, edit_dir, output_pak, protect_new=protect_new, sm4_type=47)
                section_footer()
                panel_success("INJECT COMPLETE",
                              f"Edited:  {edited} files\nAdded:   {added} files\nOutput:  {output_pak}\n\n🎮 PAK is GAME READY!")
            except Exception as e:
                panel_error("Inject Failed", escape(str(e)))
                import traceback
                traceback.print_exc()
            safe_input('\n  Press Enter...')

        elif choice == '3':
            pak_tool_dir = data_path / "PAK TOOL"
            pak_dir = pak_tool_dir / "PAK"
            edit_dir = pak_tool_dir / "EDIT"
            result_dir = pak_tool_dir / "RESULT"
            if not pak_dir.exists():
                panel_error("Missing Folder", f"PAK TOOL/PAK not found: {pak_dir}")
                safe_input('\n  Press Enter...')
                continue
            pak_file, _ = display_file_selector("🔨 AVAILABLE .PAK FILES TO REPACK", pak_dir)
            if not pak_file:
                safe_input('\n  Press Enter...')
                continue
            if not edit_dir.exists() or not any(edit_dir.iterdir()):
                panel_error("No Files in EDIT", "Place files in PAK TOOL/EDIT.")
                safe_input('\n  Press Enter...')
                continue
            try:
                section_header("🚀", f"REPACKING {pak_file.name}")
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name
                count = repack_pak_file_full(pak, edit_dir, output_pak)
                section_footer()
                if count > 0:
                    panel_success("REPACK COMPLETE", f"Repacked {count} files\nOutput: {output_pak}")
                else:
                    panel_error("Repack Failed", "No files were processed.")
            except Exception as e:
                panel_error("Repack Failed", escape(str(e)))
                import traceback
                traceback.print_exc()
            safe_input('\n  Press Enter...')

        elif choice == '4':
            pak_tool_dir = data_path / "PAK TOOL"
            pak_dir = pak_tool_dir / "PAK"
            edit_dir = pak_tool_dir / "EDIT"
            result_dir = pak_tool_dir / "RESULT"
            if not pak_dir.exists():
                panel_error("Missing Folder", f"PAK TOOL/PAK not found: {pak_dir}")
                safe_input('\n  Press Enter...')
                continue
            pak_file, _ = display_file_selector("📁 AVAILABLE .PAK FILES TO REPACK TO PATH", pak_dir)
            if not pak_file:
                safe_input('\n  Press Enter...')
                continue
            if not edit_dir.exists() or not any(edit_dir.iterdir()):
                panel_error("No Files in EDIT", "Place files in PAK TOOL/EDIT.")
                safe_input('\n  Press Enter...')
                continue
            console.print()
            console.print(f"[{GOLD}]╭──────────────── 🎯 TARGET PATH ────────────────╮[/{GOLD}]")
            console.print(f"[{GOLD}]│[/{GOLD}]  [{DEEP_GOLD}]Example: Content/Lua/GameLua/Mod/BRMod[/{DEEP_GOLD}]  [{GOLD}]│[/{GOLD}]")
            console.print(f"[{GOLD}]╰────────────────────────────────────────────────╯[/{GOLD}]")
            target_path = safe_input(f"[{LIGHT_GOLD}]  ➤ Path: [/{LIGHT_GOLD}]").strip()
            if not target_path:
                panel_error("No Path", "Please provide a target path.")
                safe_input('\n  Press Enter...')
                continue
            target_path = target_path.replace('\\', '/').strip('/')
            if not target_path:
                panel_error("Invalid Path", "Path is empty.")
                safe_input('\n  Press Enter...')
                continue
            try:
                section_header("🚀", f"ADDING FILES TO {target_path}")
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name
                count = repack_pak_file_full(pak, edit_dir, output_pak, target_path, force_add=True)
                section_footer()
                if count > 0:
                    panel_success("REPACK COMPLETE",
                                  f"Processed {count} files → {target_path}\nOutput: {output_pak}\n\n🎮 PAK is GAME READY!")
                else:
                    panel_error("Repack Failed", "No files were processed.")
            except Exception as e:
                panel_error("Repack Failed", escape(str(e)))
                import traceback
                traceback.print_exc()
            safe_input('\n  Press Enter...')

        elif choice == '5':
            pak_tool_dir = data_path / "PAK TOOL"
            pak_dir = pak_tool_dir / "PAK"
            result_dir = pak_tool_dir / "RESULT"
            if not pak_dir.exists():
                panel_error("Missing Folder", f"PAK TOOL/PAK not found: {pak_dir}")
                safe_input('\n  Press Enter...')
                continue
            pak_file, _ = display_file_selector("🔐 AVAILABLE .PAK FILES TO PROTECT", pak_dir)
            if not pak_file:
                safe_input('\n  Press Enter...')
                continue
            console.print()
            console.print(f"[{CRIMSON}]╭──────────────── 🔐  P R O T E C T   M O D E  ────────────────╮[/{CRIMSON}]")
            console.print(f"[{CRIMSON}]│[/{CRIMSON}]  [{CREAM}]Re-encrypts EVERY file with game-native SM4.[/{CREAM}]          [{CRIMSON}]│[/{CRIMSON}]")
            console.print(f"[{CRIMSON}]│[/{CRIMSON}]  [{CREAM}]Generic unpackers will NOT be able to read it.[/{CREAM}]         [{CRIMSON}]│[/{CRIMSON}]")
            console.print(f"[{CRIMSON}]│[/{CRIMSON}]  [{CREAM}]The game still loads it normally.[/{CREAM}]                       [{CRIMSON}]│[/{CRIMSON}]")
            console.print(f"[{CRIMSON}]╰──────────────────────────────────────────────────────────────╯[/{CRIMSON}]")
            confirm = safe_input(f"[{CRIMSON}]  ➤ Start PROTECT? (yes/no): [/{CRIMSON}]").strip().lower()
            if confirm not in ('y', 'yes'):
                panel_warn("Cancelled", "No protection applied.")
                safe_input('\n  Press Enter...')
                continue
            try:
                section_header("🔐", f"PROTECTING {pak_file.name}")
                pak = TencentPakFile(pak_file)
                output_pak = result_dir / pak_file.name
                protected, skipped = protect_pak_file(pak, output_pak, sm4_type=47)
                section_footer()
                panel_success("PROTECTION COMPLETE",
                              f"Protected: {protected} files\nSkipped:   {skipped} files\nOutput:    {output_pak}\n\n🎮 Game-ready + protected!")
            except Exception as e:
                panel_error("Protect Failed", escape(str(e)))
                import traceback
                traceback.print_exc()
            safe_input('\n  Press Enter...')

        elif choice == '6':
            delete_folder(data_path)
            safe_input('\n  Press Enter...')

        elif choice == '0':
            console.print()
            console.print(f"[{GOLD}]╔══════════════════════════════════════════════════════════════╗[/{GOLD}]")
            console.print(f"[{GOLD}]║[/{GOLD}]   [{LIGHT_GOLD}]🎩 Thank you for using @AFTAB MODZ![/{LIGHT_GOLD}]              [{GOLD}]║[/{GOLD}]")
            console.print(f"[{GOLD}]║[/{GOLD}]   [{CREAM}]Goodbye, Boss. Until next time.[/{CREAM}]                        [{GOLD}]║[/{GOLD}]")
            console.print(f"[{GOLD}]╚══════════════════════════════════════════════════════════════╝[/{GOLD}]")
            console.print()
            time.sleep(2)
            break
        else:
            panel_error("Invalid Choice", "Please pick a number between 0 and 6.")
            time.sleep(2)


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print()
        panel_warn("Interrupted", "Exiting...")
        sys.exit(0)
    except Exception as e:
        panel_error("FATAL ERROR", escape(str(e)))
        import traceback
        traceback.print_exc()
        safe_input('\n  Press Enter to exit...')
        sys.exit(1)