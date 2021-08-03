# Just an example of something I modified for a school project

import requests
import base64
from bs4 import BeautifulSoup

user = "darrens"
login = "tomcat:"

session = requests.session()
session.headers["Authorization"] = "Basic " + base64.b64encode(login.encode("utf8")).decode("utf8")
g = session.get("http://%s.lwtech-csd297.com/manager/" % user)
parsed = BeautifulSoup(g.content, features="html5lib")

undeploy = ""

for form in parsed.find_all("form", method="POST"):
    if "?path=/&" in form["action"] and "undeploy" in form["action"]:
        undeploy = form["action"]
        break
if undeploy:
    p = session.post(("http://%s.lwtech-csd297.com"+undeploy) % user)
    parsed = BeautifulSoup(p.content, features="html5lib")


upload = ""

for form in parsed.find_all("form", method="post"):
    if "upload" in form["action"]:
        upload = form["action"]
        break

print("Uploading...")
up = session.post(("http://%s.lwtech-csd297.com"+upload) % user, files={"deployWar": open("target/ROOT.war", "rb")})
print("Uploaded!", up)