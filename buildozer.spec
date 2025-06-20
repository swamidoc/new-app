[app]
title = DICOM AI Viewer
package.name = dicom_ai_viewer
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivymd,pillow,pydicom,opencv-python,torch,torchvision,numpy
orientation = sensor
fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 1

[app/android]
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.minapi = 23
android.target = 31
android.sdk = 31
android.ndk = 23b
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.6.10
