import sys, os
import re

uname = sys.argv[1]

yamlstring =\
r'''kind: Role
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  namespace: '''+ uname +r'''-namespace
  name: ''' + uname +'''
rules:
- apiGroups: ["", "extensions", "apps"]
  resources: ["pods", "pods/log", "pods/exec"]
  verbs: ["*"]
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  name: '''+ uname +'''-psprole
rules: 
- apiGroups: ["extensions"]
  resources: ["podsecuritypolicies"]
  resourceNames: ["''' + uname + '''-psp"]
  verbs: ["use"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get", "list", "watch", "describe"]
- apiGroups: ["", "extensions", "apps"]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch", "describe"]
'''

fh=open('manifests/role.yaml','w')
fh.write(yamlstring)
fh.close()
