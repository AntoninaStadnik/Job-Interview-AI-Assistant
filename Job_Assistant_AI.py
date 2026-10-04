import dotenv
import os

import langchain
import streamlit as st
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    BaseMessage,
    trim_messages,
)

dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

st.title("Job Assistant AI")


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=api_key
)


class UserProfile(BaseModel):
    skills: list[str]
    experience: str
    desired_position: str


parser = PydanticOutputParser(
    pydantic_object=UserProfile
)

instructions = parser.get_format_instructions()


prompt1 = PromptTemplate.from_template("""
    Ти -- Career Profile Agent.

    Твоя задача: проаналізувати інформацію про користувача
    та сформувати його професійний профіль.
    Не шукай вакансії.
    Не проводь interview.

    ### ВХІДНІ ДАНІ ###
    {user_text}

    ### ФОРМАТ ВІДПОВІДІ ###
    {format_instructions}
""",
    partial_variables={
        "format_instructions": instructions
    }
)

chain1 = prompt1 | llm | parser


user_text = st.text_input("Введіть інформацію про себе: досвід в роках, навички, бажана посада")


if user_text:
    response = chain1.invoke({
        "user_text": user_text
    })

    st.markdown("Ваш профіль")

    st.write(f"Бажана позиція: {response.desired_position}")
    st.write(f"Досвід: {response.experience}")

    st.write("Навички:")
    for skill in response.skills:
        st.write(f"- {skill}")


google_serper = GoogleSerperAPIWrapper(
    type="search",
)

@tool
def search_vacancies(query: str) -> str:
    """
    Searches the web for current job vacancies based on the user's query.
    Returns information about relevant job postings.
    """
    result = google_serper.results(query)

    return result


agent = create_agent(
    model=llm,
    tools=[search_vacancies],
    system_prompt="""
    Ти — Job Search Agent.

    Твоя задача — знаходити актуальні вакансії,
    які відповідають професійному профілю користувача.

    Ти маєш використовувати search_vacancies,
    щоб отримувати актуальні вакансії з інтернету.

    Не вигадуй вакансії.
    Не вигадуй URL.
    Використовуй тільки інформацію,
    яку отримав через пошук.

    При пошуку враховуй:
    - бажану позицію
    - skills
    - experience
    """
)


class JobSearchResults(BaseModel):
    jobs: list[str] = Field(description="список знайдених вакансій")


parser2 = PydanticOutputParser(pydantic_object=JobSearchResults)

instructions2 = parser2.get_format_instructions()

prompt = PromptTemplate.from_template("""
    Ти -- досвідчений Job Search Agent.
    Твоя задача сформувати список підходящих вакансій виходячи з навичок користувача.

    ###ІНСТРУКЦІЇ###
    1. Має бути посилання на вакансію
    2. Короткий опис - 2 речення,  чому ця вакансія може підійти користувачу

    ###ВХІДНІ ДАНІ###
    Навички: {skills}
    Досвід: {experience}
    Бажана позиція: {desired_position}

    ### РЕЗУЛЬТАТИ ПОШУКУ ###
    {search_results}  

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}

""",
    partial_variables={"format_instructions": instructions2}
    )

chain2 = prompt | llm | parser2

if user_text:
    response = chain1.invoke({
        "user_text": user_text
    })

    job_search_prompt = f"""
    Знайди актуальні вакансії для цього користувача:

    Бажана позиція: {response.desired_position}
    Досвід: {response.experience}
    Навички: {", ".join(response.skills)}

    Використай search_vacancies для пошуку.
    Не вигадуй вакансії та URL.
    """

    response2 = agent.invoke({
        "messages": [
            HumanMessage(content=job_search_prompt)
        ]
    })

    search_results = ""

    for message in response2["messages"]:
        if isinstance(message, ToolMessage):
            search_results = message.content

    data2 = {
        "skills": response.skills,
        "experience": response.experience,
        "desired_position": response.desired_position,
        "search_results": search_results
    }

    response_ai = chain2.invoke(data2)

    st.markdown("Вакансії які Вам підійдуть")

    for job in response_ai.jobs:
        st.markdown(f"- {job}")

#add 2 agents - Analyst agent and Interview agent






