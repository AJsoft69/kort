import random
from html import escape
from urllib.parse import quote

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

PLEADING = [
    "Are you sure? 🥺",
    "Please? I even debugged this code for you…",
    "I promise I'll be a gentleman. 🌹",
    "I'll treat you to milk tea! 🧋",
    "Last chance… my heart has a stack overflow. 💔",
]
DATES = ["Milk tea and a walk 🧋", "Dinner at a cozy restaurant 🍝",
         "Movie night 🎬", "Sunset by the sea 🌅"]


def page(body: str) -> HTMLResponse:
    """Wrap any content in a basic styled HTML page."""
    return HTMLResponse(f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>May I court you?</title>
      <style>
        body {{ font-family: sans-serif; text-align: center; margin-top: 15vh; }}
        a, button {{ display: inline-block; margin: 8px; padding: 12px 24px;
                     border-radius: 10px; border: 0; background: #e5446d;
                     color: white; text-decoration: none; font-size: 1rem; }}
        a.no {{ background: #ddd; color: #333; }}
        input {{ padding: 10px; font-size: 1rem; }}
      </style>
    </head>
    <body>{body}</body>
    </html>""")


@app.get("/")
def home():
    return page("""
        <h1>Hi there! 👋</h1>
        <p>What's your name?</p>
        <form action="/ask">
          <input name="name" placeholder="Your name" required>
          <button>Continue</button>
        </form>""")


@app.get("/ask")
def ask(name: str, attempt: int = 0):
    raw = name.strip().title()
    safe = escape(raw)      # protects against HTML injection
    link = quote(raw)       # makes the name safe inside a URL

    if attempt == 0:
        note = ""
    elif attempt <= len(PLEADING):
        note = PLEADING[attempt - 1]
    else:
        note = "The “No” button has been deleted. 😌"

    no_link = ""
    if attempt <= len(PLEADING):
        no_link = f'<a class="no" href="/ask?name={link}&attempt={attempt + 1}">No</a>'

    return page(f"""
        <h1>{safe}, may I court you? 🌹</h1>
        <p>{note}</p>
        <a href="/yes?name={link}">Yes 💖</a>
        {no_link}""")


@app.get("/yes")
def yes(name: str):
    safe = escape(name.strip().title())
    return page(f"""
        <h1>🎉 YES!! 🎉</h1>
        <p>Thank you, {safe}! You just made me the happiest person.</p>
        <p>First date idea: {random.choice(DATES)}</p>
        <p>The courtship begins… ❤️</p>""")