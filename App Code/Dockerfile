# syntax=docker/dockerfile:1
FROM python:3.10-slim

WORKDIR /App

COPY requeriments.txt ./requeriments.txt
COPY TFM_Banner.png ./TFM_Banner.png
COPY Modelo_Optimizado.h5 ./Modelo_Optimizado.h5
COPY app.py ./app.py
COPY .streamlit ./.streamlit

RUN python -m pip install --upgrade pip
RUN pip3 install -r requeriments.txt

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]