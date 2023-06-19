#Base Images
FROM ubuntu:latest

RUN apt -y update && apt -y upgrade

VOLUME ["/data", "/etc/nginx-site-enabled", "/var/log/nginx"]

# server execution
ENTRYPOINT ["top"]
CMD ["-d","10"]
