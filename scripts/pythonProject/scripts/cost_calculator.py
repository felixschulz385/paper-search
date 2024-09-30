import xml.etree.ElementTree as ET
import tiktoken

xml_file_path = '../data/source-papers.xml'

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

prompt = "Based on the title and abstract of the following research paper, evaluate its relevance to the topic 'linking environmental changes to health' on a scale from 0 (no relevance) to 10 (highly relevant). Please provide only a single number (from 0 to 10) as your response without any additional explanation."
prompt_all = prompt*2933

total = input_text + prompt_all

print("Total character length: " + str(len(total)))

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
tokens = encoding.encode(total)
token_count = len(tokens)

print(f"Token count: {token_count}")
print(f"Token cost in dollar for gpt3.5: {token_count * (0.0015/1000)}")
