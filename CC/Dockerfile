FROM python:3.9-alpine

RUN adduser -D appuser 

USER appuser 

COPY requirements.txt /usr/src

RUN pip install -r /usr/src/requirements.txt

COPY --chown=appuser:appuser ./app /usr/src/app

WORKDIR /usr/src/app

CMD ["python", "app.py"]