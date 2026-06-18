from gemini_client import model

response = model.generate_content(
    "Summarize: Python Developer Internship at Levroxen. Apply now."
)

print(response.text)