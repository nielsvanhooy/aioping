import asyncio
import functools

# parameterless decorator
def async_lru_cache(async_function):
    @functools.lru_cache
    def cached_async_function(*args, **kwargs):
        coroutine = async_function(*args, **kwargs)
        return asyncio.ensure_future(coroutine)
    return cached_async_function