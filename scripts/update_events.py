#!/usr/bin/env python3
"""Regenerate the events sections of the org profile README from data/events.yml."""
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "profile" / "README.md"
DATA = ROOT / "data" / "events.yml"
TZ = ZoneInfo("Africa/Nairobi")
MAX_PAST = 8

TRACKS = {
    "cloud": ("☁️ Cloud", "4285F4"),
    "ai-ml": ("🤖 AI / ML", "EA4335"),
    "mobile": ("📱 Mobile", "34A853"),
    "cybersecurity": ("🔐 Cybersecurity", "FBBC04"),
    "women-in-tech": ("👩‍💻 Women in Tech", "EA4335"),
    "hackathons": ("🏆 Hackathons", "EA4335"),
    "web": ("🌐 Web", "4285F4"),
    "general": ("🎉 Community", "4285F4"),
}


def load_events():
    raw = yaml.safe_load(DATA.read_text(encoding="utf-8")) or {}
    events = []
    for e in raw.get("events", []):
        d = e["date"]
        if isinstance(d, str):
            d = datetime.strptime(d, "%Y-%m-%d").date()
        e["date"] = d
        events.append(e)
    return events


def fmt_date(d: date) -> str:
    return f"{d.day} {d.strftime('%b')} {d.year}"


def badge(text: str, color: str) -> str:
    safe = text.replace("-", "--").replace("_", "__")
    return f"![{text}](https://img.shields.io/badge/{quote(safe, safe='')}-{color}?style=for-the-badge)"


def track_info(e):
    return TRACKS.get(e.get("track", "general"), TRACKS["general"])


def render_featured(e) -> str:
    label, color = track_info(e)
    track_text = f"{label} · {e['series']}" if e.get("series") else label
    badges = [badge(f"📆 {fmt_date(e['date'])}", "4285F4")]
    if e.get("free", True):
        badges.append(badge("Free registration", "34A853"))
    badges.append(badge(track_text, color))

    lines = [
        "<table>", "  <tr>", "    <td>", "",
        "\n".join(badges), "",
        f"### {e.get('emoji', '📌')} {e['title']}", "",
    ]
    if e.get("venue") or e.get("time"):
        bits = []
        if e.get("venue"):
            bits.append(f"📍 {e['venue']}")
        if e.get("time"):
            bits.append(f"🕑 {e['time']}")
        lines += [" · ".join(bits), ""]
    if e.get("description"):
        lines += [" ".join(str(e["description"]).split()), ""]
    if e.get("learn"):
        lines += ["**You'll learn how to:**"] + [f"- {item}" for item in e["learn"]] + [""]
    lines += [
        f"[**👉 Register{' for free' if e.get('free', True) else ''}**]({e['url']})", "",
        "</td>", "  </tr>", "</table>",
    ]
    return "\n".join(lines)


def render_upcoming(upcoming) -> str:
    if not upcoming:
        return "_No events scheduled right now. Follow us on LinkedIn to hear about the next session._"
    out = [render_featured(upcoming[0])]
    if len(upcoming) > 1:
        out += ["", "**Also coming up**", "", "| Date | Event | Track |", "|:-----|:------|:------|"]
        for e in upcoming[1:]:
            out.append(f"| {fmt_date(e['date'])} | [{e['title']}]({e['url']}) | {track_info(e)[0]} |")
    return "\n".join(out)


def render_past(past) -> str:
    if not past:
        return "_Our past events will appear here._"
    out = ["| Date | Event | Track |", "|:-----|:------|:------|"]
    for e in past[:MAX_PAST]:
        out.append(f"| {fmt_date(e['date'])} | [{e['title']}]({e['url']}) | {track_info(e)[0]} |")
    return "\n".join(out)


def replace_block(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"Markers for {name} not found in {README}")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    today = datetime.now(TZ).date()
    events = load_events()
    upcoming = sorted((e for e in events if e["date"] >= today), key=lambda e: e["date"])
    past = sorted((e for e in events if e["date"] < today), key=lambda e: e["date"], reverse=True)

    text = README.read_text(encoding="utf-8")
    new = replace_block(text, "UPCOMING", render_upcoming(upcoming))
    new = replace_block(new, "PAST", render_past(past))

    if new != text:
        README.write_text(new, encoding="utf-8")
        print("README updated.")
    else:
        print("No changes.")


if __name__ == "__main__":
    main()
