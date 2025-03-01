FROM python:3.11.11-alpine

LABEL Maintainer="sampozki"

RUN apk update && apk add --no-cache gcc libc-dev musl-dev python3-dev

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY *.py ./

CMD ["python3.11", "bot.py"]
