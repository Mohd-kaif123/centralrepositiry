#!/bin/bash
############################################################################
: '
echo "====================================="
Date=$(date)
echo "Date: $Date"
c_user=$(whoami)
echo "Current User: $c_user"
c_dir=$(pwd)
echo "Current Directory: $c_dir"
d_usage=$(df / | awk 'NR==2 {print $5}' )
echo "Disk Usage: $d_usage"
r_usage=$(free -m | awk 'NR==2 {print $4}')
echo "RAM USAGE: $r_usage"
echo "======================================="
'

############################################################################
: '
show_date() {
    date
}
show_user() {
    whoami
}
show_pwd() {
    pwd
}

echo "1. Today Date"
echo "2. User Name"
echo "3. Current Directory"
echo "4. Exit"

read -p "Chose option between 1 to 4" choice

case $choice in 
    
    1)
        show_date
        ;;
    2)
        show_user
        ;;
    3)
        show_pwd
        ;;
    4) 
        echo "Exiting..."
        exit 0
        ;;
    *) 
        echo "Choose correct option."
esac
'

############################################################################

server=("web1" "web2" "db1")
echo ${server[0]}
for server in "${server[@]}"
do 
    echo "$server"
done