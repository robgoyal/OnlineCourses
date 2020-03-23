import termcolor
import pyfiglet
import requests

from random import choice


def welcome_msg():
    """None -> str

    Return a welcome message for the Dad Joke 300 app.
    """

    msg = "Dad Joke 3000"
    f = pyfiglet.figlet_format(msg)
    return termcolor.colored(f, color="magenta")


def request_topic():
    """None -> str

    Request input for a joke topic and return topic.
    """

    topic = input("Let me tell you a joke! Give me a topic: ")
    return topic


def request_joke(topic):
    """request_joke(str)

    (str) -> requests.Response

    Return a response with joke data
    """
    url = "https://icanhazdadjoke.com/search"
    headers = {"Accept": "application/json"}
    query = {"term": topic}

    r = requests.get(url, params=query, headers=headers)

    return r.json()


def joke(topic):
    data = request_joke(topic)

    num_jokes = int(data["total_jokes"])

    if num_jokes == 0:
        joke_resp = f"Sorry, I don't have any jokes about {topic}! Please try again"
    elif num_jokes == 1:
        joke_resp = f"I've got one joke about {topic}. Here it is:\n{data['results'][0]['joke']}"
    else:
        joke_resp = f"I've got {num_jokes} jokes about {topic}. Here's one:\n{choice(data['results'])['joke']}"

    return joke_resp


if __name__ == "__main__":
    print(welcome_msg())
    topic = request_topic()
    print(joke(topic))
