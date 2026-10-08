from prompts.profile import prompt1, parser
from llm import llm


chain1 = prompt1 | llm | parser