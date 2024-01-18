import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import copy
import sys

import common
from common import str_to_bool,wrapper_edit_live_scheduler_img_config,wrapper_edit_live_scheduler_grid_config,wrapper_end_screen

entrys = {
    "icons":{
        "entry":[],
        "img_entry":[]
    },
    "contents":{
        "entry":[],
        "img_entry":[]
    },
    "platform":{
        "entry":[],
        "img_entry":[]
    },
    "number_img":{
        "entry":[],
        "img_entry":[]
    }
}

def add_label_entry(screen,category,row,col):
    def inner():
        global entrys
        entry1 = entrys[category]["entry"]
        entry2 = entrys[category]["img_entry"]
        print(entry1)
        #左側
        entry1.append(ttk.Entry(screen))
        entry1[-1].grid(row=row+len(entry1)+1, column=col, sticky="w")
        #右側
        entry2.append(ttk.Entry(screen))
        entry2[-1].grid(row=row+len(entry2)+1, column=col+1, sticky="w")
        entrys[category]["entry"] = entry1 
        entrys[category]["img_entry"] = entry2
    return inner

def load_images(screen,category,row,col):
    global entrys
    entry1 = entrys[category]["entry"]
    entry2 = entrys[category]["img_entry"]
    def inner():
        file = filedialog.askopenfilenames()
        for f in file:
            file_name = f.split("/")[-1].replace(".png", "")
            #左側
            entry1.append(ttk.Entry(screen))
            entry1[-1].insert(tk.END,file_name)
            entry1[-1].grid(row=row+len(entry1)+1, column=col, sticky="w")
            #右側
            entry2.append(ttk.Entry(screen))
            entry2[-1].insert(tk.END,f)
            entry2[-1].grid(row=row+len(entry2)+1, column=col+1, sticky="w")
        entrys[category]["entry"] = entry1
        entrys[category]["img_entry"] = entry2
    return inner

def load_image(entry):
    def inner():
        file = filedialog.askopenfilename()
        entry.insert(tk.END,file)
    return inner


def load_default_val(conf_dic,screen,category,row,col):
    global entrys
    entry1 = entrys[category]["entry"]
    entry2 = entrys[category]["img_entry"]
    for key,val in conf_dic.items():
        entry1.append(ttk.Entry(screen))
        entry1[-1].insert(tk.END,key)
        entry1[-1].grid(row=row+len(entry1)+1, column=col, sticky="w")
        #右側
        entry2.append(ttk.Entry(screen))
        entry2[-1].insert(tk.END,val)
        entry2[-1].grid(row=row+len(entry2)+1, column=col+1, sticky="w")
    entrys[category]["entry"] = entry1 
    entrys[category]["img_entry"] = entry2

def decide_live_scheduler_config(root,screen,config_val):
    def inner():
        config = common.config["function"]["live_scheduler"]
        for key,item in config_val.items():
            if(key not in  ["commands","files","grid"]):
                if(key == "use"):
                    config[key] = str_to_bool(config_val[key].get())
                else:
                    config[key] = config_val["use"].get()
        for key,val in config_val["commands"].items():
            config["commands"][key]["discription"] = val["discription"].get()
            config["commands"][key]["use"] = str_to_bool(val["use"].get())
        config["files"]["format"] = config_val["files"]["format"].get()
        config["files"]["schedule"] = config_val["files"]["schedule"].get()
        common.config["function"]["live_scheduler"] = config
        screen.destroy()
        common.screens["live_scheduler"] = None
        wrapper_edit_live_scheduler_img_config(root)
    return inner

def decide_live_scheduler_img_config(root,screen):
    def inner():
        config = common.config["function"]["live_scheduler"]["files"]
        for category,category_val in entrys.items():
            for i in range(len(category_val["entry"])):
                config[category][category_val["entry"][i]] = category_val["img_entry"][i].get()
        common.config["function"]["live_scheduler"]["files"] = config
        screen.destroy()
        common.screens["live_scheduler"] = None
        wrapper_edit_live_scheduler_grid_config(root)
    return inner

def edit_live_scheduler_config(root):
    file_label = "ファイルパス"
    gDrive_flag = common.config["common"]["use_google_drive"]
    button_state = "normal"
    if(gDrive_flag):
        file_label = "Google Driveの共有リンク"
        button_state = "disable"
    common.screens["live_scheduler"] = tk.Frame(root)
    screen = common.screens["live_scheduler"]
    config = common.config["function"]["live_scheduler"]
    config_val = copy.deepcopy(config)
    use_flag = (True,False)
    row = 0
    #機能のON/OFF
    live_scheduler_label = tk.Label(screen, text="live_scheduler機能の読み込みを許可するか（許可：True、不許可：False）")
    config_val["use"] = ttk.Combobox(screen, values=use_flag,state='readonly')
    if(config["use"]):
        config_val["use"].current(0)
    else:
        config_val["use"].current(1)
    live_scheduler_label.grid(row=row,column=0,columnspan=2,sticky=tk.NW)
    config_val["use"].grid(row=row,column=3,columnspan=2,sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row,column=0)
    row += 1
    #OPENAIのAPIKey入力欄
    GoogleDrive_label = tk.Label(screen, text="Google Driveを使用するかどうか")
    config_val["googleDrive"] = ttk.Combobox(screen, values=use_flag,state='readonly')
    if(config["googleDrive"]):
        config_val["googleDrive"].current(0)
    else:
        config_val["googleDrive"].current(1)
    GoogleDrive_label.grid(row=row,column=0,columnspan=2,sticky=tk.NW)
    config_val["googleDrive"].grid(row=row,column=3,columnspan=2,sticky=tk.NW)
    row += 1
    tk.Label(screen, text="").grid(row=row,column=0)
    row += 1
    #コマンド入力欄作成
    for key,val in config["commands"].items():
        discription = val["discription"]
        use = val["use"]
        label = tk.Label(screen, text="{}コマンドを使用するか(使用:True, 不使用：False)".format(key))
        label.grid(row=row,column=0,columnspan=2,sticky=tk.NW)
        config_val["commands"][key]["use"] = ttk.Combobox(screen, values=use_flag,state='readonly')
        if(val):
            config_val["commands"][key]["use"].current(0)
        else:
            config_val["commands"][key]["use"].current(1)
        config_val["commands"][key]["use"].grid(row=row,column=3,columnspan=5,sticky=tk.NW)
        row += 1
        label = tk.Label(screen, text="{}コマンドの説明".format(key))
        label.grid(row=row,column=0,columnspan=2,sticky=tk.NW)
        config_val["commands"][key]["discription"] = ttk.Entry(screen, width=40)
        config_val["commands"][key]["discription"].insert(tk.END,discription)
        config_val["commands"][key]["discription"].grid(row=row,column=3,columnspan=5,sticky=tk.NW)
        row += 1 
        label = tk.Label(screen, text="")
        label.grid(row=row,column=0,columnspan=2)
        row += 1 
    #formatの読み込み欄
    label = tk.Label(screen, text="スケジュールのベース画像({})".format(file_label))
    label.grid(row=row,column=0,columnspan=2,sticky=tk.NW)
    config_val["files"]["format"] = ttk.Entry(screen, width=30)
    config_val["files"]["format"].insert(tk.END,config["files"]["format"])
    config_val["files"]["format"].grid(row=row,column=3,columnspan=3,sticky=tk.NW)
    load_img = ttk.Button(screen, text="ファイル",command=load_image(config_val["files"]["format"]),state=button_state)
    load_img.grid(row=row,column=6,columnspan=3,sticky=tk.NW)
    row += 1 
    #スケジュールのエクセルファイル読み込み欄
    label = tk.Label(screen, text="スケジュールが書かれたエクセルファイル({})".format(file_label))
    label.grid(row=row,column=0,columnspan=2,sticky=tk.NW)
    config_val["files"]["schedule"] = ttk.Entry(screen, width=30)
    config_val["files"]["schedule"].insert(tk.END,config["files"]["schedule"])
    config_val["files"]["schedule"].grid(row=row,column=3,columnspan=3,sticky=tk.NW)
    load_img = ttk.Button(screen, text="ファイル",command=load_image(config_val["files"]["schedule"]),state=button_state)
    load_img.grid(row=row,column=6,columnspan=3,sticky=tk.NW)
    row += 1 
    submit = ttk.Button(screen, text="決定",command=decide_live_scheduler_config(root,screen,config_val))
    submit.grid(row=row, column=8)
    screen.grid(row=0,column=0)

def edit_live_scheduler_img_config(root):
    common.screens["live_scheduler"] = tk.Frame(root)
    screen = common.screens["live_scheduler"]
    config = common.config["function"]["live_scheduler"]
    file_label = "ファイル名"
    gDrive_flag = common.config["common"]["use_google_drive"]
    button_state = "normal"
    if(gDrive_flag):
        file_label = "Google Driveの共有リンク"
        button_state = "disable"
    config_val = copy.deepcopy(config)
    use_flag = (True,False)
    row = 0
    col = 0
    button_row = 1
    col_span = 5
    #icon
    label = tk.Label(screen, text="毎回配信者が異なり、画像にアイコンを表示する場合入力")
    label.grid(row=row,column=col,columnspan=col_span,sticky=tk.NW)
    #defaultの値を読み込み
    load_default_val(config["files"]["icons"],screen,"icons",button_row+2,col)
    
    load_img = ttk.Button(screen, text="まとめて読みこみ",command=load_images(screen,"icons",button_row+2,col),state=button_state)
    load_img.grid(row=button_row, column=col,sticky=tk.NW)
    add_line = ttk.Button(screen, text="1行追加",command=add_label_entry(screen,"icons",button_row+2,col))
    add_line.grid(row=button_row, column=col+1,sticky=tk.NW)
    
    label = tk.Label(screen, text="配信者名")
    label.grid(row=button_row+1,column=col,columnspan=col_span,sticky=tk.NW)
    label = tk.Label(screen, text=file_label)
    label.grid(row=button_row+1,column=col+1,columnspan=col_span,sticky=tk.NW)

    #contents
    row = 0
    col += col_span
    contents_entry=[]
    contents_img_entry=[]
    label = tk.Label(screen, text="配信内容の文字画像（配信内容はエクセルと合わせる）")
    label.grid(row=row,column=col,columnspan=col_span,sticky=tk.NW)
    
    load_default_val(config["files"]["contents"],screen,"contents",button_row+2,col)

    load_img = ttk.Button(screen, text="まとめて読みこみ",command=load_images(screen,"contents",button_row+2,col),state=button_state)
    load_img.grid(row=button_row, column=col,sticky=tk.NW)
    add_line = ttk.Button(screen, text="1行追加",command=add_label_entry(screen,"contents",button_row+2,col))
    add_line.grid(row=button_row, column=col+1,sticky=tk.NW)
    
    label = tk.Label(screen, text="配信内容")
    label.grid(row=button_row+1,column=col,columnspan=col_span,sticky=tk.NW)
    label = tk.Label(screen, text=file_label)
    label.grid(row=button_row+1,column=col+1,columnspan=col_span,sticky=tk.NW)
    #platform
    row = 0
    col += col_span
    platform_entry=[]
    platform_img_entry=[]
    label = tk.Label(screen, text="配信サイトの画像（配信サイト名はエクセルと合わせる）")
    label.grid(row=row,column=col,columnspan=col_span,sticky=tk.NW)
    load_default_val(config["files"]["platform"],screen,"platform",button_row+2,col)

    load_img = ttk.Button(screen, text="まとめて読みこみ",command=load_images(screen,"platform",button_row+2,col),state=button_state)
    load_img.grid(row=button_row, column=col,sticky=tk.NW)
    add_line = ttk.Button(screen, text="1行追加",command=add_label_entry(screen,"platform",button_row+2,col))
    add_line.grid(row=button_row, column=col+1,sticky=tk.NW)
    
    label = tk.Label(screen, text="配信サイト")
    label.grid(row=button_row+1,column=col,columnspan=col_span,sticky=tk.NW)
    label = tk.Label(screen, text=file_label)
    label.grid(row=button_row+1,column=col+1,columnspan=col_span,sticky=tk.NW)

    #number
    row = 0
    col += col_span
    number_entry=[]
    number_img_entry=[]
    label = tk.Label(screen, text="時刻などの数字の文字画像(数字半角の0~9と「:」のみ)")
    label.grid(row=row,column=col,columnspan=col_span,sticky=tk.NW)
    load_default_val(config["files"]["number_img"],screen,"number_img",button_row+2,col)
    
    load_img = ttk.Button(screen, text="まとめて読みこみ",command=load_images(screen,"number_img",button_row+2,col),state=button_state)
    load_img.grid(row=button_row, column=col,sticky=tk.NW)
    add_line = ttk.Button(screen, text="1行追加",command=add_label_entry(screen,"number_img",button_row+2,col))
    add_line.grid(row=button_row, column=col+1,sticky=tk.NW)
    
    label = tk.Label(screen, text="数字")
    label.grid(row=button_row+1,column=col,columnspan=col_span,sticky=tk.NW)
    label = tk.Label(screen, text=file_label)
    label.grid(row=button_row+1,column=col+1,columnspan=col_span,sticky=tk.NW)


    col += col_span
    submit = ttk.Button(screen, text="決定",command=decide_live_scheduler_img_config(root,screen))
    submit.grid(row=row, column=col,sticky=tk.NW)
    screen.grid(row=0,column=0)


def edit_live_scheduler_grid_config(root):
    sys.path.append("./task_scr")
    import live_scheduler
    common.screens["live_scheduler"] = tk.Frame(root)
    screen = common.screens["live_scheduler"]
    config = common.config["function"]["live_scheduler"]
    loading = tk.Label(screen, text="Loading...")
    loading.grid(row=0,column=0,sticky=tk.NW)

    config = common.config["function"]["live_scheduler"]
    use_drive = common.config["common"]["use_google_drive"]
    use_service_account = common.config["common"]["use_google_service_account"]
    gdrive_setting_path = common.config["common"]["google_dirive_setting"]
    live_scheduler = live_scheduler.LiveScheduer(config,use_drive,use_service_account,gdrive_setting_path)
    #load images
    base_image = live_scheduler.get_schedule_base_image()
    liver_images = live_scheduler.get_liver_icon()
    platform_images = live_scheduler.get_live_platform_icon()
    contents_images = live_scheduler.get_live_contents_icon()
    number_pictures = live_scheduler.get_number_picture()

