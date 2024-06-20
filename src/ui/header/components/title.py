from nicegui import ui


def title():
    ui.label("Segmentación facial en imágenes térmicas").classes(
        "text-4xl w-fit text-center"
    ).style("font-family: 'Ubuntu', sans-serif;")
