[app]
title = DICOM AI Viewer
package.name = dicomviewer
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt,zip,so
version = 1.0
requirements = python3,kivy,kivymd,pillow,pydicom,opencv-python-headless,torch,torchvision,numpy
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b
android.sdk = 33
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
android.packaging_options =
    exclude libs/armeabi/*
    exclude META-INF/*.kotlin_module
    exclude META-INF/DEPENDENCIES
    exclude META-INF/LICENSE
    exclude META-INF/LICENSE.txt
    exclude META-INF/license.txt
    exclude META-INF/NOTICE
    exclude META-INF/NOTICE.txt
    exclude META-INF/notice.txt
android.allow_cleartext = 1
android.add_src = backend
log_level = 2
