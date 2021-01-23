FROM node:12.7-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build


#FROM nginx:alpine

#COPY nginx.conf /etc/nginx/nginx.conf

#WORKDIR /usr/share/nginx/html
#COPY /resume-app/dist/resume-app .
