from nicegui import ui


def image_banner():
    with ui.element("div").classes(
        "flex flex-row justify-center items-center justify-between px-10"
    ):
        ui.element("img").props('src="static/images/base_demostration.jpg"').classes(
            "rounded-md"
        ).style("width: 40%;")
        ui.icon("r_arrow_forward").classes(
            "text-4xl text-gray-600 dark:text-gray-300"
        ).style("margin: 0 20px;")
        ui.element("img").props('src="static/images/image_with_mask.jpg"').classes(
            "rounded-md"
        ).style("width: 40%;")
