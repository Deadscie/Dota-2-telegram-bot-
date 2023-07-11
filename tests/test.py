from bs4 import BeautifulSoup as bs
import asyncio
from fake_useragent import UserAgent
import aiohttp
matches = {':)':'July 8, 2023 - 8:29 UTC'}
URL_TEMPLATE_MATCHES = "https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches"
URL_TEMPLATE_TOURNAMENTS = "https://liquipedia.net/dota2/Portal:Tournaments"
FILE_NAME = "test.csv"
HEADERS = {'User-Agent':UserAgent().random}

tournaments_dict = {}

async def parse_tournaments():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_TEMPLATE_TOURNAMENTS,headers = HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            count = 0
            soup = bs(r,'html.parser')
            tournaments_place = soup.find_all('div',{'class':'gridTable tournamentCard NoGameIcon'})
            count_dizinfo = len(tournaments_place[2])
            tournaments_place.pop(2)
            for tournaments in tournaments_place:
                for tournament in tournaments:
                    tournament_info = []
                    if count != 0:
                        find_link = soup.find_all('div',{'class','gridCell Tournament Header'})
                        find_link = find_link[:count_dizinfo]

                        for i in tournament:
                            tournament_info.append(i.text.replace('\xa0',''))
                        tournaments_dict[tournament_info[1]] = {'tier':tournament_info[0],
                        'date':tournament_info[2],'prize_pool':tournament_info[3],
                        'location':tournament_info[4],'participants_count':tournament_info[5].replace('participants',''),'participants' :'',
                        'link':''}
                        list_link = []
                        for i in find_link:
                            link = i.contents[-1]
                            list_link.append(link['href'])
                        link_count = 0
                        for i in tournaments_dict:
                            tournaments_dict[i]['link'] = list_link[link_count]
                            link_count+=1




                    count +=1

            print('w')
async def parse_matches(tournament):
    URL_TEMPLATE_TOURNAMENT = 'https://liquipedia.net/dota2/'+tournament
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_TEMPLATE_TOURNAMENT,headers = HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = bs(r,'html.parser')
            participants = soup.find_all('div',{'class':'template-box'})
            list_participants = []
            print(participants)
            for i in participants:
                name = i.find('div',{'class':'teamcard toggle-area toggle-area-1d'})
                list_participants.append(name.text)
            tournaments_dict[tournament]['participants'] = list_participants


if __name__ == '__main__':
    loop =asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(parse_tournaments())
    loop.run_until_complete(parse_matches('2022 Asian Games'))
for i in tournaments_dict:
    print(i,tournaments_dict[i])