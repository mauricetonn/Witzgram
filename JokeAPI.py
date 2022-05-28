from re import sub
from nbformat import read
import requests
import json

from sqlalchemy import false, true 

# Declaring Variables for getting and submitting Jokes

get_URL = URL = 'https://v2.jokeapi.dev/joke/'
submit_URL = 'https://v2.jokeapi.dev/submit?dry-run' # Use for Testing
# submit_URL = 'https://v2.jokeapi.dev/submit        # Use for real Application

def req(category = "Any", format = "json", black_list = "sexist,nsfw", type = "single", amount = "1" ):
    """
    Function to generate HTTP Request

    Args:
        category (str): Sets the joke-category. Avaiable Categories: "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas". Defaults to "Any".
        format (str, optional): Sets the response-format.Available formats: "json", "xml", "yaml", "txt". Defaults to "json".
        black_list (str, optional): Sets black-listed flags. Has to be a single String. Available flags: "nsfw", "religious", "political", "racist", "sexist", "explicit". Defaults to "sexist,nsfw".
        type (str, optional): Sets the type of the joke. Available types: "single", "twopart". Defaults to "single".
        amount (str, optional): Sets the Amount of Jokes in the Response JSON. Available amounts: "1"..."10" Defaults to "1".

    Returns:
        str: Request URL

    Tests:
        1) URL = req() should return 'https://v2.jokeapi.dev/joke/Any?format=json&blacklistFlags=nsfw,sexist&type=single&lang=de&amount=1'
        2) 2) URL = req("Programming", "json", "sexist", "single", "1") should return 'https://v2.jokeapi.dev/joke/Programming?format=json&blacklistFlags=sexist&type=single&lang=de&amount=1'
    """
    # 'https://v2.jokeapi.dev/joke/Any?format=json&blacklistFlags=nsfw,sexist&type=single&lang=de&amount=1'
    full_req = URL + category + "?" + "format=" + format + "&" + "blacklistFlags=" + black_list + "&" + "type=" + type + "&lang=de&" + "amount=" + amount 
    return full_req

def Joke(response):
    """
    Converts two part jokes to single jokes

    Args:
        response (json/dict): Response from GET-Request

    Returns:
        str: combined joke
    Test:
        1) lets
        2) see
    """
    if response["type"] == "twopart":
        setup = response["setup"]
        delivery = response["delivery"]
        joke = setup + "\n" + delivery
    elif response["type"] == "single":
        joke = response["joke"]
    return joke

def get_joke(category = "Any"):
    """
    Function for getting a Joke from a Category.

    Args:
        category (str): Sets the joke-category. Avaiable Categories: "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas". Defaults to "Any".
    
    Returns:
        str: Ready Joke
        str: Category (In Case "Any" was chosen)
    Test:
        1) joke, category = get_joke(category="Programming") should return a random Joke and the Category "Programming"
        2) joke, category = get_joke() should return a random Joke from a random Category
    """
    res = requests.get(req(category=category))
    res_json = json.loads(res.text)

    joke = Joke(res_json)
    category = res_json["category"]
    print(joke, category)

    return joke, category

joke, category = get_joke()
print(joke)
print(category)




def payload(category, joke, language, nsfw=True, religious= False, political= True,racist= False,sexist= False,explicit= False):
    """
    Generate Payload for POST-Request

    Args:
        category (str): category (str): Sets the joke-category. Avaiable Categories: "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas". Defaults to "Any".
        joke (str): Joke Text
        language (str): Joke Language. Available Languages: "cs", "de", "en", "es", "fr", "pt"
        Blacklist Params: 
        nsfw (bool, optional): Not Safe for Work Jokes. Defaults to True.
        religious (bool, optional): Religious Jokes. Defaults to False.
        political (bool, optional): Political Jokes. Defaults to True.
        racist (bool, optional): Racist Jokes. Defaults to False.
        sexist (bool, optional): Sexist Jokes. Defaults to False.
        explicit (bool, optional): Explicit Jokes. Defaults to False.

    Returns:
        json: Returns JSON-Object for Payload
    """
    data = {
    "formatVersion": 3,
    "category": category,
    "type": "single",
    "joke": joke,
    "flags": {
        "nsfw": nsfw,
        "religious": religious,
        "political": political,
        "racist": racist,
        "sexist": sexist,
        "explicit": explicit
    },
    "lang": language
    }
    print(data)
    ready_data = json.dumps(data)
    print(ready_data)
    return ready_data


def submit_joke(category, joke, language,  nsfw=True, religious= False, political= True,racist= False,sexist= False,explicit= False):
    """
    Submits Joke to JokeAPI

    Args:
        category (str): category (str): Sets the joke-category. Avaiable Categories: "Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas". Defaults to "Any".
        joke (str): Joke Text
        language (str): Joke Language. Available Languages: "cs", "de", "en", "es", "fr", "pt"
        Blacklist Params: 
        nsfw (bool, optional): Not Safe for Work Jokes. Defaults to True.
        religious (bool, optional): Religious Jokes. Defaults to False.
        political (bool, optional): Political Jokes. Defaults to True.
        racist (bool, optional): Racist Jokes. Defaults to False.
        sexist (bool, optional): Sexist Jokes. Defaults to False.
        explicit (bool, optional): Explicit Jokes. Defaults to False.
    Returns:
        requests.models.Response: Response from the POST Request
    """
    data = payload(category, joke, language,  nsfw=True, religious= False, political= True,racist= False,sexist= False,explicit= False)
    response = requests.post(url = submit_URL, data = data)
    return response

response = submit_joke("Programming", "Wie viele Programmierer braucht man, um eine Gluehbirne zu wechseln? Keinen einzigen, ist ein Hardware-Problem!", "de")
print(response.text)
