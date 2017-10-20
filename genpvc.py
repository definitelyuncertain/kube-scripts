import sys, os
import re

name = sys.argv[1]

yamlstring =\
r'''apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: '''+ name + '''
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ""
  resources:
    requests:
      storage: 6Gi
'''

fh=open('manifests/pvc-'+ name +'.yaml','w')
fh.write(yamlstring)
fh.close()
