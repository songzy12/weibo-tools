import requests


def follower_ids(uid, access_token):
    # Doc: https://open.weibo.com/wiki/2/friendships/followers/ids

    url = "https://api.weibo.com/2/friendships/followers/ids.json"
    params = {'uid': uid,
              'access_token': access_token}

    resp = requests.get(url, params).json()
    print("resp of followers/ids:")
    print(str(resp))
    ids = resp['ids']
    return ids