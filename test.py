import asyncio

from thispersondoesnotexist import get_online, save_online


async def main():
    # picture = await get_online_person()
    # print(picture)

    await save_online('person', 'test_human.png')
    await save_online('horse', 'test_horse.png')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
