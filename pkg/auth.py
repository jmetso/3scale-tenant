# file -- pkg.auth.py --

import pkg.common

def set_admin_portal_authentication_as_keycloak(tenant_token, tenant_base_url, client_id, client_secret, site_url, tenant_name):
    values = { 'access_token': tenant_token,
               'name': tenant_name+'-admin-keycloak',
               'kind': 'keycloak',
               'client_id': client_id,
               'client_secret': client_secret,
               'site': site_url,
               'skip_ssl_certificate_validation': 'true',
               'published': 'true' }
    result = pkg.common.post_json(tenant_base_url+'/account/authentication_providers.json', payload=values)
    print('Admin portal authentication set to keycloak')

def set_developer_portal_authentication_as_keycloak(tenant_token, tenant_base_url, client_id, client_secret, site_url, tenant_name):
    values = { 'access_token': tenant_token,
               'name': tenant_name+'-dev-keycloak',
               'kind': 'keycloak',
               'client_id': client_id,
               'client_secret': client_secret,
               'site': site_url,
               'trust_email': 'true',
               'skip_ssl_certificate_validation': 'true',
               'published': 'true' }
    result = pkg.common.post_json(tenant_base_url+'/authentication_providers.json', payload=values)
    print('Developer portal authentication set to keycloak')
