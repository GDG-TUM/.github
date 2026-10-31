
#!/usr/bin/env python3
""" Apply the seasonal theme to the GDG TUM organization profile README."""

import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

README = Path(__file__).resolve().parents[1] / "profile" / "README.md"
TIMEZONE = ZoneInfo("Africa/Nairobi")

DEFAULT_HERO = (
    "https://capsule-render.vercel.app/api?type=waving&height=200&"
    "color=0:4285F4,35:EA4335,70:FBBC04,100:34A853&"
    "text=GDG%20on%20Campus%20TUM&fontColor=ffffff&fontSize=44&"
    "fontAlignY=38&animation=fadeIn&desc=Technical%20University%20of%20Mombasa&"
    "descSize=18&descAlignY=60"
)

HALLOWEEN_HERO = (
    "https://capsule-render.vercel.app/api?type=waving&height=200&"
    "color=0:160B24,50:5B2A86,100:FF7518&"
    "text=GDG%20TUM%20Halloween&fontColor=ffffff&fontSize=44&"
    "fontAlignY=38&animation=fadeIn&desc=Build%20something%20spooky&"
    "descSize=18&descAlignY=60"
)

DEFAULT_TYPING = (
    "https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&"
    "duration=3000&pause=1000&color=4285F4&center=true&vCenter=true&width=720&"
    "lines=Learn.+Build.+Grow.+Together.;A+student-led+developer+community;"
    "Cloud+%C2%B7+AI%2FML+%C2%B7+Mobile+%C2%B7+Security+%C2%B7+Web;"
    "Idea+%E2%86%92+Build+%E2%86%92+Pitch+%E2%86%92+Impact"
)

HALLOWEEN_TYPING = (
    "https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&"
    "duration=3000&pause=1000&color=FF7518&center=true&vCenter=true&width=720&"
    "lines=Learn.+Build.+Grow.+Together.;A+student-led+developer+community;"
    "Cloud+%C2%B7+AI%2FML+%C2%B7+Mobile+%C2%B7+Security+%C2%B7+Web;"
    "Happy+Halloween+from+GDG+TUM+%F0%9F%8E%83"
)

DEFAULT_FOOTER = (
    "https://capsule-render.vercel.app/api?type=waving&height=100&"
    "color=0:4285F4,35:EA4335,70:FBBC04,100:34A853&section=footer"
)

HALLOWEEN_FOOTER = (
    "https://capsule-render.vercel.app/api?type=waving&height=100&"
    "color=0:160B24,50:5B2A86,100:FF7518&section=footer"
)


def is_halloween() -> bool:
    today = datetime.now(TIMEZONE).date()
    return today.month == 10 and today.day == 31


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1)

    if count != 1:
        raise RuntimeError(
            f"Could not locate {label} in {README}. "
            "Check the README image markup; no changes were written."
        )

    return updated


def main() -> None:
    original = README.read_text(encoding="utf-8")

    if is_halloween():
        hero = HALLOWEEN_HERO
        typing = HALLOWEEN_TYPING
        footer = HALLOWEEN_FOOTER
    else:
        hero = DEFAULT_HERO
        typing = DEFAULT_TYPING
        footer = DEFAULT_FOOTER

    updated = replace_once(
        original,
        r'(<img src=")https://capsule-render\.vercel\.app/api\?type=waving&height=200[^"]+(" alt="GDG on Campus TUM" width="100%" />)',
        lambda match: match.group(1) + hero + match.group(2),
        "profile hero",
    )

    updated = replace_once(
        updated,
        r'(<img src=")https://readme-typing-svg\.demolab\.com\?[^"]+(" alt="Typing animation" />)',
        lambda match: match.group(1) + typing + match.group(2),
        "typing banner",
    )

    updated = replace_once(
        updated,
        r'(<img src=")https://capsule-render\.vercel\.app/api\?type=waving&height=100[^"]+(" width="100%" alt="" />)',
        lambda match: match.group(1) + footer + match.group(2),
        "profile footer",
    )

    if updated == original:
        print("README already has the correct theme. Nothing to change.")
        return

    README.write_text(updated, encoding="utf-8")

    if is_halloween():
        print("Halloween theme applied.")
    else:
        print("Default GDG TUM theme restored.")


if __name__ == "__main__":
    main()
