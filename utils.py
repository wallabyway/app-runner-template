import requests, time, base64, json, os
from dotenv import load_dotenv

# Get APS credentials and bucket name from environment variables
load_dotenv()
APS_CLIENT_ID = os.getenv('APS_CLIENT_ID')
APS_SECRET_ID = os.getenv('APS_SECRET_ID')
BUCKET_KEY = os.getenv('BUCKET_KEY')
APS_BASE_URL = "https://developer.api.autodesk.com"
SCOPE = ["data:read", "data:write"]

def get_token():
    r = requests.post(f"{APS_BASE_URL}/authentication/v2/token", data={
        "grant_type": "client_credentials",
        "client_id": APS_CLIENT_ID,
        "client_secret": APS_SECRET_ID,
        "scope": " ".join(SCOPE)
    })
    return r.json()["access_token"]

def upload_file(token, filename, filedata):
    url = f"{APS_BASE_URL}/oss/v2/buckets/{BUCKET_KEY}/objects/{filename}/signeds3upload"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        signed_url = r.json()["urls"][0]
        upload_key = r.json()["uploadKey"]
        requests.put(signed_url, data=filedata)
        complete_url = f"{APS_BASE_URL}/oss/v2/buckets/{BUCKET_KEY}/objects/batchcompleteupload"
        complete_payload = {"requests": [{"objectKey": filename, "uploadKey": upload_key}]}
        requests.post(complete_url, headers=headers, json=complete_payload)
        return filename
    else:
        raise Exception(f"Failed to get signed URL: {r.text}")

def translate(token, urn):
    print(f"Starting translation for URN: {urn}")
    url = f"{APS_BASE_URL}/modelderivative/v2/designdata/job"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", "x-ads-force": "true"}
    _urn = f"urn:adsk.objects:os.object:{BUCKET_KEY}/{urn}"
    urn_b64 = base64.b64encode(_urn.encode()).decode()
    data = {"input": {"urn": urn_b64}, "output": {"formats": [{"type": "svf", "views": ["2d", "3d"]}]}}
    r = requests.post(url, headers=headers, json=data)
    print(f"Response from translation job: {r.status_code} - {r.text}")
    return urn_b64

def status(token, urn_b64):
    url = f"{APS_BASE_URL}/modelderivative/v2/designdata/{urn_b64}/manifest"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    return r.json()

def list_bucket(token):
    url = f"{APS_BASE_URL}/oss/v2/buckets/{BUCKET_KEY}/objects"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    return r.json()["items"] 
