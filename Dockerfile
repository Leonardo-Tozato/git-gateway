FROM python:3.7-alpine
ENV APPDIR /usr/git_gateway

RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre

COPY /git_gateway $APPDIR
COPY Pipfile $APPDIR
COPY Pipfile.lock $APPDIR

RUN pip install pipenv && \
cd $APPDIR && \
pipenv install && \
apk del .build-dependencies && \
rm -rf /var/cache/apk/*

EXPOSE 5000
CMD ["python3", "/usr/git_gateway/wsgi.py"]