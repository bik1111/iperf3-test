# Use the official Ubuntu 20.04 base image
FROM ubuntu:20.04

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Python 3 and required libraries
RUN apt-get update && apt-get install -y python3 python3-pip iperf3 iproute2

# Install iperf3 Python module
RUN pip3 install iperf3
