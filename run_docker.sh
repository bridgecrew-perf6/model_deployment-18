#!/bin/bash

DOCKER_BUILDKIT=1 docker build . -t model_app_v1

docker run -it -p 8000:8000 model_app_v1