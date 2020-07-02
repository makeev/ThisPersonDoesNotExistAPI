import aiohttp
from .helpers import *


async def get_online_person() -> bytes:
    url = "https://thispersondoesnotexist.com/image"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    async with aiohttp.ClientSession() as s:
        async with s.get(url, headers=headers) as r:
            return await r.read()


async def save_online_person(file: str = None) -> int:
    picture = await get_online_person()
    return await save_picture(picture, file)
