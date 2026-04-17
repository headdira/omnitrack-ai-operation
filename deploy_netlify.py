import os
import requests
import zipfile
import io

# Config
NETLIFY_AUTH_TOKEN = os.getenv("NETLIFY_AUTH_TOKEN")
SITE_ID = os.getenv("NETLIFY_SITE_ID")

class NetlifyDeployer:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.base_url = "https://api.netlify.com/api/v1"

    def deploy(self, site_id, folder_path):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if not file.startswith(".") and not file.endswith(".py"):
                        z.write(os.path.join(root, file), arcname=file)
        buf.seek(0)
        url = f"{self.base_url}/sites/{site_id}/deploys"
        headers = {**self.headers, "Content-Type": "application/zip"}
        return requests.post(url, headers=headers, data=buf.read())

if __name__ == "__main__":
    # Logic to run...
    pass
