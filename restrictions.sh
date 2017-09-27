# Generate and Apply Pod Security Policy
python genpsp.py $1
kubectl create -f manifests/psp.yaml --namespace=$1-namespace

# Generate and Apply Resource Quotas
python genpq.py $1
kubectl create -f manifests/podquota.yaml --namespace=$1-namespace

# Generate and Apply Role
python genrole.py $1
kubectl create -f manifests/role.yaml

# Generate and Apply RoleBinding
python genrbind.py $1
kubectl create -f manifests/rolebind.yaml
