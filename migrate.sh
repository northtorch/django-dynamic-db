#!/bin/sh
TARGET_APPS="contenttypes sessions main"
DATABASES="default main"

# exec migration for transaction data
for DATABASE in ${DATABASES}
do
    for APP_LABEL in ${TARGET_APPS}
    do
        echo python manage.py migrate ${APP_LABEL} --database=${DATABASE}
        python manage.py migrate ${APP_LABEL} --database=${DATABASE}
    done
done
# exec migration for master data
echo python manage.py migrate master
python manage.py migrate master