#!/bin/bash

# Function to install nginx
install_nginx() {
    # Update package list
    sudo apt-get update
    
    # Install nginx
    sudo apt-get install nginx -y
    
    # Check if nginx is running
    if pgrep -x "nginx" > /dev/null
    then
        echo "Nginx is installed and running"
    else
        echo "Nginx installation failed"
    fi
}

# Call the function
install_nginx
