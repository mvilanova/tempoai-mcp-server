"""
Date utility functions for Tempo AI MCP Server.

This module provides helper functions for date parsing and default date calculations.
"""

from datetime import datetime, timedelta, timezone


def get_default_start_date(days_ago: int = 30) -> str:
    """
    Get a default start date string in YYYY-MM-DD format.

    Args:
        days_ago: Number of days ago from today (UTC). Defaults to 30.

    Returns:
        Date string in YYYY-MM-DD format (UTC).
    """
    return (datetime.now(timezone.utc) - timedelta(days=days_ago)).strftime("%Y-%m-%d")


def get_default_end_date() -> str:
    """
    Get tomorrow's date string in YYYY-MM-DD format (UTC).

    Uses tomorrow instead of today to ensure workouts from "today" in UTC
    are not missed due to timezone differences when queries are made.

    Returns:
        Date string in YYYY-MM-DD format (UTC).
    """
    return (datetime.now(timezone.utc) + timedelta(days=1)).strftime("%Y-%m-%d")


def get_default_future_end_date(days_ahead: int = 30) -> str:
    """
    Get a default future end date string in YYYY-MM-DD format.

    Args:
        days_ahead: Number of days ahead from today (UTC). Defaults to 30.

    Returns:
        Date string in YYYY-MM-DD format (UTC).
    """
    return (datetime.now(timezone.utc) + timedelta(days=days_ahead)).strftime("%Y-%m-%d")


def parse_date_range(
    start_date: str | None, end_date: str | None, default_start_days_ago: int = 30
) -> tuple[str, str]:
    """
    Parse and validate a date range, providing defaults if needed.

    Args:
        start_date: Start date in YYYY-MM-DD format (optional).
        end_date: End date in YYYY-MM-DD format (optional).
        default_start_days_ago: Number of days ago for default start date. Defaults to 30.

    Returns:
        Tuple of (start_date, end_date) as strings in YYYY-MM-DD format (UTC).
    """
    if not start_date:
        start_date = get_default_start_date(default_start_days_ago)
    if not end_date:
        end_date = get_default_end_date()
    return start_date, end_date
