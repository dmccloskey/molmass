# Dockerfile to build molmas images
# Based on Ubuntu

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Douglas McCloskey <dmccloskey87@gmail.com>

# Install wget
RUN apt-get update && apt-get install -y wget

# Install molmass from http
WORKDIR /usr/local/
RUN mkdir molmass
WORKDIR /usr/local/molmass
RUN wget http://www.lfd.uci.edu/~gohlke/code/molmass.py.html
RUN wget http://www.lfd.uci.edu/~gohlke/code/elements.py.html
RUN http://www.lfd.uci.edu/~gohlke/code/molmass_cgi.py.html

# add cufflinks to path
ENV PATH /usr/local/molmass:$PATH

# Cleanup
RUN apt-get clean

# Create an app user
ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
    && chmod -R u+rwx $HOME \
    && chown -R user:user $HOME

WORKDIR $HOME
USER user
