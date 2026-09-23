from pydantic import BaseModel, Field
from typing import Annotated
from groq import Groq
from dotenv import load_dotenv
import json
load_dotenv()

class JobDescription(BaseModel):
    role: Annotated[str, Field(..., description="Role or position being advertised")]
    required_skills: Annotated[list[str], Field(..., description="List of skills required for the job")]
    preferred_skills: Annotated[list[str], Field(..., description="List of preferred skills for the job")]
    min_experience: Annotated[int, Field(..., description="Minimum years of experience required for the job")]
    educational_requirements: Annotated[list[str], Field(..., description="List of educational qualifications required for the job")]
    responsibilities: Annotated[list[str], Field(..., description="List of responsibilities associated with the job")]

class JobDescriptionConverter:

    def __init__(self, job_description: str):
        self.job_description: str = job_description
    
    def __generate_answer_from_llm(self):

        client = Groq()

        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that extracts structured information from job descriptions."
                },
                {
                    "role": "user",
                    "content": f"Extract the following information from the job description: role, required skills, preferred skills, minimum experience, educational requirements, and responsibilities. Format the output as a JSON object.\n\nJob Description:\n{self.job_description}"
                }
            ],
            temperature=0,
            max_tokens=100,
            response_format={
                "type": "json_schema",
                "json_schema":{
                    "name": "JobDescription",
                    "strict": True,
                    "schema": JobDescription.model_json_schema()
                }
            }
        )

        return response

    
    def get_structured_description(self)-> json:
        response = self.__generate_answer_from_llm()
        structured_response = response.choices[0].message.content
        if JobDescription.model_validate_json(structured_response):
            return json.dumps(structured_response)
        else:
            raise ValueError("Failed to extract structured information from the job description.")