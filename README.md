# Market Research & Use Case Generation Agent

## Description

The Market Research & Use Case Generation Agent is an AI-powered tool designed to assist users in performing comprehensive financial and market analyses of any company or industry segment. The tool employs multiple specialized AI agents, including a Research Agent, AI Use Case Generation Agent, Dataset Finder, and Report Generation Agent, to gather, analyze, and compile data from publicly available sources. The output is a detailed and actionable report that can help decision-makers better understand market trends, potential AI use cases, and relevant datasets to enhance operations and customer experience.

Key technologies used in this project include CrewAI, LangChain, Streamlit, Python, and Google Gemini Flash 1.5 LLM.

## Demo of the app
A demo showcasing the Market Research & Use Case Generation Agent in action can be viewed at the link below:

## Installation

To run this project, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone [https://github.com/jindalayush326/Multi_Agent_Market_Research_System.git]
   ```

2. Navigate to the project directory.
   ```bash
   cd Multi_Agent_Market_Research_System
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

Set up API keys:

4. Create a .env file in the root directory and add your API keys for Google Gemini Flash 1.5 and SerperAPI as follows:
   GOOGLE_API_KEY=<your-google-api-key>
   SERPER_API_KEY=<your-serper-api-key>

## Usage

1. Ensure you have installed all dependencies as instructed above.

2. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

3. Access the app through your browser at http://localhost:8501

4. Interact with the app:

   Enter the name of the company and the relevant industry (e.g., Automotive, Finance, Retail).
   The app will generate a detailed financial and market research report, including AI use cases and relevant datasets.

## Key Features
1. Market Research: The Research Agent gathers relevant market trends, competitor information, and strategic insights.
2. AI Use Case Generation: The AI Use Case Analyst proposes relevant AI, ML, and GenAI solutions tailored to the company's industry.
3. Dataset Finder: The Resource Collection Agent identifies and formats publicly available datasets to support AI use case implementation.
4. Report Generation: The Reporting Agent compiles all the research, use cases, and datasets into a cohesive, actionable report.

## Technologies Used
1. CrewAI: A framework for building and managing AI agents.
2. LangChain: An API that allows agents to interact with language models for deeper insights.
3. Google Gemini Flash 1.5 LLM: A powerful large language model used to gather and analyze data.
4. Streamlit: A framework to build and run the web-based front-end of the app.
5. SerperAPI: Used for advanced web search and data extraction.
6. Python: The programming language used to build the core logic.

## Credits

- [CrewAI](https://www.crewai.com/)
- [Langchain](https://www.langchain.com/)
- [Google Gemini Flash 1.5](https://deepmind.google/technologies/gemini/flash/)
- [Streamlit](https://streamlit.io/)
- [SerperAPI](https://serper.dev/)
- [Python](https://www.python.org/)

## License

This project is licensed under the [MIT License](LICENSE).
```
