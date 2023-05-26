#!/bin/bash

cd src
celery -A config worker -l info