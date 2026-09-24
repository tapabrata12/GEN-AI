from groq import Groq
from dotenv import load_dotenv
import json
from pprint import pprint

try:
    from .services.match_result import MatchResult
    from .services.job_description import JobDescriptionConverter
    from .services.read_resume import ReadResume
except ImportError:
    from services.match_result import MatchResult
    from services.job_description import JobDescriptionConverter
    from services.read_resume import ReadResume

load_dotenv()


class ATS:
    def __init__(self, job_description: str):

        self.job_description: str = job_description
    
    def __calculate_score(self, user_resume: str, job_description: str):
        client = Groq()
        response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "system",
            "content": "You are a expert HR in a company. Your work is to evaluate (Give score, listout matched and unmatched skills, and explain reasions why this got selected or rejected) upcomming resume Json data from the applicants and give them proper score out of 100 according to the given Job description json data and applicant's Resume json data",
        },
        {"role": "user", "content": f"Evaluate score and give suggession wheather this particulaer resume: {str(user_resume)} will be shortlisted or not on the basis of this job description: {str(job_description)}"},
        ],
        response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "MatchResult",
            "strict": True,
            "schema": MatchResult.model_json_schema()
            }})
        
        response_content = response.choices[0].message.content
        if not response_content:
            raise ValueError("The scoring model returned an empty response.")

        validated_response = MatchResult.model_validate_json(response_content)
        return json.dumps(validated_response.model_dump(), indent=2)

    
    def get_score(self):

        try:

        # Getting structured JD

            job_description_object = JobDescriptionConverter(self.job_description)
            description = job_description_object.get_structured_description()

        # Get resume:
            resume_obj = ReadResume()
            resume = resume_obj.parse_document()

        # Get Score:
            score_json = self.__calculate_score(user_resume=resume, job_description=description)

            return score_json
        
        except Exception as e:
            raise RuntimeError("Failed to analyse the resume.") from e



if __name__ == "__main__":
    x = """Job Description: Software Development Engineer 1 (SDE-1)Location: Remote / HybridExperience: 0–1 YearsEmployment Type: Full-TimeJob OverviewWe are looking for a passionate and driven Software Development Engineer 1 (SDE-1) to join our growing engineering team. In this role, you will design, build, test, and maintain high-quality software features under the guidance of senior engineers. You will turn business requirements into clean, scalable, and reliable code, accelerating your technical growth in a fast-paced environment.Key ResponsibilitiesCoding & Development: Write clean, maintainable, and efficient code using modern programming languages (e.g., Java, Python, or JavaScript).Feature Implementation: Implement new features and fix bugs across the application stack based on detailed technical specifications.Testing & Debugging: Write unit tests and participate in code troubleshooting to ensure software reliability and high performance.Collaboration: Work closely with product managers, QA testers, and senior developers in an agile environment to meet project milestones.Continuous Learning: Actively absorb feedback, learn new frameworks, and adhere to best coding practices and version control workflows (Git/GitLab).Required Qualifications & SkillsEducation: Bachelor’s degree in Computer Science, Information Technology, Engineering, or a related field.Technical Foundation: Strong understanding of Data Structures, Algorithms (DSA), and Object-Oriented Programming (OOP) concepts.Programming Proficiency: Hands-on familiarity with at least one core language such as Java, Python, C++, or JavaScript.Tools & Workflow: Basic knowledge of version control systems like Git or GitHub/GitLab.Soft Skills: Eagerness to learn, strong logical problem-solving abilities, and effective communication skills to work in a team.Preferred / Bonus SkillsExperience with backend frameworks (e.g., Spring Boot, Node.js) or frontend frameworks (e.g., Angular, React).Familiarity with basic database management (SQL / NoSQL) and cloud services (AWS or Azure)."""
    result_obj = ATS(job_description=x)
    pprint(result_obj.get_score())