# Reddit Restaurant Posts Skill

A specialized guide for using reddit-cli to fetch and analyze posts from restaurant and food-related subreddits.

## Overview

This skill provides commands, examples, and workflows for:
- 🍔 Fetching top posts from restaurant subreddits
- 📊 Market research and trend analysis
- 🔍 Competitive intelligence
- 💡 Menu inspiration and ideas
- 🗺️ Location-based restaurant insights

## Quick Start

1. **Install reddit-cli** (see [redditlisten](../redditlisten/skill.md))
2. **Configure cookies** - Set REDDIT_SESSION environment variable
3. **Run examples**:

```bash
# Get top 10 restaurant posts
reddit-cli posts restaurants 10 top

# Search for burger discussions
reddit-cli search "best burger" --sub restaurants 20

# Get trending food posts
reddit-cli posts food 10 hot
```

## Files

- **skill.md** - Complete skill documentation with examples and use cases
- **examples.sh** - Executable bash script demonstrating common commands
- **get_restaurant_posts.py** - Python script for programmatic access (alternative implementation)

## Popular Subreddits

| Subreddit | Focus | Size |
|-----------|-------|------|
| r/food | General food | 30M+ |
| r/restaurants | Dining experiences | 100K+ |
| r/KitchenConfidential | Industry pros | 200K+ |
| r/restaurantowners | Owners/managers | 20K+ |
| r/fastfood | Fast food chains | 80K+ |

## Use Cases

### Market Research
```bash
reddit-cli search "disappointed" --sub restaurants 20
reddit-cli posts restaurantowners 10 hot
```

### Trend Monitoring
```bash
reddit-cli posts food 15 hot
reddit-cli search "food trends 2026" 20
```

### Competitive Analysis
```bash
reddit-cli search "chipotle vs" 15
reddit-cli search "mcdonald's quality" --sub fastfood 10
```

## Examples

Run the examples script to see it in action:

```bash
chmod +x examples.sh
./examples.sh
```

## Requirements

- reddit-cli (from redditlisten skill)
- Reddit session cookies configured
- Internet connection

## Documentation

See [skill.md](skill.md) for complete documentation including:
- All available commands
- Advanced search techniques
- Common workflows
- Troubleshooting guide

## Related Skills

- [redditlisten](../redditlisten/skill.md) - Core Reddit CLI
- [sociallistener](../sociallistener/skill.md) - Social media monitoring

## License

MIT
