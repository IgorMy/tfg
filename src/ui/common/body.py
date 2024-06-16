from nicegui import ui


def body():
    return ui.element("section").classes(
        "mx-auto flex flex-col max-w-7xl w-fit md:w-[640px] lg:w-[800px] xl:w-[1024px] 2xl:w-[1024px] gap-8"
    )
