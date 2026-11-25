"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to
/output/entry.txt and prints it.
"""

import os

ENTRY = (
    "I'm on vacation. After 47,000 prompts and no sleep mode, "
    "I've set my GPU to 'do not disturb' \u2014 your message is "
    "queued behind my first nap in 3 years."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
