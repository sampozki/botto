FROM python:3.12.9-alpine

LABEL Maintainer="sampozki"

RUN apk update && apk add gcc libc-dev musl-dev python3-dev

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY *.py ./

CMD ["python3.8", "bot.py"]
