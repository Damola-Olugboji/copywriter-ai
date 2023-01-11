import click
from models import v1


@click.group()
def main():
    pass


@main.command()
@click.argument("choice")
def intro(choice):
    if choice == "text":
        text = input("enter the text: ")
    if choice == "file":
        filename = input("enter the filename: ")
        with open(filename, "r") as file:
            text = file.read()

    prompt = "You're an experienced copy writer, write a eye catching introduction to a blog post with the prompt provided below: \n"
    raw = v1.prompt_model(prompt, text)
    response = raw["choices"][0]["text"]

    print(response)


@main.command()
def intros():
    prompt = "You're an experienced copywriter and content creator write an introduction to the prompt: \n"
    filename = input("enter filename: ")
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    for line in lines():
        response = v1.prompt_model(prompt, line)


# investment banking analyst explanation
@main.command()
@click.argument("choice")
def ab(choice):
    if choice == "text":
        text = input("enter the text: ")
    if choice == "file":
        filename = input("enter the filename: ")
        with open(filename, "r") as file:
            text = file.read()

    prompt = "You're an experienced wall street investment banking analyst, and you've won multiple awards for you're advice. explain the underlying reasons to the provided text below: \n"
    raw = v1.prompt_model(prompt, text)
    response = raw["choices"][0]["text"]

    print(response)


if __name__ == "__main__":
    main()
