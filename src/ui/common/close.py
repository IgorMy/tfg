from nicegui import ui


def close_button(function: lambda: None):

    ui.button(
        "Cerrar",
        on_click=function,
        icon="r_close",
    ).classes(
        "[&>span]:text-[#8b0000] dark:[&>span]:text-[#ef9a9a] bg-transparent dark:before:bg-[#52525b]"
    )
