"""
VibeDispatch Configuration Constants
"""

# Cache settings
CACHE_TTL = 300  # 5 minutes

# API limits
MAX_REPOS = 100
MAX_CONCURRENT_REQUESTS = 10
MAX_REPOS_FOR_STAGE = 15  # Max repos to check in stage endpoints

# VibeCheck workflow template
VIBECHECK_WORKFLOW = """name: VibeCheck
on:
  workflow_dispatch:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]
  schedule:
    - cron: '0 0 * * 0'

jobs:
  vibecheck:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
    steps:
      - uses: actions/checkout@v4
      - name: Run VibeCheck
        uses: WolffM/vibecheck@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
"""
