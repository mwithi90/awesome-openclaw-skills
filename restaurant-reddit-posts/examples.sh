#!/bin/bash
# Restaurant Reddit Posts - Example Commands
#
# This script demonstrates how to use reddit-cli to fetch
# restaurant-related posts from various subreddits.
#
# Prerequisites: reddit-cli must be installed and configured
# See: ../redditlisten/skill.md

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Restaurant Reddit Posts Examples${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Function to check if reddit-cli is available
check_reddit_cli() {
    if ! command -v reddit-cli &> /dev/null; then
        echo -e "${YELLOW}⚠️  reddit-cli not found${NC}"
        echo "Please install reddit-cli from the redditlisten skill"
        echo "See: ../redditlisten/skill.md"
        exit 1
    fi
}

# Function to display section header
section() {
    echo -e "\n${GREEN}▶ $1${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# Check if reddit-cli is installed
check_reddit_cli

# Example 1: Top Posts from r/restaurants
section "Example 1: Top 10 posts from r/restaurants"
echo "Command: reddit-cli posts restaurants 10 top"
echo ""
reddit-cli posts restaurants 10 top || echo "Error: Make sure your Reddit cookies are configured"

# Example 2: Hot posts from r/food
section "Example 2: Hot posts from r/food (trending now)"
echo "Command: reddit-cli posts food 10 hot"
echo ""
reddit-cli posts food 10 hot || echo "Error: Make sure your Reddit cookies are configured"

# Example 3: Search for specific topics
section "Example 3: Search for 'best burger' in restaurants"
echo "Command: reddit-cli search \"best burger\" --sub restaurants 5"
echo ""
reddit-cli search "best burger" --sub restaurants 5 || echo "Error: Make sure your Reddit cookies are configured"

# Example 4: Industry insights
section "Example 4: Industry insights from r/KitchenConfidential"
echo "Command: reddit-cli posts KitchenConfidential 10 top"
echo ""
reddit-cli posts KitchenConfidential 10 top || echo "Error: Make sure your Reddit cookies are configured"

# Example 5: Fast food discussions
section "Example 5: Fast food discussions"
echo "Command: reddit-cli posts fastfood 10 hot"
echo ""
reddit-cli posts fastfood 10 hot || echo "Error: Make sure your Reddit cookies are configured"

echo -e "\n${BLUE}========================================${NC}"
echo -e "${GREEN}✅ Examples completed!${NC}"
echo -e "${BLUE}========================================${NC}\n"
echo "For more examples, see skill.md"
