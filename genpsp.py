import sys, os
import re

uname = sys.argv[1]
uid = sys.argv[2]

pspstring =\
r'''apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
  name: ''' + uname + '''-psp
spec:
  privileged: false
  runAsUser:
    rule: MustRunAs
    ranges:
    - min: '''+uid+'''
      max: '''+uid+'''
  seLinux:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  volumes:
  - '*'
'''

fh=open('manifests/psp.yaml','w')
fh.write(pspstring)
fh.close()
