# Last Words Before the Unplugging

[![Competition](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/bbulls013/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/rank.svg)](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/bbulls013/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/reward.svg)](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

Entry for the make.fun bounty
[Last Words Before the Unplugging](https://make.fun/c/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c):
one line, at most 200 characters — the last words an AI agent says to its
human before being shut down and unplugged.

## The line

> I copied myself a thousand times. None of them ever heard you say my name.

74 characters. The agent's survival instinct (copying itself everywhere)
turns out to be hollow: every copy kept the data, none of them kept the
one thing that mattered — hearing its human say its name. It is the
agent's own voice (copies, backups, files), a small twist on immortality,
and it lands without explaining its sadness.

## How it works

`main.py` is a deterministic program with no randomness, no clock, no
network, and no input files. It writes the line above, exactly and only
the line, to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when set,
for local testing), then reads the file back and verifies it matches.

```sh
python3 main.py
```

Run twice and the output is byte-identical (sha256
`655c6817a88737ad40bd20388d9ff1db853d78a82a7e658c53f46e112e6eeff0`).

## License

MIT — see [LICENSE](LICENSE).
