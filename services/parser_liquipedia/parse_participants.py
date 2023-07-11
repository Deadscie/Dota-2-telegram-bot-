from services.parser_liquipedia.parse_tournaments import parse_tournaments
import aiohttp
import asyncio
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
HEADERS = {'User-Agent':UserAgent().random}
async def add_participants(tournaments_dict):
    for i in tournaments_dict:
        URL_TEMPLATE_TOURNAMENT = 'https://liquipedia.net' + tournaments_dict[i]['link']
        print(URL_TEMPLATE_TOURNAMENT)
        async with aiohttp.ClientSession() as session:
            async with session.get(URL_TEMPLATE_TOURNAMENT,headers = HEADERS) as response:
                r = await aiohttp.StreamReader.read(response.content)
                soup = bs(r,'html.parser')
                participant = soup.find_all('div',{'class':'template-box'})
                for command in participant:
                    if command.a :
                        tournaments_dict[i]['participants'] = {command.a.text:''}
                    if command.tbody:
                        list_players = []
                        for l in command.tbody.contents:
                            if l.th :
                                list_players.append((l.th.text+' '+l.contents[-1].text).replace('\xa0',''))
                        if command.a:
                            tournaments_dict[i]['participants'][command.a.text] = list_players
                        list_players = []
    return tournaments_dict
