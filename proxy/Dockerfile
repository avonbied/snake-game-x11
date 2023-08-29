FROM alpine:latest

RUN apk update && apk add --no-cache git bash python3

WORKDIR /home/novnc
RUN wget https://github.com/novnc/noVNC/archive/refs/tags/v1.4.0.tar.gz &&\
	tar -xvf v1.4.0.tar.gz --strip-components=1 &&\
	rm -f v1.4.0.tar.gz

ENV PATH /home/novnc/utils:$PATH

EXPOSE 6080
ENTRYPOINT [ "novnc_proxy" ]