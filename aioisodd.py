async def is_odd(x: int | str | float | bool) -> bool:
    return int(x[-1]) % 2 != 0

