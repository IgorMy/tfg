from nicegui import ui
from src.ui.header.components.change_theme import ChangeThemeComponent
from src.ui.header.components.title import title


def header():
    dark = ui.dark_mode()
    with ui.element("div").classes("w-full flex justify-between"):
        ui.element("div").classes("w-10")
        title()
        with ChangeThemeComponent():
            ui.tooltip("Alternar tema")
    with ui.element("div").classes("w-full flex justify-center"):
        ui.label(
            "Aplicación de una implementación de la red neuronal U-Net, desarrollada en tensorflow, para la segmentación facial en imágenes térmicas con perfil de colór White Hot. Esta aplicación es una muestra de funcionamiento y está limitado su uso."
        ).classes("text-center text-lg")
