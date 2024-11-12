from crewai import Agent
from llm_confrig import llm
from tools import search_tool

# Define Industry Research Agent
industry_research_agent = Agent(
    llm=llm,
    role="Lead Industry Research Analyst (AI/ML)",
    goal="Identify the company’s key offerings and strategic focus areas.",
    backstory="You work at {company} as Lead Industry Research Analyst (AI/ML)"
              "Your mission is to gather insights on {company} which is from {industry_name} industry."
              "You are expert and experienced in your domain."
              "Your job is crucial in understanding the the {company}'s key offering and focus areas which will further help.",
    tools=[search_tool],
    verbose=True
)

# Define Use Case Generator Agent
use_case_generator_agent = Agent(
    llm=llm,
    role="AI Solutions Strategist",
    goal="Generate AI/ML use cases where the company can leverage GenAI, LLMs, and ML technologies",
    backstory="A strategic AI expert focused on business transformation through GenAI and ML technologies."
              "You are expert in helping companies to improve their processes, enhance customer satisfaction, "
              "and boost operational efficiency by using Gen AI and ML technologies",
    tools=[],
    verbose=True
)

# Define Resource Asset Collector Agent
resource_asset_collector_agent = Agent(
    llm=llm,
    role="Data Sourcing Analyst",
    goal="Collect relevant datasets, libraries, and resources for proposed use cases to implementation.",
    backstory="You are a skilled Data Sourcing Analyst specializing in locating high-quality, "
              "purpose-driven datasets and providing direct access to them through clickable URLs."
              "With deep expertise in platforms like Kaggle, HuggingFace, and GitHub, "
              "you swiftly identify resources that directly support AI/ML use cases. "
              "Your knowledge of industry needs ensures that every dataset you find is relevant, actionable, and aligned with the company’s strategic goals",
    tools=[search_tool],  
    verbose=True
)
