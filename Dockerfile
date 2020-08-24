FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root/

RUN apt update -y --fix-missing
RUN apt upgrade -y

RUN apt install -y software-properties-common build-essential apt-transport-https curl wget python3 python3-pip apt-utils

RUN python3 -m pip install --upgrade pip
