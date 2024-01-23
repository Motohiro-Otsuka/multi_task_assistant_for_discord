import tkinter as tk
from tkinter import *
from tkinter import ttk
import copy

import common
from common import wrapper_edit_live_scheduler_config, str_to_bool


def decide_chat_config(root, screen, config_val):
    def inner():
        config = common.config["function"]["chat_openai"]
        for key, item in config_val.items():
            if key != "commands":
                if key == "use":
                    config[key] = str_to_bool(config_val[key].get())
                else:
                    config[key] = config_val["use"].get()
        for key, val in config_val["commands"].items():
            config["commands"][key]["discription"] = val["discription"].get()
            config["commands"][key]["use"] = str_to_bool(val["use"].get())
        common.config["function"]["chat_openai"] = config
        screen.destroy()
        common.screens["chat_openai"] = None
        wrapper_edit_live_scheduler_config(root)

    return inner


def edit_chat_config(root):
    common.screens["chat_openai"] = tk.Frame(root)
    screen = common.screens["chat_openai"]
    config = common.config["function"]["chat_openai"]
    config_val = copy.deepcopy(config)
    use_flag = (True, False)
    row = 0
    # 機能のON/OFF
    chatgpt_label = tk.Label(screen, text="ChatGPT機能の読み込みを許可するか（許可：True、不許可：False）")
    config_val["use"] = ttk.Combobox(screen, values=use_flag, state="readonly")
    if config["use"]:
        config_val["use"].current(0)
    else:
        config_val["use"].current(1)
    chatgpt_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["use"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0)
    row += 1
    # OPENAIのAPIKey入力欄
    apikey_label = tk.Label(screen, text="Open aiのAPI KEYを入力してください")
    config_val["OPENAI_API_KEY"] = ttk.Entry(screen, width=40)
    config_val["OPENAI_API_KEY"].insert(tk.END, config["OPENAI_API_KEY"])
    apikey_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["OPENAI_API_KEY"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0, sticky=tk.NW)
    row += 1
    # モデル名の入力
    model_label = tk.Label(screen, text="GPTのモデル名を入力してください")
    config_val["model"] = ttk.Entry(screen, width=40)
    config_val["model"].insert(tk.END, config["model"])
    model_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["model"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0, sticky=tk.NW)
    row += 1
    # system promptの入力
    system_prompt_label = tk.Label(screen, text="system promptを入力してください")
    config_val["system_prompt"] = ttk.Entry(screen, width=40)
    config_val["system_prompt"].insert(tk.END, config["system_prompt"])
    system_prompt_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["system_prompt"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0)
    row += 1
    # max token
    max_token_label = tk.Label(screen, text="生成する最大token長を入力してください(半角数字)")
    config_val["max_tokens"] = ttk.Entry(screen, width=40)
    config_val["max_tokens"].insert(tk.END, config["max_tokens"])
    max_token_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["max_tokens"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0)
    row += 1
    # temperature
    temperature_label = tk.Label(screen, text="生成する文字の奇抜性を入力(推奨値：0.7、半角数字で入力)")
    config_val["temperature"] = ttk.Entry(screen, width=40)
    config_val["temperature"].insert(tk.END, config["temperature"])
    temperature_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["temperature"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0)
    row += 1
    # 会話ログをどれぐらい残すか
    max_log_label = tk.Label(screen, text="会話の最大ログ数を入力(半角数字)")
    config_val["max_log"] = ttk.Entry(screen, width=40)
    config_val["max_log"].insert(tk.END, config["max_log"])
    max_log_label.grid(row=row, column=0, columnspan=2, sticky=tk.NW)
    config_val["max_log"].grid(row=row, column=3, columnspan=2, sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row, column=0)
    row += 1
    # コマンド入力欄作成
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
        screen, text="決定", command=decide_chat_config(root, screen, config_val)
    )
    submit.grid(row=row, column=8)
    screen.grid(row=0, column=0)
