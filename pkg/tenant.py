# file -- pkg.tenant.py --

import pkg.common
import base64

# Creates a new tenant into 3scale
def create_tenant(master_token, master_base_url, org_name, username, email, password):
    values = { 'access_token': master_token,
               'org_name': org_name,
               'username': username,
               'email': email,
               'password': password }
    # Create tenant with values from above
    response = pkg.common.post_json(master_base_url+'/master/api/providers.json', data=values)

    # read tenant account id and account mangement access token value
    account_id = response['signup']['account']['id']
    account_management_token = response['signup']['access_token']['value']

    # get url to read users for the tenant
    users_url = response['signup']['account']['links'][0]['href']

    users_params = { 'access_token': master_token }
    users_response = pkg.common.get_json(users_url+'.json', params=users_params)

    # read list of users for the tenant
    user_id = users_response['users'][0]['user']['id']

    # enable admin user account
    activate_account_user(master_token, master_base_url, account_id, user_id)

    print('Created tenant '+org_name+' with admin token: '+account_management_token)
    return { 'token': account_management_token, 'admin_domain': response['account']['admin_domain'] }

# Activates a given user in an account
def activate_account_user(master_token, master_base_url, account_id, user_id):
    values = { 'access_token': master_token }
    response = pkg.common.put_json(master_base_url+'/admin/api/accounts/'+str(account_id)+'/users/'+str(user_id)+'/activate.json', data=values)

def write_tenant_secret(tenant_details, tenant_name):
    # TBD
    print('ASDF!')