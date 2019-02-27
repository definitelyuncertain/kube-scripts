sudo touch /etc/kubernetes/manifests/kube-apiserver.yaml
sleep 10
sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
sudo systemctl daemon-reload && sudo systemctl restart kubelet
