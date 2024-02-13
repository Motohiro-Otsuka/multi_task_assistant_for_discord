# chat_openai機能説明
ディスコード上で`/chat `で呼び出す。  
呼び出されると、botが自動的にスレッドを立ち上げる。  
そのあとは、スレッドの中で対話する
さらに質問をする場合は、スレッド内でチャットを送信すればよい。

# 設定項目の説明
configで設定する値は下記の通り
```json
"chat_openai":{
    "use":true,#task/chat_openai.pyを読み込んでよい場合はtrue,ダメなときはfalse
    "commands":{
        "chat":{
            "discription":"chatGPTを使ってチャットボットの応答をする",
            "use":true #chatGPT機能を使う場合はtrue,ダメなときはfalse
        }
    },
    "OPENAI_API_KEY":"Enter your openai api key",
    "model":"gpt-3.5-turbo-1106", #お好きなGPTのモデルをを入力。こだわりなければこのままで良い（安いので）
    "system_prompt":"あなたは親切なアシスタントです。", #GPTの役割を入力。こだわりがなければこのままで良い。
    "max_tokens":200, #GPTの応答の最大token数。こだわりがなければこのままで良い。
    "temperature":0.7,#GPTの創造性。こだわりがなければこのままで良い。
    "max_log":5#会話のログを何発話分、記憶するか。こだわりがなければこのままで良い。
    },
```
※設定する際は、#記号も含めて、それ以降の1行は記載しないこと。（正常にjsonが読み込めない）
