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
ADD /git_gateway $APPDIR
ADD Pipfile $APPDIR
ADD Pipfile.lock $APPDIR

RUN pip install pipenv && \
cd $APPDIR && \
pipenv install --dev --system --deploy --ignore-pipfile && \
apk del .build-dependencies && \
rm -rf /var/cache/apk/*
