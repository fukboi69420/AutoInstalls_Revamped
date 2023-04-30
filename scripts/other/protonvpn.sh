#!/bin/bash

# This function installs ProtonVPN on Ubuntu-based systems
function install_protonvpn() {
    # Install ProtonVpn Windows package
    wget https://protonvpn.com/download-windows/

    # check if wine is installed
    if ! wine > /dev/null; then
   echo -e "Command not found! Install? That's an error \c"
   read
   if "$REPLY" = "y"; then
      sudo apt-get install wine
   fi
fi


    # Log success message
    echo "ProtonVPN has been successfully installed!"
}

# Call the function to install ProtonVPN
sudo wine /scripts/other/ProtonVPN_win_v2.4.2
