FROM python:3.11.11-alpine

LABEL Maintainer="sampozki"

RUN apk update && apk add gcc \
                        libc-dev

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY *.py ./

CMD ["python3.8", "bot.py"]
