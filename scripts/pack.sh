#!/bin/bash

# Function to install Apache, MySQL, PHP
function install_lamp_stack() {
    # Update package list
    sudo apt-get update
    
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
