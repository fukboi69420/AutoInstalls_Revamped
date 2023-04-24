#!/bin/bash

# This script runs through a list of security tools with a clean UI

# Install required dependencies
sudo apt-get update
sudo apt-get install -y aircrack-ng nmap python3-pip
pip3 install phoneinfoga osintgram socialphish sherlock nexfil maigret social-analyzer theHarvester Anubis Infoga daprofiler Investigo

# Define function to run the tools
run_security_tools() {
    # Run aircrack
    aircrack-ng -h
    
    # Run nmap
    nmap -h
    
    # Run phoneinfoga
    phoneinfoga -h
    
    # Run Osintgram
    osintgram -h
    
    # Run socialphish
    socialphish -h
    
    # Run sherlock
    sherlock -h
    
    # Run nexfil
    nexfil -h
    
    # Run maigret
    maigret -h
    
    # Run social-analyzer
    social-analyzer -h
    
    # Run theHarvester
    theHarvester -h
    
    # Run Anubis
    anubis -h
    
    # Run Infoga
    infoga -h
    
    # Run daprofiler
    daprofiler -h
    
    # Run Investigo
    investigo -h
}

# Run the function
