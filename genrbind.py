import sys, os
import re

uname = sys.argv[1]

yamlstring =\
r'''kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: '''+ uname +r'''-binding
  namespace: '''+ uname +r'''-namespace
subjects:
- kind: User
  name: '''+ uname +r'''
  apiGroup: ""
roleRef:
  kind: Role
  name: '''+ uname +r'''
  apiGroup: ""
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
    name: '''+ uname +'''-psprolebind
subjects:
- kind: User
  apiGroup: ""
  name: ''' + uname + '''
roleRef:
   apiGroup: ""
   kind: ClusterRole
   name: ''' + uname + '''-psprole
'''

fh=open('manifests/rolebind.yaml','w')
fh.write(yamlstring)
fh.close()
