# 3scale tenant scripts

## Set tenant auth to keycloak

Creates a Keycloak authentication configuration for an existing 3scale tenant. The script is able to set up both admin portal and developer portal authentication.

Works using the standard 3scale Operator CRs where possible. Reads secret data and sso configs based on the organizationName specified in the tenant CR. All data is aasumed to be as a local file. This script can't pull info from OpenShift directly.

Example of linking of data:
A **tenant.yaml** defines 'example' as _organizationName_ -> script reads tenant-secret-**example**.yaml to load tenant access secrets and sso-config-**example**.yaml to read keycloak details.

Example tenant definition:
````
apiVersion: capabilities.3scale.net/v1alpha1
kind: Tenant
metadata:
  name: tenant-sample
spec:
  username: admin
  systemMasterUrl: https://master.example.com
  email: admin@example.com
  organizationName: example
  masterCredentialsRef:
    name: system-seed
  passwordCredentialsRef:
    name: ecorp-admin-secret
  tenantSecretRef:
    name: ecorp-tenant-secret
    namespace: operator-test
````

Example tenant secret for API access:
````
apiVersion: v1
kind: Secret
metadata:
  name: tenant-secret
type: Opaque
data:
  adminURL: https://my3scale-admin.3scale.net:443
  token: ""
````

Example sso config:
````
admin:
  enabled: true
  realm: "<realm-name>"
  auth-server-url: "https://<sso-host>/auth"
  ssl-required: "external"
  resource: "<client-name>"
  credentials:
    id: "<client-id>"
    secret: "<client-secret>"
  confidential-port": 0
dev:
  enabled: true
  realm: "<realm-name>"
  auth-server-url: "https://<sso-host>/auth"
  ssl-required: "external"
  resource: "<client-name>"
  credentials:
    id: "<client-id>"
    secret: "<client-secret>"
  confidential-port: 0
````

