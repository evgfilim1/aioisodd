async def is_odd(x: int | str | float | bool) -> bool:
    return str(int(x))[-1] in map(str, range(1, 10, 2))

