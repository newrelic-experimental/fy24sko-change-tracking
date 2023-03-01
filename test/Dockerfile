# Base image
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy the Artillery config file and test script to the container
COPY ./artilleryTest.yml /app

# Install Artillery
RUN npm install -g artillery

# Start the load test
CMD ["artillery", "run", "artilleryTest.yml"]
