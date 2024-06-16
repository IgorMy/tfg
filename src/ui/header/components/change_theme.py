from nicegui import ui


class ChangeThemeComponent(ui.button):

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)
        # get dark mode element
        self.dark = ui.dark_mode()
        # set text of button based on current dark mode
        if self.dark.value:
            self.props(f"icon=wb_sunny")
        else:
            self.props(f"icon=dark_mode")

        # add click event listener
        self.on("click", self.change_theme_component)
        self.classes(
            "!bg-transparent !text-black dark:!text-white !rounded-full !h-8 !px-2 w-10 before:shadow-none"
        )

    def change_theme_component(self):
        if self.dark.value:
            self.dark.disable()
            self.props(f"icon=dark_mode")
        else:
            self.dark.enable()
            self.props(f"icon=wb_sunny")
