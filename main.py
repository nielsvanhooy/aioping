
import asyncio
import time
import logging

from aioping import ping_list
from ips import lala




if __name__ == "__main__":
    # for x in lala[0:100]:
    #     asyncio.run(ping(x))
    start = time.time()
    logging.basicConfig(level=logging.INFO)     # or logging.DEBUG
    results = asyncio.run(ping_list(lala, timeout=5, max_parallelism=3500))
    print(results)
    end = time.time()
    total = end - start
    print(total)
