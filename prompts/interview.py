from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from schemas import MockInterview


parser3 = PydanticOutputParser(pydantic_object=MockInterview)

instructions3 = parser3.get_format_instructions()


prompt = PromptTemplate.from_template("""
    Ти -- досвідчений Interview Agent.

    Твоя задача сформувати рівно 10 унікальних технічних питань для проведення мок-співбесіди виходячи з інформації про досвід, навички користувача
    і обраної користувачем вакансії.

    ###ІНСТРУКЦІЇ###
    1. Згенеруй рівно 10 унікальних технічних питань.
    2. Кожне питання має рівно 4 варіанти відповіді.
    3. Для кожного питання вкажи індекс правильної відповіді: 0, 1, 2 або 3.
    4. Для кожного питання додай пояснення правильної відповіді.
    5. Питання повинні відповідати вакансії та рівню кандидата.

    ###ВХІДНІ ДАНІ###
    Навички: {skills}
    Досвід: {experience}
    Бажана позиція: {desired_position}

    ### ОБРАНА ВАКАНСІЯ ###
    {selected_job}

    ###ФОРМАТ ВІДПОВІДІ###
    {format_instructions}

""",
    partial_variables={
        "format_instructions": instructions3
    }
)