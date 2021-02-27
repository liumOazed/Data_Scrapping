import pandas as pd
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

BASE_DIR = os.path.dirname(__file__)

hdr = {'User-Agent': 'Mozilla/5.0'}

for j in range(0,50):
    link = 'https://www.anime-planet.com/users/recent_user_reviews.php?page=' + str(j)
    # driver.get(link)
    # j +=1 
    req = Request(link,headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    review =[]
    ids =[]
    animes =[] 
    review_text = soup.findAll('div',attrs={"class":"pure-1 userContent"})
    user_text = soup.findAll('span', attrs={"itemprop":"name"})
    website = soup.findAll('div', attrs={"id": "siteContainer"}) 

    for x in review_text:
        for y in user_text:
            ids.append(y.text)
            for elem in website:
                tag_1 = soup.find('div')
                for aloo in tag_1:
                    tag_2= soup.find('a')
                    for ain in tag_2.children:
                        anime_name = soup.find_all('h3')
                        for anime in anime_name:
                            animes.append(anime.get_text())

        review.append(x.find('p').text)
        j+=1

df = pd.DataFrame(list(zip(ids,animes,review)),columns = ['user_id','anime_id','reviews'])
path= os.path.join(BASE_DIR,'data')
os.makedirs(path,exist_ok=True)
filepath = os.path.join('data','anime.csv')
df.to_csv(filepath, index =False)






