#!/bin/bash

gunicorn -c gunicorn_conf.py female_ghost.wsgi:application