import sys, os
import re

name = sys.argv[1]
mode = sys.argv[2]
cap = sys.argv[3]

yamlstring =\
r'''apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: '''+ name + '''
spec:
  accessModes:
    - ''' + mode + '''
  storageClassName: ""
  resources:
    requests:
      storage: ''' + cap + '''
'''

fh=open('manifests/pvc-'+ name +'.yaml','w')
fh.write(yamlstring)
fh.close()
