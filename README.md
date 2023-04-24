# AutoInstalls_Revamped 
![bash logo](https://github.com/fukboi69420/AutoInstalls_Revamped/tree/main/assets/logo.png)

AutoInstalls_Revamped is a collection of scripts and tools designed to automate the installation and configuration of various software packages on a Linux server. This repository is a fork of the original AutoInstalls project, with additional features and improvements.

## Features

- Automated installation and configuration of popular software packages such as NGINX, Apache, MySQL, PHP, and more.
- Easy-to-use scripts with interactive prompts and customizable options.
- Support for multiple Linux distributions including Ubuntu, Debian, CentOS, and Fedora.
- Ability to install packages individually or as part of a bundled package.
- Flexible configuration options to customize the installation and setup process.
- Continuous development and improvements with regular updates.
- Inclusion of Osint Tools and more packages defaulted from Kali-Linux

## Installation

To install AutoInstalls_Revamped, simply clone the repository to your local machine:

```
git clone https://github.com/fukboi69420/AutoInstalls_Revamped.git
cd AutoInstalls_Revamped
chmod +x update.sh
chmod +x /scripts/osint_tools.sh
ls -1
```

Once you have cloned the repository, you can run the scripts in the `scripts` directory to install and configure the desired software packages.

## Usage

To use AutoInstalls_Revamped, navigate to the `scripts` directory and run the script for the software package you want to install. For example, to install NGINX, run the following command:

```
bash <program.sh> [OPTIONS]
python3 <program.py>
```

The script will prompt you for any necessary configuration options and install the software package.

# Update
to udpate AutoInstalls to the newest version enter the following commands (from @usr path), replace @usr with username
(ex: kali => home/kali/...) 
```
cd AutoInstalls_Revamped
mv update.sh /home/@usr
```
and for future updates, you can just refer back to the update.sh file that should be located in your home/usr/... .

## Contributing

Contributions to AutoInstalls_Revamped are welcome and encouraged! If you have an idea for a new feature or improvement, please submit a pull request with your changes.

## License

AutoInstalls_Revamped is released under the GNU PUBLIC License. See the LICENSE file for details.
