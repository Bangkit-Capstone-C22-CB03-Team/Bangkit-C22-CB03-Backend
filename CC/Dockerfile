FROM ubuntu:20.04

RUN set -ex \
  	&& sed -i -e "s%http://archive.ubuntu.com/ubuntu/%http://no.archive.ubuntu.com/ubuntu/%g" /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y \
 			python3-pip \
 			python3-dev \
 			build-essential \
 	&& apt-get clean \
 	&& rm -rf /var/lib/apt/lists/* \
 	&& pip3 install --upgrade pip

ENV APPPATH /opt/chatbot-tvlk
COPY . $APPPATH
WORKDIR $APPPATH/app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["src/app.py"]
