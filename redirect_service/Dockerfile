FROM python:3.12

EXPOSE 8000

WORKDIR /SmartLinks/redirect_service

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY /*.py ./
