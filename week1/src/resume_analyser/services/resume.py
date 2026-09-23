from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
import json


class Experience(BaseModel):
    model_config = ConfigDict(extra="forbid")

    company_name: Annotated[
        str | None,
        Field(description="Name of the company")
    ]

    position: Annotated[
        str | None,
        Field(description="Position held at the company")
    ]

    tenure: Annotated[
        int | None,
        Field(description="Number of years of experience")
    ]

    responsibilities: Annotated[
        list[str] | None,
        Field(description="List of responsibilities held during the experience")
    ]

    skills_used: Annotated[
        list[str] | None,
        Field(description="List of skills used during the experience")
    ]


class Resume(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: Annotated[
        str | None,
        Field(description="Full name of the candidate")
    ]

    email: Annotated[
        str | None,
        Field(description="Email address of the candidate")
    ]

    phone: Annotated[
        str | None,
        Field(description="Phone number of the candidate")
    ]

    summary: Annotated[
        str | None,
        Field(description="Summary or objective statement of the candidate")
    ]

    experiences: Annotated[
        list[Experience],
        Field(description="List of professional experiences")
    ]

    education: Annotated[
        list[str] | None,
        Field(description="List of educational qualifications")
    ]

    skills: Annotated[
        list[str] | None,
        Field(description="List of skills possessed by the candidate")
    ]


# print(json.dumps(Resume.model_json_schema(), indent=2))