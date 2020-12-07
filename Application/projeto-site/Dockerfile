FROM node:12-alpine

WORKDIR /usr/app
COPY package.json package-lock.json ./

RUN npm

COPY . . 

EXPOSE 3333
CMD ["npm", "start"]

