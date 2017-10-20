# Provision NFS volumes

python genpv.py $1-home $2 "/storage/home/$1" ReadWriteOnce
kubectl create -f manifests/pv-$1-home.yaml --namespace=$1-namespace

python genpvc.py $1-home ReadWriteOnce
kubectl create -f manifests/pvc-$1-home.yaml --namespace=$1-namespace


python genpvc.py tools ReadOnlyMany
kubectl create -f manifests/pvc-tools.yaml --namespace=$1-namespace


python genpvc.py datasets ReadOnlyMany
kubectl create -f manifests/pvc-datasets.yaml --namespace=$1-namespace
