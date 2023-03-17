import os
import openai

openai.api_key = os.environ.get("OPEN_AI_API_KEY")



# print(api_key)

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
pre_prompt = "Summarize the following text: ### \n"
txt = "A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei"

response_chat = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": pre_prompt + txt},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
    ]
)


response_davinci = openai.ChatCompletion.create(
  model="text-davinci-003",
  prompt= pre_prompt + txt,
  temperature=0.7,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=1
)

print(response_davinci['choices'])
print(response_chat['choices'])