#check if root
if [ "$EUID" -ne 0 ];then
    echo "Please run this script as root"
    exit 1
fi

#!/bin/bash

# This function installs multiple tools for OSINT investigations
function install_osint_tools() {
    # Install aircrack-ng
sudo apt-get install aircrack-ng -y

# Install nmap
sudo apt-get install nmap -y

# Install spiderfoot
sudo apt-get install spiderfoot -y

# Install phoneinfoga
sudo git clone https://github.com/ExpertAnonymous/PhoneInfoga.git /opt/PhoneInfoga
sudo pip3 install -r /opt/PhoneInfoga/requirements.txt

# Install Go
sudo apt-get install golang-go -y

# Install Tool-X
sudo git clone https://github.com/rajkumardusad/Tool-X.git /opt/Tool-X
sudo chmod +x /opt/Tool-X/install.aex
sudo /opt/Tool-X/install.aex

# Install Osintgram
sudo git clone https://github.com/Datalux/Osintgram.git /opt/Osintgram
sudo pip3 install -r /opt/Osintgram/requirements.txt

# Install socialpish
sudo git clone https://github.com/xHak9x/socialpish.git /opt/socialpish
sudo pip3 install -r /opt/socialpish/requirements.txt
    
    # Install Sherlock
    git clone https://github.com/sherlock-project/sherlock.git
    cd sherlock
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install Nexfil
    git clone https://github.com/Datalux/Osintgram.git
    cd Osintgram
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install Maigret
    git clone https://github.com/soxoj/maigret.git
    cd maigret
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install social-analyzer
    git clone https://github.com/qeeqbox/social-analyzer.git
    cd social-analyzer
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install theHarvester
    git clone https://github.com/laramies/theHarvester.git
    cd theHarvester
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install Holehe
    git clone https://github.com/megadose/holehe.git
    cd holehe
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install Anubis
    git clone https://github.com/jonluca/Anubis.git
    cd Anubis
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install Infoga
    git clone https://github.com/m4ll0k/Infoga.git
    cd Infoga
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install daprofiler
    git clone https://github.com/zer0yu/DaProfiler.git
    cd DaProfiler
    python3 -m pip install -r requirements.txt
    cd ..
    
    # Install Investigo
    git clone https://github.com/nmilosev/investigo.git
    cd investigo
    python3 -m pip install -r requirements.txt
    cd ..
}

# Call the function to install the tools
install_osint_tools


echo "All tools have been installed successfully!"
