#!/bin/bash
: '
echo "=================================================="
today=$(date +%Y-%m-%d)
echo "Date: $today"
c_user=$(whoami)
echo "Current user: $c_user"
#all_loged=$(who)
echo "Logged in Users: "
who
s_uptime=$(uptime)
echo "System Uptime: $s_uptime"
echo "==================================================="
'
#############################################################################
: '
read -p "Enter Service Name: " s_name
s_runn=$(systemctl is-active $s_name)
if [ "$s_runn" = "active" ];then
    echo "$s_name is running"
else
    echo "$s_name is not running"
fi
'
#############################################################################
: '
d_usage=$(df -h | awk 'NR==2 {print $5}' | tr -d '%')
today=$(date +%Y-%m-%d)
if [ "$d_usage" -ge 80 ];then
    echo -e "[$today] Warning: Disk is usage more than 80% \nCurrent Usage: ${d_usage}%" >> log/monitor.log
else
    echo -e "[$today] Disk is Normal \nCurrent Usage: ${d_usage}%" >> log/monitor.log
fi
'
#############################################################################
: '
servers=$("nginx" "Node.js")

for server in "${servers[@]}";do
    echo "Checkind $server....."

    if ping -c 1 "$server" &>/dev/null; then
        echo "$server is Online"
        ssh "ubuntu@$server" "df -h" 2>/dev/null | awk 'NR==2 {print $5}' 
    else
        echo "$server is Offline"
        #echo "$(date "+%Y-%m-%d) $server is Offline "
    fi
done
'
#############################################################################

show_date() {
    Date=$(date +%Y-%m-%d)
    echo "Date: $Date"
}
show_user() {
    user=$(whoami)
    echo "User: $user"
}
show_d_usage() {
    d_usage=$(df -h | awk 'NR==2 {print $5}')
    echo "Disk Usage: $d_usage"
}
show_r_usage() {
    r_usage=$(free -m | awk 'NR==2 {print $3}')
    echo "RAM Usage: $r_usage"
}
show_uptime() {
    u_time=$(uptime)
    echo "UPTIME: $u_time"
}
show_b_folder() {
    src_dir="/mnt/d/python_practise/centralrepositiry/bash_script/dir"
    backup_dir="/mnt/d/python_practise/centralrepositiry/bash_script/backup"
    backup_file="backup_$(date +%Y-%m-%d).tar.gz"
    tar -czf "${backup_dir}/${backup_file}" "$src_dir"
    echo "Backup sucessful: ${backup_dir}/${backup_file}"
}

echo "======================================"
echo "                Menu                  "
echo "======================================"
echo " 1. Date"
echo " 2. User"
echo " 3. Disk Usage"
echo " 4. RAM Uasage"
echo " 5. Uptime"
echo " 6. Backup Folder"
echo " 7. Exit"
echo "======================================"

read -p "Choice between 1 to 7" choice

case $choice in

    1) 
        show_date
        ;;
    2)
        show_user
        ;;
    3)
        show_d_usage
        ;;
    4)
        show_r_usage
        ;;
    5)
        show_uptime
        ;;
    6)
        show_b_folder
        ;;
    7)
        echo "Exit"
        exit 1
        ;;
    *)
        echo "Enter Correct option."
        ;;
esac