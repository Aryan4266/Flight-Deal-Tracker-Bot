# 🚀 Flight Deal Tracker Bot

Automatically track flight prices and get alerts when deals appear!

## Features
- Monitor specific routes
- Get alerts if prices drop
- Email + Discord notification support


## How to Use

1. Clone this repo.
2. Update `config.py` with your own email, password, webhook, and routes.
3. Run it manually:
```bash
python tracker.py
```
4. (Optional) Schedule it with cronjob or deploy it as AWS Lambda for automatic daily checking!

## Requirements
```bash
pip install requests
```

## Scheduling Example (Linux Cron)
Every 6 hours:
```bash
0 */6 * * * /usr/bin/python3 /path/to/tracker.py
```

---

# Happy flying! ✈️