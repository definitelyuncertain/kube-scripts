import sys, os
import re

pqstring =\
r'''apiVersion: v1
kind: ResourceQuota
metadata:
  name: podquota
spec:
  hard:
    pods: "2"
    requests.cpu: "8"
    requests.memory: 50Gi
    limits.cpu: "8"
    limits.memory: 50Gi
'''

fh=open('manifests/podquota.yaml','w')
fh.write(pqstring)
fh.close()
