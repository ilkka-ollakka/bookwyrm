#!/bin/bash
set -e

CANARY=/app/static/.dbinit_done

info() { echo >&2 "$*"; }
die() {
    echo >&2 "$*"
    exit 1
}

trap exit TERM

if [ "$1" == "exit" ]; then
    info "**** base container exiting"
    exit 0
fi

if [ "$1" = "gunicorn" ]; then
    info "**** Checking needed migrations"
    python manage.py migrate || die "failed to migrate"
    python manage.py migrate django_celery_beat || die "failed to migrate django"
    python manage.py collectstatic --no-input || die "failed to collect static"
    info "**** Done with migration checking and static asset collection"
    if [ ! -r "$CANARY" ]; then
        info "**** Doing initial setup!"
        python manage.py initdb || die "failed to initdb"
    fi
    chown -c -R bookwyrm /app/exports
    chown -c -R bookwyrm /app/images
    if [ ! -r "$CANARY" ]; then
        python manage.py admin_code
        info "**** Done with initial setup!"
    fi

    touch "$CANARY"
else
    while [ ! -r "$CANARY" ]; do
        info "**** Waiting for database and migrations to finish"
        sleep 3
    done
fi

exec gosu bookwyrm "$@"
