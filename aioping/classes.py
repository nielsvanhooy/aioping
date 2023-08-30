import asyncio

class BoundedTaskGroup(asyncio.TaskGroup):
    def __init__(self, *args, max_parallelism=0, **kwargs):
        super().__init__(*args)
        self._sem = asyncio.Semaphore(max_parallelism) if max_parallelism else None

    def create_task(self, coro, *args, **kwargs):
        if self._sem:
            async def _wrapped_coro(sem, coro):
                async with sem:
                    return await coro

            coro = _wrapped_coro(self._sem, coro)

        return super().create_task(coro, *args, **kwargs)
