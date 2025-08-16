import re

url = input("URL: ").strip()
pattern = r"^(?:https?://)?(?:www\.)?twitter\.(?:com|org|net)/(\w+)$"
if clear := re.search(pattern, url, re.IGNORECASE):
    print(f"Username:", clear.group(1))


