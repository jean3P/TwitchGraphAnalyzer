FROM node:18 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --fetch-retries=5 --fetch-retry-factor=2 --fetch-retry-mintimeout=10000 # Install dependencies
COPY . ./
RUN npm run build

# Production stage
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]