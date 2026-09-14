import re


POST_AGE_PATTERN = re.compile(
    r"\[r/[^\]]+\]\([^)]+\)•\s*(\d+)\s*(mo|m|h|d|w|y)\s+ago",
    re.IGNORECASE,
)


def parse_reddit_age_hours(text):
    """
    Extract the age of the Reddit post from Tavily raw content.

    Examples:
        •23h ago  -> 23 hours
        •2d ago   -> 48 hours
        •3d ago   -> 72 hours
        •1w ago   -> 168 hours

    Returns:
        Number of hours, or None if no matching timestamp is found.
    """

    match = POST_AGE_PATTERN.search(text[:3000])

    if not match:
        return None

    amount = int(match.group(1))
    unit = match.group(2).lower()

    multipliers = {
        "m": 1 / 60,
        "h": 1,
        "d": 24,
        "w": 168,
        "mo": 720,
        "y": 8760,
    }

    return amount * multipliers[unit]


def is_recent_reddit_post(text, max_age_hours=48):
    """
    Return True if the Reddit post is within the allowed age.
    """

    age_hours = parse_reddit_age_hours(text)

    if age_hours is None:
        return False

    return age_hours <= max_age_hours
