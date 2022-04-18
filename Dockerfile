FROM node:12.18.1 as build-deps
WORKDIR /usr/src/app
COPY package.json yarn.lock ./
COPY . ./
EXPOSE 3000
ENV PROD="TRUE"
ENV PROD_IP="http://10.0.0.185"
ENV LOCAL_IP="http://localhost"
ENV CLIENT_PORT="3000"
ENV BACKEND_PORT="3001"
ENV SERVER_PORT="6000"
ENTRYPOINT yarn startboth