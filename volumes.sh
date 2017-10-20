# Provision NFS volumes

python genpv.py home $2 "/storage/home/$1"
kubectl create -f manifests/pv-home.yaml

python genpvc.py home
kubectl create -f manifests/pvc-home.yaml


python genpv.py tools $2 "/tools"
kubectl create -f manifests/pv-tools.yaml

python genpvc.py tools
kubectl create -f manifests/pvc-tools.yaml


python genpv.py datasets $2 "/datasets"
kubectl create -f manifests/pv-dataset.yaml

python genpvc.py datasets
kubectl create -f manifests/pvc-datasets.yaml
