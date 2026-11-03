eddit API

## Description

This project uses the Reddit API to get information about subreddits.

It contains a Python function that returns the total number of subscribers for a given subreddit. If the subreddit is invalid, the function returns `0`.

## Requirements

- Python 3
- Requests library
- Internet connection

## Installation

Install the Requests library:

```bash
pip install requests
```

## Files

- `0-subs.py` – Contains the `number_of_subscribers()` function.

## Usage

Example:

```python
from 0-subs import number_of_subscribers
```

The function can be tested using:

```python
number_of_subscribers("python")
```

It returns the total number of subscribers for the subreddit.

