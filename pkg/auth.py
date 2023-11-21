# file -- pkg.auth.py --

import pkg.common

def set_admin_portal_authentication_as_keycloak(tenant_token, tenant_base_url, client_id, client_secret, site_url, tenant_name):
    values = { 'access_token': tenant_token,
               'name': tenant_name+'-admin-keycloak',
               'kind': 'keycloak',
               'client_id': client_id,
               'client_secret': client_secret,
               'site': site_url,
               'skip_ssl_certificate_verification': 'true',
               'published': 'true' }
    # list existing providers
    get_params =  { 'access_token': tenant_token }
    provider_list = pkg.common.get_json(url=tenant_base_url+'/account/authentication_providers.json', params=get_params)
    existing_id = -1
    for provider in provider_list['authentication_providers']:
        if provider['authentication_provider']['name'] == tenant_name+'-admin-keycloak':
            existing_id = provider['authentication_provider']['id']

    if existing_id > 0:
        print('Updating admin portal authentication')
        values['id'] = existing_id
        del values['name']
        result = pkg.common.put_json(url=tenant_base_url + '/account/authentication_providers/' + str(existing_id) +'.json', payload=values)
    else:
        print('Setting admin portal authentication to keycloak')
        result = pkg.common.post_json(url=tenant_base_url+'/account/authentication_providers.json', payload=values)

    print('Admin portal authentication set to keycloak')

def set_developer_portal_authentication_as_keycloak(tenant_token, tenant_base_url, client_id, client_secret, site_url, tenant_name):
    values = { 'access_token': tenant_token,
               'name': tenant_name+'-dev-keycloak',
               'kind': 'keycloak',
               'client_id': client_id,
               'client_secret': client_secret,
               'site': site_url,
               'trust_email': 'true',
               'skip_ssl_certificate_verification': 'true',
               'published': 'true' }
    # list existing providers
    get_params =  { 'access_token': tenant_token }
    provider_list = pkg.common.get_json(url=tenant_base_url+'/authentication_providers.json', params=get_params)
    existing_id = -1
    for provider in provider_list['authentication_providers']:
        if provider['authentication_provider']['name'] == tenant_name+'-dev-keycloak':
            existing_id = provider['authentication_provider']['id']

    if existing_id > 0:
        print('Updating developer portal authentication')
        values['id'] = existing_id
        del values['name']
        result = pkg.common.put_json(url=tenant_base_url + '/authentication_providers/' + str(existing_id) +'.json', payload=values)
    else:
        print('Setting developer portal authentication to keycloak')
        result = pkg.common.post_json(url=tenant_base_url+'/authentication_providers.json', payload=values)

    print('Developer portal authentication set to keycloak')
