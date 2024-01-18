import tkinter as tk
from tkinter import ttk
import copy

import common
from common import wrapper_edit_parrot_config,str_to_bool

def decide_common_config(root,screen,config_val):
    def inner():
        config = common.config["common"]
        for key,val in config_val.items():
            if("use" in key):
                config[key]=str_to_bool(val.get())
            else:
                config[key]=val.get()
        common.config["common"] = config
        screen.destroy()
        common.screens["common"] = None
        wrapper_edit_parrot_config(root)
    return inner

def edit_common_config(root):
    common.screens["common"] = tk.Frame(root)
    screen = common.screens["common"]
    config = common.config["common"]
    config_val = copy.deepcopy(config)
    variable_dict = {}
    use_flag = (True,False)
    
    row = 0
    for key,val in config.items():
        if("use" in key):
            variable_dict[key] = tk.StringVar()
            config_val[key] = ttk.Combobox(screen, values=use_flag,state='readonly')
            if(val):
                config_val[key].current(0)
            else:
                config_val[key].current(1)
        else:
            config_val[key] = ttk.Entry(screen, width=40)
            config_val[key].insert(tk.END,val)
        #必用に応じてリファクタリング
        #各入力カラムの説明
        if(key=="discord_api_key"):
            label = tk.Label(screen, text="discord api keyを入力してください。")
            label.grid(row=row, column=0,columnspan=8,sticky=tk.NW)
            row+=1
        elif(key=="use_replit"):
            label = tk.Label(screen, text="replitにサーバを立てる場合はTrue,そうでない場合はFalse")
            label.grid(row=row, column=0,columnspan=8,sticky=tk.NW)
            row+=1
        elif(key=="use_google_drive"):
            label = tk.Label(screen, text="google driveにAPI経由でアクセスする場合はTrue、そうでない場合はFalse")
            label.grid(row=row, column=0,columnspan=8,sticky=tk.NW)
            row+=1
        elif(key=="use_google_service_account"):
            label = tk.Label(screen, text="google driveにAPI経由でアクセスする場合、google driveのサービスアカウントを使用する場合はTrue,そうでない場合はFalse（基本Flase）")
            label.grid(row=row, column=0,columnspan=8,sticky=tk.NW)
            row+=1
        elif(key=="google_dirive_setting"):
            label = tk.Label(screen, text="google driveにAPI経由でアクセスする場合、その設定値が書かれたファイルパスを入力する")
            label.grid(row=row, column=0,columnspan=8,sticky=tk.NW)
            row+=1
        #入力欄の描画
        label = tk.Label(screen, text=key)
        label.grid(row=row, column=0, columnspan=2,sticky=tk.NW)
        config_val[key].grid(row = row,column=2,sticky=tk.NW)
        row += 1
        label = tk.Label(screen, text="")
        label.grid(row=row, column=0, columnspan=2,sticky=tk.NW)
        row += 1
        #決定ボタン
    submit = ttk.Button(screen, text="決定",command=decide_common_config(root,screen,config_val))
    submit.grid(row=row, column=8)
    screen.grid(row=0,column=0)