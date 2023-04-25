#!bin/bash

#remove dir
sudo rm -rf AutoInstalls_Revamped

#clone repository
git clone https://github.com/fukboi69420/AutoInstalls_Revamped

#cd in AutoInstalls
cd AutoInstalls_Revamped

#cd in scripts
cd scripts

# enable osint_tools & pack to use sh
chmod +x osint_tools.sh pack.sh

# cd dir main
cd ..

#list
tree
