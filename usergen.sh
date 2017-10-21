mkdir -p manifests
mkdir -p key

kubectl create namespace $1-namespace

bash volumes.sh $1 $2

bash keygen.sh $1

sudo mkdir -p /storage/home/$1/.kube/key

sudo cp ./key/$1.key ./key/$1.crt ./key/$1.csr /storage/home/$1/.kube/key/

sudo chmod -R u+rwx,go-rwx /storage/home/$1/.kube/key/

sudo chown -R $1: /storage/home/$1/.kube

kubectl config set-credentials $1 --client-certificate=/storage/home/$1/.kube/key/user1.crt  --client-key=/storage/home/$1/.kube/key/user1.key

kubectl config set-context $1-context --cluster=kubernetes --namespace=$1-namespace --user=$1

bash restrictions.sh $1
