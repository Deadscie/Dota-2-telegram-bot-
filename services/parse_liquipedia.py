
from bs4 import BeautifulSoup as bs
import asyncio
from fake_useragent import UserAgent
import aiohttp
matches = {':)':'July 8, 2023 - 8:29 UTC'}
URL_TEMPLATE = "https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches"
FILE_NAME = "test.csv"
HEADERS = {'User-Agent':UserAgent().random}

async def parse():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_TEMPLATE,headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = bs(r,'html.parser')
            games = soup.find_all('table',{'class':'wikitable wikitable-striped infobox_matches_content'})
            for i in games:
                team_left_place = i.find('td',{'class':'team-left'})
                team_right_place = i.find('td',{'class':'team-right'})
                team_left = team_left_place.find('span',{'class':'team-template-text'})
                team_right = team_right_place.find('span',{'class':'team-template-text'})
                game_time = i.find('span',{'class':'match-countdown'})
                bali = i.find('a',{'title': 'Bali Major/2023'})
                if bali:
                    if team_left.text != 'TBD' and team_right.text != 'TBD' or team_left.text != 'TBD' and team_right.text == 'TBD' or team_left.text == 'TBD' and team_right.text != 'TBD':
                        matches[team_left.text+' vs '+ team_right.text] = game_time.text
            return matches
loop =asyncio.get_event_loop()
loop.run_until_complete(parse())
