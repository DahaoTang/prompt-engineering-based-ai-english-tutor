###############
### IMPORTS ###
###############
import openai
import os
# import warnings
# from urllib3.exceptions import NotOpenSSLWarning
# warnings.simplefilter('ignore', NotOpenSSLWarning)


##############
### SET UP ###
##############
# Read .env contents
env_file = open("./.env", "r")
env_content = []
for line in env_file:
	env_content.append(line)
env_file.close()

# Plugin values for global variables
for line in env_content:
	if "OPENAI_API_KEY" in line:
		openai_api_key = line.split("\"")[1]
		openai.api_key = openai_api_key # set uo the global variable openai.api_key

# Customize get_completion function
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


#############
### TESTS ###
#############
def test_1():

	return


####################
### MAIN PROGRAM ###
####################
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
# response = get_completion(prompt)
# print(response)
print(prompt)