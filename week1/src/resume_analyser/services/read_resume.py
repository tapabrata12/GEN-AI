from pathlib import Path
from pypdf import PdfReader
import docx
from resume import Resume
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

class ReadResume:
    def __init__(self):
        # 1. Define and check if the directory exists
        self.document_dir = Path(__file__).resolve().parents[1] / "document"
        
        if not self.document_dir.exists():
            raise FileNotFoundError(f"The directory {self.document_dir} does not exist.")

        # 2. Gather all PDF and DOCX files
        self.files = sorted(self.document_dir.glob("*.pdf")) + sorted(self.document_dir.glob("*.docx"))

        # 3. Check if any matching files were found
        if not self.files:
            raise FileNotFoundError(f"No PDF or DOCX files found in {self.document_dir}")

        # Pick the first available file
        self.file_path = self.files[0]

    def __check_document(self)-> str:
        print(f"Checking document at: {self.file_path}")

        if not self.file_path.is_file():
            raise FileNotFoundError(f"File {self.file_path} does not exist.")

        # 4. Read the file header (magic numbers) to safely confirm the type
        with open(self.file_path, 'rb') as f:
            header = f.read(4)

            # %PDF
            if header == b'%PDF':
                return "Confirmed PDF"
            
            # DOCX files are essentially ZIP archives. Their magic bytes start with PK\x03\x04
            elif header.startswith(b'PK\x03\x04'):
                return "Confirmed DOCX"
            
            return "Unknown file format"
    
    def __extract_text_from_pdf(self)-> str:
        reader = PdfReader(self.file_path)
        full_document_text = []

        for page in reader.pages:

            text = page.extract_text()
            if text:
                full_document_text.append(text)

        return "\n" .join(full_document_text)

    def __extract_text_from_docx(self)-> str:
        doc = docx.Document(self.file_path)
        full_document_text = []

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                full_document_text.append(paragraph.text)

        return "\n" .join(full_document_text)

    
    def __get_structured_JD_by_llm(self, document_text: str)-> dict:
        client = Groq()
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages= [
                {"role": "system", "content": "You are a helpful assistant that extracts structured information from given Resume String."},
                {"role": "user", "content": f"Extract the following information from the Resume String: Format the output as a JSON object.\n\nResume:\n{document_text}"}
            ],

            response_format={
                "type": "json_schema",
                "json_schema": {
                "name": "resume",
                "strict": True,
                "schema": Resume.model_json_schema()
                }
            },
            temperature=0,
            max_tokens=2000
        )
        
        return response.choices[0].message.content
        
    def parse_document(self):
        is_document_type = self.__check_document()

        if is_document_type == "Confirmed PDF":
            PDF_text = self.__extract_text_from_pdf()
            structured_JD_response = self.__get_structured_JD_by_llm(PDF_text)
            validated_response = Resume.model_validate(json.loads(structured_JD_response))
            return json.dumps(validated_response.model_dump(), indent=2)
        
        DOCS_text = self.__extract_text_from_docx()
        structured_JD_response = self.__get_structured_JD_by_llm(DOCS_text)
        validated_response = Resume.model_validate(json.loads(structured_JD_response))
        return validated_response.model_dump_json(indent=2)



# Example execution
if __name__ == "__main__":
    try:
        a = ReadResume()
        print(a.parse_document())
    except FileNotFoundError as e:
        print(f"Error: {e}")
