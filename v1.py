import os
import openai

openai.api_key = "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"


def run_model(news_text):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="You're an experienced wall street analyst summarize this for me: \n " + news_text,
    temperature=0,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  return response


response = run_model("Japan considers green transition bonds issuance for next fiscal year")
print(response['choices'][0]['text'])