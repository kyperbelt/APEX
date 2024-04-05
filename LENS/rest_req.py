import requests


def s2t_voice(voice_string):
    url = "http://localhost:8080/voice"

    response = requests.post(url=url, data=voice_string)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['command']
    else:
        print(f'Request failed for {url} with status code {response.status_code}')
        return "NA_COMMAND"


# s2t_voice("scroll down")
