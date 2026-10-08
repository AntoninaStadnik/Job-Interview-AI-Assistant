from prompts.jobs import prompt, parser2
from llm import llm


chain2 = prompt | llm | parser2