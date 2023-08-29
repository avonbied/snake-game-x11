FROM python:3-alpine

RUN apk add --no-cache xvfb x11vnc mesa-dri-gallium xvfb-run

ENV DISPLAY=:99
ENV XAUTHORITY=CookieFile

WORKDIR /home/app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5900
ENTRYPOINT [ "./entrypoint.sh" ]