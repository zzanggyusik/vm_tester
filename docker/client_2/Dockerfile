From ubuntu:20.04

COPY . /data/

RUN sed -i 's@archive.ubuntu.com@kr.archive.ubuntu.com@g' /etc/apt/sources.list

RUN apt update && apt install -y python3.8 \
	python3-dev \
	python3-pip

RUN pip3 install -r /data/requirements.txt

WORKDIR /root
RUN echo 'alias python=python3.8' >> .bashrc

WORKDIR /
# dafault python version 3.8

VOLUME ["/data/"]

WORKDIR /data/

ENTRYPOINT [ "/data/start.sh" ]