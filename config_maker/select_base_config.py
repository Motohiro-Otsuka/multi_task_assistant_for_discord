import tkinter as tk
from tkinter import ttk
import json

import common
from common import wrapper_edit_common_config

config_labels = ["初めから作る","(サンプルから作る)毎回配信者が同じ","(サンプルから作る)毎回配信者がバラバラ_4人チーム","現在使用中の設定"]
def load_config_json(file_name):
    config_file = open(file_name, "r", encoding="utf-8")
    common.config = json.load(config_file)


def decide_base_config(root,screen,radio_var):
    def inner():
        from common import wrapper_edit_common_config
        #ラジオボタンの値を取得する
        number = radio_var.get()
        if(number == 0):
            load_config_json("config/config_base.json")
        elif(number == 1):
            load_config_json("sample/毎回配信者が同じ/config.json")
        elif(number == 2):
            load_config_json("sample/毎回配信者がバラバラ_4人チーム/config.json")
        elif(number == 3):
            load_config_json("config/config.json")
        screen.destroy()
        common.screens["select_base_config"] = None
        wrapper_edit_common_config(root)
    return inner



def select_base(root):
    #フレームを作成する
    common.screens["select_base_config"] = tk.Frame(root)
    screen = common.screens["select_base_config"]
    #説明文を書く
    label = tk.Label(screen, text="編集する設定（config）を選んでください")
    label.pack()
    #ベースとなるconfigの選択ボタン
    radio_var = tk.IntVar()
    for i,val in enumerate(config_labels):
        radio = ttk.Radiobutton(screen,value=i,variable=radio_var,text=val)
        radio.pack( anchor=tk.NW)

    #決定ボタン
    submit = ttk.Button(screen, text="決定",command=decide_base_config(root,screen,radio_var))
    submit.pack()
    screen.pack()