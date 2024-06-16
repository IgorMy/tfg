from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from nicegui import ui
from src.ui.common.body import body
from src.ui.header.header import header
from src.ui.demo.demo import image_banner
from src.ui.file_selection.file_selection import file_selection
from src.ui.footer.footer import footer

app = FastAPI()

# add public folder to the static files
app.mount("/static", StaticFiles(directory="static"), name="static")


def init_frontend(fastapi_app: FastAPI) -> None:
    @ui.page("/", title="TFG - Ihar Myshkevich Kiryanav")
    def show():

        ui.add_css(
            """
                @import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap');
            """
        )

        ui.add_head_html(
            """
            <style>
            .q-page {
                display: flex !important; 
                justify-content: center !important; 
                align-items: center !important;
            }
            </style>
            """
        )
        with body():
            header()
            image_banner()
            file_selection()
            footer()

    ui.run_with(
        fastapi_app,
        viewport="width=device-width, initial-scale=1.0, height=device-height",
        favicon="static/favicon.ico",
    )


init_frontend(app)

if __name__ == "__app__":
    print(
        'Please start the app with the "uvicorn" command as shown in the start.sh script'
    )
