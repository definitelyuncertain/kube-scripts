export PATH="/usr/local/nvidia/bin:/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/nvidia/lib:$LD_LIBRARY_PATH"
cd /home/kube/workdir
python getdevices.py &> out
#nvidia-smi &> out
#nvcc --version &> out
