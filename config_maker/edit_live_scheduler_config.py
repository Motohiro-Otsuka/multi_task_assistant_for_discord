import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import copy
import sys
from PIL import Image, ImageTk
import asyncio

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

def calc_new_grid(entrys,grid,menber_num):
    top_r_y = int(entrys["top_r_y"].get())
    buttom_r_y = int(entrys["buttom_r_y"].get())
    row_height = buttom_r_y - top_r_y
    day_x = int(entrys["day_x"].get())
    time_x = int(entrys["time_x"].get())
    content_x = int(entrys["content_x"].get())
    liver_x = int(entrys["liver_x"].get()) if entrys["liver_x"] != None else None
    platform_x = int(entrys["platform_x"].get())
    end_x = int(entrys["end_x"].get())
    
    column_size = grid["column_size"]

    column_size["day"]["x"] = int(((time_x - day_x)/2)*(6/7))
    column_size["day"]["y"] = row_height

    column_size["time"]["x"] = int(((content_x - time_x)/5)*(0.615))
    column_size["time"]["y"] = row_height
    if(liver_x != None):
        column_size["content"]["x"] = liver_x - content_x
        column_size["content"]["y"] = row_height
        column_size["liver"]["x"] = int((platform_x - liver_x)/menber_num)
        column_size["liver"]["y"] = row_height
    else:
        column_size["content"]["x"] = platform_x - content_x
        column_size["content"]["y"] = row_height
    print( end_x, platform_x)
    column_size["platform"]["x"] = end_x - platform_x
    column_size["platform"]["y"] = row_height

    column_first_point = grid["column_first_point"]
    column_first_point["day"]["x"] = day_x
    column_first_point["day"]["y"] = top_r_y

    column_first_point["time"]["x"] = time_x
    column_first_point["time"]["y"] = top_r_y

    column_first_point["content"]["x"] = content_x
    column_first_point["content"]["y"] = top_r_y

    if(liver_x != None):
        column_first_point["liver"]["x"] = liver_x
        column_first_point["liver"]["y"] = top_r_y
    
    column_first_point["platform"]["x"] = platform_x
    column_first_point["platform"]["y"] = top_r_y

    grid["column_size"] = column_size
    grid["column_first_point"] = column_first_point
    return grid

def show_preview(entrys):
    #ファイル読み込みの設定
    def inner():
        print("show_preview")
        sys.path.append("./task_scr")
        import live_scheduler
        config = common.config["function"]["live_scheduler"]
        use_drive = common.config["common"]["use_google_drive"]
        use_service_account = common.config["common"]["use_google_service_account"]
        gdrive_setting_path = common.config["common"]["google_dirive_setting"]
        menber_num = len(common.config["function"]["live_scheduler"]["files"]["icons"].keys())
        config["grid"] = calc_new_grid(entrys,config["grid"],menber_num)
        print(config)
        live_scheduler =  live_scheduler.LiveScheduer(config,use_drive,use_service_account,gdrive_setting_path)
        live_scheduler.preview_schedule_img()
        
    return inner


def edit_live_scheduler_grid_config():
    sys.path.append("./task_scr")
    import live_scheduler
    #ファイル読み込みの設定
    config = common.config["function"]["live_scheduler"]
    use_drive = common.config["common"]["use_google_drive"]
    use_service_account = common.config["common"]["use_google_service_account"]
    gdrive_setting_path = common.config["common"]["google_dirive_setting"]
    live_scheduler = live_scheduler.LiveScheduer(config,use_drive,use_service_account,gdrive_setting_path)
    grid_move_command = [100,10,1,-1,-10,-100]
    entrys = {}

    files = config["files"]

    icons = None
    if("icons" in files):
        icons = files["icons"]
    contents = files["contents"]
    platform = files["platform"]
    number_img  = files["number_img"]

    grid = config["grid"]
    column_size = grid["column_size"]
    column_first_point = grid["column_first_point"]
    
    #画像の取得
    #liver_images = live_scheduler.get_liver_icon()
    #platform_images = live_scheduler.get_live_platform_icon()
    #contents_images = live_scheduler.get_live_contents_icon()
    #number_pictures = live_scheduler.get_number_picture()
    base_image = live_scheduler.get_schedule_base_image()

    # 画面作成
    version = tk.Tcl().eval('info patchlevel')
    window = tk.Tk()
    #window.geometry("400x300")
    window.title("画像表示：" + version)
    
    img_width,img_height= base_image.size
    #tkinterで表示できるように図のフォーマットを変更
    base_image = ImageTk.PhotoImage(base_image,master=window)

    # キャンバス作成
    canvas = tk.Canvas(window, bg="#deb887", height=img_height, width=img_width)
    # キャンバス表示
    canvas.grid(row=0, column=0, rowspan=40)

    # キャンバスにイメージを表示
    canvas.create_image(0, 0, image=base_image, anchor=tk.NW)

    def move_line(move,tag,entry,decide=True):
        def inner():
            y_move = ["top_y","buttom_y"]
            if(tag in y_move):
                canvas.move(tag,0,move)
            else:
                canvas.move(tag,move,0)
            new_num = int(entry.get()) + move
            entry.delete(0,tk.END)
            entry.insert(0,str(new_num))
        return inner
    
    def on_entry_dicide(tag,entry):#デバッグして修正
        def inner():
            item_ids = canvas.find_withtag(tag)
            coords = canvas.coords(item_ids[0])
            y_move = ["top_y","buttom_y"]
            try:
                new_point = int(entry.get())
                print(new_point)
                if(tag in y_move):
                    move = int(new_point) - int(coords[1])
                    canvas.move(tag,0,move)
                else:
                    move = int(new_point) - int(coords[0])
                    canvas.move(tag,move,0)
            except:
                pass
        return inner

    def make_arrange_button(window,entry,tag):
        for i,button_label in enumerate(grid_move_command):
            if(button_label > 0):
                #command の引数にroot,top_r_y_entryとtag名,row
                button = ttk.Button(window, text="+{}".format(button_label),command=move_line(button_label,tag,entry))
                button.grid(row=row,column=2+i,sticky=tk.NW)
            else:
                button = ttk.Button(window, text="{}".format(button_label),command=move_line(button_label,tag,entry))
                button.grid(row=row,column=2+i,sticky=tk.NW)
            button = ttk.Button(window, text="入力欄の値を反映",command=on_entry_dicide(tag,entry))
            button.grid(row=row+1,column=2,columnspan=2,sticky=tk.NW)

    #１行目の枠の幅を示すための線の描画
    row = 0
    top_r_y = int(column_first_point["day"]["y"])
    canvas.create_line(0, top_r_y, img_width, top_r_y, fill = "Blue", width = 2,tag="top_y")
    label = tk.Label(window, text="1行目の上辺に合わせる（青色の線）")
    label.grid(row=row,column=1,columnspan=3,sticky=tk.NW)
    top_r_y_entry = ttk.Entry(window, width=10)
    top_r_y_entry.insert(tk.END,column_first_point["day"]["y"])
    row += 1
    top_r_y_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,top_r_y_entry,"top_y")
    row += 3
    entrys["top_r_y"] = top_r_y_entry

    buttom_r_y = int(column_first_point["day"]["y"])+int(column_size["day"]["y"])
    canvas.create_line(0, buttom_r_y, img_width, buttom_r_y, fill = "red", width = 2,tag="buttom_y")
    label = tk.Label(window, text="1行目の下辺に合わせる（赤色の線）")
    label.grid(row=row,column=1,columnspan=3,sticky=tk.NW)
    buttom_r_y_entry = ttk.Entry(window, width=10)
    buttom_r_y_entry.insert(tk.END,str(buttom_r_y))
    row += 1
    buttom_r_y_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,buttom_r_y_entry,"buttom_y")
    row += 3
    entrys["buttom_r_y"] = buttom_r_y_entry


    #日付の枠
    day_x = int(column_first_point["day"]["x"])
    canvas.create_line(day_x, 0, day_x, img_height, fill = "green", width = 2,tag="day_x")
    label = tk.Label(window, text="日付の枠の左辺に合わせる（緑色の線）")
    label.grid(row=row,column=1,columnspan=3,sticky=tk.NW)
    day_entry = ttk.Entry(window, width=10)
    day_entry.insert(tk.END,column_first_point["day"]["x"])
    row += 1
    day_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,day_entry,"day_x")
    row += 3
    entrys["day_x"] = day_entry


    #time
    time_x = int(column_first_point["time"]["x"])
    canvas.create_line(time_x, 0, time_x, img_height, fill = "yellow", width = 2,tag="time_x")
    label = tk.Label(window, text="配信開始時間の枠の左辺に合わせる（黄色の線）")
    label.grid(row=row,column=1,columnspan=4,sticky=tk.NW)
    time_entry = ttk.Entry(window, width=10)
    time_entry.insert(tk.END,column_first_point["time"]["x"])
    row += 1
    time_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,time_entry,"time_x")
    row += 3
    entrys["time_x"] = time_entry

    #content
    content_x = int(column_first_point["content"]["x"])
    canvas.create_line(content_x, 0, content_x, img_height, fill = "MediumPurple", width = 1,tag="content_x")
    label = tk.Label(window, text="配信内容の枠の左辺に合わせる（紫色の線）")
    label.grid(row=row,column=1,columnspan=4,sticky=tk.NW)
    content_entry = ttk.Entry(window, width=10)
    content_entry.insert(tk.END,column_first_point["content"]["x"])
    row += 1
    content_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,content_entry,"content_x")
    row += 3
    entrys["content_x"] = content_entry


    #liver
    if(icons != None):
        liver_x = int(column_first_point["liver"]["x"])
        canvas.create_line(liver_x, 0, liver_x, img_height, fill = "cyan", width = 1,tag="liver_x")
        label = tk.Label(window, text="メンバーの枠の左辺に合わせる（水色の線）")
        label.grid(row=row,column=1,columnspan=4,sticky=tk.NW)
        liver_entry = ttk.Entry(window, width=10)
        liver_entry.insert(tk.END,column_first_point["liver"]["x"])
        row += 1
        liver_entry.grid(row=row,column=1,sticky=tk.NW)
        make_arrange_button(window,liver_entry,"liver_x")
        row += 3
        entrys["liver_x"] = liver_entry
    else:
        entrys["liver_x"] = None

    #platform
    platform_x = int(column_first_point["platform"]["x"])
    canvas.create_line(platform_x, 0, platform_x, img_height, fill = "chartreuse", width = 1,tag="platform_x")
    label = tk.Label(window, text="サイトの枠の左辺に合わせる（黄緑の線）")
    label.grid(row=row,column=1,columnspan=4,sticky=tk.NW)
    platform_entry = ttk.Entry(window, width=10)
    platform_entry.insert(tk.END,platform_x)
    row += 1
    platform_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,platform_entry,"platform_x")
    row += 3
    entrys["platform_x"] = platform_entry

    #end
    end_x = int(column_first_point["platform"]["x"]) + int(column_size["platform"]["x"])
    canvas.create_line(end_x, 0, end_x, img_height, fill = "firebrick1", width = 1,tag="platform_x")
    label = tk.Label(window, text="サイトの枠の右辺に合わせる（オレンジの線）")
    label.grid(row=row,column=1,columnspan=4,sticky=tk.NW)
    end_entry = ttk.Entry(window, width=10)
    end_entry.insert(tk.END,end_x)
    row += 1
    end_entry.grid(row=row,column=1,sticky=tk.NW)
    make_arrange_button(window,end_entry,"platform_x")
    row += 3
    entrys["end_x"] = end_entry

    submit = ttk.Button(window, text="プレビュー",command=show_preview(entrys))
    submit.grid(row=row, column=1,sticky=tk.NW)


    window.mainloop()