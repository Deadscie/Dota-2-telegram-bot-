
from bs4 import BeautifulSoup as bs
import asyncio
from fake_useragent import UserAgent
import aiohttp
from services.parser_liquipedia.parse_participants import add_participants
from services.parser_liquipedia.parse_tournaments import parse_tournaments
matches = {':)':'July 8, 2023 - 8:29 UTC'}
URL_TEMPLATE_MATCHES = "https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches"
URL_TEMPLATE_TOURNAMENTS = "https://liquipedia.net/dota2/Portal:Tournaments"
FILE_NAME = "test.csv"
HEADERS = {'User-Agent':UserAgent().random}
tournaments_dict = {}
async def parse():
    global tournaments_dict
    loop =asyncio.get_event_loop()
    tournaments_dict = await parse_tournaments(tournaments_dict)
    tournaments_dict = await add_participants(tournaments_dict)
    print(tournaments_dict)
