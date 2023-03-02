# Create build stage based on buster image
FROM golang:1.17-buster AS builder

# Create working directory under /app
WORKDIR /app

# Copy over all go config (go.mod, go.sum etc.)
COPY go.* ./

# Install any required modules
RUN go mod download

# Copy over Go source code
COPY *.go ./

# Run the Go build and output binary under fy24sko_change_tracking
RUN go build -o /fy24sko_change_tracking

# Create a new release stage to copy only the binary from the builder stage above
# This is done to dramatically lower the final Docker image size
FROM gcr.io/distroless/base-debian10

# Set the working directory to root in the new image
WORKDIR /

# Copy over the binary from the first stage to the new image
COPY --from=builder /fy24sko_change_tracking /fy24sko_change_tracking

# Make sure to expose the port the HTTP server is using
EXPOSE 8000

# Run the app binary when we run the container
ENTRYPOINT ["/fy24sko_change_tracking"]
