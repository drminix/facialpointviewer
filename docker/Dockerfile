# specify base image
FROM ubuntu:18.04 as build
ENV TARGET_BRANCH master
ENV FACIALPOINT_PATH /home

# set up node
WORKDIR $FACIALPOINT_PATH
# wget https://raw.githubusercontent.com/username/reponame/branch/path/to/file
wget https://github.com/drminix/facialpointviewer/master/webserver/package.json

WORKDIR $FACIALPOINT_PATH/webserver
RUN npm install

# pull files from repo

# Specify the default command
CMD ["sh"]