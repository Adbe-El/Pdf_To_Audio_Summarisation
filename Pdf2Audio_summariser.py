from gtts import gTTS
from PyPDF2 import PdfReader
import os
import openai

# function to call openai key

def askai(prompt):
    API_KEY = "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"
    openai.api_key = API_KEY
    model = "text-davinci-003"

    response = openai.Completion.create(
        prompt = prompt,
        model = model,
        temperature = 0.1,
    )

    for result in response.choices:
        return result.text
    

# Extract text from PDF
pdf_name = 'The_word.pdf'
reader = PdfReader(pdf_name)
page = reader.pages[0] 
text_pdf = page.extract_text()

text_pdf= " ".join(text_pdf.splitlines())


# Generate summary using chatGPT

summary_pdf = askai("Generate the summary - " + text_pdf)

print(summary_pdf)


# Convert summary to audio

audio = gTTS(text=summary_pdf, lang='en', tld= 'us', slow=False)

audio.save("audio_summary.mp3")