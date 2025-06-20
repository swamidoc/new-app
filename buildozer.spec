[app]

# App Info
title = DICOM AI Viewer
package.name = dicomai
package.domain = org.swamidoc
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1
orientation = all
fullscreen = 0

# Icon and splash (optional)
icon.filename = %(source.dir)s/assets/icons/logo.png
presplash.filename = %(source.dir)s/assets/icons/logo.png

# Permissions (needed for file access)
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android Requirements
requirements = python3==3.9,kivy==2.2.1,kivymd,pillow,pydicom,numpy,scipy,matplotlib,opencv-python-headless,torch==2.0.1,torchvision==0.15.2

# Native architectures
android.arch = armeabi-v7a, arm64-v8a

# Use the patched Python-for-Android branch to fix pyjnius errors
p4a.branch = develop

# Android API & NDK
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.ndk_api = 21

# Additional build settings
copy_libs = 1
log_level = 2
warn_on_root = 1
# storage location (keep internal for privacy)
android.private_storage = True

# Don't use service or splash if not defined
# service = 
# presplash_color = #FFFFFF

# Buildozer internal storage
build_dir = .buildozer

# Enable debug build
debug = 1
