#!/bin/bash

# nmap -p 3389 xxx.xxx.xxx.1-254 -oG remote_host.txt

for ip in $(cat remote_host.txt | grep open | cut -d " " -f2); 
	do rdesktop $ip -u offsec -p lab -g 1024x768 -x 0X80; 
done
