# AIGA Discord Bot
## Age of Empires Mobile AI Advisor
### Built by Network Grey | Powered by Anthropic Claude

---

## Files

| File | Purpose |
|---|---|
| `bot.py` | Main bot code |
| `requirements.txt` | Python dependencies |
| `Procfile` | Railway deployment config |

---

## Deployment on Railway

### Step 1 — GitHub
1. Create a new GitHub repository (private)
2. Upload all three files to the repo

### Step 2 — Railway
1. Go to railway.app and sign up with GitHub
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your repository
4. Railway will detect the Procfile automatically

### Step 3 — Environment Variables
In Railway, go to your project → **Variables** tab → add these two:

| Variable | Value |
|---|---|
| `DISCORD_TOKEN` | Your Discord bot token |
| `ANTHROPIC_API_KEY` | Your Anthropic API key |

**Never put real tokens in the code files.**

### Step 4 — Deploy
Click **Deploy**. Railway will install dependencies and start the bot.
Check the logs tab — you should see:
```
AIGA is online as AIGA#XXXX
Listening in channel: #aiga-advisor
```

---

## Configuration

All settings are at the top of `bot.py`:

| Setting | Default | What it does |
|---|---|---|
| `AIGA_CHANNEL_NAME` | `aiga-advisor` | Channel name to listen in |
| `RATE_LIMIT_MAX` | `10` | Max messages per user per hour |
| `RATE_LIMIT_WINDOW` | `3600` | Rate limit window in seconds |
| `CONTEXT_WINDOW` | `10` | Messages to remember per user |

---

## Changing the Channel Name

In `bot.py` line 18, change:
```python
AIGA_CHANNEL_NAME = "aiga-advisor"
```
to match your exact Discord channel name (lowercase, hyphens, no #).

---

## Monitoring Costs

Check usage at console.anthropic.com → Usage.
For a small alliance server, expect $2-5/month at moderate use.
