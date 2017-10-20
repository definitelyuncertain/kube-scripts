# Provision NFS volumes

python genpv.py $1-home $2 "/storage/home/$1"
kubectl create -f manifests/pv-$1-home.yaml --namespace=$1-namespace

python genpvc.py $1-home
kubectl create -f manifests/pvc-$1-home.yaml --namespace=$1-namespace


python genpv.py tools $2 "/tools"
kubectl create -f manifests/pv-tools.yaml --namespace=$1-namespace

python genpvc.py tools
kubectl create -f manifests/pvc-tools.yaml --namespace=$1-namespace


python genpv.py datasets $2 "/datasets"
kubectl create -f manifests/pv-datasets.yaml --namespace=$1-namespace

python genpvc.py datasets
kubectl create -f manifests/pvc-datasets.yaml --namespace=$1-namespace
