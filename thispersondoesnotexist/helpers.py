import asyncio
import aiofiles
import hashlib
from hashlib import algorithms_available

__all__ = ("get_checksum_from_picture", "algorithms_available", "save_picture", "run_and_get")


def run_and_get(coro):
    """
    Creates a task, runs the task, and gets its results
    Derived from `https://stackoverflow.com/questions/55696053/using-async-await-in-python-init-method`
    """
    task = asyncio.create_task(coro)
    asyncio.get_running_loop().run_until_complete(task)
    return task.result()

def get_checksum_from_picture(picture: bytes, method: str = "md5") -> str:
    """Calculate the checksum of the provided picture, using the desired method.
    Available methods can be fetched using the the algorithms_available function.
    :param picture: picture as bytes
    :param method: hashing method as string (optional, default=md5)
    :return: checksum as string
    """
    h = hashlib.new(method.lower())
    h.update(picture)
    return h.hexdigest()


async def save_picture(picture: bytes, file: str = None) -> None:
    """Save a picture to a file.
    The picture must be provided as it content as bytes.
    The filename must be provided as a str with the absolute or relative path where to store it.
    If no filename is provided, a filename will be generated using the MD5 checksum of the picture, with jpeg extension.
    :param picture: picture content as bytes
    :param file: filename as string, relative or absolute path (optional)
    :return: None
    """
    if file is None:
        file = get_checksum_from_picture(picture) + ".jpeg"
    async with aiofiles.open(file, "wb") as f:
        await f.write(picture)
