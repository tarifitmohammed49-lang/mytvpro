name: Update Live Channels

on:
  schedule:
    # يعمل تلقائياً كل ساعة (00:00, 01:00, إلخ)
    - cron: '0 * * * *'
  # يسمح لك بتشغيله يدوياً لتجربته
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install requests

      - name: Run Simo Sniper
        # ✅ هذا السطر يجب أن يطابق اسم الملف الذي احتفظنا به
        run: python Simo_Sniper.py

      - name: Commit and Push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "Simo Sniper Bot"
          git add links.json
          git commit -m "Update links.json [Simo Sniper]" || exit 0
          git push
