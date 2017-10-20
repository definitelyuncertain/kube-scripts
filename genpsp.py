import sys, os
import re

uid = sys.argv[1]

pspstring =\
r'''apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restrict-root
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
