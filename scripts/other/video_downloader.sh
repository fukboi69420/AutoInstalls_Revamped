#!/bin/bash

function install_video_downloader() {
    # This function installs the video-downloader snap package from snapcraft.io

    # Install snapd if not already installed
    if ! command -v snap &> /dev/null
    then
        echo "snapd not found. Installing snapd..."
        sudo apt update
        sudo apt install snapd -y
    fi

    # Install video-downloader snap package
    echo "Installing video-downloader snap package..."
    sudo snap install video-downloader

    # Check if installation was successful
    if ! command -v video-downloader &> /dev/null
    then
        echo "Installation failed. Please try again."
        exit 1
    fi

    echo "Installation successful. You can now use the video-downloader command."
}

# Call the function to install video-downloader
install_video_downloader
