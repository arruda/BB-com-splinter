FROM python:2.7

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN pip install splinter

RUN apt-get update -qqy \
  && apt-get -qqy install \
    xorg openbox libasound2-dev libdbus-glib-1-2 \
  && rm -rf /var/lib/apt/lists/*

RUN echo 'deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main' > /etc/apt/sources.list.d/ubuntuzilla.list && \
    apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    firefox \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update -qqy \
    && apt-get -qqy install software-properties-common \
  && rm -rf /var/lib/apt/lists/*

# Install Java.
RUN \
  echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" > /etc/apt/sources.list.d/webupd8team-java.list && \
  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/webupd8team-java.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
  apt-get -qqy update && \
  apt-get install -y oracle-java7-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk7-installer

ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

RUN javaws -userConfig deployment.expiration.check.enabled false

ADD java_confs/security/trusted.certs /root/.java/deployment/security/trusted.certs

RUN pip install ipdb

WORKDIR /data/
VOLUME /data

CMD ["/bin/bash"]