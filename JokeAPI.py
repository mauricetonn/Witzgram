import requests
import json 

def req(category, format = "json", black_list = "sexist,nsfw", type = "single,twopart", amount = "1" ):
    URL = 'https://v2.jokeapi.dev/joke/'
    # 'https://v2.jokeapi.dev/joke/Programming,Misc?format=json&blacklistFlags=nsfw,sexist&type=single&lang=de&amount=1'
    full_req = URL + category + "?" + "format=" + format + "&" + "blacklistFlags=" + black_list + "&" + "type=" + type + "&lang=de&" + "amount=" + amount 
    return full_req

res = requests.get(req(category="Programming"))
res_json = json.loads(res.text)

def joke(response):
    if res_json["type"] == "twopart":
        setup = res_json["setup"]
        delivery = res_json["delivery"]
        joke = setup + "\n" + delivery
    elif res_json["type"] == "single":
        joke = res_json["joke"]
    return joke

joke = joke(res_json)
category = res_json["category"]
print(joke, category)