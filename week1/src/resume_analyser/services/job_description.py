from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from groq import Groq
from dotenv import load_dotenv
import json
load_dotenv()

class JobDescription(BaseModel):
    model_config = ConfigDict(extra="forbid")
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
            response_format={
                "type": "json_schema",
                "json_schema":{
                    "name": "JobDescription",
                    "strict": True,
                    "schema": JobDescription.model_json_schema()
                }
            }
        )

        return response.choices[0].message.content

    
    def get_structured_description(self)-> json:
        structured_response = self.__generate_answer_from_llm()

        try:
            # Convert JSON string -> Pydantic object
            return JobDescription.model_validate_json(structured_response)

        except Exception as e:
            raise ValueError(
                "Failed to extract structured information from the job description."
            ) from e


# if __name__ == "__main__":
#     try:

#         x = """
#         Job Description: Software Development Engineer 1 (SDE-1)Location: Remote / HybridExperience: 0–1 YearsEmployment Type: Full-TimeJob OverviewWe are looking for a passionate and driven Software Development Engineer 1 (SDE-1) to join our growing engineering team. In this role, you will design, build, test, and maintain high-quality software features under the guidance of senior engineers. You will turn business requirements into clean, scalable, and reliable code, accelerating your technical growth in a fast-paced environment.Key ResponsibilitiesCoding & Development: Write clean, maintainable, and efficient code using modern programming languages (e.g., Java, Python, or JavaScript).Feature Implementation: Implement new features and fix bugs across the application stack based on detailed technical specifications.Testing & Debugging: Write unit tests and participate in code troubleshooting to ensure software reliability and high performance.Collaboration: Work closely with product managers, QA testers, and senior developers in an agile environment to meet project milestones.Continuous Learning: Actively absorb feedback, learn new frameworks, and adhere to best coding practices and version control workflows (Git/GitLab).Required Qualifications & SkillsEducation: Bachelor’s degree in Computer Science, Information Technology, Engineering, or a related field.Technical Foundation: Strong understanding of Data Structures, Algorithms (DSA), and Object-Oriented Programming (OOP) concepts.Programming Proficiency: Hands-on familiarity with at least one core language such as Java, Python, C++, or JavaScript.Tools & Workflow: Basic knowledge of version control systems like Git or GitHub/GitLab.Soft Skills: Eagerness to learn, strong logical problem-solving abilities, and effective communication skills to work in a team.Preferred / Bonus SkillsExperience with backend frameworks (e.g., Spring Boot, Node.js) or frontend frameworks (e.g., Angular, React).Familiarity with basic database management (SQL / NoSQL) and cloud services (AWS or Azure).If you want to customize this further, let me know:What tech stack (e.g., Java, Python, MERN) do you want to target?Is this for a startup or an enterprise company? 
#         """
#         a = JobDescriptionConverter(x)
#         print(a.get_structured_description())
#     except FileNotFoundError as e:
#         print(f"Error: {e}")