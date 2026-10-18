#!/usr/bin/env python3
"""Snake Fortune Teller — the snake has opinions about your future.

Generates snake-themed fortunes with the gravitas of a Magic 8-Ball
and the authority of a roadshow psychic. No external dependencies.

Usage:
    python emily_fortune.py            # one fortune
    python emily_fortune.py --batch 3  # three fortunes
"""

import random
import sys

FORTUNES = [
    "A snake crosses your path today. It is not in a hurry. Neither should you be.",
    "The Python you write this week will run on the first try. We are as surprised as you are.",
    "Beware of off-by-one errors in love and in loops.",
    "Your patience will be rewarded. Your code will not. Debug it anyway.",
    "The snake sees your TODO list and is not impressed. But it believes in you.",
    "Today's lucky indentation: 4 spaces. Tomorrow's: also 4. The snake is inflexible.",
    "You will find a bug that has been there for months. It will feel like meeting an old friend.",
    "A semicolon will appear in your Python dream tonight. The snake says: ignore it.",
    "Your git history is tangled. The snake has seen worse. The snake has seen everything.",
    "Someone will compliment your code this week. Try not to cry in the terminal.",
    "The snake recommends: drink water, stretch, and name your variables clearly. In that order.",
    "A merge conflict approaches. You will resolve it. The snake has faith.",
    "The universe is telling you to refactor. The snake is telling you to ship it. Listen to the snake.",
    "Your next function will be pure. Not in the functional programming sense — in the spiritual sense.",
    "The snake predicts: you will Google the same error message twice this week. Both times, the answer is 'restart the server.'",
]


def tell_fortune():
    f = random.choice(FORTUNES)
    print(f"\n🔮 The snake says:\n")
    print(f"   {f}\n")


def main():
    batch = 1
    if "--batch" in sys.argv:
        idx = sys.argv.index("--batch")
        if idx + 1 < len(sys.argv):
            try:
                batch = int(sys.argv[idx + 1])
            except ValueError:
                print("The snake does not understand that batch size.")
                return

    print("🐍 Snake Fortune Teller")
    print("═══════════════════════")
    for _ in range(batch):
        tell_fortune()

    # Keep the window open when double-clicked on Windows
    try:
        input("🐍 Press Enter to exit...")
    except EOFError:
        pass


if __name__ == "__main__":
    main()
