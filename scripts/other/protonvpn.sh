#!/bin/bash

# This function installs ProtonVPN on Ubuntu-based systems
function install_protonvpn() {
    # Install ProtonVpn DEB package
    wget https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3_all.deb

    # Add ProtonVPN repository
    sudo apt-get install /homne/kali/protonvpn-stable-release_1.0.3_all.deb

    # Update package list
    sudo apt-get update

    # Install ProtonVPN
    sudo apt-get install protonvpn
    # Install ProtonVPN CLI
    sudo apt-get install protonvpn-cli

    # Log success message
    echo "ProtonVPN has been successfully installed!"
}

# Call the function to install ProtonVPN
install_protonvpn
