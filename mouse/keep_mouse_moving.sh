#!/bin/bash

# Function to install and update qBittorrent to the latest version
function install_qbittorrent() {
    # Add the qBittorrent stable PPA
    sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable -y
    
    # Update the package list
    sudo apt-get update
    
    # Install qBittorrent
    sudo apt-get install qbittorrent -y
    
    # Upgrade qBittorrent to the latest version
    sudo apt-get upgrade qbittorrent -y
}

# Call the function to install and update qBittorrent
install_qbittorrent
