async def is_odd(x: int | str | float | bool) -> bool:
    return bool(int(x) & 1)

