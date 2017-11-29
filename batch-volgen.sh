for line in `cat $1`; do
    username=`echo $line | cut -d',' -f1`;
    bash volumes.sh $username $2
    echo "======\nUser $username done\n======"
done
