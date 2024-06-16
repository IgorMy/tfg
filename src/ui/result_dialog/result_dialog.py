from nicegui import ui
from PIL import Image
from src.ui.U_Net.U_Net import UNet
import numpy as np
from src.ui.common.close import close_button
import asyncio


def show_loading_dialog(dialog: ui.dialog):
    with dialog, ui.element("div").classes("flex flex-col gap-4"):
        ui.spinner("dots", size="10rem", color="white").classes("text-center")

    dialog.open()


async def result_dialog(image: Image, dialog: ui.dialog):

    show_loading_dialog(dialog)

    await asyncio.sleep(0.01)

    processed_image_array = UNet(image)

    extra_image = image

    # Put red mask over exta image using processed_image_array
    extra_image_array = extra_image.convert("RGB")

    # resize
    extra_image_array = extra_image_array.resize((336, 256))

    extra_image_array = np.array(extra_image_array)
    extra_image_array[processed_image_array == 255] = (
        extra_image_array[processed_image_array == 255] * 0.7
        + np.array([255, 0, 0]) * 0.3
    )
    extra_image = Image.fromarray(extra_image_array)

    processed_image = Image.fromarray(processed_image_array)

    dialog.clear()

    with dialog, ui.card().classes("!max-w-[70%] mb-10"):
        ui.label("Resultado de la segmentación").classes("text-2xl w-full text-center")
        with ui.element("div").classes(
            "flex flex-row items-center justify-center w-full gap-4"
        ):
            with ui.element("div").classes("flex flex-col gap-4"):
                with ui.element("div"):
                    ui.label("Imagen original").classes("w-full text-center text-lg")
                    ui.image(image).classes(
                        "rounded-md w-[20rem] row-start-1 col-start-1"
                    )
                with ui.element("div"):
                    ui.label("Máscara obtenida").classes("w-full text-center text-lg")
                    ui.image(processed_image).classes(
                        "rounded-md w-[20rem] row-start-2 col-start-1"
                    )
            with ui.element("div").classes("flex flex-col row-span-2"):
                ui.label("Imagen con máscara").classes("w-full text-center text-lg")
                ui.image(extra_image).classes("rounded-md w-[40rem]")
        with ui.element("div").classes("w-full flex justify-center mt-6"):
            close_button(lambda: (dialog.close(), dialog.clear()))
    dialog.open()
