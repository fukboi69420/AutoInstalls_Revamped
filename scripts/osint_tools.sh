#!/bin/bash

# This function installs multiple tools for OSINT investigations
function install_osint_tools() {
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
