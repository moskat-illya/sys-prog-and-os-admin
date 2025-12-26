FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && apt-get install -y \
    rpm \
    build-essential \
    debhelper \
    devscripts \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
