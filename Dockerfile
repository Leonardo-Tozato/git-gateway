FROM python:3.7-alpine
ENV APPDIR git_gateway
EXPOSE 8080
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
pipenv install --system --deploy --ignore-pipfile && \
apk del .build-dependencies && \
rm -rf /var/cache/apk/*

CMD ["gunicorn", "--workers", "1", "--worker-class", "gthread", "-b", "0.0.0.0:8080", "--reload", "--threads", "8", "--timeout", "60", "--keep-alive", "1", "git_gateway.app:app" ]