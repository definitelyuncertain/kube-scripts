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
  resources: ["pods", "pods/log"]
  verbs: ["*"]
'''

fh=open('manifests/role.yaml','w')
fh.write(yamlstring)
fh.close()
