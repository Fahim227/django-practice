FROM python:3.8-alpine
ENV PYTHONUNBEFFERED=1
# RUN apk update \
#     && apk add --virtual build-deps gcc python3-dev musl-dev \
#     && pip install --no-cache-dir mysql-python\
#     && apk add mysql-client \
#     && apk --no-cache add --virtual build-dependencies 

RUN apk add --no-cache mariadb-dev build-base
        
WORKDIR /django

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

