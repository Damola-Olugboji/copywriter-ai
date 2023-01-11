from lib2to3.pgen2.token import OP
import os
import openai
from keys import OPEN_AI_API_KEY

openai.api_key = OPEN_AI_API_KEY


def prompt_model(
    prompt,
    text,
    temperature=0.8,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}: \n " + text,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response['choices'][0]['text']


def free_model(
    prompt,
    temperature=0.8,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}: \n ",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response["choices"][0]["text"]
