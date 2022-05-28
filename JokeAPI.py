import requests
import json 

def req(category, format = "json", black_list = "sexist,nsfw", type = "single,twopart", amount = "1" ):
    URL = 'https://v2.jokeapi.dev/joke/'
    # 'https://v2.jokeapi.dev/joke/Programming,Misc?format=json&blacklistFlags=nsfw,sexist&type=single&lang=de&amount=1'
    full_req = URL + category + "?" + "format=" + format + "&" + "blacklistFlags=" + black_list + "&" + "type=" + type + "&lang=de&" + "amount=" + amount 
    return full_req

def Joke(response):
    if response["type"] == "twopart":
        setup = response["setup"]
        delivery = response["delivery"]
        joke = setup + "\n" + delivery
    elif response["type"] == "single":
        joke = response["joke"]
    return joke

def get_joke(category = ""):
    res = requests.get(req(category=category))
    res_json = json.loads(res.text)

    joke = Joke(res_json)
    category = res_json["category"]
    print(joke, category)

get_joke(category="Programming")
