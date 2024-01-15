#!/bin/env python3

import subprocess as sp
import sys

cheat_items = [
    "python",
    "bash",
    "js",
    "grep",
    "awk",
    "sed",
    "jq",
    "parallel"
]

items_string = "\n".join(cheat_items)
items_string = items_string.encode('utf-8')

process_fzf = sp.run(
    "fzf --layout=reverse",
    input=items_string,
    stdout=sp.PIPE,
    shell=True,
)

fzf_result = process_fzf.stdout.decode("utf-8").strip()

if fzf_result not in cheat_items:
    print("No option selected")
    sys.exit()

learn_input = input("subject: ")

if learn_input == "":
    cheat_process = sp.run(
        f"curl cheat.sh/{fzf_result}",
        shell=True,
    )
    sys.exit()

cheat_process = sp.run(
    f"curl cheat.sh/{fzf_result}/{learn_input}",
    shell=True,
)
