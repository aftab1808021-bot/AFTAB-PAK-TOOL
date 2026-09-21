[app]
title = AFTAB MODZ PAK TOOL
package.name = aftabpaktool
package.domain = com.aftabmodz
source.dir = .
source.include_exts = py,png,jpg,kv,txt,so,c
version = 1.0.0
requirements = python3,kivy,rich,pytz,requests,pycryptodome,zstandard,gmalg
orientation = portrait
fullscreen = 0
android.api = 35
android.minapi = 23
android.archs = arm64-v8a,armeabi-v7a
android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO
android.add_src = .

[buildozer]
log_level = 2
warn_on_root = 1
