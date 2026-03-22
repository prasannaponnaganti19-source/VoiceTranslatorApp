[app]
title = Voice Translator
package.name = voicetranslator
package.domain = org.prasanna

source.dir = .
source.include_exts = py

version = 0.1
entrypoint = main.py

requirements = python3,kivy,requests,speechrecognition,gtts,deep-translator,playsound

orientation = portrait
fullscreen = 0
log_level = 2

android.permissions = INTERNET,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
