mkdir -p key

openssl genrsa -out "key/$1.key" 2048

openssl req -new -key "key/$1.key" -out "key/$1.csr" -subj "/CN=$1/O=$1"

sudo openssl x509 -req -in "key/$1.csr" -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out "key/$1.crt" -days 1000
