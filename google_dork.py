import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote

user_input = input("query: ")

req = requests.get("https://www.google.com/search?q="+user_input)
soup = BeautifulSoup(req.text, "html.parser")

search_result = soup.findAll("a", {'data-uch':'1'})
for link in search_result:
    url = link.get('href')
    try:
        url = re.search('url\?q=(.+?)\&sa', url).group(1)
        print(unquote(url))
    except:
        continue

# text = "/url?q=http://otaku-it.blogspot.com/&sa=U&ved=2ahUKEwjpl96ur-TpAhXz7XMBHRZ8AZ4QFjAAegQIARAB&usg=AOvVaw2-ybQLARyroRAJ9bvyG1ol"
# print(re.search('url\?q=(.+?)\&sa', text).group(1))