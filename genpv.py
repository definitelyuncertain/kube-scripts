import sys, os
import re

name = sys.argv[1]
ip = sys.argv[2]
path = sys.argv[3]
mode = sys.argv[4]

yamlstring =\
r'''apiVersion: v1
kind: PersistentVolume
metadata:
  name: ''' + name + '''
spec:
  capacity:
    storage: 6Gi
  accessModes:
    - '''+ mode +'''
  nfs:
    server: ''' + ip + '''
    path: ''' + path + '''
'''

fh=open('manifests/pv-'+ name +'.yaml','w')
fh.write(yamlstring)
fh.close()
