import openai
import xml.etree.ElementTree as ET

xml_file_path = '../data/source-papers.xml'
tree = ET.parse(xml_file_path)
root = tree.getroot()

title = root.find('.//atl').text #find returns first instance of title, abstract
abstract = root.find('.//ab').text

# environmental effects on health

prompt = f"""
Based on the title and abstract of the following research paper, evaluate its relevance to the topic 'linking environmental changes to health' on a scale from 0 (no relevance) to 10 (highly relevant). Please provide only a single number (from 0 to 10) as your response without any additional explanation.
Title: {title}
Abstract: {abstract}
"""


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a research assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=10,  # output tokens cap
    temperature=0.2,  # low temp values means more deterministic
    n=2, # generates two responses to the prompt
    stop=["\n"] # stop generating at new line
)

print("Response from OpenAI API:")
print(response['choices'][0]['message']['content'])
