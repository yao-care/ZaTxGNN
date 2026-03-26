#!/usr/bin/env python3
"""South Africa health news fetcher.

Fetches health news from South African sources via Google News RSS.
"""

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Optional
from urllib.parse import quote

import requests

# South African health keywords
HEALTH_KEYWORDS = [
    "health", "medicine", "drug", "pharmaceutical", "clinical trial",
    "SAHPRA", "medical", "hospital", "treatment", "therapy",
    "doctor", "patient", "disease", "virus", "vaccine",
    "HIV", "AIDS", "tuberculosis", "TB", "malaria",
    "diabetes", "hypertension", "cancer", "COVID",
]

# South African news sources
SA_NEWS_DOMAINS = [
    "news24.com",
    "dailymaverick.co.za",
    "timeslive.co.za",
    "iol.co.za",
    "ewn.co.za",
    "health24.com",
    "businesslive.co.za",
    "mg.co.za",  # Mail & Guardian
]


def fetch_google_news_rss(query: str, region: str = "ZA") -> list[dict]:
    """Fetch news from Google News RSS.

    Args:
        query: Search query
        region: Country code (ZA for South Africa)

    Returns:
        List of news items
    """
    encoded_query = quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-ZA&gl=ZA&ceid=ZA:en"

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ZaTxGNN/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        items = []

        for item in root.findall(".//item"):
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubDate")
            source = item.find("source")

            if title is not None and link is not None:
                items.append({
                    "title": title.text,
                    "link": link.text,
                    "published": pub_date.text if pub_date is not None else None,
                    "source": source.text if source is not None else None,
                })

        return items

    except Exception as e:
        print(f"Error fetching news: {e}")
        return []


def filter_health_news(items: list[dict]) -> list[dict]:
    """Filter news items to health-related content.

    Args:
        items: List of news items

    Returns:
        Filtered list of health-related news
    """
    health_items = []

    for item in items:
        title = item.get("title", "").lower()
        source = item.get("source", "").lower()

        # Check if title contains health keywords
        is_health = any(kw.lower() in title for kw in HEALTH_KEYWORDS)

        # Check if source is a known SA news domain
        is_sa_source = any(domain in source for domain in SA_NEWS_DOMAINS)

        if is_health or is_sa_source:
            health_items.append(item)

    return health_items


def fetch_sa_health_news(drug_name: Optional[str] = None) -> list[dict]:
    """Fetch South African health news.

    Args:
        drug_name: Optional drug name to search for

    Returns:
        List of relevant news items
    """
    queries = [
        "South Africa health medicine",
        "SAHPRA pharmaceutical",
        "South Africa clinical trial",
    ]

    if drug_name:
        queries.insert(0, f"{drug_name} South Africa")

    all_items = []
    seen_links = set()

    for query in queries:
        items = fetch_google_news_rss(query)
        filtered = filter_health_news(items)

        for item in filtered:
            if item["link"] not in seen_links:
                seen_links.add(item["link"])
                all_items.append(item)

    return all_items


if __name__ == "__main__":
    print("Fetching South Africa health news...")
    news = fetch_sa_health_news()

    print(f"\nFound {len(news)} health news items:")
    for item in news[:10]:
        print(f"- {item['title'][:80]}...")
        print(f"  Source: {item['source']}")
        print()
