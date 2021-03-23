import aiohttp
from .helpers import *

URL_PERSON: str = "https://thispersondoesnotexist.com/image"
URL_HORSE: str = "https://thishorsedoesnotexist.com"


async def get_online(thing_type: str) -> bytes:
    if thing_type == 'horse':
        return await get_online_thing(URL_HORSE)
    else:
        return await get_online_thing(URL_PERSON)


async def get_online_thing(url: str = URL_PERSON) -> bytes:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    async with aiohttp.ClientSession() as s:
        async with s.get(url, headers=headers) as r:
            return await r.read()


async def save_online(thing_type: str = 'person', file: str = None) -> int:
    picture = await get_online(thing_type)

    return run_and_get(save_picture(picture, file))
