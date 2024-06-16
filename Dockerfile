FROM python:3.11-slim

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install make -y
RUN pip3 install --upgrade pip

# add export PATH=$PATH:$HOME/.local/bin to .bashrc
RUN echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc

COPY . /var/www

WORKDIR /var/www

RUN pip3 install -r requirements.txt

CMD [ "uvicorn", "src.app:app","--host", "0.0.0.0" ]

