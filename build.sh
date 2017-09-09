#!/bin/bash
###shell script to build out the zeppelin environment

### Set up system with up to date dependencies
apt-get update
apt-get upgrade -y

### install htop
apt-get install htop

### Do the docker install
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

apt-get update

apt-get install docker-ce -y

docker run hello-world

### Docker compose install
curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

### Get the source code
git clone https://github.com/albre116/SocialMedia.git




