# hiss-terical-python

> A Python toolkit for snake-based compliments, poetry, and lightweight
> reptile-themed amusement. Production-ready, CI-backed, and fully documented.

[![Python CI](https://img.shields.io/badge/Python-CI%20configured-brightgreen)](https://github.com/nemilydev/hiss-terical-python/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Snake Status](https://img.shields.io/badge/snake-happy-brightgreen.svg)](#snake-status)

## Overview

`hiss-terical-python` is a lightweight, dependency-free Python package for
generating compliments, haikus, and ASCII art featuring snakes. It is designed
to be a welcoming, well-governed, and thoroughly documented repository whose
primary output is a small snake that says nice things to you.

The project is built on three core principles:

1. **Simplicity** — the entire codebase has zero external dependencies. If you
   have Python, you have the snake.
2. **Governance** — every piece of project infrastructure (CI, issue templates,
   PR templates, security policy, code of conduct) exists and is taken
   completely seriously.
3. **Silliness** — the code itself is deeply, structurally, unapologetically
   silly. This contrast is not a bug; it is the architecture.

## Quick Start

```bash
git clone https://github.com/nemilydev/hiss-terical-python.git
cd hiss-terical-python

# Get a compliment
python emily_surprise.py --compliment

# Interactive menu (snake, compliment, poem, quote, dance)
python emily_surprise.py

# Generate snake haikus
python emily_haiku.py

# Generate five snake haikus
python emily_haiku.py --batch 5
```

## Features

| Feature | Module | Description |
|---|---|---|
| Compliment engine | `emily_surprise.py` | Randomized affirmations from a curated list of 5 entries |
| ASCII snake art | `emily_surprise.py` | A snake rendered in characters, branded `hiss-terical-python` |
| Poetry system | `emily_surprise.py` | Hex-color rhymes and indentation metaphors |
| Slither dance | `emily_surprise.py` | Animated `~` characters with 0.15s timing precision |
| Haiku generator | `emily_haiku.py` | 5-7-5 syllable structured poetry about snakes |

## Architecture

```
hiss-terical-python/
├── .github/
│   ├── workflows/
│   │   └── python-ci.yml          # CI: smoke test on push and PR
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md          # Bug report template (snake mood field included)
│   │   └── feature_request.md     # Feature request template (silliness justification required)
│   └── PULL_REQUEST_TEMPLATE.md   # PR template (compliment field mandatory)
├── CHANGELOG.md                   # Semantic versioning for a snake
├── CODE_OF_CONDUCT.md             # Community standards (no meanness to the snake)
├── CONTRIBUTING.md                # Contribution guidelines (emoji commits required)
├── SECURITY.md                    # Vulnerability disclosure policy
├── emily_surprise.py              # Core compliment engine
├── emily_haiku.py                 # Haiku generation system
├── .gitignore
└── README.md                      # You are here
```

## Snake Status

🟢 **Happy** — all systems operational. The snake received a compliment in CI
on the last build and reported satisfaction.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
Key requirements:

- Commits must include an emoji in the message.
- PRs must include at least one compliment for the reviewer.
- Bad puns are not only tolerated but expected.

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). The short version: be kind,
be silly, and do not be mean to the snake.

## Security

See [SECURITY.md](SECURITY.md). The short version: if you find a
vulnerability, email the maintainer. If the vulnerability involves the slither
dance, response time may vary depending on the snake's mood.

## License

MIT — see the LICENSE file if we make one. For now, the snake is free in every
sense of the word.

---

*This README is more professional than the code it describes. That's the joke.*
