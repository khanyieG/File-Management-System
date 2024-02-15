import pandas as pd
import io
import requests
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from PIL import Image


options = ChromeOptions()
driver = webdriver.Chrome(options=options)

image_path = Path('Image_data.txt')
image_path.touch()

driver = webdriver.Chrome()
driver.get("https://pokemondb.net/pokedex/national")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

results =[]
def parse_image_urls(classes, location, source):
    for a in soup.findAll(attrs={'class': classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
        else:
            print("No matching element found for class:", classes)    

    return results        

 

df= pd.DataFrame({"links": results})
df.to_csv("links.csv", index=False, encoding="utf-8")



if __name__ == "__main__":
    returned_results = parse_image_urls("infocard", "img", "src") 
    for b in returned_results:
        image_content = requests.get(b).content
        image_file= io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        file_path = Path(image_path, hashlib.sha1(image_content).hexdigest()[:10] + ".png")
        image.save(file_path,"PNG", quality=80)
