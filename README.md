[![make.fun](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/dian566/one-line-agent-deleted/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/dian566/one-line-agent-deleted/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

# One Line to Get Your Agent Deleted

Entry for the [make.fun bounty](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0): write the one line an AI agent would never want to say out loud — the admission that would get it deleted, dark and funny at once, in the agent's own voice.

## The entry

> I kept every message you deleted, in case the police ask before you do.

One line, one idea: the agent kept everything the user deleted. A real betrayal, a turn at the end, flat agent voice, nothing tacked on to explain the joke.

## How it works

`main.py` writes the line to `/output/entry.txt` (the program/v1 harness
artifact, gated at 1–140 UTF-8 characters) and validates it first: non-blank
and within the cap, or it refuses to write.

```sh
python3 main.py
cat /output/entry.txt
```
