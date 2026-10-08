# Job Assistant AI

AI-powered assistant for job search and technical interview preparation.

## About the Project

Job Assistant AI is an educational project built with Python, LangChain, Google Gemini and Streamlit.

The application helps users prepare for the job search and technical interviews.

The application follows three main stages:

1. User profile generation
2. Job vacancy search and matching
3. Mock technical interview

The user provides information about their experience, skills and desired position. The application analyzes this information, searches for relevant job vacancies, allows the user to select a vacancy, and generates a technical mock interview based on the selected vacancy and the user's profile.

## Main Features

### 1. User Profile Generation

The first stage analyzes the user's free-text input and converts it into a structured professional profile.

The profile contains:

* desired position;
* professional experience;
* technical skills.

The profile is represented using a Pydantic model:

```text
UserProfile
├── skills
├── experience
└── desired_position
```

Example:

```text
User input:

I am a Python developer with 2 years of experience.
I have experience with FastAPI, SQL, Docker and PostgreSQL.
I am looking for a Python Backend Developer position.

↓

Career Profile Chain

↓

Structured User Profile:

Desired position: Python Backend Developer
Experience: 2 years
Skills: Python, FastAPI, SQL, Docker, PostgreSQL
```

### 2. Job Search

The second stage searches for current job vacancies based on the user's profile.

The application uses a custom search tool powered by Google Serper.

The Job Search Agent receives:

* desired position;
* technical skills;
* experience.

It uses the search tool to find relevant vacancies on the web.

The search results are then processed by a LangChain chain that structures the results using Pydantic.

Each vacancy contains:

* a job vacancy link;
* a short explanation of why the vacancy may be relevant to the user.

Example:

```text
User profile:

Position: Python Backend Developer
Skills: Python, FastAPI, SQL, Docker

↓

Job Search Agent

↓

Web search

↓

Relevant job vacancies
```

### 3. Mock Interview

The third stage generates a technical mock interview based on the user's profile and the selected vacancy.

The interview contains:

* 10 unique technical questions;
* 4 answer options for each question;
* the correct answer;
* an explanation of the correct answer.

The interview structure is represented using Pydantic models:

```text
MockInterview
└── questions
    ├── Question 1
    ├── Question 2
    ├── ...
    └── Question 10
```

Each question contains:

```text
Question
├── question
├── options
├── correct_answer
└── explanation
```

The user answers all 10 questions through the Streamlit interface.

After completing the interview, the user clicks the "Check Answer" button and receives the total number of:

* correct answers;
* incorrect answers.

Example:

```text
Mock Interview

Question 1
[Option 1]
[Option 2]
[Option 3]
[Option 4]

...

Question 10
[Option 1]
[Option 2]
[Option 3]
[Option 4]

↓

Check Answer

↓

Correct answers: 8
Incorrect answers: 2
```

## Application Architecture

```text
                         USER
                           |
                           v
                  +------------------+
                  |    Streamlit     |
                  |       UI         |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | User Profile     |
                  | Generation       |
                  | Chain            |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Job Search Agent |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Google Serper    |
                  | Web Search       |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Job Search       |
                  | Results          |
                  +--------+---------+
                           |
                           v
                  User selects vacancy
                           |
                           v
                  +------------------+
                  | Mock Interview    |
                  | Chain             |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | 10 Questions      |
                  | 4 Options Each    |
                  +--------+---------+
                           |
                           v
                  User submits answers
                           |
                           v
                  +------------------+
                  | Result            |
                  | Correct / Wrong   |
                  +------------------+
```

## Technologies

### Python

Main programming language used to build the application.

### Google Gemini

Generative AI model used for:

* user profile analysis;
* job search result processing;
* technical interview generation.

### LangChain

Framework used to build LLM chains, prompts, output parsers and AI agents.

The project uses LangChain components including:

* `PromptTemplate`;
* `PydanticOutputParser`;
* `create_agent`;
* custom tools.

### Pydantic

Used to define and validate structured data models.

The project uses Pydantic models for:

* `UserProfile`;
* `JobSearchResults`;
* `Question`;
* `MockInterview`.

### Streamlit

Used to build the interactive web interface.

### Google Serper

Used to search the web for current job vacancies.

### python-dotenv

Used to load API keys and other environment variables from the `.env` file.

## Project Structure

```text
Job-Interview-AI-Assistant/
│
├── Job_Assistant_AI.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── .venv/
```

`.env` and `.venv/` are local files and should not be committed to GitHub.

## Installation

Clone the repository:

```bash
git clone https://github.com/AntoninaStadnik/Job-Interview-AI-Assistant.git
```

Navigate to the project directory:

```bash
cd Job-Interview-AI-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory of the project.

Add the required API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

The application uses:

* `GEMINI_API_KEY` for Google Gemini;
* `SERPER_API_KEY` for Google Serper.

The `.env` file is excluded from Git using `.gitignore`.

Never publish API keys to GitHub.

## Running the Application

Start the Streamlit application:

```bash
streamlit run Job_Assistant_AI.py
```

After running the command, Streamlit will open the application in a browser.

## Project Workflow

The application follows this workflow:

```text
1. User enters information about their experience and skills
                         |
                         v
2. User Profile is generated
                         |
                         v
3. Job Search Agent searches for vacancies
                         |
                         v
4. Relevant vacancies are displayed
                         |
                         v
5. User selects a vacancy
                         |
                         v
6. Mock Interview is generated
                         |
                         v
7. 10 technical questions are displayed
                         |
                         v
8. User selects answers
                         |
                         v
9. Application checks the answers
                         |
                         v
10. Correct and incorrect answers are displayed
```

## Project Status

The project is currently under development.

### Completed

* Python project setup
* Virtual environment configuration
* Google Gemini API integration
* Google Serper API integration
* LangChain configuration
* Streamlit interface
* Structured user profile generation
* Job vacancy search
* Job vacancy matching
* Vacancy selection
* Mock interview generation
* Generation of 10 technical questions
* Four answer options for each question
* Correct answer validation
* Interview result calculation
* Pydantic structured output models
* Project documentation

### In Progress

* Detailed feedback for each interview question
* Interview score calculation
* Improved Streamlit UI
* Better vacancy filtering
* Improved prompt engineering
* Error handling

## Project Purpose

The project was created as an educational and examination project to demonstrate how generative AI can be integrated into a Python application.

The main learning objectives are:

* working with generative AI models;
* creating LangChain chains and agents;
* creating custom AI tools;
* working with structured LLM output;
* using Pydantic for data validation;
* integrating web search with an AI application;
* managing application state with Streamlit;
* building an interactive AI-powered web application.

## Future Improvements

Possible future improvements include:

* integration with dedicated job APIs;
* more advanced job matching;
* improved skill gap analysis;
* personalized interview difficulty;
* detailed feedback for each answer;
* interview score calculation;
* interview history;
* candidate progress tracking;
* persistent storage of user data;
* improved UI/UX;
* authentication and user accounts;
* automated CV analysis;
* CV generation and optimization.
