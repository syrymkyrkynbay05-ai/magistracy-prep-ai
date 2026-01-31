# Build stage
FROM node:20-slim AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html
# If using React Router, we need a custom nginx config to handle SPA
# For now, standard serving.

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
