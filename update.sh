#!/bin/bash

#AutoInstalls update script

#update repository

echo "Updating AutoInstalls_Revamped repository..."
git pull

#update packages

echo "Updating packages..."

#update apt packages

sudo apt update -y
sudo apt upgrade -y

#update pip packages

pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U

#update npm packages

npm update -g

echo "Cleaing up files..."

for i in {1..50}
do
    echo -ne '/'
    sleep 0.05
done

echo "][100%]"

echo "AutoInstalls_Revamped is now up-to-date!"

ls
