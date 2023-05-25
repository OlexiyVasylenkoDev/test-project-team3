# Stage 1: Build React app
FROM node:14-alpine as build-stage

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci --silent

# Copy the source code
COPY . .

# Build the React app
RUN npm run build

# Stage 2: Serve React app with Nginx
FROM nginx:1.21-alpine as production-stage

# Copy the build files from the previous stage
COPY --from=build-stage /app/build /usr/share/nginx/html

# Copy custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
