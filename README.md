### **Market Research & AI Use Case Generator**

This project provides a multi-agent system for conducting market research, generating AI use cases, and collecting relevant resources for a given company or industry. The application is built with Crew AI for multi-agent management and Streamlit for a user-friendly UI.

---

### **Table of Contents**
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Architecture Overview](#architecture-overview)
- [License](#license)

---

### **Features**

- **Industry Analysis**: Collects insights on market trends and competitor information for a specified company or industry.
- **AI Use Case Generation**: Recommends AI/ML-based use cases that align with the company's industry and operational focus.
- **Resource Collection**: Provides relevant datasets and resources from platforms like Kaggle and HuggingFace for implementing the AI use cases.

---

### **Project Structure**

```
project-root/
│
├── main.py                  # Main application entry point with Streamlit UI
├── llm_config.py            # LLM configurations and API key management
├── tools.py                 # Tool configurations for web search (e.g., Serper)
├── agent.py                 # Agent definitions (industry research, use case generation, resource collection)
├── tasks.py                 # Task definitions aligned with agents
└── README.md                # Project documentation
```

---

### **Setup & Installation**

#### **Requirements**

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- Crew AI, Serper API, and any other listed requirements in `requirements.txt`

#### **Installation Steps**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/market-research-ai.git
   cd market-research-ai
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory for API keys.
   - Example:
     ```plaintext
     SERPER_API_KEY=your_serper_api_key
     LLM_API_KEY=your_llm_api_key
     ```

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```

---

### **Usage**

1. **Start the Application**: Open the app in your browser (default at `http://localhost:8501`) after running `main.py`.

2. **Enter Company and Industry Information**: Input the company name and industry in the fields provided.

3. **View Results**: The app will display:
   - **Market Report**: Industry insights and competitor analysis.
   - **Use Case Analysis**: AI/ML-based use cases tailored to the company.
   - **Resource Links**: Clickable links to relevant datasets and resources for each use case.

---

### **Architecture Overview**

The project is divided into components that handle specific tasks in a sequential flow. Below is a brief outline of each component:

1. **LLM Configuration** (`llm_config.py`): Manages LLM settings and API keys, ensuring secure handling of credentials.

2. **Tool Configuration** (`tools.py`): Sets up tools, including Serper for Google Search, used in industry research.

3. **Agents** (`agent.py`): Defines agents that perform tasks, including:
   - **Industry Research Agent**: Collects data on market and competitor trends.
   - **Use Case Generator Agent**: Recommends AI use cases aligned with industry insights.
   - **Resource Collector Agent**: Collects relevant datasets for AI use cases.

4. **Tasks** (`tasks.py`): Outlines tasks for each agent to ensure structured data flow.

5. **Main Application** (`main.py`): Orchestrates the multi-agent process and UI display in Streamlit.

---

### **License**

This project is licensed under the MIT License. Please refer to `LICENSE` for details.

---
