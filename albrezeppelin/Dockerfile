FROM gettyimages/spark:2.0.2-hadoop-2.7

# SciPy
RUN set -ex \
 && buildDeps=' \
    libpython3-dev \
    build-essential \
    pkg-config \
    gfortran \
 ' \
 && apt-get update && apt-get install -y --no-install-recommends \
    $buildDeps \
    ca-certificates \
    wget \
    liblapack-dev \
    libopenblas-dev \
 && packages=' \
    numpy \
    pandasql \
    scipy \
 ' \
 && pip3 install $packages \
 && apt-get purge -y --auto-remove $buildDeps \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Zeppelin
ENV ZEPPELIN_PORT 8080
ENV ZEPPELIN_HOME /usr/zeppelin
ENV ZEPPELIN_CONF_DIR $ZEPPELIN_HOME/conf
ENV ZEPPELIN_NOTEBOOK_DIR $ZEPPELIN_HOME/notebook
ENV ZEPPELIN_VERSION 0.7.0

#Build from pre-compiled binaries versus off site for Version 0.7.0
RUN curl -OL http://apache.mirrors.tds.net/zeppelin/zeppelin-${ZEPPELIN_VERSION}/zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz \
    && tar -xvzf zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz -C /usr/ \
    && rm zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz \
    && mv /usr/zeppelin* $ZEPPELIN_HOME \
    && mkdir -p $ZEPPELIN_HOME/logs \
    && mkdir -p $ZEPPELIN_HOME/run 
    
ADD about.json $ZEPPELIN_NOTEBOOK_DIR/2BTRWA9EV/note.json
WORKDIR $ZEPPELIN_HOME
CMD ["bin/zeppelin.sh"]
