import tkinter as tk
from tkinter import ttk
import copy

import common
from common import wrapper_edit_chat_config, str_to_bool


def decide_parrot_config(root, screen, config_val):
    def inner():
        config = common.config["function"]["parrot"]
        config["use"] = str_to_bool(config_val["use"].get())
        for key, val in config_val["commands"].items():
            config["commands"][key]["discription"] = val["discription"].get()
            config["commands"][key]["use"] = str_to_bool(val["use"].get())
        common.config["function"]["parrot"] = config
        screen.destroy()
        common.screens["parrot"] = None
        wrapper_edit_chat_config(root)

    return inner


def edit_parrot_config(root):
    common.screens["parrot"] = tk.Frame(root)
    screen = common.screens["parrot"]
    config = common.config["function"]["parrot"]
    config_val = copy.deepcopy(config)
    use_flag = (True, False)
    row = 0
    parrot_label = tk.Label(screen, text="オウム返し機能の読み込みを許可するか（許可：True、不許可：False）")
    config_val["use"] = ttk.Combobox(screen, values=use_flag, state="readonly")
    if config["use"]:
        config_val["use"].current(0)
    else:
        config_val["use"].current(1)
    parrot_label.grid(row=row, column=0, columnspan=2)
    config_val["use"].grid(row=row, column=3, columnspan=2)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0)
    row += 1
    for key, val in config["commands"].items():
        discription = val["discription"]
        use = val["use"]
        label = tk.Label(screen, text="{}コマンドを使用するか(使用:True, 不使用：False)".format(key))
        label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
        config_val["commands"][key]["use"] = ttk.Combobox(
            screen, values=use_flag, state="readonly"
        )
        if val:
            config_val["commands"][key]["use"].current(0)
        else:
            config_val["commands"][key]["use"].current(1)
        config_val["commands"][key]["use"].grid(
            row=row, column=3, columnspan=5, sticky=tk.NW
        )
        row += 1
        label = tk.Label(screen, text="{}コマンドの説明".format(key))
        label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
        config_val["commands"][key]["discription"] = ttk.Entry(screen, width=40)
        config_val["commands"][key]["discription"].insert(tk.END, discription)
        config_val["commands"][key]["discription"].grid(
            row=row, column=3, columnspan=5, sticky=tk.NW
        )
        row += 1
        label = tk.Label(screen, text="")
        label.grid(row=row, column=0, columnspan=2)
        row += 1
    submit = ttk.Button(
        screen, text="決定", command=decide_parrot_config(root, screen, config_val)
    )
    submit.grid(row=row, column=8)
    screen.grid(row=0, column=0)
