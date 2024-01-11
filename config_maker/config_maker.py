import gradio as gr
import json
import tkinter as tk
from tkinter import filedialog


config_file = open("../config/config_sample.json", "r", encoding="utf-8")
config = json.load(config_file)

common_config = config["common"]
function_config = config["function"]

parrot_config = function_config["parrot"]
chat_openai_config = function_config["chat_openai"]
live_scheduler_config = function_config["live_scheduler"]

check_use_str = "使用する場合はTrue、使用しない場合はFalseを選択"
min_w = 300
f = None


def save_config(input1, input2):
    return "done"


def get_content_title_html(str):
    return str


def file_selected(file):
    print("ファイルが選択されました。")
    print(file)
    # print(f.name)


def arrenge_length(max_len, list1, list2):
    if max_len < len(list1):
        return list1[:max_len], list2[:max_len]
    else:
        while max_len > len(list1):
            list1.append("")
            list2.append("")
        return list1, list2


def update_icon(records):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file = filedialog.askopenfilenames()
    liver_name = [a for a in list(records["liver name"][:]) if a != ""]
    file_name = [a for a in list(records["file"][:]) if a != ""]
    for f in file:
        liver_name.append(f.split("/")[-1].replace(".png", ""))
        file_name.append(f)
    liver_name, file_name = arrenge_length(
        len(records["liver name"]), liver_name, file_name
    )
    records["liver name"] = liver_name
    records["file"] = file_name
    return records


def update_contents(records):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file = filedialog.askopenfilenames()
    contents_name = [a for a in list(records["contents_name"][:]) if a != ""]
    file_name = [a for a in list(records["file"][:]) if a != ""]
    for i, f in enumerate(file):
        contents_name.append(f.split("/")[-1].replace(".png", ""))
        file_name.append(f)
    contents_name, file_name = arrenge_length(
        len(records["contents_name"]), contents_name, file_name
    )
    records["contents_name"] = contents_name
    records["file"] = file_name
    return records


def update_platform(records):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file = filedialog.askopenfilenames()
    platform_name = [a for a in list(records["platform_name"][:]) if a != ""]
    file_name = [a for a in list(records["file"][:]) if a != ""]
    for i, f in enumerate(file):
        platform_name.append(f.split("/")[-1].replace(".png", ""))
        file_name.append(f)
    platform_name, file_name = arrenge_length(
        len(records["platform_name"]), platform_name, file_name
    )
    records["platform_name"] = platform_name
    records["file"] = file_name
    return records


def update_number_img(records):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file = filedialog.askopenfilenames()
    # number = [a for a in list(records["number"][:]) if a != '']
    file_name = [a for a in list(records["file"][:]) if a != ""]
    for i, f in enumerate(file):
        # number.append(f.split("/")[-1].replace(".png",""))
        file_name.append(f)
    number, file_name = arrenge_length(len(records["number"]), number, file_name)
    # records["number"] += number
    records["file"] += file_name
    return records


interfaces = {}
with gr.Blocks(title="config_maker") as app:
    # commonの設定値
    gr.HTML(get_content_title_html("共通設定の入力欄"))
    with gr.Row():
        interfaces["common"] = {}
        for key, val in common_config.items():
            if "use" in key:
                interfaces["common"][key] = gr.Dropdown(
                    choices=[True, False], value=val, label=key, interactive=True
                )
            else:
                interfaces["common"][key] = gr.Textbox(
                    label=key, value=str(val), interactive=True
                )
    # parrotの設定値
    gr.HTML(get_content_title_html("parrotに関係する設定"))
    with gr.Row():
        interfaces["parrot"] = {}
        interfaces["parrot"]["use"] = gr.Dropdown(
            choices=[True, False],
            label="parrot機能を使うか",
            value=parrot_config["use"],
            interactive=True,
        )
        interfaces["parrot"]["commands"] = {}
    with gr.Row():
        for key, commands in parrot_config["commands"].items():
            interfaces["parrot"]["commands"][key] = {}
            for k, v in commands.items():
                if "use" == k:
                    interfaces["parrot"]["commands"][key][k] = gr.Dropdown(
                        choices=[True, False],
                        value=v,
                        label="{}コマンドを{}".format(key, check_use_str),
                        interactive=True,
                    )
                else:
                    interfaces["parrot"]["commands"][key][k] = gr.Textbox(
                        label="{}コマンドの説明を記入してください".format(key),
                        value=v,
                        interactive=True,
                    )
    # chat_openaiの設定値
    gr.HTML(get_content_title_html("openaiに関係する設定"))
    with gr.Column(scale=4):
        interfaces["chat_openai"] = {}
        interfaces["chat_openai"]["commands"] = {}
        with gr.Row():
            for key, val in chat_openai_config.items():
                if key != "commands":
                    if key == "use":
                        interfaces["chat_openai"][key] = gr.Dropdown(
                            choices=[True, False],
                            value=v,
                            label="chat_openai機能を使用するか。{}".format(check_use_str),
                            interactive=True,
                            min_width=min_w,
                        )
                    else:
                        interfaces["chat_openai"][key] = gr.Textbox(
                            label=key, value=val, interactive=True, min_width=min_w
                        )
    with gr.Row():
        for key, val in chat_openai_config["commands"].items():
            interfaces["chat_openai"]["commands"][key] = {}
            for c_k, v in val.items():
                interfaces["chat_openai"]["commands"][key][c_k] = gr.Textbox(
                    label=c_k, value=v, interactive=True
                )

    # live schedulerの設定
    gr.HTML(get_content_title_html("live schedulerに関係する設定"))
    # live scheduerを使用するか否かの設定
    with gr.Row():
        interfaces["live_scheduler"] = {}
        interfaces["live_scheduler"]["use"] = gr.Dropdown(
            choices=[True, False],
            label="live_scheduler機能を使うか{}".format(check_use_str),
            value=live_scheduler_config["use"],
            interactive=True,
        )
    # live scheduerの各コマンドの使用の有無の設定
    with gr.Column():
        interfaces["live_scheduler"]["commands"] = {}
        for key, commands in live_scheduler_config["commands"].items():
            with gr.Row():
                interfaces["live_scheduler"]["commands"][key] = {}
                for k, v in commands.items():
                    if "use" == k:
                        interfaces["live_scheduler"]["commands"][key][k] = gr.Dropdown(
                            choices=[True, False],
                            value=v,
                            label="{}コマンドを{}".format(key, check_use_str),
                            interactive=True,
                            min_width=min_w,
                        )
                    else:
                        interfaces["live_scheduler"]["commands"][key][k] = gr.Textbox(
                            label="{}コマンドの説明を記入してください".format(key),
                            value=v,
                            interactive=True,
                            min_width=min_w,
                        )
    # live scheduerで使用するファイルの設定
    with gr.Column():
        gr.HTML(get_content_title_html("ライバーのアイコンの共有リンクか保存されているパスを入力"))
        interfaces["live_scheduler"]["files"] = {}
        interfaces["live_scheduler"]["files"]["icons"] = gr.Dataframe(
            headers=["liver name", "file"],
            row_count=4,
            col_count=(2, "fixed"),
            interactive=True,
        )
    with gr.Column():
        icon_select_button = gr.Button(value="icon selecter(パスの入力はこちら)")
        icon_select_button.click(
            update_icon,
            inputs=interfaces["live_scheduler"]["files"]["icons"],
            outputs=interfaces["live_scheduler"]["files"]["icons"],
        )
    # 配信内容の文字画像で使用するファイルの設定
    with gr.Column():
        gr.HTML(get_content_title_html("配信内容の文字画像の共有リンクかパスを入力"))
        interfaces["live_scheduler"]["files"] = {}
        interfaces["live_scheduler"]["files"]["contents"] = gr.Dataframe(
            headers=["contents_name", "file"],
            row_count=10,
            col_count=(2, "fixed"),
            interactive=True,
        )
    with gr.Column():
        contents_select_button = gr.Button(value="contents selecter(パスの入力はこちら)")
        contents_select_button.click(
            update_contents,
            inputs=interfaces["live_scheduler"]["files"]["contents"],
            outputs=interfaces["live_scheduler"]["files"]["contents"],
        )
    # 配信サイトの文字画像で使用するファイルの設定
    with gr.Column():
        gr.HTML(get_content_title_html("配信サイトの文字画像の共有リンクかパスを入力"))
        interfaces["live_scheduler"]["files"] = {}
        interfaces["live_scheduler"]["files"]["platform"] = gr.Dataframe(
            headers=["platform_name", "file"],
            row_count=3,
            col_count=(2, "fixed"),
            interactive=True,
        )
    with gr.Column():
        platform_select_button = gr.Button(value="platform selecter(パスの入力はこちら)")
        platform_select_button.click(
            update_platform,
            inputs=interfaces["live_scheduler"]["files"]["platform"],
            outputs=interfaces["live_scheduler"]["files"]["platform"],
        )
    # 配信時刻などの文字画像で使用するファイルの設定
    with gr.Column():
        gr.HTML(get_content_title_html("配信時刻などの数字の文字画像の共有リンクかパスを入力"))
        interfaces["live_scheduler"]["files"] = {}
        interfaces["live_scheduler"]["files"]["number_img"] = gr.Dataframe(
            headers=["number", "file"],
            value=[
                ["0", ""],
                ["1", ""],
                ["2", ""],
                ["3", ""],
                ["4", ""],
                ["5", ""],
                ["6", ""],
                ["7", ""],
                ["8", ""],
                ["9", ""],
                [":", ""],
            ],
            row_count=(11, "fixed"),
            col_count=(2, "fixed"),
            interactive=True,
        )
    with gr.Column():
        number_select_button = gr.Button(value="number file selecter(パスの入力はこちら)")
        number_select_button.click(
            update_number_img,
            inputs=interfaces["live_scheduler"]["files"]["number_img"],
            outputs=interfaces["live_scheduler"]["files"]["number_img"],
        )


app.launch()
