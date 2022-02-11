#!/bin/bash

IMAGE_NAME=pyblackslope
APP_NAME=pyblackslope

docker stop ${APP_NAME} 
docker rm ${APP_NAME}

docker build -t ${IMAGE_NAME} .  &&  \
    docker run --rm -d --name ${APP_NAME} -p 8000:8000 \
    -v $(pwd)/configs:/app/configs ${IMAGE_NAME} 
# wait for a container to be ready
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/health/)" != "200" ]] 
do 
    echo "waiting for container to be up"
    sleep 1
done

# output and tail the logs for the container
docker logs -f ${APP_NAME}