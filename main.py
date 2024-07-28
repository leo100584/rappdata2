import datetime
import time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def showTime():
    print("Hello wolrd from Azure functions!")
    print("Current date and time in Norway: ")
    now = datetime.datetime.now()
    # Print the current date and time in a specific format
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def main(req: func.HttpRequest) -> func.HttpResponse:
    connection_string = "din_azure_storage_connection_string"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client("din_container", "din_blob")

    data = "Ditt innhold her"  # Erstatt dette med innholdet i Excel-dokumentet ditt

    blob_client.upload_blob(data)
    showTime()

if __name__ == '__main__':
  showTime()
