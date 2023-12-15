urls = """https://www.savemyexams.com/igcse/additional-maths/cie/25/revision-notes/
https://www.savemyexams.com/igcse/biology/cie/23/revision-notes/
https://www.savemyexams.com/igcse/business/cie/23/revision-notes/
https://www.savemyexams.com/igcse/chemistry/cie/23/revision-notes/
https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/
https://www.savemyexams.com/igcse/economics/cie/20/revision-notes/
https://www.savemyexams.com/igcse/english-language/cie/20/revision-notes/
https://www.savemyexams.com/igcse/geography/cie/20/revision-notes/
https://www.savemyexams.com/igcse/ict/cie/23/revision-notes/
https://www.savemyexams.com/igcse/maths_core/cie/23/revision-notes/
https://www.savemyexams.com/igcse/maths_extended/cie/25/revision-notes/
https://www.savemyexams.com/igcse/physics/cie/23/revision-notes/""".split("\n")

import requests, os, markdownify
import vimeo_downloader as vdl
from bs4 import BeautifulSoup

def downloadFile(url, fileName, content=""):
  # Create directory if it doesn't exist
  os.makedirs(os.path.dirname(fileName), exist_ok=True)
  
  # Download file from the given URL and save it
  with open(fileName, "wb") as file:
    if content:
      file.write(content)
    else:
      response = requests.get(url)
      file.write(response.content)

# Loop through the list of URLs
for i, url in enumerate(urls):
  # Fetch the HTML content from the URL
  r = requests.get(url)
  
  # Parse HTML content using BeautifulSoup
  soup = BeautifulSoup(r.text, 'html.parser')
  
  subject = soup.select("h1")[0].contents[0].replace("CIE IGCSE ","")
  print(f"\nStarting {subject}")

  # Find all links with class "name"
  links = soup.select("li.resource_topic__8inpl")
  
  links = [link.contents[0]["href"] for link in links]
  
  # Extract information from the HTML and download files
  for j, link in enumerate(links):
    link = "https://www.savemyexams.com"+link
    
    r = requests.get(link)
    
    soup = BeautifulSoup(r.text, 'html.parser')

    title = soup.select("h1.revision-notes_title__R2QMx")[0].contents[0]
    print(f"Starting {title}")
    
    for part in soup.select("article.Parts_parts____q6M"):
      for col in part.select("div.row > div.col-12 > div.Wrapper_wrapper__cRDPF"):
        md = col.select("div > div")[0]
        try:
          if md.select("div.col-12 > div")[0]["id"].startswith("vimeo-"):
            continue
        except:
          pass
        topic = md.select("header > h2 > *")[0]
        filename = f"DATA/revisionNotes/{subject}/{title}/{topic}.md"
        downloadFile("", filename, markdownify.markdownify(str(md)))
    
    # Print progress information
    print(f"{title} done {j+1}/{len(links)}")
  
  # Print overall progress information for the current URL
  print(f"{title} done {i+1}/{len(urls)}")

