import random

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

DATES = [
    "Milk tea and a walk 🧋",
    "Dinner at a cozy restaurant 🍝",
    "Movie night 🎬",
    "Sunset by the sea 🌅",
    "Coffee and a bookstore date 📚",
]

HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>May I court you?</title>
<style>
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:grid;place-items:center;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:#fff;
  background:linear-gradient(135deg,#ff758c,#ff7eb3,#a18cd1,#fbc2eb);background-size:400% 400%;animation:bg 12s ease infinite;overflow:hidden}
@keyframes bg{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
#card{position:relative;z-index:2;width:min(92vw,460px);padding:32px 26px;border-radius:24px;text-align:center;
  background:rgba(255,255,255,.2);backdrop-filter:blur(12px);box-shadow:0 20px 60px rgba(0,0,0,.2);animation:pop .7s ease}
@keyframes pop{from{opacity:0;transform:translateY(24px) scale(.95)}to{opacity:1;transform:none}}
h1{margin:0 0 14px;font-size:1.8rem}
p{font-size:1.1rem;line-height:1.5;margin:0 0 12px}
input{width:100%;font:inherit;padding:12px 14px;border-radius:14px;border:0;margin:8px 0 14px;text-align:center;color:#3a1f2b}
input:focus{outline:3px solid #fff}
button{font:inherit;font-weight:700;border:0;border-radius:14px;padding:12px 26px;cursor:pointer;transition:transform .2s}
button:hover{transform:scale(1.06)}
.yes{background:#fff;color:#e5446d;animation:pulse 1.4s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(255,255,255,.7)}100%{box-shadow:0 0 0 16px rgba(255,255,255,0)}}
.no{background:rgba(0,0,0,.28);color:#fff}
#arena{position:relative;height:180px;display:flex;align-items:center;justify-content:center;gap:14px}
#arena .no{transition:left .25s,top .25s}
.float{position:fixed;bottom:-60px;z-index:1;opacity:.7;pointer-events:none;animation:rise linear infinite}
@keyframes rise{to{transform:translateY(-120vh) rotate(40deg)}}
.shake{animation:shake .4s}
@keyframes shake{25%{transform:translateX(-10px)}75%{transform:translateX(10px)}}
.conf{position:fixed;top:-20px;width:10px;height:14px;z-index:5;pointer-events:none;animation:fall linear forwards}
@keyframes fall{to{transform:translateY(112vh) rotate(720deg)}}
</style>
</head>
<body>
<div id="card"></div>
<script>
const card = document.getElementById("card");
let name = "Baby";
const sleep = ms => new Promise(r => setTimeout(r, ms));

// floating background hearts
["💖","💕","🌹","✨","💗","🌸"].forEach((e, i) => {
  for (let k = 0; k < 3; k++) {
    const s = document.createElement("span");
    s.className = "float";
    s.textContent = e;
    s.style.left = Math.random() * 96 + "vw";
    s.style.fontSize = 16 + Math.random() * 26 + "px";
    s.style.animationDuration = 9 + Math.random() * 8 + "s";
    s.style.animationDelay = -Math.random() * 12 + "s";
    document.body.appendChild(s);
  }
});

async function say(text, tag = "p") {
  const el = document.createElement(tag);
  card.appendChild(el);
  for (const ch of text) { el.textContent += ch; await sleep(26); }
  await sleep(250);
  return el;
}
function btn(label, cls, fn) {
  const b = document.createElement("button");
  b.textContent = label; b.className = cls; b.onclick = fn;
  return b;
}
function confetti() {
  const colors = ["#fff", "#ffd1dc", "#ffe066", "#ff4d6d", "#b388ff"];
  for (let i = 0; i < 90; i++) {
    const c = document.createElement("div");
    c.className = "conf";
    c.style.left = Math.random() * 100 + "vw";
    c.style.background = colors[i % colors.length];
    c.style.animationDuration = 2 + Math.random() * 2.5 + "s";
    c.style.animationDelay = Math.random() * 0.8 + "s";
    document.body.appendChild(c);
    setTimeout(() => c.remove(), 5500);
  }
}

async function start() {
  card.innerHTML = "";
  await say("Hi babyyy hehehehe 👋", "h1");
  card.appendChild(btn("Continue", "yes", intro));
}
async function intro() {
  card.innerHTML = "";
  await say("Baby, can I ask you something? ✨", "h1");
  const row = document.createElement("div");
  row.append(
    btn("Yes", "yes", main),
    btn("No", "no", async () => { await say("Aww, okay… 😢"); main(); })
  );
  row.style.display = "flex"; row.style.gap = "12px"; row.style.justifyContent = "center";
  card.appendChild(row);
}

async function main() {
  card.innerHTML = "";
  await say(`${name}, you make my day better without even trying.`);
  await say("I’d really like to get to know you more, the proper way.");
  await say(`${name}, may I court you? 🌹`, "h1");

  const pleading = [
    "Are you sure? 🥺",
    "Please? I even debugged this code for you…",
    "I promise I’ll be a gentleman. 🌹",
    "I’ll treat you to milk tea! 🧋",
    "Last chance… my heart has a stack overflow. 💔",
  ];
  const arena = document.createElement("div");
  arena.id = "arena";
  const note = document.createElement("p");
  const yes = btn("Yes 💖", "yes", celebrate);
  const no = btn("No", "no", () => {});
  arena.append(yes, no);
  card.append(arena, note);

  let attempts = 0, last = 0;
  const dodge = e => {
    if (e) e.preventDefault();
    const now = Date.now();
    if (now - last < 300) return;
    last = now;
    attempts++;
    card.classList.remove("shake"); void card.offsetWidth; card.classList.add("shake");
    if (attempts > pleading.length) {
      no.remove();
      note.textContent = "The “No” button has been deleted. 😌";
    } else {
      note.textContent = pleading[attempts - 1];
      no.style.position = "absolute";
      no.style.left = Math.random() * (arena.clientWidth - no.offsetWidth) + "px";
      no.style.top = Math.random() * (arena.clientHeight - no.offsetHeight) + "px";
    }
    yes.style.transform = `scale(${1 + attempts * 0.14})`;
  };
  no.addEventListener("pointerenter", dodge);
  no.addEventListener("pointerdown", dodge);
  no.addEventListener("click", dodge);
}

async function celebrate() {
  card.innerHTML = "";
  confetti();
  await say("🎉 YES!! 🎉", "h1");
  await say(`Thank you, ${name}! You just made me the happiest person.`);
  await say("Let me plan the first date… 🌹");
  let idea = "Milk tea and a walk 🧋";
  try {
    const r = await fetch("/api/date");
    idea = (await r.json()).idea;   // this comes from your Python code
  } catch (e) {}
  await say("First date idea: " + idea);
  await say("The courtship begins… ❤️", "h1");
  confetti();
}

start();
</script>
</body>
</html>
"""


@app.get("/")
def home():
    return HTMLResponse(HTML)


@app.get("/api/date")
def date_idea():
    return {"idea": random.choice(DATES)}