import os
import json
import requests
from agno.agent import Agent
from agno.models.google import Gemini

# 1. CORE BRAIN: Agno Agent for Business Decission
brain_agent = Agent(
    name="OmniBrain",
    model=Gemini(id="gemini-2.5-flash"),
    instructions=[
        "You are the Head of Operations for OmniTrack AI.",
        "Your task is to: 1. Find a product, 2. Optimize the funel, 3. Trigger Deploy.",
        "Use the Netlify API to deploy the project."
    ]
)

# 2. REAL NETLIFY INTEGRATION (Using Token from MCP Config)
NETLIFY_TOKEN = "nfp_X1nu8NcU57u5E2RQT7PAYUYEq6DV6Bvzfa2a"
SITE_NAME = "omnitrack-ai-live"

class NetlifyAutomation:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {NETLIFY_TOKEN}"}
        
    def deploy_operation(self):
        print("[*] Launching Netlify Deployment Pipeline...")
        # Step 1: Check if site exists
        url_sites = "https://api.netlify.com/api/v1/sites"
        sites = requests.get(url_sites, headers=self.headers).json()
        
        target_site = next((s for s in sites if s['name'] == SITE_NAME), None)
        
        if not target_site:
            print("[+] Creating new site on Netlify...")
            target_site = requests.post(url_sites, headers=self.headers, json={"name": SITE_NAME}).json()
            
        site_id = target_site['id']
        print(f"[+] Operational Site ID: {site_id}")
        
        return f"Pipeline Linked: https://{SITE_NAME}.netlify.app"

if __name__ == "__main__":
    automation = NetlifyAutomation()
    print(automation.deploy_operation())
