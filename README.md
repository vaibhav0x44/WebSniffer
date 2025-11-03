![Logo](https://thumbs.dreamstime.com/b/website-icon-vector-illustration-web-browser-internet-symbol-83920968.jpg)
# WebSniffer 

WebSniffer is a command Line information gathering tool built in Python 3.x . It Basically Asks For Domain Name to Enumerate different URL Based Parameter , Website Endpoints , Ip address . and Sensitive Files enumeration .


## Features


- dns lookup - resolves domain to IPs via dns-Python Module

- robots.txt - Reads diallowed paths from target domains.

- directory-enumeration - uses a wordlist of common list of endpoints via word.csv 

- packet sniffer - captures live packets on a interface via pyshark

- reporting - saves all results in json format = (<domain>.json)

- cross-platform support - works for both linux (posix env.) and windows (nt)




## Installation


prerequisites:

- In windows , install git .
- Use the updated version of python 3.x

Linux Installation(posix)

Command : 

```bash
~# git clone https://github.com/vaibhav0x44/WebSniffer.git
```
Navigate :

```bash 
~# cd dir/WebSniffer 
```

Install requirements : 
```bash
(venv) ~# pip3 install -r  requirements.txt
```

Set all permissions : -rwxrwxrwx

```bash 
~# chmod ugo=rwx websniffer.py or chmod 777 websniffer.py 
```

Run : 

```bash 
~# python3 websniffer.py 
~# ./websniffer.py --> if permissions set to -rwxrwxrwx
```

Windows Installation(nt)

- Open cmd with administartor 

 Command : 
```bash 
> git clone https://github.com/vaibhav0x44/WebSniffer.git
```
Naviagte : 
```bash 
> cd users\dir\websniffer
```
Install requirements : 
```bash 
> pip install -r requirements.txt
```
Run : 
```bash 
> python websniffer.py 
```




## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Authors

- [@vaibhav0x44](https://www.github.com/vaibhav0x44)

