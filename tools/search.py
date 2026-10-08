from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool


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