---
name: reddit-restaurant-posts
version: 1.0.0
description: Get top posts from restaurant and food-related subreddits using reddit-cli
author: claude
category: food-research
---

# Reddit Restaurant Posts

Use the reddit-cli tool to fetch top posts from restaurant and food-related subreddits. Perfect for market research, trend analysis, and discovering what people are talking about in the restaurant industry.

## Prerequisites

This skill uses the `reddit-cli` tool from the [redditlisten](../redditlisten/skill.md) skill. Make sure you have:
- reddit-cli installed and configured
- Reddit session cookies set up (see [redditlisten setup](../redditlisten/skill.md))

## Quick Examples

### Get Top Restaurant Posts

```bash
# Top 10 posts from r/restaurant
reddit-cli posts restaurant 10 top

# Top 10 posts from r/restaurants (more active community)
reddit-cli posts restaurants 10 top

# Top posts from this week only
reddit-cli posts restaurants 10 top --time week
```

### Popular Food & Restaurant Subreddits

Here are the most popular restaurant-related subreddits to monitor:

```bash
# General food discussion (30M+ members)
reddit-cli posts food 10 top

# Restaurant industry professionals (200K+ members)
reddit-cli posts KitchenConfidential 10 top

# Restaurant owners and managers
reddit-cli posts restaurantowners 10 top

# Fast food discussions
reddit-cli posts fastfood 10 top

# Fine dining
reddit-cli posts finedining 10 top

# Local restaurant recommendations
reddit-cli posts FoodLosAngeles 10 top
reddit-cli posts FoodNYC 10 top
reddit-cli posts ChicagoFood 10 top
```

### Search for Specific Topics

```bash
# Search for "best burger" in restaurant subreddits
reddit-cli search "best burger" --sub restaurants 20

# Search for "food trends" across all subreddits
reddit-cli search "food trends 2026" 15

# Search for negative feedback (great for market research)
reddit-cli search "worst service" --sub restaurants 10

# Search for specific cuisines
reddit-cli search "authentic italian" --sub food 15
```

### Get Latest/Hot Posts

```bash
# Hot posts (trending now)
reddit-cli posts restaurants 10 hot

# New posts
reddit-cli posts restaurants 10 new

# Rising posts (gaining traction)
reddit-cli posts restaurants 10 rising
```

## Use Cases

### 1. Market Research
Monitor what customers are saying about restaurants and food:
```bash
# Get top complaints
reddit-cli search "disappointed" --sub restaurants 20

# Find popular dishes
reddit-cli search "best dish" --sub food 30

# Track trends
reddit-cli posts foodtrends 15 hot
```

### 2. Competitive Analysis
See what people say about competitors:
```bash
# Search for specific restaurant chains
reddit-cli search "chipotle vs qdoba" 20
reddit-cli search "mcdonald's quality" --sub fastfood 15
```

### 3. Menu Ideas
Discover trending foods and dishes:
```bash
reddit-cli posts FoodPorn 20 top
reddit-cli posts seriouseats 15 hot
reddit-cli search "unique menu items" --sub restaurants 10
```

### 4. Location Research
Find insights about restaurant scenes in specific cities:
```bash
reddit-cli posts FoodNYC 10 top
reddit-cli search "best new restaurants" --sub sanfrancisco 15
```

## Common Subreddits for Restaurant Research

| Subreddit | Focus | Members |
|-----------|-------|---------|
| r/food | General food discussion | 30M+ |
| r/restaurants | Restaurant experiences | 100K+ |
| r/KitchenConfidential | Industry professionals | 200K+ |
| r/restaurantowners | Owners & managers | 20K+ |
| r/fastfood | Fast food chains | 80K+ |
| r/finedining | Fine dining experiences | 50K+ |
| r/seriouseats | Recipe testing & techniques | 600K+ |
| r/FoodPorn | Food photography | 5M+ |
| r/AskCulinary | Culinary questions | 300K+ |
| r/Cooking | Home cooking | 7M+ |

## Advanced Examples

### Combine Multiple Searches
```bash
# Create a comprehensive report
echo "=== TOP RESTAURANT POSTS ===" > restaurant_report.txt
reddit-cli posts restaurants 10 top >> restaurant_report.txt

echo "\n=== KITCHEN PROFESSIONAL INSIGHTS ===" >> restaurant_report.txt
reddit-cli posts KitchenConfidential 10 top >> restaurant_report.txt

echo "\n=== TRENDING FOOD DISCUSSIONS ===" >> restaurant_report.txt
reddit-cli posts food 10 hot >> restaurant_report.txt
```

### Monitor Specific Topics
```bash
# Check for health code violations discussions
reddit-cli search "health inspection" --sub restaurants 10

# Find delivery service feedback
reddit-cli search "doordash problems" --sub restaurants 15

# Track pricing discussions
reddit-cli search "expensive" --sub restaurants 20
```

### Time-Based Analysis
```bash
# What was trending this week
reddit-cli posts restaurants 20 top --time week

# Hot topics today
reddit-cli posts restaurants 15 hot

# New complaints/issues
reddit-cli posts restaurants 10 new
```

## Tips

1. **Rate Limits**: Reddit has rate limits. Space out your requests if making multiple calls.

2. **Best Times to Check**:
   - Morning (8-10 AM EST): Fresh overnight posts
   - Evening (6-9 PM EST): Peak activity time

3. **Sort Options**:
   - `top`: Best overall content (use with time filters)
   - `hot`: Currently trending
   - `new`: Latest posts
   - `rising`: Gaining momentum

4. **Search Tips**:
   - Use quotes for exact phrases: `"best pizza"`
   - Use subreddit filter for focused results
   - Increase limit for comprehensive research (max 100)

5. **Cookie Refresh**: Reddit session cookies expire. If you get errors, refresh your cookies.

## Common Workflows

### Daily Restaurant Trend Check
```bash
#!/bin/bash
# Save as: daily_restaurant_trends.sh

echo "Daily Restaurant Trends - $(date)"
echo "================================"

echo "\n📈 TOP POSTS TODAY"
reddit-cli posts restaurants 5 hot

echo "\n👨‍🍳 KITCHEN INSIGHTS"
reddit-cli posts KitchenConfidential 5 hot

echo "\n🍔 FAST FOOD BUZZ"
reddit-cli posts fastfood 5 hot
```

### Weekly Competitive Analysis
```bash
#!/bin/bash
# Save as: weekly_competitor_analysis.sh

COMPETITOR="YourCompetitorName"

echo "Weekly Analysis: $COMPETITOR"
echo "============================="

reddit-cli search "$COMPETITOR" 20 | tee competitor_mentions.txt

echo "\n\nIndustry Trends:"
reddit-cli posts restaurants 10 top --time week
```

## Troubleshooting

### "Command not found"
Install reddit-cli:
```bash
# Follow instructions in ../redditlisten/skill.md
```

### "403 Forbidden"
Your Reddit cookies expired. Get fresh cookies:
1. Login to reddit.com
2. F12 → Application → Cookies
3. Update REDDIT_SESSION and TOKEN_V2 environment variables

### "No results found"
- Check subreddit name spelling
- Try a more active subreddit (e.g., r/food instead of r/restaurant)
- Verify your cookies are valid with: `reddit-cli check`

## Related Skills

- [redditlisten](../redditlisten/skill.md) - Core Reddit CLI tool
- [sociallistener](../sociallistener/skill.md) - Multi-platform social listening

## License

MIT
