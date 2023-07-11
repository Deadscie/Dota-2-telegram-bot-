from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import aiohttp
URL_TEMPLATE_TOURNAMENTS = "https://liquipedia.net/dota2/Portal:Tournaments"
FILE_NAME = "test.csv"
HEADERS = {'User-Agent':UserAgent().random}



async def parse_tournaments(tournaments_dict):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_TEMPLATE_TOURNAMENTS,headers = HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            count = 0
            soup = bs(r,'html.parser')
            tournaments_place = soup.find_all('div',{'class':'gridTable tournamentCard NoGameIcon'})
            tournaments_place.pop(2)
            for tournaments in tournaments_place:
                for tournament in tournaments:
                    tournament_info = []
                    if count != 0:
                        for i in tournament:
                            tournament_info.append(i.text.replace('\xa0',''))
                        if tournament_info[1] != 'S':
                            tournaments_dict[tournament_info[1]] = {'tier':tournament_info[0],
                        'date':tournament_info[2],'prize_pool':tournament_info[3],
                        'location':tournament_info[4],'participants_count':tournament_info[5].replace('participants',''),'participants' :'',
                        'link':'','participants':''}
                    count +=1
            tournaments_dict = add_link_in_dict(soup,tournaments_dict)
            return tournaments_dict

def add_link_in_dict(soup,tournaments_dict):
    tournaments_place = soup.find_all('div',{'class':'gridTable tournamentCard NoGameIcon'})
    slice_matches = len(tournaments_place[2])
    link_place = soup.find_all('div',{'class':'gridCell Tournament Header'})
    link_place = link_place[:slice_matches]
    list_link = []
    for i in link_place:
        link = i.contents[-1]
        list_link.append(link['href'])
    link_count = 0
    for i in tournaments_dict:
        tournaments_dict[i]['link'] = list_link[link_count]
        link_count+=1
    return tournaments_dict
