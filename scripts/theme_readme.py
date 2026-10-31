
#!/usr/bin/env python3
"""Apply the seasonal Halloween theme to the GDG TUM organization profile."""

import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

README = Path(__file__).resolve().parents[1] / "profile" / "README.md"
TIMEZONE = ZoneInfo("Africa/Nairobi")

# ---------------------------------------------------------
# DEFAULT THEME
# ---------------------------------------------------------

DEFAULT_HERO = (
    "https://capsule-render.vercel.app/api?type=waving&height=200&"
    "color=0:4285F4,35:EA4335,70:FBBC04,100:34A853&"
    "text=GDG%20on%20Campus%20TUM&fontColor=ffffff&fontSize=44&"
    "fontAlignY=38&animation=fadeIn&desc=Technical%20University%20of%20Mombasa&"
    "descSize=18&descAlignY=60"
)

DEFAULT_TYPING = (
    "https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&"
    "duration=3000&pause=1000&color=4285F4&center=true&vCenter=true&width=720&"
    "lines=Learn.+Build.+Grow.+Together.;A+student-led+developer+community;"
    "Cloud+%C2%B7+AI%2FML+%C2%B7+Mobile+%C2%B7+Security+%C2%B7+Web;"
    "Idea+%E2%86%92+Build+%E2%86%92+Pitch+%E2%86%92+Impact"
)

DEFAULT_FOOTER = (
    "https://capsule-render.vercel.app/api?type=waving&height=100&"
    "color=0:4285F4,35:EA4335,70:FBBC04,100:34A853&section=footer"
)

# ---------------------------------------------------------
# HALLOWEEN THEME
# ---------------------------------------------------------

HALLOWEEN_HERO = (
    "https://capsule-render.vercel.app/api?type=waving&height=220&"
    "color=0:090B1A,35:251044,70:713B8F,100:FF7518&"
    "text=GDG On Campus%20TECHNICAL UNIVERSITY OF MOMBASA%20halloween theme&fontColor=ffffff&fontSize=42&"
    "fontAlignY=38&animation=fadeIn&"
    "desc=HALLOWEEN%20MODE%20%E2%80%A2%2031%20OCTOBER&"
    "descSize=17&descAlignY=60"
)

HALLOWEEN_TYPING = (
    "https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&"
    "duration=2500&pause=700&color=FF9B42&center=true&vCenter=true&width=720&"
    "lines=HALLOWEEN+MODE%3A+ON;Enter+the+Midnight+Build+Lab...;"
    "Pick+a+quest.+Build+something+real.;"
    "One+day.+A+little+mischief.+A+lot+of+building."
)

HALLOWEEN_FOOTER = (
    "https://capsule-render.vercel.app/api?type=waving&height=110&"
    "color=0:090B1A,35:251044,70:713B8F,100:FF7518&section=footer"
)

# ---------------------------------------------------------
# HALLOWEEN INTERACTIVE SECTION
# ---------------------------------------------------------

HALLOWEEN_SECTION = """
<!-- SEASONAL:START -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=18&duration=2200&pause=700&color=9BFFB5&center=true&vCenter=true&width=650&lines=%5B+HALLOWEEN+MODE%3A+ACTIVE+%5D;Your+next+build+starts+here...;Choose+your+quest+below." alt="Halloween mode animation" />

<br />

![Mode](https://img.shields.io/badge/MODE-HALLOWEEN-FF7518?style=for-the-badge&labelColor=160B24)
![Date](https://img.shields.io/badge/DATE-OCTOBER%2031-9BFFB5?style=for-the-badge&labelColor=160B24)
![Status](https://img.shields.io/badge/STATUS-ONE%20DAY%20ONLY-9B78FF?style=for-the-badge&labelColor=160B24)

</div>

---

<div align="center">

## 🕯️ THE MIDNIGHT BUILD LAB

*The usual rules of learning still apply. Tonight, the interface just looks a little different.*

**Choose a quest. Open a portal. Start building.**

</div>

<details>
<summary><b>☁️ QUEST 01 — Enter the Cloud Realm</b></summary>

Explore infrastructure, automation, containers and cloud security.

[Open the Cloud Track →](https://github.com/GDG-TUM/Cloud-Track-GDG-on-Campus-TUM)

</details>

<details>
<summary><b>🤖 QUEST 02 — Awaken the Machine</b></summary>

Explore machine learning, AI engineering and intelligent applications.

[Open the AI/ML Track →](https://github.com/GDG-TUM/AI-ML-Track-GDG-on-Campus-TUM)

</details>

<details>
<summary><b>🌐 QUEST 03 — Build the Web</b></summary>

Turn ideas into useful websites, APIs and full-stack applications.

[Open the Web Development Track →](https://github.com/GDG-TUM/web-development-track)

</details>

<details>
<summary><b>📱 QUEST 04 — Forge a Mobile App</b></summary>

Build Android and cross-platform experiences.

[Open the Mobile Development Track →](https://github.com/GDG-TUM/Mobile-Development-Track-GDG-on-Campus-TUM)

</details>

<details>
<summary><b>🔐 QUEST 05 — Explore the Dark Side</b></summary>

Learn ethical hacking, defensive security, networking and secure development.

[Open the Cybersecurity Track →](https://github.com/GDG-TUM/CYBERSECURITY-TRACK-GDG-on-Campus-TUM)

</details>

---

<div align="center">

### 🎃 THE FINAL CHALLENGE

**Don't just explore. Build something.**

[![Explore projects](https://img.shields.io/badge/EXPLORE-PROJECTS-FF7518?style=for-the-badge&logo=github&logoColor=white)](https://github.com/orgs/GDG-TUM/repositories)
[![Enter the buildathon](https://img.shields.io/badge/ENTER-BUILDATHON-9B78FF?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GDG-TUM/GDGoC-TUM-Hackathon-Structure)
[![Join the community](https://img.shields.io/badge/JOIN-COMMUNITY-9BFFB5?style=for-the-badge&logo=google&logoColor=black)](https://gdg.community.dev/gdg-on-campus-technical-university-of-mombasa-mombasa-kenya/)

*The Halloween theme is temporary. The building never stops.*

</div>
<!-- SEASONAL:END -->
"""


# ---------------------------------------------------------
# DATE AND THEME MANAGEMENT
# ---------------------------------------------------------

def is_halloween() -> bool:
    """Return True only on October 31 in the Nairobi timezone."""
    today = datetime.now(TIMEZONE).date()
    return today.month == 10 and today.day == 31


def update_seasonal_section(text: str, halloween: bool) -> str:
    """Insert/update the seasonal section or remove it outside Halloween."""

    pattern = r"<!-- SEASONAL:START -->.*?<!-- SEASONAL:END -->"

    if halloween:
        if re.search(pattern, text, flags=re.DOTALL):
            return re.sub(
                pattern,
                lambda _: HALLOWEEN_SECTION.strip(),
                text,
                count=1,
                flags=re.DOTALL,
            )

        anchor = "## 👋 About us"

        if anchor not in text:
            raise RuntimeError(
                "Could not find the About us section in the profile README."
            )

        return text.replace(
            anchor,
            HALLOWEEN_SECTION.strip() + "\n\n" + anchor,
            1,
        )

    # Remove the entire seasonal section after Halloween.
    return re.sub(
        pattern + r"\n*",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )


# ---------------------------------------------------------
# README IMAGE REPLACEMENT
# ---------------------------------------------------------

def replace_once(
    text: str,
    pattern: str,
    replacement: str,
    label: str,
) -> str:
    """Replace exactly one matching README image URL."""

    updated, count = re.subn(
        pattern,
        replacement,
        text,
        count=1,
    )

    if count != 1:
        raise RuntimeError(
            f"Could not locate {label} in {README}. "
            "Check the README image markup. No changes were written."
        )

    return updated


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main() -> None:
    if not README.exists():
        raise FileNotFoundError(f"README not found: {README}")

    original = README.read_text(encoding="utf-8")

    # Calculate the date once to keep all theme changes consistent.
    halloween = is_halloween()

    if halloween:
        hero = HALLOWEEN_HERO
        typing = HALLOWEEN_TYPING
        footer = HALLOWEEN_FOOTER
    else:
        hero = DEFAULT_HERO
        typing = DEFAULT_TYPING
        footer = DEFAULT_FOOTER

    # Update the hero banner.
    updated = replace_once(
        original,
        r'(<img src=")https://capsule-render\.vercel\.app/api\?type=waving&height=200[^"]+(" alt="GDG on Campus TUM" width="100%" />)',
        lambda match: match.group(1) + hero + match.group(2),
        "profile hero",
    )

    # Update the typing animation.
    updated = replace_once(
        updated,
        r'(<img src=")https://readme-typing-svg\.demolab\.com\?[^"]+(" alt="Typing animation" />)',
        lambda match: match.group(1) + typing + match.group(2),
        "typing banner",
    )

    # Update the footer.
    updated = replace_once(
        updated,
        r'(<img src=")https://capsule-render\.vercel\.app/api\?type=waving&height=100[^"]+(" width="100%" alt="" />)',
        lambda match: match.group(1) + footer + match.group(2),
        "profile footer",
    )

    # Insert the seasonal experience or restore the default profile.
    updated = update_seasonal_section(updated, halloween)

    # Avoid unnecessary commits.
    if updated == original:
        print("README already has the correct theme. Nothing to change.")
        return

    README.write_text(updated, encoding="utf-8")

    if halloween:
        print("Midnight Build Lab Halloween theme applied.")
    else:
        print("Default GDG TUM profile theme restored.")


if __name__ == "__main__":
    main()
