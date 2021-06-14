FROM python:3.9.4-slim
WORKDIR /api
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY .. .
