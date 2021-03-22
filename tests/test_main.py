import pytest
import asyncio
import nest_asyncio
from ..thispersondoesnotexist.online_getter import get_online, save_online


@pytest.mark.asyncio
async def test_main():
    # picture = await get_online_person()
    # print(picture)

    await save_online('person', 'test_human.png')
    await save_online('horse', 'test_horse.png')


nest_asyncio.apply()
loop = asyncio.get_event_loop()
loop.run_until_complete(test_main())
