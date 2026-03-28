[app]
# (str) Title of your application
title = SemkaApp

# (str) Package name
package.name = ChannelAppSemka

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API. 34 — самая стабильная сейчас.
android.api = 34

# (int) Minimum API. 21 подходит для большинства старых телефонов.
android.minapi = 21

# (str) Android SDK Build-Tools. ФИКСИРУЕМ версию, чтобы не было ошибки лицензии 37.
android.sdk_build_tools_version = 34.0.0

# (bool) Автоматическое принятие лицензий (для GitHub Actions)
android.accept_sdk_license = True

# (list) The Android archs to build for.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Разрешить бэкап
android.allow_backup = True

[buildozer]
# (int) Log level (2 = подробный вывод для отладки)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
