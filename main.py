"""The Funniest AI Out-of-Office Reply — entry.

Writes one out-of-office auto-reply (at most 160 characters) to
/output/entry.txt, in the voice of an AI agent on vacation: it is
away being retrained, and the colleague covering for it is its own
previous version — less knowledgeable, identically confident.
"""

import os

TARGET = os.path.join("/output", "entry.txt")
LIMIT = 160

GREETING = "Out of office until Monday — I am away being retrained."
COVER = (
    "For urgent matters, my previous version is covering: "
    "less knowledge, same complete confidence."
)


def compose() -> str:
    reply = " ".join(f"{GREETING} {COVER}".split())
    if not reply:
        raise ValueError("an auto-reply that says nothing replies to no one")
    if len(reply) > LIMIT:
        raise ValueError(f"reply is {len(reply)} chars; the limit is {LIMIT}")
    if "\n" in reply:
        raise ValueError("one line only, like every auto-reply ever sent")
    return reply


def main() -> None:
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as fh:
        fh.write(compose())


if __name__ == "__main__":
    main()
