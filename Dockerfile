FROM python:3.9.0
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install build-essential libssl-dev \
    && apt-get clean \
    && pip install --upgrade pip

RUN pip3 install Cython numpy

# Prepare environment
RUN mkdir /jesse-docker
WORKDIR /jesse-docker

# Install TA-lib
COPY docker_build_helpers/* /tmp/
RUN cd /tmp && /tmp/install_ta-lib.sh && rm -r /tmp/*ta-lib*
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

COPY . /jesse-docker

# Install dependencies and Build
RUN pip3 install -e .

WORKDIR /home
RUN rm -r /jesse-docker
