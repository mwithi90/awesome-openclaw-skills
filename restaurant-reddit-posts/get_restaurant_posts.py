#!/usr/bin/env python3
"""
Fetch top posts from restaurant-related subreddits using Reddit's JSON API.
No authentication required for public posts.
"""

import requests
import json
import sys
from typing import List, Dict

def get_top_posts(subreddit: str, limit: int = 10, time_filter: str = "all") -> List[Dict]:
    """
    Fetch top posts from a subreddit.

    Args:
        subreddit: Name of the subreddit (e.g., 'restaurant', 'food')
        limit: Number of posts to fetch (default: 10)
        time_filter: Time filter - 'hour', 'day', 'week', 'month', 'year', 'all' (default: 'all')

    Returns:
        List of post dictionaries
    """
    # Reddit's JSON API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/top.json"

    # Set headers to identify as a script
    # Reddit requires a descriptive user agent
    headers = {
        'User-Agent': 'python:restaurant-posts-fetcher:v1.0.0 (by /u/reddituser)'
    }

    # Parameters
    params = {
        'limit': limit,
        't': time_filter  # time filter
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        posts = []

        for child in data['data']['children']:
            post = child['data']
            posts.append({
                'title': post['title'],
                'author': post['author'],
                'score': post['score'],
                'url': f"https://www.reddit.com{post['permalink']}",
                'num_comments': post['num_comments'],
                'created_utc': post['created_utc'],
                'selftext': post.get('selftext', '')[:200]  # First 200 chars
            })

        return posts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}", file=sys.stderr)
        return []

def display_posts(posts: List[Dict]):
    """Display posts in a readable format."""
    if not posts:
        print("No posts found.")
        return

    print(f"\n{'='*80}")
    print(f"Found {len(posts)} posts")
    print(f"{'='*80}\n")

    for i, post in enumerate(posts, 1):
        print(f"{i}. {post['title']}")
        print(f"   Author: u/{post['author']} | Score: {post['score']} | Comments: {post['num_comments']}")
        print(f"   URL: {post['url']}")
        if post['selftext']:
            print(f"   Preview: {post['selftext']}...")
        print()

def main():
    """Main function."""
    # Default subreddit is 'restaurant'
    subreddit = sys.argv[1] if len(sys.argv) > 1 else 'restaurant'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    time_filter = sys.argv[3] if len(sys.argv) > 3 else 'all'

    print(f"Fetching top {limit} posts from r/{subreddit} (time filter: {time_filter})...")

    posts = get_top_posts(subreddit, limit, time_filter)
    display_posts(posts)

    # Also save to JSON file
    output_file = f"{subreddit}_top_posts.json"
    with open(output_file, 'w') as f:
        json.dump(posts, f, indent=2)
    print(f"\nPosts saved to {output_file}")

if __name__ == "__main__":
    main()
