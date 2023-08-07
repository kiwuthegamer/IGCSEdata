urls = """https://papers.gceguide.com/Cambridge%20IGCSE/English%20-%20First%20Language%20(0500)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Mathematics%20(0580)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Physics%20(0625)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Chemistry%20(0620)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Geography%20(0460)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/English%20-%20Literature%20in%20English%20(0475)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Accounting%20(0452)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Economics%20(0455)/2022/
https://papers.gceguide.com/Cambridge%20IGCSE/Computer%20Science%20(0478)/2022/""".split("\n")

# English 0500
# Math 0580
# Physics 0625
# Chemistry 0620
# Geography 0460
# English Literature 0475
# Accounting 0452
# Economics 0455
# Computer Science 0478

import requests, os
from bs4 import BeautifulSoup


def downloadFile(url, fileName):
  os.makedirs(os.path.dirname(fileName), exist_ok=True)
  with open(fileName, "wb") as file:
    response = requests.get(url)
    file.write(response.content)


for i,url in enumerate(urls):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  files = soup.find_all("a", class_="name")
  for j,file in enumerate(files):
    title = soup.head.title.get_text() # Past Papers | Cambridge IGCSE | Mathematics (0580) | 2022 | GCE Guide
    title = title.replace("Past Papers | Cambridge IGCSE | ","").replace(" | 2022 | GCE Guide","")
    filename = title + "/" + file["href"]
    downloadFile(url + file["href"], "Cambridge IGCSE - Past Papers - 2022/" + filename)
    print(f"{filename} done {j+1}/{len(files)}")
  print(f"{title} done {i+1}/{len(urls)}")
