from crewai import Task
from tools import tool
from agents import research_agent, use_case_generation_agent, resource_collection_agent, report_generation_agent

# 1. Research Analysis Task
research_analysis = Task(
    description="Conduct research to gather insights about {company} in the {industry} sector.",
    expected_output="A comprehensive market research report detailing industry trends, competitor analysis, and strategic focus areas.",
    tools=[tool],  
    agent=research_agent,
)

# 2. AI Use Case Generation Task
use_case_analysis = Task(
    description="Generate AI/ML and GenAI use cases for {company} based on research findings.",
    expected_output="A set of AI use cases that align with {company}'s goals to improve processes, customer satisfaction, and operational efficiency.",
    tools=[tool],  
    agent=use_case_generation_agent,
)

# 3. Resource Collection (Dataset Search) Task
dataset_collection = Task(
    description="Search for relevant datasets for the proposed AI/ML use cases from platforms like Kaggle, HuggingFace, and GitHub.",
    expected_output="A structured list of relevant datasets, including titles, descriptions, and links to publicly available resources.",
    tools=[tool],
    agent=resource_collection_agent,
)


# 4. Report Writing Task
report_generation = Task(
    description="Compile the research, use cases, and dataset findings into a detailed report.",
    expected_output="A detailed report 4-5 pages containing market research, AI use cases, and datasets, formatted for decision-making purposes.",
    tools=[tool],  
    agent=report_generation_agent,
    async_execution=False,  
)
