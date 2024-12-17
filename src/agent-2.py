# template for the scraping pipeline

import json
from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv
import os
load_dotenv()

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Find me all topics under subheading: `Patients`. Ensure to provide exhaustive list of all topics in this.",
    source="https://kipuhealth.zendesk.com/hc/en-us/categories/360003364352-Knowledge-Base",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()
print(json.dumps(result, indent=4))

