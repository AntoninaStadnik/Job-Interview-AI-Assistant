🤖 Job Assistant AI

AI-powered assistant for job search and technical interview preparation.

📌 About the Project

Job Assistant AI is an educational project that uses a generative AI model to help users prepare for the job search and technical interviews.

The application analyzes the user's skills and experience, searches for relevant job vacancies, compares the user's skills with job requirements, and provides a simulated technical interview.

The project is built with Python, LangChain, Google Gemini and Streamlit.

🎯 Main Features

The application consists of three specialized AI agents.

🔎 Agent 1 — Job Search Agent

The first agent helps the user find relevant job vacancies.

The user provides:

desired position;

technical skills;

experience.

The agent uses this information to search for suitable vacancies and returns relevant job opportunities.

Example:

User skills:
Python, FastAPI, SQL, Docker

Desired position:
Python Backend Developer

↓

Job Search Agent

↓

Relevant vacancies

📊 Agent 2 — Tech Lead Agent

The second agent acts as a Technical Lead.

It analyzes the requirements of a selected vacancy and compares them with the user's skills and experience.

The agent identifies:

skills that match the vacancy requirements;

missing skills;

skills that require improvement;

recommendations for preparation.

Example:

Job requirements:

Python
FastAPI
PostgreSQL
Docker
AWS

User skills:

Python
FastAPI
SQL
Docker

↓

Tech Lead Agent

↓

Strong matches:
Python
FastAPI
Docker

Missing skills:
PostgreSQL
AWS

Recommendations:
Practice PostgreSQL
Learn AWS fundamentals

🎤 Agent 3 — Mock Interview Agent

The third agent simulates a technical interview.

The agent generates technical questions based on:

the selected job position;

job requirements;

user's skills;

identified skill gaps.

The user answers the questions through the Streamlit interface.

The agent then analyzes the answer and provides feedback.

Example:

Interviewer:

What is the difference between
asyncio and threading in Python?

User:

[User's answer]

↓

AI evaluation

Score: 7/10

Strengths:
- Correct understanding of asynchronous execution

Needs improvement:
- Event loop
- I/O-bound operations

Recommended answer:
...

🏗️ Application Architecture
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │    Streamlit    │
                  │       UI        │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
       ┌───────────┐ ┌───────────┐ ┌──────────────┐
       │  Agent 1  │ │  Agent 2  │ │   Agent 3    │
       │Job Search │ │ Tech Lead │ │Mock Interview│
       └─────┬─────┘ └─────┬─────┘ └──────┬───────┘
             │             │              │
             ▼             ▼              ▼
          Vacancies    Skill Analysis   Questions
                        & Skill Gaps     & Feedback

🛠️ Technologies

Python — main programming language

Google Gemini — generative AI model

LangChain — framework for working with LLMs and AI agents

Pydantic — structured data validation

Streamlit — web interface

python-dotenv — environment variable management

📂 Project Structure
Job-Interview-AI-Assistant/
│
├── agents/
│   ├── job_agent.py
│   ├── tech_lead_agent.py
│   └── interview_agent.py
│
├── main.py
├── Job_Assistant_AI.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── .venv/


.env and .venv/ are local files and should not be committed to GitHub.

⚙️ Installation

Clone the repository:

git clone https://github.com/AntoninaStadnik/Job-Interview-AI-Assistant.git


Navigate to the project directory:

cd Job-Interview-AI-Assistant


Create a virtual environment:

python -m venv .venv


Activate the virtual environment on Windows:

.venv\Scripts\activate


Install the required dependencies:

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the root directory of the project.

Add your Google Gemini API key:

GOOGLE_API_KEY=your_api_key_here


The .env file is excluded from Git using .gitignore.

Never publish your API key on GitHub.

▶️ Running the Application

Start the Streamlit application:

streamlit run streamlit_app.py


After running the command, Streamlit will open the application in your browser.

🚧 Project Status

The project is currently under development.

Completed

 Python project setup

 Virtual environment configuration

 Google Gemini API connection

 LangChain configuration

 Streamlit interface setup

 Project documentation

In Progress

 Implement Job Search Agent

 Implement Tech Lead Agent

 Implement Mock Interview Agent

 Add job search functionality

 Add skill matching

 Add AI interview evaluation

 Improve Streamlit UI

🎓 Project Purpose

The project was created as an educational/examination project to demonstrate how generative AI can be integrated into a Python application.

The main focus is on:

working with generative AI models;

creating specialized AI agents;

processing structured data;

integrating AI into a web application;

building an interactive user interface with Streamlit.

🔮 Future Improvements

Possible future improvements include:

more advanced job search;

integration with external job APIs;

improved skill matching;

personalized interview questions;

interview history;

candidate progress tracking;

improved UI/UX;

persistent storage of user data.