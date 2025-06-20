# viewer.py

from backend.ai_models import (
    run_lung_inference,
    run_abdomen_inference,
    run_pelvis_inference,
    run_neck_inference,
    overlay_heatmap,
    save_heatmap_image
)

from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.snackbar import Snackbar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class DicomViewerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_image = None  # should be set when image is loaded
        self.last_used_model_func = run_lung_inference
        self.image_widget = Image()
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='horizontal')
        tools_panel = BoxLayout(orientation='vertical', size_hint_x=0.25, spacing=10, padding=5)

        buttons = [
            ("Window: Bone", self.set_bone_window),
            ("Window: Lung", self.set_lung_window),
            ("Window: Abdomen", self.set_abdomen_window),
            ("Window: Brain", self.set_brain_window),
            ("AI: Lung Detect", self.ai_detect_lung),
            ("AI: Abdomen", self.ai_detect_abdomen),
            ("AI: Pelvis", self.ai_detect_pelvis),
            ("AI: Neck", self.ai_detect_neck),
            ("Export Image", self.export_current_image),
            ("Export AI Image", self.export_ai_image),
            ("Export Heatmap", self.export_ai_heatmap),
            ("Export Options", self.open_export_menu),
            ("Measure Distance", self.enable_measure_mode),
            ("MPR: Axial", self.show_mpr_axial),
            ("MPR: Coronal", self.show_mpr_coronal),
            ("MPR: Sagittal", self.show_mpr_sagittal)
        ]

        for label, method in buttons:
            tools_panel.add_widget(MDRaisedButton(text=label, on_release=method))

        layout.add_widget(tools_panel)
        layout.add_widget(self.image_widget)
        self.add_widget(layout)

    def export_ai_heatmap(self, *args):
        try:
            model_func = self.last_used_model_func or run_lung_inference
            heatmap = model_func(self.current_image)
            save_heatmap_image(heatmap, "ai_heatmap.jpg")
            Snackbar(text="✅ Heatmap exported.").open()
        except Exception as e:
            Snackbar(text=f"❌ Export failed: {e}").open()

    # Placeholder methods — implement real logic for each tool
    def set_bone_window(self, *args): pass
    def set_lung_window(self, *args): pass
    def set_abdomen_window(self, *args): pass
    def set_brain_window(self, *args): pass

    def ai_detect_lung(self, *args):
        self.last_used_model_func = run_lung_inference
        Snackbar(text="Running lung AI...").open()

    def ai_detect_abdomen(self, *args):
        self.last_used_model_func = run_abdomen_inference
        Snackbar(text="Running abdomen AI...").open()

    def ai_detect_pelvis(self, *args):
        self.last_used_model_func = run_pelvis_inference
        Snackbar(text="Running pelvis AI...").open()

    def ai_detect_neck(self, *args):
        self.last_used_model_func = run_neck_inference
        Snackbar(text="Running neck AI...").open()

    def export_current_image(self, *args): pass
    def export_ai_image(self, *args): pass
    def open_export_menu(self, *args): pass
    def enable_measure_mode(self, *args): pass
    def show_mpr_axial(self, *args): pass
    def show_mpr_coronal(self, *args): pass
    def show_mpr_sagittal(self, *args): pass
