FROM python:3.7-alpine
ENV APPDIR git_gateway
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre

WORKDIR $APPDIR
COPY /git_gateway $APPDIR
COPY Pipfile $APPDIR
COPY Pipfile.lock $APPDIR

RUN pip install pipenv && \
cd $APPDIR && \
pipenv install --system --deploy --ignore-pipfile && \
apk del .build-dependencies && \
rm -rf /var/cache/apk/*
