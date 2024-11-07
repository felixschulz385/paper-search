import xml.etree.ElementTree as ET
import tiktoken
import os


xml_file_path = '../data/Task2_3_combined/combined.xml'


if os.path.exists(xml_file_path):
    print("The path is valid and the file exists.")
    absolute_path = os.path.abspath(xml_file_path)
    print("Absolute path:", absolute_path)
else:
    print("The path is invalid or the file does not exist.")


tree = ET.parse(xml_file_path)
root = tree.getroot()

titles = root.findall('.//atl')  #list of element objects, in particular atl, a.k.a, title objects
abstracts = root.findall('.//ab')

character_length_of_titles = 0
character_length_of_abstracts = 0

total = 0
input_text = ""
for title in titles:
    text = title.text
    input_text += text

for abstract in abstracts:
    text = abstract.text
    input_text += text

prompt = f""" 
            Based on the title and abstract of the following research paper, evaluate its relevance to the topic "linking environmental changes to health" with the following three criteria: 
            First, the paper should explicitly establish a connection between specific environmental changes (such as pollution, climate change, deforestation, etc.) and specific health outcomes (such as respiratory diseases, mental health, etc.). 
            Secondly, you should prefer studies that demonstrate or hypothesize a direct impact or correlation between the environmental change and health. 
            Thirdly, avoid papers that only discuss environmental changes or health outcomes in isolation. Both elements should be central to the study. 

            Your task is to rate the paper on a scale from 0 (no relevance) to 10 (highly relevant), focusing on papers with a clear, direct link between environmental changes and health outcomes as highly relevant. Keep the three criteria in mind while providing the rating. Provide only a single number (from 0 to 10) without any additional explanation. 
"""
prompt_all = prompt*5514

total = input_text + prompt_all

print("Total character length: " + str(len(total)))

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
tokens = encoding.encode(total)
token_count = len(tokens)

print(f"Token count: {token_count}")
print(f"Token cost in dollar for gpt3.5: {token_count * (0.0015/1000)}")
