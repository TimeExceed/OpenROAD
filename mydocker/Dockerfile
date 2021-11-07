FROM ubuntu:21.10
COPY repeat.sh /usr/local/bin/
COPY sources.list /etc/apt/
WORKDIR /opt/code/

RUN repeat.sh apt-get update
RUN DEBIAN_FRONTEND="noninteractive" repeat.sh apt-get install -y tzdata \
    && apt-get clean
RUN repeat.sh apt-get install -y \
    less vim tmux python3 \
    gcc clang cmake build-essential pkg-config \
    libreadline-dev libboost-all-dev tcl tcl-dev swig3.0 \
    libspdlog1 libspdlog-dev bison flex libeigen3-dev \
    liblemon-dev liblemon-utils \
    && apt-get clean
