# specify base image
FROM ubuntu:18.04 as build
ENV TARGET_BRANCH master
ENV FACIALPOINT_PATH /home

# update apt sources.list
ARG ubuntu_mirror=us.archive.ubuntu.com
# mirrors.ocf.berkeley.edu
ARG ubuntu_ports_mirror=ports.ubuntu.com
# mirrors.mit.edu
RUN sed -Ei "s/archive.ubuntu.com/${ubuntu_mirror}/g" /etc/apt/sources.list
RUN sed -Ei "s/ports.ubuntu.com/${ubuntu_ports_mirror}/g" /etc/apt/sources.list

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y software-properties-common --no-install-suggests --no-install-recommends
RUN add-apt-repository ppa:apt-fast/stable && apt-get update && apt-get install -y apt-fast && rm -rf /var/lib/apt/lists/*
RUN apt-get update

# install default packages
RUN apt-fast install -y --no-install-suggests --no-install-recommends \
	wget \
	nodejs \
	npm


# set up node
WORKDIR $FACIALPOINT_PATH
RUN wget https://raw.githubusercontent.com/drminix/facialpointviewer/master/webserver/package.json
RUN npm install

# pull files from repo
#git

#clean up
RUN rm -rf /var/lib/apt/lists/*

# Specify the default command
CMD ["sh"]