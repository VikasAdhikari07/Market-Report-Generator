import streamlit as st
import time
from crewai import Crew, Process
from tasks import industry_research_task, use_case_generation_task, resource_collection_task
from agents import industry_research_agent, use_case_generator_agent, resource_asset_collector_agent

GROQ_API_KEY="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"



# Assemble the Crew with the defined agents and tasks
research_and_use_case_crew = Crew(
    agents=[industry_research_agent, use_case_generator_agent, resource_asset_collector_agent],
    tasks=[industry_research_task, use_case_generation_task, resource_collection_task],
    process=Process.sequential  # Tasks are executed in order, passing data to the next
)



# Set up the Streamlit app title
st.title("AI Use Case Generator")

# Input fields for Company Name and Industry
company_name = st.text_input("Enter Company Name")
industry = st.text_input("Enter Industry")

# Button to submit and process the inputs
if st.button("Generate Reports"):
    if company_name and industry:
        with st.spinner("Gathering information..."):
            result = research_and_use_case_crew.kickoff(inputs={"company": company_name, "industry_name":industry})
            time.sleep(2)
        st.write(f"Market Research and AI Use Case for {company_name} in the {industry} industry")
        
        
        st.header("Market Report")
        with open("Market_report.md", "r") as file:
            st.markdown(file.read())    
            st.download_button(
                label="Download Market Report",
                data=file,
                file_name="Market_report.md",
                mime="text/markdown"
            )       
            
        st.header("AI Use Cases Report")
        with open("use_cases_report.md", "r") as file:
            st.markdown(file.read())
            st.download_button(
                label="Download Use Cases Report",
                data=file,
                file_name="use_cases_report.md",
                mime="text/markdown"
            )       

        st.header("Resources")
        with open("resource_assets_report.md", "r") as file:
            st.markdown(file.read())
            st.download_button(
                label="Download Resource fo Use Cases",
                data=file,
                file_name="resource_assets_report.md",
                mime="text/markdown"
            )       


    else:
        st.warning("Please enter both the Company Name and Industry.")

# Run with `streamlit run your_script_name.py`
