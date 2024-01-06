import gradio as gr
import json

config_file = open("../config/config_sample.json", "r", encoding="utf-8")
config = json.load(config_file)

common_config = config["common"]
function_config = config["function"]

parrot_config = function_config["parrot"]
chat_openai_config = function_config["chat_openai"]
live_scheduler_config = function_config["live_scheduler"]


def save_config(input1,input2):
    return "done"

def get_content_title_html(str):
    return str

interfaces={}
with gr.Blocks(title="config_maker") as app:
    with gr.Tab("Google drive"):
        #commonの設定値
        gr.HTML(get_content_title_html("共通設定の入力欄"))
        with gr.Row():
            interfaces["common"] ={}
            for key,val in common_config.items():
                if("use" in key):
                    interfaces["common"][key] = gr.Dropdown(choices=[True,False],value=val,label=key,interactive=True) 
                else:
                    interfaces["common"][key] = gr.Textbox(label=key,value=str(val),interactive=True) 
        #parrotの設定値
        gr.HTML(get_content_title_html("parrotに関係する"))
        with gr.Row():
            interfaces["parrot"] ={}
            interfaces["parrot"]["use"] = gr.Dropdown(choices=[True,False],label="parrot機能を使うか",value=parrot_config["use"],interactive=True) 
            interfaces["parrot"]["commands"] = {}
            for key,commands in parrot_config["commands"].items():
                interfaces["parrot"]["commands"][key] = {}
                for k,v in commands.items():
                    if("use" == k):
                        interfaces["parrot"]["commands"][key][k] = gr.Dropdown(choices=[True,False],value=v,label=key,interactive=True) 
                    else:
                        interfaces["parrot"]["commands"][key][k] = gr.Textbox(label=k,value=v,interactive=True)
            
        #chat_openaiの設定値
        gr.HTML(get_content_title_html("openaiに関係する"))
        with gr.Row():
            interfaces["chat_openai"] ={}
            for key,val in chat_openai_config.items():
                if(key=="commands"):
                    interfaces["chat_openai"]["commands"] = {}
                    for k,commands in parrot_config["commands"].items():
                        interfaces["chat_openai"]["commands"][k] = {}
                        for c_k , v in commands.items():
                            interfaces["chat_openai"]["commands"][k][c_k] = gr.Textbox(label=c_k,value=v,interactive=True)
                else:
                    interfaces["chat_openai"][key] = gr.Textbox(label=key,value=val,interactive=True) 
            

        #for key,val in chat_openai_config.items():
    with gr.Tab("ローカル"):
        gr.Button()

app.launch()