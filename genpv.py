import sys, os
import re

name = sys.argv[1]
ip = sys.argv[2]
path = sys.argv[3]
cap = sys.argv[4]
mode = sys.argv[5]
uname = sys.argv[6]
claimname = sys.argv[7]

yamlstring =\
r'''apiVersion: v1
kind: PersistentVolume
metadata:
  name: ''' + name + '''
spec:
  capacity:
    storage: ''' + cap + '''
  accessModes:
    - '''+ mode +'''
  claimRef:
    namespace: ''' + uname + '''-namespace
    name: '''+ claimname + '''
  nfs:
    server: ''' + ip + '''
    path: ''' + path + '''
'''

fh=open('manifests/pv-'+ name +'.yaml','w')
fh.write(yamlstring)
fh.close()
