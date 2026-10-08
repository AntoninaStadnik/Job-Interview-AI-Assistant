
import streamlit as st

from langchain_core.messages import HumanMessage, ToolMessage

from chains.profile import chain1
from chains.jobs import chain2
from chains.interview import chain3
from agents.job_search import agent


st.title("Job Assistant AI")


user_text = st.text_input("Введіть інформацію про себе: досвід в роках, навички, бажана посада")


if "jobs" not in st.session_state:
    st.session_state.jobs = None

if "interview" not in st.session_state:
    st.session_state.interview = None

if "selected_job" not in st.session_state:
    st.session_state.selected_job = None

if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = 0

if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = 0

if "answer_checked" not in st.session_state:
    st.session_state.answer_checked = False


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


    if st.session_state.jobs is None:

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

        st.session_state.jobs = response_ai.jobs


    if st.session_state.interview is None:

        st.markdown("Вакансії які Вам підійдуть")

        selected_job = st.radio(
            "Оберіть вакансію для mock interview:",
            st.session_state.jobs,
            key="selected_job"
        )


if st.button("Почати mock interview згідно обраної вакансії"):

    st.session_state.correct_answers = 0
    st.session_state.wrong_answers = 0
    st.session_state.result_checked = False

    data3 = {
        "skills": response.skills,
        "experience": response.experience,
        "desired_position": response.desired_position,
        "selected_job": st.session_state.selected_job
    }

    st.session_state.interview = chain3.invoke(data3)

    st.rerun()


if st.session_state.interview is not None:

    interview = st.session_state.interview

    for index, question in enumerate(interview.questions):

        st.write(f"Питання: {question.question}")

        selected_option = st.radio(
            "Оберіть відповідь:",
            question.options,
            key=f"selected_option_{index + 1}"
        )

        st.write("Ви обрали:")
        st.write(selected_option)


    if st.button("Перевірити відповідь"):

        correct_answers = 0
        wrong_answers = 0

        for index, question in enumerate(interview.questions):

            selected_option = st.session_state[f"selected_option_{index + 1}"]

            selected_index = question.options.index(selected_option)

            if selected_index == question.correct_answer:
                correct_answers += 1
            else:
                wrong_answers += 1

        st.write(f"Правильних відповідей: {correct_answers}")
        st.write(f"Неправильних відповідей: {wrong_answers}")

