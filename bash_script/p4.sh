#!/bin/bash
: '
read -p "Enter Folder name: " folder_name
if [ -d "$folder_name" ];then
    echo "Folder Exist"
else
    echo "Folder not found"
    exit 1
fi
Today=$(date +%Y-%m-%d)
Backup_file="${folder_name}_${Today}.tar.gz"
tar -czf "$Backup_file" "$F_name"
'
#############################################################################
: '
read -p "Enter file Name:" f_name
if [ -d "$f_name" ];then
    echo "Folder Exist"
else
    echo "Folder Not Found"
    exit 1
fi
if [ -d "backup" ];then
    echo "backup folder is present"
else
    echo "backup folder not found!"
    echo "Creating backup folder...."
    mkdir -p backup
fi
Today=$(date +%Y-%m-%d)
Backup_f="${f_name}_${Today}.tar.gz"
tar -czf "backup/$Backup_f" "$f_name"
echo "backup Created successfully: backup/$Backup_f"
find backup -mtime +7
find backup -mtime +7 -delete
'
#############################################################################

if [ -d "log" ];then
    echo "Folder Exist!"
else
    echo "File Not Found!"
    echo "Folder creating...."
    mkdir -p log
    echo "Folder created"
fi
today=$(date +%Y-%m-%d)
read -p "Enter folder Name: " f_name
log_file="log/${f_name}_${today}.log"
touch $log_file

c_user=$(whoami)
d_usage=$( df -h | awk 'NR==2 {print $5}')
echo "Date: $today" >> $log_file
echo "Current User: $c_user" >> $log_file
echo "Disk Usage: $d_usage" >> $log_file
find log/ -mtime +7
find log/ -mtime +7 -delete