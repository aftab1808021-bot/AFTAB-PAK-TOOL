# AFTAB MODZ PAK TOOL — Android GUI structure

This project separates the existing PAK engine from the Android GUI:

- `tool_core.py` — existing PAK parsing/crypto/compression/repack engine.
- `main.py` — Kivy Android GUI wrapper.
- `buildozer.spec` — Buildozer/python-for-android configuration.

## Android layout

The app creates its private working area automatically:

```
PAK/
UNPACK/
REPACK/
RESULT/
PAK TOOL/
  PAK/
  EDIT/
  RESULT/
```

Put `.pak` files into `PAK TOOL/PAK` and files to inject into `PAK TOOL/EDIT`.

## Important Android change

The original engine can generate/compile `sm4_fast.c` into a desktop `.so`. Android should not compile native code at runtime, so `tool_core.py` disables that path on Android and uses its existing pure-Python SM4 implementation instead.

## Build

On a Linux/Termux build machine with Buildozer installed:

```bash
cd AFTAB_PAK_ANDROID
buildozer android debug
```

The APK is produced under `bin/` when the build succeeds.

The native dependencies (`zstandard` and potentially `gmalg`) may require python-for-android recipes depending on the selected toolchain. The GUI/core split is ready, but an APK should only be considered complete after a real Android build and runtime test.
