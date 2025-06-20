[app]
title = Dicom AI Viewer
package.name = dicom_ai_viewer
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,pillow,pydicom,opencv-python,numpy,cython==0.29.36,pyjnius==1.5.0,torch,torchvision
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET
