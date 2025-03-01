FROM python:3.12.9-alpines

LABEL Maintainer="sampozki"

RUN apk update && apk add gcc libc-dev python3-dev

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY *.py ./

CMD ["python3.8", "bot.py"]
