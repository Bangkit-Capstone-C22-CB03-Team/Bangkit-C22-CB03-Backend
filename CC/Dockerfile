FROM python:3.9-slim as build

ENV APPPATH /opt/chatbot-tvlk

WORKDIR $APPPATH/app

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	gcc build-essential && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	pip3 install --upgrade pip && \
	python -m venv /opt/chatbot-tvlk/app/venv

ENV PATH="/opt/chatbot-tvlk/app/venv/bin:$PATH"

COPY ./app/requirements.txt .

RUN pip3 install -r requirements.txt

#final stage
FROM python:3.9-slim

WORKDIR /opt/chatbot-tvlk/app

COPY --from=build /opt/chatbot-tvlk/app/venv ./venv

COPY /app .

ENV PATH="/opt/chatbot-tvlk/app/venv/bin:$PATH"

WORKDIR /opt/chatbot-tvlk/app/src

CMD ["python3", "app.py" ]
