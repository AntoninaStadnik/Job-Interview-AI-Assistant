from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    skills: list[str]
    experience: str
    desired_position: str


class JobSearchResults(BaseModel):
    jobs: list[str] = Field(description="список знайдених вакансій")


class Question(BaseModel):
    question: str = Field(description="технічне питання для проходження співбесіди")
    options: list[str] = Field(description="варіанти відповіді на технічне питання")
    correct_answer: int = Field(description="правильна відповідь, індекс правильної відповіді у списку options: 0, 1, 2 або 3")
    explanation: str = Field(description="пояснення правильної відповіді")


class MockInterview(BaseModel):
    questions: list[Question] = Field(description="10 технічних питань")