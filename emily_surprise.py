#!/usr/bin/env python3
"""Emily's Playful Python Arcade.

A polished-but-playful CLI mini-game collection for the hiss-terical-python repo.

Usage:
  python3 emily_surprise.py
  python3 emily_surprise.py --mini
  python3 emily_surprise.py --leaderboard
"""

from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Dict, List

EMILY = "Emily"

def _get_score_file_path() -> Path:
    """Return a per-user writable location for the leaderboard file."""
    try:
        from platformdirs import user_data_dir
    except Exception:
        user_data_dir = None

    if user_data_dir:
        base = Path(user_data_dir("hiss-terical-python", roaming=False))
    else:
        if os.name == "nt":
            base = Path(
                os.environ.get("LOCALAPPDATA")
                or os.environ.get("APPDATA")
                or str(Path.home())
            )
        else:
            xdg_data_home = os.environ.get("XDG_DATA_HOME")
            if xdg_data_home:
                base = Path(xdg_data_home)
            elif sys.platform == "darwin":
                base = Path.home() / "Library" / "Application Support"
            else:
                base = Path.home() / ".local" / "share"

            base = base / "hiss-terical-python"

    try:
        base.mkdir(parents=True, exist_ok=True)
    except OSError:
        base = Path.home()

    return base / ".hiss_scores.json"


SCORE_FILE = _get_score_file_path()

TITLE_ART = r"""
    ___ _     _     _     _     _     _     _     _     _     _
   / _ \ | |  | |   | |   | |   | |   | |   | |   | |   | |
  / /_\ \| |__| |__ | |__| |__| |__| |__| |__| |__| |__| |__
  |  _  || '_ \ '_ \| '_ \ '_ \ '_ \ '_ \ '_ \ '_ \ '_ \ '_ \
  | | | || | | | | | | | | | | | | | | | | | | | | | | | |
  |_| |_||_| |_|_| |_|_| |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|

           _   _   _   _   _   _   _   _   _   _   _   _
          | |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |
          |  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ |
          | | | | | | | | | | | | | | | | | | | | | | | | |
          |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|

                   ~ hiss-terical-python arcade ~
"""

SNAKE = r"""
          _
         / )
        / /
       / /       _
      / /  ___  //\
     / /  / _ \/ / /
    / /__/ /_)  / /
   (____/\___/ /_/   ~ hello, Emily ~
"""

COMPLIMENTS = [
    "You write code that makes the world a little brighter.",
    "Your debugging skills are dangerously sharp.",
    "You turn coffee into elegant logic.",
    "You make Python look like poetry.",
    "Pair-programming with you is an adventure.",
    "Your creativity is the secret power-up.",
]

POEMS = [
    "Roses are #FF0000, violets are #0000FF, she writes in Python, and the tests all pass too.",
    "Indentation whispers, a colon glows — in Emily's code the magic flows.",
    "When the terminal brightens, you know the code is right, and the whole room feels lighter.",
]

QUOTES = [
    "Simplicity is the soul of good design. — Anonymous",
    "Programs must be written for people to read, and only incidentally for machines to execute. — Harold Abelson",
    "Good code is like a good joke — it has perfect timing. — Emily, probably.",
]

SYMBOLS = ["🐍", "✨", "🎉", "💻", "☕", "🌈", "🦋"]


def slow_print(text: str, delay: float = 0.03) -> None:
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def sound_effect(kind: str) -> None:
    sounds = {
        "coin": ["*ding*", "*ding*", "BONK!"],
        "win": ["BEEP!", "BOOP!", "PING!"],
        "lose": ["hiss...", "tink...", "plip."],
        "menu": ["tap-tap", "whoosh", "zzt!"],
    }
    effect = sounds.get(kind, ["blip"])
    print(random.choice(effect))


def clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def load_scores() -> Dict[str, List[Dict[str, object]]]:
    try:
        if not SCORE_FILE.exists():
            return {}
        data = json.loads(SCORE_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except (json.JSONDecodeError, OSError):
        pass
    return {}


def save_scores(scores: Dict[str, List[Dict[str, object]]]) -> None:
    try:
        SCORE_FILE.write_text(json.dumps(scores, indent=2), encoding="utf-8")
    except OSError as exc:
        print(f"Warning: couldn't save scores to {SCORE_FILE}: {exc}")


def record_score(game_name: str, score: int) -> None:
    scores = load_scores()
    records = scores.setdefault(game_name, [])
    records.append({
        "player": EMILY,
        "score": int(score),
        "timestamp": time.time(),
    })
    records = sorted(records, key=lambda item: int(item["score"]), reverse=True)[:10]
    scores[game_name] = records
    save_scores(scores)
    sound_effect("coin")


def show_leaderboard() -> None:
    scores = load_scores()
    if not scores:
        slow_print("No scores yet — be the first to set the arcade record! ✨")
        return

    slow_print("\nTop scores — hiss-terical-python arcade", 0.01)
    for game_name, entries in sorted(scores.items()):
        print(f"\n{game_name}:")
        for index, entry in enumerate(entries[:5], start=1):
            stamp = time.strftime("%Y-%m-%d %H:%M", time.localtime(float(entry["timestamp"])))
            print(f"  {index}. {entry['score']} points — {entry['player']} ({stamp})")


def show_snake() -> None:
    print(SNAKE)
    sound_effect("win")


def compliment() -> None:
    c = random.choice(COMPLIMENTS)
    slow_print(f"Hey {EMILY} — {c}", 0.02)


def poem() -> None:
    p = random.choice(POEMS)
    slow_print(p, 0.02)


def quote() -> None:
    q = random.choice(QUOTES)
    slow_print(q, 0.02)


def number_guesser() -> None:
    slow_print("Number Guesser — I am hiding a number between 1 and 30. Try to guess it!", 0.01)
    secret = random.randint(1, 30)
    attempts = 0
    while True:
        attempts += 1
        try:
            guess = int(input("Your guess: ").strip())
        except ValueError:
            print("Please enter a number.")
            continue
        if guess < secret:
            print("Too low! Sneak up higher.")
        elif guess > secret:
            print("Too high! Coil back down.")
        else:
            points = max(10, 100 - (attempts * 7))
            slow_print(f"You got it in {attempts} tries! Score: {points} points. Nice slither, {EMILY}! 🐍", 0.02)
            record_score("Number Guesser", points)
            return


def memory_sequence() -> None:
    slow_print("Memory Chain — watch the sequence and repeat it exactly.", 0.01)
    length = 3
    rounds_won = 0
    for _ in range(5):
        seq = [random.choice(SYMBOLS) for _ in range(length)]
        slow_print(f"Round {rounds_won + 1}: Watch closely...", 0.01)
        print(" ".join(seq), flush=True)
        time.sleep(0.7)
        print("\r" + " " * 80, end="", flush=True)
        answer = input("Repeat it: ").strip().split()
        if answer == seq:
            rounds_won += 1
            slow_print("Correct! Round cleared.", 0.01)
            length += 1
            sound_effect("win")
        else:
            slow_print(f"Nope! The sequence was {' '.join(seq)}. You reached {rounds_won} rounds.", 0.02)
            points = max(0, rounds_won * 25)
            record_score("Memory Chain", points)
            return
    points = rounds_won * 35 + length * 5
    slow_print(f"Amazing memory, {EMILY}! You cleared the full challenge. Score: {points} points. ✨", 0.02)
    record_score("Memory Chain", points)


def typing_sprint() -> None:
    slow_print("Typing Sprint — press Enter as fast as you can when GO appears!", 0.01)
    time.sleep(1)
    slow_print("Ready...")
    time.sleep(random.uniform(1.0, 3.0))
    slow_print("GO!", 0.01)
    start = time.time()
    input()
    elapsed = time.time() - start
    points = max(0, int(120 - (elapsed * 20)))
    slow_print(f"You reacted in {elapsed:.3f}s. Score: {points} points. Quick fingers! 🎉", 0.01)
    record_score("Typing Sprint", points)


def rps_slither() -> None:
    slow_print("RPS Slither — Fang beats Coil, Coil beats Hiss, Hiss beats Fang. Best of 5!", 0.01)
    options = {"1": "Fang", "2": "Coil", "3": "Hiss"}
    beats = {"Fang": "Coil", "Coil": "Hiss", "Hiss": "Fang"}
    player_wins = 0
    cpu_wins = 0
    rounds_played = 0
    while rounds_played < 5 and max(player_wins, cpu_wins) < 3:
        for key, value in options.items():
            print(f" {key}) {value}")
        choice = input("Pick 1-3 (or q to quit): ").strip().lower()
        if choice == "q":
            return
        if choice not in options:
            print("Pick 1, 2, or 3.")
            continue
        player = options[choice]
        comp = random.choice(list(options.values()))
        slow_print(f"You chose {player}; I chose {comp}.", 0.02)
        if player == comp:
            slow_print("Tie! No points, but no panic.")
        elif beats[player] == comp:
            player_wins += 1
            slow_print(f"You win this round, {EMILY}! {player} > {comp}")
            sound_effect("win")
        else:
            cpu_wins += 1
            slow_print(f"I win this round. {comp} > {player} — better luck next time!")
            sound_effect("lose")
        rounds_played += 1

    if player_wins > cpu_wins:
        points = player_wins * 50 + 10
        slow_print(f"You win the series {player_wins} to {cpu_wins}! Score: {points} points. 🎊", 0.02)
    else:
        points = cpu_wins * 35
        slow_print(f"The CPU takes the series {cpu_wins} to {player_wins}. Score: {points} points. Better luck next round!", 0.02)
    record_score("RPS Slither", points)


def mini_game_menu() -> None:
    while True:
        print("\nBonus Mini-Games Arcade")
        print("  1) Number Guesser")
        print("  2) Memory Chain")
        print("  3) Typing Sprint")
        print("  4) RPS Slither")
        print("  5) View Leaderboard")
        print("  6) Back to main menu")
        choice = input("Choice: ").strip()
        if choice == "1":
            number_guesser()
        elif choice == "2":
            memory_sequence()
        elif choice == "3":
            typing_sprint()
        elif choice == "4":
            rps_slither()
        elif choice == "5":
            show_leaderboard()
        elif choice == "6":
            break
        else:
            print("Choose a valid option.")


def start_screen() -> None:
    clear_screen()
    slow_print(TITLE_ART, 0.005)
    time.sleep(0.2)
    sound_effect("menu")
    print("Welcome to the hiss-terical-python arcade.")
    print("Built for Emily, with a little chaos, a little code, and a lot of personality.")


def main_menu() -> None:
    while True:
        print("\nMain Menu")
        print("  1) View the hiss-terical snake")
        print("  2) Get a compliment")
        print("  3) Read a tiny poem")
        print("  4) Read a wisdom quote")
        print("  5) Bonus mini-games")
        print("  6) View leaderboard")
        print("  7) Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            show_snake()
        elif choice == "2":
            compliment()
        elif choice == "3":
            poem()
        elif choice == "4":
            quote()
        elif choice == "5":
            mini_game_menu()
        elif choice == "6":
            show_leaderboard()
        elif choice == "7":
            slow_print(f"Thanks for visiting the arcade, {EMILY}! 🙃")
            break
        else:
            print("Try a valid menu option.")


def main() -> None:
    start_screen()
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] in {"-c", "--compliment"}:
                compliment()
                return
            if sys.argv[1] in {"-m", "--mini"}:
                mini_game_menu()
                return
            if sys.argv[1] in {"-l", "--leaderboard"}:
                show_leaderboard()
                return
        main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nThe arcade session ended. See you next time, snake friend! 🐍")


if __name__ == "__main__":
    main()
