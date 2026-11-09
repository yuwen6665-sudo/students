import requests

url = "https://api.github.com/users/yuwen6665-sudo"
try:
    r = requests.get(url, timeout=10)
    data = r.json()
    print("用户名：", data["login"])
    print("公开仓库数：", data["public_repos"])
except Exception as e:
    print("请求失败：", e)