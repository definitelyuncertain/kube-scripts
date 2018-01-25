echo Creating user "$1" in programme "$2"

user="$1"
prog="$2"
cwd=`pwd`

if [ "$prog" = "phd" ]
    then
        exp=`date --rfc-3339=date -d "5 years"`
fi

if [ "$prog" = "ms" ]
    then
        exp=`date --rfc-3339=date -d "3 years"`
fi

if [ "$prog" = "mtech" ]
    then
	exp=`date --rfc-3339=date -d "2 years"`
fi

if [ "$prog" = "dual" ]
    then
	exp=`date --rfc-3339=date -d "1 years"`
fi

if [ "$prog" = "btech" ]
    then
	exp=`date --rfc-3339=date -d "1 years"`
fi

if [ "$prog" = "project" ]
    then
	exp=`date --rfc-3339=date -d "1 year"`
fi

if [ "$prog" = "intern" ]
    then
	exp=`date --rfc-3339=date -d "6 months"`
fi

sudo useradd -m -d /storage/home/"$user" -s /bin/bash -e "$exp" "$user"
echo "$user":"$user" | sudo chpasswd
sudo edquota -p master "$user"
cd /var/yp
sudo make
cd "$pwd"
echo Created user "$user"
