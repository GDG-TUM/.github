# Contributing to GDG on Campus TUM

Thanks for wanting to contribute! 🎉 GDG on Campus TUM is a student community where we learn by building together. Every contribution counts, whether it's code, documentation, a bug report, a design, or a workshop idea. You don't need to be an expert. You just need to be willing to learn.

By taking part, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Ways to contribute

- **Code**: fix bugs, build features, improve existing projects
- **Documentation**: improve READMEs, write tutorials, fix typos
- **Learning resources**: add notes, labs, cheat sheets and study guides to the track repos
- **Design**: UI mockups, graphics, event posters
- **Ideas and feedback**: suggest workshops, projects or improvements
- **Review**: read other people's pull requests and leave kind, useful feedback
- **Testing**: try our projects and report what breaks

New here? Look for issues labelled **`good first issue`** or **`help wanted`**.

---

## Before you start

1. **Check existing issues and pull requests** so you don't duplicate work.
2. **Open an issue first** for anything bigger than a small fix, and describe what you want to do. Wait for a maintainer or track lead to confirm before you invest hours.
3. **Ask to be assigned** by commenting on the issue. One person per issue keeps things clear.
4. **Ask questions early.** Nobody here expects you to figure everything out alone.

---

## Getting started

### 1. Fork and clone
```bash
# Fork the repo on GitHub, then:
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
git remote add upstream https://github.com/GDG-TUM/<repo-name>.git
```

### 2. Create a branch
Never work directly on `main`. Name your branch after what you're doing:

```bash
git checkout -b <type>/<short-description>
```

Examples: `feat/add-login-page`, `fix/broken-readme-link`, `docs/cloud-track-guide`

### 3. Make your changes
- Keep changes focused. One pull request should do one thing.
- Follow the style and structure already used in the project.
- Update documentation if your change affects how something works.
- Test your changes before submitting.

### 4. Commit with clear messages
We follow a simple convention:

```
<type>: <short summary in present tense>
```

| Type | Use for |
|------|---------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructuring, no behaviour change |
| `test` | Adding or fixing tests |
| `chore` | Maintenance, dependencies, config |

Example: `docs: add setup steps to cloud track README`

### 5. Keep your fork up to date
```bash
git fetch upstream
git rebase upstream/main
```

### 6. Push and open a pull request
```bash
git push origin <your-branch-name>
```
Then open a pull request on GitHub against `main`.

---

## Pull request guidelines

A good pull request:
- Has a clear title and describes **what** changed and **why**
- Links the related issue (e.g. `Closes #12`)
- Is small enough to review in one sitting
- Includes screenshots for visual changes
- Passes any automated checks

**What happens next:**
1. A maintainer or track lead reviews your pull request, usually within a week.
2. They may request changes. This is normal and part of learning, not a judgment on you.
3. Once approved, a maintainer merges it.

---

## Reporting bugs

Open an issue and include:
- What you expected to happen
- What actually happened
- Steps to reproduce it
- Your environment (OS, browser, versions) where relevant
- Screenshots or error messages

---

## Suggesting ideas

Open an issue describing the idea, the problem it solves, and who it helps. You can also bring ideas to a chapter meeting or your track lead.

---

## Reporting security issues

**Please don't report security vulnerabilities in public issues.** Email **gdgtum@gmail.com** with the details, and we'll respond as soon as we can. Also never commit passwords, API keys, tokens or other secrets. If you do by accident, tell a maintainer right away so the secret can be revoked.

---

## Community expectations

- Be respectful, patient and encouraging, especially with beginners.
- Give feedback that is specific and kind.
- Credit other people's work.
- Ask for help when you're stuck.

---

## Recognition

Contributors are credited in project READMEs, highlighted at chapter events and shared in our community channels. Your contributions are also public on your GitHub profile, which makes them a good part of your portfolio.

---

## Need help?

- Ask your **track lead** or a core team member
- Comment on the relevant issue
- Email **gdgtum@gmail.com**

Thank you for helping us build a stronger developer community at TUM. 💙
