#!/usr/bin/env python3

import pkg.common
import pkg.auth
import base64
import sys

# Set 3scale tenant authentication to use Keycloak

def print_help():
    print('Usage:')
    print('\tWith defaults:')
    print('\t\tpython3 set-tenant-auth-to-keycloak.py')
    print('\tWith parameters:')
    print('\t\tpython3 set-tenant-auth-to-keycloak.py <tenant-config-file>')
    sys.exit(0)

def main():
    if(len(sys.argv) == 2 and sys.argv[1] == '-h'):
        print_help()

    if(len(sys.argv) >= 2):
        tenant = pkg.common.read_yaml_file(file=sys.argv[1])
    else:
        tenant = pkg.common.read_yaml_file(file='tenant.yaml')

    tenant_name = str(tenant['metadata']['name'])
    print('Tenant name: '+tenant_name)
    tenant_creds = pkg.common.read_yaml_file(file='tenant-secret-' + tenant_name + '.yaml')
    print('Token: '+str(tenant_creds['stringData']['token']))
    tenant_token = str(base64.b64decode(str(tenant_creds['stringData']['token'])).decode('UTF-8')).strip()
    print('Tenant token: '+tenant_token)
    tenant_base_url = 'https://' + tenant_name + str(tenant['spec']['systemMasterUrl'])[14:] + '/admin/api'
    sso_config = pkg.common.read_yaml_file(file='sso-config-' + tenant_name + '.yaml')

    pkg.auth.set_admin_portal_authentication_as_keycloak(tenant_token=tenant_token, 
                                                         tenant_base_url=tenant_base_url, 
                                                         client_id=str(sso_config['admin']['credentials']['id']), 
                                                         client_secret=str(sso_config['admin']['credentials']['secret']), 
                                                         site_url=str(sso_config['admin']['auth-server-url']) + '/realms/' + str(sso_config['admin']['realm']), 
                                                         tenant_name=tenant_name)
    pkg.auth.set_developer_portal_authentication_as_keycloak(tenant_token=tenant_token, 
                                                         tenant_base_url=tenant_base_url, 
                                                         client_id=str(sso_config['dev']['credentials']['id']), 
                                                         client_secret=str(sso_config['dev']['credentials']['secret']), 
                                                         site_url=str(sso_config['dev']['auth-server-url']) + '/realms/' + str(sso_config['dev']['realm']), 
                                                         tenant_name=tenant_name)


main()