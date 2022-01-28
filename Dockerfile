FROM thumbororg/alpine-pyvips:latest

RUN set -x -o pipefail \
    && export PYCURL_SSL_LIBRARY=openssl \
    && apk update \
    && apk upgrade \
    && apk add libcurl curl-dev openssl-dev \
	jpeg-dev zlib-dev libjpeg \
    && rm -rf /var/cache/apk/* \
    && rm -rf /root/.cache/pip

WORKDIR /app
COPY setup.py /app/setup.py
COPY thumbor_vips_engine/__init__.py /app/thumbor_vips_engine/__init__/py
RUN /bin/bash -l -c "pip install --no-cache-dir -e .[tests]"
