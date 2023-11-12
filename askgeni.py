import openai

openai.api_key = 'YOUR_API_KEY'

# Define the parameters
relationship = "great-grandmother"
given_name = "Mary"
surname = "Johnson"
birth_date = "1880"
birth_place = "County Cork, Ireland"

# Construct the prompt
prompt = f"I've hit a dead end with my {relationship}, {given_name} {surname} born in {birth_date} in {birth_place}. What should be my next steps?"

# Create the OpenAI schema
schema = {
    "model": "davinci",
    "prompt": prompt,
    "temperature": 0.7,
    "max_tokens": 150,
    "top_p": 1,
    "frequency_penalty": 0.5,
    "presence_penalty": 0.5
}

# Make the API request
response = openai.Completion.create(**schema)
print(response.choices[0].text.strip())
