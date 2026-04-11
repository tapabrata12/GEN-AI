from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional
import json


class Output(BaseModel):
    """Extract a structured movie review."""
    title: str = Field(description="This is the title of the movie being reviewed and should be a string.")
    genre: List[str] = Field(description="This is the genre of the movie being reviewed and should be a list of strings.")
    cast: Optional[List[str]] = Field(description="This is the cast of the movie being reviewed and should be a list of strings.")
    sentiment: Optional[str] = Field(description="This is the sentiment of the movie review and should be a string.")
    score: Optional[float] = Field(description="This is the score of the movie review and should be a float.")
    summary: str = Field(description="This is a summary of the movie review and should be a string.")


def movie_json(review: str) -> json:  # type: ignore

    llm = ChatGroq(model='openai/gpt-oss-120b', temperature=0)

    parser = PydanticOutputParser(pydantic_object=Output)  # type: ignore

    prompt = ChatPromptTemplate.from_messages([  # type: ignore
        ('system', 'You are a movie analyzer that extracts structured information from movie paragraphs according to the following format: {output_format}'),
        ("human", "{user_review}")
    ])

    final_prompt = prompt.invoke({  # type: ignore
        'user_review': review,
        'output_format': parser.get_format_instructions()
    })

    response = llm.invoke(final_prompt)  # type: ignore

    output_json = json.loads(response.content)  # type: ignore

    return output_json