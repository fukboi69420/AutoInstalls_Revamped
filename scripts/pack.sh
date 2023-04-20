#!/bin/bash

# Function to install Apache, MySQL, PHP, neofetch, tree, and similar other packages
function install_lamp_stack() {
    # Update package list
    sudo apt-get update

    # Install neofetch
    sudo apt-get install neofetch -y

    # Install tree
    sudo apt-get install tree -y

    # Install other packages here
    # ...
    
    # Install Apache
    sudo apt-get install apache2 -y
    
    # Install MySQL
    sudo apt-get install mysql-server -y
    
    # Install PHP
    sudo apt-get install php libapache2-mod-php php-mysql -y
    
    # Restart Apache
    sudo systemctl restart apache2
    
    # Check Apache status
    sudo systemctl status apache2
}

# Call the function
install_lamp_stack


    # Print success message
    echo "Packages installed successfully"
