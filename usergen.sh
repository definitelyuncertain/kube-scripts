mkdir -p manifests
mkdir -p key

kubectl create namespace $1-namespace

bash volumes.sh $1 $2

bash keygen.sh $1

sudo mkdir -p /home/$1/.kube/key

sudo cp ./key/*.key ./key/*.crt ./key/*.csr /home/$1/.kube/key/

sudo chown -R $1: /storage/home/$1/.kube

kubectl config set-credentials $1 --client-certificate=/home/$1/.kube/key/user1.crt  --client-key=/home/$1/.kube/key/user1.key

kubectl config set-context $1-context --cluster=kubernetes --namespace=$1-namespace --user=$1

bash restrictions.sh $1
