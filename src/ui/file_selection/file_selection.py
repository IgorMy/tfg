from nicegui import ui
from src.ui.result_dialog.result_dialog import result_dialog
from PIL import Image
from src.ui.common.close import close_button
import asyncio
import io
import cv2


def open_file_dialog(srcImage: str, dynamic_dialog: ui.dialog):
    asyncio.create_task(
        result_dialog(
            image=Image.open(srcImage),
            dialog=dynamic_dialog,
        )
    )


def upload_file_handler(dynamic_dialog: ui.dialog, e):

    pil_image = Image.open(io.BytesIO(e.content.read()))
    asyncio.create_task(
        result_dialog(
            image=pil_image,
            dialog=dynamic_dialog,
        )
    )
    e.sender.reset()


def file_selection():

    dynamic_dialog = ui.dialog()

    with ui.dialog() as dialog, ui.card().classes("!max-w-full xl:!max-w-[80%] mb-10"):
        ui.label("Seleccione una imagen de la galería de imágenes de prueba").classes(
            "text-xl w-full text-center"
        )
        with ui.element("div").classes(
            "flex flex-row gap-4 items-center justify-center"
        ):
            for i in range(1, 11):
                with ui.button(
                    on_click=lambda i=i: (
                        dialog.close(),
                        open_file_dialog(
                            srcImage=f"static/test_images/{i}.jpg",
                            dynamic_dialog=dynamic_dialog,
                        ),
                    )
                ).classes("p-0 bg-transparent"):
                    ui.image(f"/static/test_images/{i}.jpg").classes(
                        "rounded-md w-[20em] md:w-80"
                    )
        with ui.element("div").classes("flex flex-row justify-center w-full mt-6"):
            close_button(dialog.close)

    ui.separator().classes("xl:mt-14")
    with ui.element("div").classes("flex flex-row justify-center items-center gap-8"):
        ui.upload(
            multiple=False,
            on_upload=lambda e: upload_file_handler(dynamic_dialog=dynamic_dialog, e=e),
            label="Selección de fichero",
        ).classes(
            "h-[270px] [&>*:first-child]:bg-transparent [&>*:first-child]:text-black [&>*:first-child]:border-b-2 [&>*:first-child]:border-slate-200 dark:[&>*:first-child]:bg-[#52525b] dark:[&>*:first-child]:text-white dark:[&>*:first-child]:border-none"
        )
        ui.button(
            "Imágenes de ejemplo", on_click=dialog.open, icon="collections"
        ).classes(
            "bg-transparent [&>span]:text-black dark:before:bg-[#52525b] dark:[&>span]:text-white"
        )
