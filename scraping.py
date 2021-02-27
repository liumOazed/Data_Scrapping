import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


hdr = {'User-Agent': 'Mozilla/5.0'}

review =[]
ids =[]
animes =[]


for j in range(1,53):
    link = 'https://www.anime-planet.com/users/recent_user_reviews.php?page=' + str(j)
    req = Request(link,headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser') 
    review_text = soup.findAll('div',attrs={"class":"pure-1 userContent"})
    user_text = soup.findAll('span', attrs={"itemprop":"name"})
    website = soup.find('div', attrs={"id": "siteContainer"}).findAll('h3')

    for x in review_text:
        review.append(x.find('p').text)

    for y in user_text:
        ids.append(y.text)
    
    for anime_name in website:
        animes.append(anime_name.get_text())


    # for elem in website:
    #     tag_1 = soup.find('div')
    #     for aloo in tag_1:
    #         tag_2= soup.find('a')
    #         for ain in tag_2.children:
    #             anime_name = soup.find_all('h3')
    #             for anime in anime_name:
    #                 animes.append(anime.get_text())

                            #open csv file and write data

        

    df = pd.DataFrame(list(zip(ids,animes,review)),columns = ['user_id','anime_id','reviews'])
    df.to_csv('anime.csv', index =False)
    j+=1






