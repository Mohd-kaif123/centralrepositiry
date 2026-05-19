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