#!/bin/bash

celery -A celery worker -l info -c 4