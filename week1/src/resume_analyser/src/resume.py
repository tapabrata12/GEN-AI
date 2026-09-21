from pydantic import BaseModel, Field
from typing import Annotated

class Experience(BaseModel):
    company_name: Annotated[str, Field(..., description="Name of the company")] = None
    position: Annotated[str, Field(..., description="Position held at the company")] = None
    tenure: Annotated[int, Field(..., description="Number of years of experience")] = 0
    responsibilities: Annotated[list[str], Field(..., description="List of responsibilities held during the experience")] = None
    skills_used: Annotated[list[str], Field(..., description="List of skills used during the experience")] = None

class Resume(BaseModel):
    name: Annotated[str, Field(..., description="Full name of the candidate")] = None
    email: Annotated[str, Field(..., description="Email address of the candidate")] = None
    phone: Annotated[str, Field(..., description="Phone number of the candidate")] = None
    summary: Annotated[str, Field(..., description="Summary or objective statement of the candidate")] = None
    experiences: Annotated[list[Experience], Field(..., description="List of professional experiences")]
    education: Annotated[list[str], Field(..., description="List of educational qualifications")] = None
    skills: Annotated[list[str], Field(..., description="List of skills possessed by the candidate")] = None
