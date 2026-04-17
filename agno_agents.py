from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.website import WebsiteTools
import os
import json
import requests

# 1. Product Agent using Gemini 2.5 Flash
product_agent = Agent(
    name="OmniSourcing-v2.5",
    model=Gemini(id="gemini-2.5-flash"), 
    instructions=[
        "Search for 'GPS Tracker for Bike/Motorcycle' on AliExpress.",
        "Select the top-rated item with > 5000 orders.",
        "Extract: Title, Price, Key Features, and Image URL.",
        "Save the result to 'product_config.json'."
    ],
    tools=[WebsiteTools()],
    show_tool_calls=True
)
