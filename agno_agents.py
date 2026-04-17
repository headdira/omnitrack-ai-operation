from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.website import WebsiteTools
import json
import os

# 1. Product & Sourcing Agent (Agno)
product_agent = Agent(
    name="OmniSourcing",
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "Search for the best GPS trackers for bikes on AliExpress/Alibaba.",
        "Filter for rating > 4.7 and high sales volume.",
        "Return the product data in JSON format."
    ],
    tools=[WebsiteTools()],
    show_tool_calls=True
)

# 2. Marketing & LP Architect Agent
marketing_agent = Agent(
    name="OmniGrowth",
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "Create high-conversion copy for the selected product.",
        "Define 15 variations of the main headline focusing on security.",
        "Suggest lifestyle image prompts for Midjourney."
    ]
)

deployment_agent = Agent(
    name="OmniDeploy",
    instructions=["Take the production folder and deploy it to Netlify using the provided tools."],
    show_tool_calls=True
)

if __name__ == "__main__":
    print("--- OmniSourcing ---")
    # product_agent.print_response("Find the top selling bike GPS tracker on AliExpress today.")
