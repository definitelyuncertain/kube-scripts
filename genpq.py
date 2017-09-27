import sys, os
import re

pqstring =\
r'''apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    pods: "1"
'''

fh=open('manifests/podquota.yaml','w')
fh.write(pqstring)
fh.close()
