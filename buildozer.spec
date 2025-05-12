[app]
title = MiApp
package.name = miapp
package.domain = org.miapp
source.dir = .
source.include_exts = py,png,jpg,kv,ttf
version = 1.0
requirements = python3==3.10.13, kivy==2.3.0
orientation = portrait

# Configuración Android
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 26.1.10909125
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/26.1.10909125
android.arch = arm64-v8a

[buildozer]
log_level = 2