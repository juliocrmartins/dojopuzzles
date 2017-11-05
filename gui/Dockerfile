FROM node:latest
ENV NPM_CONFIG_LOGLEVEL warn
RUN mkdir /var/build && cd /var/build
WORKDIR /var/build
COPY ./dojopuzzles .
RUN npm install -g serve
CMD serve -s build
EXPOSE 9000