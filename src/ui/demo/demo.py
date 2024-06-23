from nicegui import ui


def image_banner():
    with ui.element("div").classes(
        "flex flex-row justify-center items-center justify-between px-10 gap-4"
    ):
        ui.element("img").props(
            'src="/static/images/base_demostration.jpg" alt="Base image"'
        ).classes("rounded-md w-[95%] sm:w-[40%]")
        ui.icon("r_arrow_forward").classes(
            "hidden sm:!inline-flex text-4xl text-gray-600 dark:text-gray-300 "
        ).style("margin: 0 20px;")
        ui.element("img").props(
            'src="/static/images/image_with_mask.jpg" alt="Mask image"'
        ).classes("rounded-md w-[95%] sm:w-[40%]")
