#!/bin/env python3

import subprocess as sp
import sys

main_menu = [
    "core-utils",
    "languages",
    "other"
]

main_menu_string = "\n".join(main_menu)
main_menu_string = main_menu_string.encode('utf-8')

process_main_menu = sp.run(
    "fzf --layout=reverse",
    input=main_menu_string,
    shell=True,
    stdout=sp.PIPE,
)

main_menu_value = process_main_menu.stdout.decode('utf-8').strip()

if main_menu_value == "languages":
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

    cheat_items_string = "\n".join(cheat_items)
    # Turn cheat_items_string into a bytes array so we can use it in
    # a subprocess
    cheat_items_string = cheat_items_string.encode('utf-8')

    process_cheat_items = sp.run(
        "fzf --layout=reverse",
        input=cheat_items_string,
        stdout=sp.PIPE,
        shell=True,
    )

    fzf_result = process_cheat_items.stdout.decode("utf-8").strip()

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
    sys.exit()

elif main_menu_value == "core-utils":
    core_utils = [
        "awk",
        "grep",
        "sed",
        "xargs",
        "parallel"
    ]
    core_utils_string = "\n".join(core_utils)
    # Turn cheat_items_string into a bytes array so we can use it in
    # a subprocess
    core_utils_string = core_utils_string.encode('utf-8').strip()

    process_core_utils = sp.run(
        "fzf --layout=reverse",
        input=core_utils_string,
        stdout=sp.PIPE,
        shell=True,
    )
    process_value = process_core_utils.stdout.decode('utf-8').strip()

    sp.run(
        f"curl cheat.sh/{process_value}",
        shell=True
    )
    sys.exit()

elif main_menu_value == "other":
    other_input = input("search: ").strip()

    sp.run(
        f"curl cheat.sh/{other_input}",
        shell=True
    )
    sys.exit()
