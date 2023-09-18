import openai
import os

OPENAI_API_KEY = ""

# Read .env contents
env_file = open("./.env", "r")
env_content = []
for line in env_file:
	env_content.append(line)
env_file.close()

# Plugin values for global variables
for line in env_content:
	if "OPENAI_API_KEY" in line:
		OPENAI_API_KEY = line.split("\"")[1]
		# print(OPENAI_API_KEY)

