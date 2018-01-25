for line in `cat $1`; do
    username=`echo $line | cut -d',' -f1`;
    bash usergen.sh $username $2
    echo "====== User $username done ======"
done
