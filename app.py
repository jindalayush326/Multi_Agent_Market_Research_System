import streamlit as st
import re
import sys
from crewai import Crew, Process
import os
from agents import (
    research_agent,
    use_case_generation_agent,
    resource_collection_agent,
    report_generation_agent,
)
from tasks import (
    research_analysis,
    use_case_analysis,
    dataset_collection,
    report_generation,
)

# Used to stream sys output on the streamlit frontend
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            self.color_index = (self.color_index + 1) % len(self.colors)
            cleaned_data = cleaned_data.replace(
                "Entering new CrewAgentExecutor chain",
                f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]",
            )

        # Apply colors to agent names
        if "Research Agent" in cleaned_data:
            cleaned_data = cleaned_data.replace("Research Agent", f":{self.colors[self.color_index]}[Research Agent]")
        if "Use Case Generation Agent" in cleaned_data:
            cleaned_data = cleaned_data.replace("Use Case Generation Agent", f":{self.colors[self.color_index]}[Use Case Generation Agent]")
        if "Resource Collection Agent" in cleaned_data:
            cleaned_data = cleaned_data.replace("Resource Collection Agent", f":{self.colors[self.color_index]}[Resource Collection Agent]")
        if "Report Generation Agent" in cleaned_data:
            cleaned_data = cleaned_data.replace("Report Generation Agent", f":{self.colors[self.color_index]}[Report Generation Agent]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []

# Streamlit UI
st.header("Market Research & Use Case Generation Agent")
st.subheader("Generate a Market Research & Use Case Analysis Report!", divider="rainbow", anchor=False)

# User input form
with st.form("form"):
    company = st.text_input("Enter the name of the Company", key="company")
    industry = st.selectbox("Select the Industry", ["Automotive", "Finance", "Retail", "Healthcare", "Manufacturing", "Steel Industry"])
    submitted = st.form_submit_button("Submit")

# Process the submission
if submitted:
    with st.status("🤖 **Agents at work...**", expanded=True, state="running") as status:
        with st.container(height=300):
            sys.stdout = StreamToContainer(st)

            # Defining the crew comprising of different agents
            crew = Crew(
                agents=[research_agent, use_case_generation_agent, resource_collection_agent, report_generation_agent],
                tasks=[research_analysis, use_case_analysis, dataset_collection, report_generation],
                process=Process.sequential,
                verbose=True
            )
            result = crew.kickoff(inputs={"company": company, "industry": industry})

        status.update(label="✅ Your Report is ready", state="complete", expanded=False)
    
    st.subheader("Market Research & Use Case Report is ready!", anchor=False, divider="rainbow")
    st.markdown(result)

    # Enable file download
    st.download_button(
        label="Download Report",
        data=result,  
        file_name=f"{company}_Market_Research_Report.txt",  
        mime="text/plain",  
    )
