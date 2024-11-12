import os
from crewai_tools import SerperDevTool

# Set API Key for Serper tool
os.environ["SERPER_API_KEY"] = "caae2111065ae3ffb28208d6809e5bd2eec4e7ba"
search_tool = SerperDevTool()