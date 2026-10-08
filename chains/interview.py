from prompts.interview import prompt, parser3
from llm import llm


chain3 = prompt | llm | parser3