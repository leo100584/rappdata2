import requests
from msal import ConfidentialClientApplication

def get_access_token(tenant_id, client_id, client_secret):
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = ConfidentialClientApplication(client_id, client_secret, authority)
    result = app.acquire_token_for_client(["https://graph.microsoft.com/.default"])
    return result['access_token']

def upload_to_sharepoint(file_path, site_id, folder, file_name, token):
    graph_endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive/root:/{folder}/{file_name}:/content"
    headers = {'Authorization': 'Bearer ' + token}
    with open(file_path, 'rb') as f:
        file_content = f.read()

    response = requests.put(graph_endpoint, headers=headers, data=file_content)
    return response.status_code

def main(req: func.HttpRequest) -> func.HttpResponse:
    tenant_id = "din_tenant_id"
    client_id = "din_client_id"
    client_secret = "din_client_secret"
    site_id = "din_site_id"
    folder = "din_folder"
    file_name = "din_file_name"
    file_path = "din_file_path"

    token = get_access_token(tenant_id, client_id, client_secret)
    status_code = upload_to_sharepoint(file_path, site_id, folder, file_name, token)

    return func.HttpResponse(f"Filopplastingen returnerte statuskoden {status_code}")
  
