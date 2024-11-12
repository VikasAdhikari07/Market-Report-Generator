from crewai import Task
from agents import industry_research_agent, use_case_generator_agent, resource_asset_collector_agent
from tools import search_tool

# Define Industry Research Task
industry_research_task = Task(
    description=(
        "Identify the company’s key offerings and strategic focus areas (e.g., operations, supply chain, customer experience, etc.)."
        "A vision and product information on the industry should be fine as well. "
        "Use web tools to scrape information on the {industry_name} industry’s segment, identify relevant trends, "
        "and analyze reports from top consulting firms like McKinsey, Deloitte, and Nexocode. "
        "Provide a competitor analysis and an overview of industry standards."
    ),
    expected_output=(
        "A Markdown file which contain indepth research of the company with detailed description of following topics with a proper heading:\n"
        "- About {industry_name} Industry (contain major development in the industry) \n"
        "- Company's key offerings  \n"
        "- strategic focus areas (e.g., operations, supply chain, customer experience, etc.) \n"
        "- Company's Vision and Product information \n"
        "- Competitor analysis and their development in AI"
    ),
    tools=[search_tool],
    agent=industry_research_agent,
    output_file="Market_report.md"
)


# Define Use Case Generation Task
use_case_generation_task = Task(
    description=(
        "Based on the industry insights provided, analyze potential applications for AI/ML and GenAI "
        "within the {company}’s industry. Propose use cases that improve operational efficiency, enhance customer experience, "
        "or streamline workflows. Describe each use case, including expected impact and suggested technologies."
        "These use cases should improve their processes, enhance customer satisfaction, and boost operational efficiency"
        
    ),
    expected_output=(
        "A markdown file which giving the overview of the use cases of AI in industry and then listing AI/ML use cases as heading and with subheading as:\n"
        "- Use case descriptions\n"
        "- AI Application\n"
        "- Cross-Functional Benefit\n"
    ),
    agent=use_case_generator_agent,
    output_file="use_cases_report.md"
)

# Define Resource Collection Task
resource_collection_task = Task(
    description=(
        "This task is super important to for the further development of AI in the company"
        "Coolect datasets, tools, and libraries from sources like Kaggle, HuggingFace, and GitHub "
        "that support the all proposed AI/ML use cases. Provide clickable links to resources, "
        "organized by use case or technology focus."
    ),
    expected_output=(
        "A markdown file listing:\n"
        "- Use case\n"
        "- Description of use case\n"
        "- Identify and provide clickable links to datasets, libraries, and resources for each use case from Kaggle, HuggingFace, and GitHub\n"
    ),
    agent=resource_asset_collector_agent,
    output_file="resource_assets_report.md"
)

