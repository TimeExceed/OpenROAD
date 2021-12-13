FROM ubuntu:21.10
COPY repeat.sh /usr/local/bin/
COPY sources.list /etc/apt/
WORKDIR /opt/code/

RUN repeat.sh apt-get update
RUN DEBIAN_FRONTEND="noninteractive" repeat.sh apt-get install -y tzdata \
    && apt-get clean
RUN repeat.sh apt-get install -y \
    less vim tmux python3 sudo \
    gcc clang cmake build-essential pkg-config \
    libreadline-dev libboost-all-dev tcl tcl-dev swig3.0 \
    libspdlog1 libspdlog-dev bison flex libeigen3-dev \
    liblemon-dev liblemon-utils \
    && apt-get clean

RUN groupadd --gid 1000 dockeruser \
    && useradd --uid 1000 --gid 1000 --shell /bin/bash --password 12345 --create-home dockeruser
COPY --chown=1000:1000 bashrc /home/dockeruser/.bash_profile
COPY --chown=1000:1000 bashrc /home/dockeruser/.bashrc
ENV COLORTERM="truecolor" TERM="xterm-256color"


