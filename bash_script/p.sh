##############################################################
: '
read -p "Enter your Age: " age
if [ age>=18 ];
then
    echo "Eligible"
else
    echo "Not Eligible"
fi
'
##############################################################
: '
read -p "Enter your Name: " name
for i in {1..5};
do
    echo "$name"
done
'
##############################################################
: '
read -p "Enter a number: " num
result=$(())
if (( num % 2 ==0 )); then
    echo "No. is Even"
else
    echo "No. is odd"
fi
'
##############################################################
: '
read -p "Enter a number: " num
for i in {1..10};
do  
    result=$(( num * i ))
    echo "$num * $i = $result"
done
'
##############################################################
: '
read -p "Enter a number: " num
for (( i=1; i<=num; i++ ))
do
    echo $i
done
'
##############################################################
: '
read -p "Enter a number: " num
sum=1
for (( i=1; i<=num; i++ ));
do
    sum=$(( sum * i ))
done

echo "Total:" $sum
'
##############################################################
: '
-f   # Regular file
-d   # Directory
-e   # File ya directory dono
-r   # Read permission
-w   # Write permission
-x   # Execute permission
'
: '
read -p "Enter File Name: " file_name
if [ -f "$file_name" ];then
    echo "File Exists"
    stat "$file_name" | grep Size | awk '{print $2}'
else
    echo "File not found" 
fi
'
##############################################################
: '
read -p "Enter DIR name: " DIR_name
if [ -d "$DIR_name" ]; then
    echo "Directory exists"
    current_date=$( date )
    count=$( ls "$DIR_name" | wc -l )
    echo "Total files: $count"
    echo "Today: $current_date"
else
    echo "Directory is not exists"
fi
'
##############################################################
: '
read -p "Enter file Name: " file_name
if [ -f "$file_name" ];then
    echo "##################################"
    echo "         File Report              "
    echo "##################################"
    echo "        File exists               "
    echo "----------------------------------"
    size=$(stat "$file_name" | grep Size | awk '{print $2}')
    echo "    File Size: $size              "
    echo "----------------------------------"
    current_date=$(date)
    echo "Today Date: $current_date         "
else
    echo "File not found"
fi
'
##############################################################

echo "#################################"
echo "           Details               "
echo "#################################"
c_date=$(date)
echo "Today : $c_date"
echo "---------------------------------"
c_user=$(whoami)
echo "  Current User: $c_user          "

echo "---------------------------------"
c_dir=$(pwd)
echo "  Current Directory: $c_dir      "

echo "---------------------------------"
t_file=$( ls | wc -l )
echo " Total file in Current Directory: $t_file" 
