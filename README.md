# aioisodd

asyncio-powered 2 LoC pure Python checking whether the number is odd

## Usage

```python
import asyncio
from aioisodd import is_odd


async def main():
    print(await is_odd(41))  # prints "True"
    print(await is_odd('42'))  # prints "False"


if __name__ == '__main__':
    asyncio.run(main())
```

## Installation

### With pip

```
pip install 'git+https://github.com/evgfilim1/aioisodd@master'
```

## Changelog

### 0.2.3-post.0

- Fixed package being empty on install
- Added lockfile

### 0.2.3

- More effective check for big numbers

### 0.2.2

- Fix bug when passing bool always returned False

### 0.2.2-beta.0

- Fix TypeError when passing anything except str into method

### 0.2.1-post.0

- Updated description

### 0.2.1

- Optimized working with big numbers

### 0.2.0

- Added type hints, now requires Python 3.10+

### 0.1.0

- Initial release
