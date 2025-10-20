#!/bin/bash
set -e
export NGINX_MAX_BODY_SIZE="${NGINX_MAX_BODY_SIZE:-30M}"
export NGINX_CACHE_DIR="${NGINX_CACHE_DIR:-/data/nginx/cache}"
export MEDIA_ROOT="${MEDIA_ROOT:-/var/media}"
export STATIC_ROOT="${STATIC_ROOT:-/var/static}"

export REDIS_LOGLEVEL="${REDIS_LOGLEVEL:-warning}"
export REDIS_MAXMEMORY="${REDIS_MAXMEMORY:-100Mb}"
export REDIS_MAXMEMORY_POLICY="${REDIS_MAXMEMORY_POLICY:-volatile-ttl}"

export DOLLAR='$'

mkdir -p /var/run /var/nginx ${NGINX_CACHE_DIR} ${MEDIA_ROOT} ${STATIC_ROOT}
echo "created support dirs /var/run '${MEDIA_ROOT}' '${STATIC_ROOT}' "
echo "Startup command is: '$1'"

case "$1" in
    "run")
        envsubst < /conf/nginx.conf.tpl > /conf/nginx.conf && /usr/sbin/nginx -tc /conf/nginx.conf

        django-admin upgrade --no-input

        /usr/sbin/nginx -c /conf/nginx.conf
        exec uwsgi --ini /conf/uwsgi.ini

    ;;
    "dev")
        until pg_isready -h db -p 5432;
          do echo "waiting for database"; sleep 2; done;
        django-admin collectstatic --no-input
        django-admin migrate
        django-admin runserver 0.0.0.0:8000
    ;;
    "setup")
        until pg_isready -h db -p 5432;
          do echo "waiting for database"; sleep 2; done;
        django-admin upgrade --no-input
    ;;
*)
exec "$@"
;;
esac
