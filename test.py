import asyncio

from thispersondoesnotexist import get_online_person, save_online_person


async def main():
    # picture = await get_online_person()
    # print(picture)

    await save_online_person('test.png')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())