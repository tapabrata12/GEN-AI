from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated

class Details(BaseModel):
    model_config = ConfigDict(extra = "forbid")
    name: Annotated[str | None, Field(description="Keep the candidate name here")]
    matched_skills: Annotated[list | None, Field(description="Keep all the matched skills in the field from the parsed resume")]
    missing_skills: Annotated[list, Field(description="Keep all the missing skills in that field")]
    short_suggession: Annotated[str, Field(description="Write in your words why this resume got selected or rejected")]
    
class MatchResult(BaseModel):
    model_config = ConfigDict(extra = "forbid")
    total_percentage: Annotated[int, Field(..., ge= 0, le= 100, description= "This field will contain matched percentage of the given resume")]
    reasion: Annotated[Details, Field(..., description="In this field LLM have to put the extracted name, matched skills, and missing skills, suggessions")]