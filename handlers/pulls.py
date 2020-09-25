import requests

def get_git_json():
    NAME = "........."
    PASS = "........."
    API = "https://api.github.com/repos/alenaPy/devops_lab/pulls?per_page=100&state=all"
    request = requests.get(API, auth=(NAME, PASS))
    key = request.json()
    return key

def get_array_object(i):
    return {"title": i["title"], "num": i["number"], "link": i["html_url"]}

def get_pulls(state):
    test_res = get_git_json()
    if state == "open" or state == "closed":
        return get_data_res(test_res, state)
    elif state == "accepted" or state == "needs work":
        return get_data_label(test_res, state)
    else:
        return get_data_all(test_res, state)


def get_data_res(res, state):
    arr = []
    for i in res:
        if i["state"] == state:
            arr.append(get_array_object(i))
    return arr


def get_data_label(res, state):
    arr = []
    for i in res:
        if len(i["labels"]) == 0:
            continue
        else:
            if i["labels"][0]["name"] == state:
                arr.append(get_array_object(i))
    return arr


def get_data_all(res, state):
    arr = []
    for i in res:
        arr.append(get_array_object(i))
    return arr

