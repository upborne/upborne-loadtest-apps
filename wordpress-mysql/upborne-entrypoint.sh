#!/bin/sh
# WordPress reads its database as four variables; Upborne hands one URL.
# mysql://user:password@host:3306/name
url="${DATABASE_URL#mysql://}"
export WORDPRESS_DB_USER="${url%%:*}"
rest="${url#*:}"
export WORDPRESS_DB_PASSWORD="${rest%%@*}"
rest="${rest#*@}"
export WORDPRESS_DB_HOST="${rest%%/*}"
export WORDPRESS_DB_NAME="${rest#*/}"
exec docker-entrypoint.sh apache2-foreground
