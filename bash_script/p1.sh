: '
while true
loop

    echo "---------------------------"
    echo "       SCRIPT MENU         "
    echo "---------------------------"
    echo "1. Check RAM"
    echo "2. Check Disk"
    echo "3. Check CPU"
    echo "4. Exit"

read -p "Chose option [1-4] : " choice

case $choice in
    1) 
        echo "----------- Check RAM ----------"
        free -m
        ;;
    2)
        echo "------------ Check Disk ---------"
        df -h
        ;;
    3)
        echo "------------- Check CPU -----------"
        top -bn1 | head -n 5
        ;;
    4)
        echo "Exit"
        exit 0
        ;;
    *) 
        echo " Option is Wrong ! please chose correct option"
esac

echo ""
done
'

# --------------------- Auto Deployment Script ------------------#
: '
PROJECT_DIR="/mnt/d/project"
FILE_NAME="My_project"
echo "    Start Automatic Deployment    "
echo "=================================="
echo "Going to project.."
cd $PROJECT_DIR || { echo "Error: directory is not found"; exit 1; }
echo "git pull request"
git checkout main
git pull origin main
if [ $? -eq 0 ];
then
    echo "pull successfully"
else
    echo "pull failed" 
    exit 1;
fi 
echo "build project"
npm install
if [ $? -eq 0 ];
then
    echo "project build hogaey"
else
    echo "buil nahi hua"
    exit 1;
fi 

echo "restart service"
systemctl service restart $FILE_NAME
if [ $? -eq 0 ];
then
    echo "service restart successgully"
else
    echo "restart fail"
    exit 1;
fi 
'