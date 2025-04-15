FROM node:22

WORKDIR /app
RUN npm install -g @angular/cli@19
COPY package*.json ./
RUN npm install
COPY . .
RUN ng build

CMD [ "ng", "serve", "--host", "0.0.0.0"]