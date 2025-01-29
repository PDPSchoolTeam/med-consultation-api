
FROM python:3.9-alpine


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MYPATH=/home/app/code


RUN apk add --no-cache


WORKDIR $MYPATH


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

