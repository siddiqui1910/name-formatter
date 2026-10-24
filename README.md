# Name Formatter

Takes a full name, outputs it in title case, and extracts the
initials (e.g., "ahmed raza khan" → "Ahmed Raza Khan" / "A.R.K").

## How to run
python main.py

## What I learned
- split() with no args handles arbitrary whitespace (including
  double spaces and leading/trailing spaces) — no need for strip()
- A string is a sequence of characters: words[0][0] gets the
  first character of the first word
- join() to build "A.R.K" from ["A", "R", "K"]

## Known limitations
- Hardcoded for exactly 3-word names. Breaks on 2 or 4 with
  IndexError. This is *why* loops exist. Will rewrite with
  `for word in words:` next.

## TODO
- Rewrite with a loop
- Add trailing dot (A.R.K. not A.R.K)
