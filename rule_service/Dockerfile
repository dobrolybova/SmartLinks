FROM python:3.12

EXPOSE 8080

WORKDIR /SmartLinks/rule_service

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY /alembic ./alembic
COPY alembic.ini alembic.ini
COPY /*.py ./
