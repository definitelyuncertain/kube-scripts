# Provision NFS volumes

kubectl delete pv $1-home --namespace=$1-namespace

kubectl delete pvc home --namespace=$1-namespace


#python genpv.py $1-tools $2 "/tools" 1Mi ReadOnlyMany $1 tools
#kubectl create -f manifests/pv-$1-tools.yaml --namespace=$1-namespace

#python genpvc.py tools ReadOnlyMany 1Mi
#kubectl create -f manifests/pvc-tools.yaml --namespace=$1-namespace


#python genpv.py $1-datasets $2 "/datasets" 1Mi ReadOnlyMany $1 datasets
#kubectl create -f manifests/pv-$1-datasets.yaml --namespace=$1-namespace

#python genpvc.py datasets ReadOnlyMany 1Mi
#kubectl create -f manifests/pvc-datasets.yaml --namespace=$1-namespace

for line in `cat volumes-list.txt`; do
    ip=`echo $line | cut -d',' -f1`
    path=`echo $line | cut -d',' -f2`
    volname=`echo $line | cut -d',' -f3`
    mode=`echo $line | cut -d',' -f4`
    cap=`echo $line | cut -d',' -f5`
    
    
    kubectl delete pv $1-$volname.yaml --namespace=$1-namespace
    

    kubectl delete pvc $volname.yaml --namespace=$1-namespace
done
