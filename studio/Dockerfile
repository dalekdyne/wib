FROM node:16.14.2-slim AS build
WORKDIR /app

COPY package.json package-lock.json ./
COPY . ./

RUN npm install -g @vue/cli-service-global
RUN npm ci

RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
