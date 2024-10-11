#!/usr/bin/env bash

# Run exporter
.local/bin/uwsgi --http 0.0.0.0:${SONAR_EXPORTER_PORT:-9119} --wsgi-file main.py --callable app
