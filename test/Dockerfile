FROM ubuntu:20.04
# 일반 알파인은 경량화로 인한 npm install 불가능
# ubuntu 18.04 == baseimg

#RUN apk add --no-cache python3 g++ make
# RUN: 도커 이미지가 생성되기 전에 수행할 쉘 명령어

ADD ./sources.list /etc/apt/source.list
ADD ./requirements.txt /data/
ADD ./zmq_test.py /data/
ADD ./zmq_test_client.py /data/

RUN apt update && apt install -y python3.8 \
	python3-dev \
	python3-pip



# /data/ 디렉토리에서 작업 COPY (source) (dist)

RUN pip3 install -r /data/requirements.txt

WORKDIR /root
RUN echo 'alias python=python3.8' >> .bashrc

#RUN /data/init.script
WORKDIR /data/
VOLUME ["/data/"]
# cmd 컨테이너 내에서 실행, 도커 파일 내에서 한번만 사용 가능
