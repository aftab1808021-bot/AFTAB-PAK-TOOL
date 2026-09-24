[app]
title = AFTAB MODZ
package.name = aftabmodz
package.domain = com.aftabmodz
source.dir = .
source.include_exts = py,jpg,png,kv,txt
version = 0.1.0
requirements = python3,kivy,pillow
orientation = portrait
fullscreen = 0
android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True

[buildozer:android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
