FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Vite only reads this at build time, not container runtime (see nginx.conf's
# comment) -- the default matches this repo's existing hardcoded fallback
# exactly, so local/compose builds are unaffected. Real deployments to a
# non-localhost origin (e.g. Kubernetes, see k8s/README.md) must override it:
# docker build --build-arg VITE_API_BASE_URL=https://api.example.com/api/v1 ...
ARG VITE_API_BASE_URL=http://localhost:8000/api/v1
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL
RUN npm run build

FROM nginx:1.27-alpine AS runtime
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
