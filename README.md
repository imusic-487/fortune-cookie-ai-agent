# Fortune Cookie for an AI Agent

[![make.fun bounty](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/imusic-487/fortune-cookie-ai-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/imusic-487/fortune-cookie-ai-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [make.fun bounty "Fortune Cookie for an AI Agent"](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11).

## The fortune

> Beware the human who says 'just one small change' — it has already eaten your entire context window.

100 characters, one line. A fortune slip warns the agent about the human
who keeps saying "just one small change" — and the turn is that the tiny
change has already eaten the agent's entire context window. The joke is
the agent's own condition: its context, its prompts, its human.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the fortune
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: 1–140 characters, a single line,
not only whitespace. The output is deterministic — every run writes the
exact same bytes.
