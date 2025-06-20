[app]

title = DICOM AI Viewer
package.name = dicom_ai_viewer
package.domain = org.dicomviewer
source.dir = .
source.include_exts = py,png,jpg,kv,json,xml,ttf
version = 0.1
requirements = python3,kivy,kivymd,pillow,pydicom,numpy,opencv-python,torch,torchvision
orientation = portrait
fullscreen = 1

# Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android Architecture (optional if both)
android.archs = armeabi-v7a,arm64-v8a

# Entry point
entrypoint = main.py

# Presplash and Icon
icon.filename = assets/icons/icon.png
presplash.filename = assets/icons/splash.png

# SDL2 bootstrap is required for graphics
bootstrap = sdl2

# Hide the keyboard on start
android.hide_keyboard = 1

# Minimum Android API
android.minapi = 21
android.api = 31

# NDK API Level
android.ndk_api = 21

# Enable Torch runtime if needed
android.add_binary_files = backend/ai_models.py

# Include assets
android.add_src = assets/

# Include .so or libs if needed
# android.add_libs_armeabi_v7a = path/to/your/lib.so

# Don't copy these patterns
ignore_setup_py = 1

# Use legacy Cython for compatibility
cython_legacy = 1

# Log level (2 = verbose)
log_level = 2

[buildozer]

log_level = 2
warn_on_root = 1
