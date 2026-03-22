[app]
title = Voice Translator
package.name = voicetranslator
package.domain = org.prasanna

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy,deep-translator

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
