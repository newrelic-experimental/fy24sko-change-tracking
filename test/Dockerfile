# Base image
FROM node:16.19-alpine

# Install Python3 and pip
RUN apk update && apk add --no-cache python3 py-pip

# Set working directory
WORKDIR /app

# Copy the Artillery config file and test script to the container
COPY ./artilleryTest.yml /app

# Install Artillery
RUN npm install -g artillery

# Start the load test
CMD ["artillery", "run", "artilleryTest.yml"]
