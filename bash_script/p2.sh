#!/bin/bash
: '
Mera logic:
...
Mera code:
...

Error:
...
'

#########################################################
: '
c_date=$(date)
echo "$c_date" >> time.log
'

#########################################################
: '
c_date=$(date)
echo "Date: $c_date"
c_user=$(whoami)
echo "User: $c_user"
d_usage=$(df / | awk 'NR==2 {print $5}')
echo "Disk Usage: $d_usage"
'
#########################################################
: '
c_date=$(date)
echo "Date: $c_date"
c_user=$(whoami)
echo "User: $c_user"
d_usage=$( df / | awk 'NR==2 {print $5}' | tr -d '%' )
if [ "$d_usage" -gt 80 ]; then
    echo "WARNING: Disk Usage High"
else
    echo "Disk is Normal"
fi
'

#########################################################
: '
read -p "Enter a Number: " num
i=1
while (( i<=$num ))
do
    echo "$i"
    ((i++))
done
'
#########################################################
: '
show_user() {
    whoami
}

show_date() {
    date
}


show_pwd() {
    pwd
}

show_user
show_date
show_pwd

greet() {
    echo "Hello: $1"
    echo "Age: $2"
}
greet "kaif" "23"

sqr() {
    echo "Square: $(($1 * $1))"
}
sqr "5"
'
#########################################################
: '
show_user() {
    whoami
}

show_date() {
    date
}


show_pwd() {
    pwd
}


echo "1. show Date"
echo "2. Show user"
echo "3. Show Directory"
echo "4. Exit"

read choice
if [ "$choice" -eq 1 ]
then
    show_date

elif [ "$choice" -eq  2 ]
then
    show_user
elif [ "$choice" -eq 3 ]
then
    show_pwd
elif [ "$choice" -eq 4 ]
then
    echo "Exit"
    exit 0
else
    echo "Choose Betn 1 to 4"
fi
'