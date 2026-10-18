#!/usr/bin/env python3
"""Snake Haiku Generator — the snake demanded poetry.

Generates haiku about snakes using a constrained vocabulary and a
5-7-5 syllable template system. No external dependencies, because
the snake is a purist.

Usage:
    python emily_haiku.py            # one haiku
    python emily_haiku.py --batch 5  # five haikus
"""

import random
import sys

# 5-syllable lines
FIVE = [
    "Soft scales in the grass",
    "Coiled in gentle loops",
    "Hissing at the moon",
    "Warm rock in the sun",
    "Quiet in the leaves",
    "Slither through the code",
    "Small fang, tiny bite",
    "Curled up on the desk",
]

# 7-syllable lines
SEVEN = [
    "Python loops that never end",
    "Glide along the forest floor",
    "Forked tongue tasting empty air",
    "No legs needed for this dance",
    "Shedding skin to start again",
    "ASCII art but make it move",
    "Every complement a hiss",
    "Sleeping where the warm bytes are",
]


def count_syllables(line):
    """Rough syllable counter — not perfect, but the snake doesn't grade."""
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for ch in line.lower():
        if ch in vowels:
            if not prev_vowel:
                count += 1
            prev_vowel = True
        else:
            prev_vowel = False
    # silent 'e' at end
    if line.rstrip() and line.rstrip()[-1] == 'e':
        count = max(1, count - 1)
    return count


def haiku():
    """Generate one snake haiku. Returns three lines."""
    return [
        random.choice(FIVE),
        random.choice(SEVEN),
        random.choice(FIVE),
    ]


def print_haiku():
    lines = haiku()
    for line in lines:
        print(line)
    print()  # breathing room


def main():
    args = sys.argv[1:]
    count = 1

    if "--batch" in args:
        idx = args.index("--batch")
        if idx + 1 < len(args):
            count = int(args[idx + 1])

    print("🐍 Snake Haiku Generator v0.1.0")
    print("═" * 30)
    print()
    for _ in range(count):
        print_haiku()

    # Keep the window open when double-clicked on Windows
    try:
        input("🐍 Press Enter to exit...")
    except EOFError:
        pass


if __name__ == "__main__":
    main()
