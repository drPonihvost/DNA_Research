FROM python:3.9.6-alpine

WORKDIR /usr/src/dnaresearch

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt install libpcre3 libpcre3-dev


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

# RUN python /usr/src/dnaresearch/manage.py makemigrations
# RUN python /usr/src/dnaresearch/manage.py migrate

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

