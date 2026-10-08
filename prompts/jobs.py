from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from schemas import JobSearchResults


parser2 = PydanticOutputParser(pydantic_object=JobSearchResults)

instructions2 = parser2.get_format_instructions()


prompt = PromptTemplate.from_template("""
    Ти -- досвідчений Job Search Agent.
    Твоя задача сформувати список підходящих вакансій
    виходячи з навичок користувача.

    ###ІНСТРУКЦІЇ###

    1. Має бути посилання на вакансію
    2. Короткий опис - 2 речення,
       чому ця вакансія може підійти користувачу

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