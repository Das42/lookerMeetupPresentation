import swagger_client as looker
import yaml

def apiConnect(config):

	with open(config, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)

	client_id = cfg['connection']['id']
	client_secret = cfg['connection']['secret']
	endpoint = cfg['connection']['endpoint']

	unauthenticated_client = looker.ApiClient(endpoint)
	unauthenticated_authApi = looker.ApiAuthApi(unauthenticated_client)

	token = unauthenticated_authApi.login(client_id = client_id, client_secret = client_secret)
	client = looker.ApiClient(endpoint, 'Authorization', 'token ' + token.access_token)
	return(client)

