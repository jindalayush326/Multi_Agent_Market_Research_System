from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool

load_dotenv()
import asyncio

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
# Defining the base llm model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    temperature=0.5,
    verbose=True
)

# Function to format datasets into the desired structure
def format_datasets(datasets):
    formatted_output = ""
    for dataset in datasets:
        title = dataset.get("title", "Unknown Title")
        description = dataset.get("description", "No description available.")
        links = dataset.get("links", [])
        formatted_output += f"{title}\t{description}\t" + "\n".join(links) + "\n\n"
    return formatted_output

# 1. Research Agent (Market Research)
research_agent = Agent(
    role="Research Agent",
    goal="Conduct research to gather market insights and understand industry trends for {company} in {industry}.",
    verbose=True,
    memory=True,
    backstory=("You are a Research Agent tasked with gathering data about {company} and the {industry} sector. "
               "Your goal is to identify market trends, competitors, and the strategic focus areas of the company."),
    tools=[tool],  
    llm=llm,
    allow_delegation=True
)

# 2. Use Case Generation Agent (AI Use Case Analyst)
use_case_generation_agent = Agent(
    role="AI Use Case Analyst",
    goal="Generate relevant AI/GenAI and ML use cases for {company} in the {industry} industry.",
    verbose=True,
    memory=True,
    backstory=("You are an AI Use Case Analyst responsible for proposing AI, ML, and GenAI use cases for {company} in {industry}. "
               "Your task is to analyze industry trends and propose AI-driven solutions to improve operations, supply chain, and customer experience."),
    tools=[tool],  
    llm=llm,
    allow_delegation=True
)

# 3. Resource Collection Agent (Dataset Finder)
resource_collection_agent = Agent(
    role="Resource Collection Agent",
    goal="Find relevant datasets and resources for implementing the proposed AI/ML use cases for {company}.",
    verbose=True,
    memory=True,
    backstory=("You are a Dataset Finder responsible for identifying and providing datasets that can be used "
               "to implement the proposed AI/ML solutions for {company}. You search on platforms like Kaggle, "
               "HuggingFace, and GitHub."),
    tools=[tool],
    llm=llm,  
    allow_delegation=True
)

# 4. Report Generation Agent (Reporting Agent)
report_generation_agent = Agent(
    role="Report Generation Agent",
    goal="Create a comprehensive report combining research findings and use cases generated for {company} in {industry}.",
    verbose=True,
    memory=True,
    backstory=("You are a Reporting Agent for {company} responsible for compiling all the findings from the Research Agent, "
               "Use Case Generation Agent, and Dataset Finder into a detailed report. This report will support strategic decision-making."),
    tools=[tool],  
    llm=llm,
    allow_delegation=False
)
