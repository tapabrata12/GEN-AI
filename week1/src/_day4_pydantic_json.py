from pydantic import BaseModel, Field
from typing import Optional, Annotated
from dotenv import load_dotenv
from groq import Groq
import json
from pprint import pprint
load_dotenv()
client = Groq()

class Ticket(BaseModel):
    name: Optional[Annotated[str, Field(None, description="This field will contain user name if given")]]
    location: Optional[Annotated[str, Field(None, description= "This field will contain the actual information about the location of the user")]]
    query: Annotated[str, Field(..., description= "This field will contain the actual underline problem statement user wants to solve")]
    phone: Annotated[int, Field(..., description= "This field will contain the actual phone number of the user")]


response = client.chat.completions.create(
    model= "openai/gpt-oss-20b",
    messages= [{"role": "system", "content": "You are a helpful assistant that translates user queries into structured JSON format."}, {"role": "user", "content": "I need help with my account, I can't log in. My name is John Doe, I'm located in New York, and my phone number is 1234567890."}], 
    max_tokens=500,
    response_format= {
        "type": "json_schema",
        "json_schema": {
            "name": "Ticket",
            "schema": Ticket.model_json_schema(),
        }
    })

raw_result = json.loads(response.choices[0].message.content or "{}") 
result = Ticket.validate(raw_result)

pprint(result)