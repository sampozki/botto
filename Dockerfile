FROM python:3.8.13-alpine

LABEL Maintainer="sampozki"

RUN apk update && apk add gcc \
                        libc-dev

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY *.py env.cfg ./

COPY . .

CMD ["python3.8", "bot.py"]
