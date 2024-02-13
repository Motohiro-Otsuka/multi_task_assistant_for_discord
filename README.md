# 初めに
本リポジトリは、Live配信者や動画配信者のアシスタントをdiscordbotさせようと試みたコードが格納されている。

機能は、機能一覧に記載の通りである。

可能な限り簡単に設定できるように配慮しておりますが、
どうしてもわからない場合などは、TwitterのDMやgithubのissueでお知らせください

ご利用に際しては、免責事項、ライセンスを一読してからご使用ください。  
リリースノートは、ReleaseNote.mdをご覧ください。

# 機能一覧
- オウム返し(parrot)
- chatGPT(chat_openai)
- 配信スケジュール関連
  - スケジュール画像の自動生成 (schedule-print)
  - スケジュールの変更(schedule-edit)
  - スケジュールの確認(schedule-show)
  - スケジュール画像のグリッド表示(schedule-grid)
- 今後も次の機能を追加予定
  - あみだくじ作成機能 (配信内容とか順番決めとかにオススメ)
  - GPTを使ったコメントの要約機能 
  - 他　複数あり


# デモ動画



https://github.com/omegarin02/multi_task_assistant_for_discord/assets/107312091/2488c181-4a19-4bbb-9c7b-bc60b0dd3e52



# 必要なPCスペック
具体的にこのレベルというのはないですが、
（インストールとかは時間かかりますが）10年前の貧弱なPCでも動きます。  
※参考までに主は、GCPの無料枠の貧弱なサーバで動かしてます。  

今後のアップデートで、機能によってはハイスペックPCが必要になるかもしれませんが、  
その機能をOFFにすると、問題なく今の機能はお使いいただけるようにするつもりです。  

# セットアップの方法
## Windows(簡単版)
1. [こちらのサイト](https://gafuburo.net/how-to-discordbot/)を参考にdiscord botを作成する。
2. [python](https://www.python.org/downloads/)をinstallする。
3. Releaseから最新版Source code(zip)をダウンロードする。
4. chatGPTを使うのであれば、openaiからOPENAIのAPIkeyを取得する。使わない場合は次へ。
   - 他の方の記事ですが参考→[OpenAIのAPIキーの発行手順](https://auto-worker.com/blog/?p=6988#:~:text=%E3%82%82%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82-,OpenAI%E3%81%AEAPI%E3%82%AD%E3%83%BC%E3%81%AE%E7%99%BA%E8%A1%8C%E6%89%8B%E9%A0%86,-%E3%81%9D%E3%81%93%E3%81%A7%E3%80%81OpenAI%E3%81%AE)
5. google driveを使うのであれば、[Googleのドキュメント](https://developers.google.com/drive/api/quickstart/python?hl=ja)を参考に、「Googleclientライブラリをインストールする」の手前の手順までやる。使わない場合は次へ。
   - サービスアカウントを使う場合は[こちら参照](https://github.com/omegarin02/multi_task_assistant_for_discord/tree/feature/release-v1.0.0#google-service-account%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88)
6. init.batをダブルクリック
7. change-bot-setting.batをダブルクリックし、画面の指示に従って入力をする（※1）
8. start.batをダブルクリックしてbotを起動する(※2)
  - 画面が１つ立ち上がって、「ログインしました」と最後に書かれていればOKです。
  - 「ログインしました」と書かれた画面は閉じないでください。※2

※1 画面の詳細は、「botの設定方法.pdf」をご覧ください 
※2 画面を閉じたりPCの電源を切ると、botが終了してしまいます。


## Windows(git command利用版)
1. [こちらのサイト](https://gafuburo.net/how-to-discordbot/)を参考にdiscord botを作成する。
2. [python3](https://www.python.org/downloads/)をinstallする。
3. chatGPTを使うのであれば、openaiからOPENAIのAPIkeyを取得する。
   - 他の方の記事ですが参考→[OpenAIのAPIキーの発行手順](https://auto-worker.com/blog/?p=6988#:~:text=%E3%82%82%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82-,OpenAI%E3%81%AEAPI%E3%82%AD%E3%83%BC%E3%81%AE%E7%99%BA%E8%A1%8C%E6%89%8B%E9%A0%86,-%E3%81%9D%E3%81%93%E3%81%A7%E3%80%81OpenAI%E3%81%AE)
4. google driveを使うのであれば、[Googleのドキュメント](https://developers.google.com/drive/api/quickstart/python?hl=ja)を参考に、「Googleclientライブラリをインストールする」の手前の手順までやる
   - サービスアカウントを使う場合は[こちら参照](https://github.com/omegarin02/multi_task_assistant_for_discord/tree/feature/release-v1.0.0#google-service-account%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88)
5. `git clone -b ${Release_Tag} https://github.com/omegarin02/multi_task_assistant_for_discord.git`
6. `pip install -r requirements.txt`
7. `python3 config/config_maker.py`
8. 画面の指示に従って入力をする（※1,※2）
9. botを起動する
  - `python main.py`を実行する
  - ログインしましたと表示されたOKです。
  - ターミナルは閉じないでください
   
※1 画面の詳細は、「botの設定方法.pdf」をご覧ください  
※2 UIでの設定が面倒な方は、`config/config_base.json` を編集し、`config/config.json` という名前で保存してください

## MacOS/Linux
Windows(git command利用版と同じ)


## config.jsonのパラメータ説明
- common要素：botの共通の設定。
  - discord_api_key:  discord botのAPIキーを入力する
  - use_replit: [replit](https://replit.com)を使用する場合、trueにする。また使用する場合は、keepaliveのために冗長構成を持つようにreplitのプロジェクトを立てる必要がある。[参考](https://qiita.com/eureyuri/items/c5f041773c93a54b9f92)
  - use_google_drive: googleドライブからファイルを取得する場合は、trueにする。ローカルのファイルから読み取って使用するにはfalseを入力。
  - google_dirive_setting: googleドライブを使う場合の設定ファイルが格納されている（使わない場合はそのままでもよい）
- function: 機能の定義などの設定。
  - use: 機能群を使用をする場合はture, 使用しない場合はfalse
  - commands: discord bot で使うコマンド。コマンド名は変更しないでください。
    - discription: `/bot-help`コマンドで表示する内容
    - use: このコマンドを使用をする場合はture, 使用しない場合はfalse

それ以外の、各機能に依存するパラメータの説明は `doc/`配下に格納しているドキュメントをご覧ください

## google service accountを使用する場合
1. GCPにアクセスして、サービスアカウントを発行する。
2. サービスアカウントに対してsecretキーを発行する。
3. 発行したsecretキーを./config/secret_key.jsonという名前で保存する
4. config/config.jsonの`use_google_service_account`をtrueにする

# 免責事項
本スクリプトは個人的な開発で作成されたものです。  
運用に際しては、必要最低限の動作確認しかしておりません。  
したがって、本スクリプトで生じた不利益については一切責任を負いませんのであらかじめご了承ください。


# ライセンス
ご利用の際は原則的に下記のクリエイティブ・コモンズのライセンスをお守りください。
詳しくは、下記の補足をご覧ください
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/omegarin02/multi_task_assistant_for_discord">multi_task_assistant_for_discord</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://twitter.com/omegarin02">Omegarin</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

**ライセンスの補足**
| ライセンス\利用者 | 個人・グループの利用※1 | 事務所所属ライバー | ライバー事務所 | 個人事業主 | 法人 |
| ----- | ----- | -----| ----- | ----- | ----- |
| 作品のクレジットを表示※2 | 必須 | 必須 | 必須 | 必須 | 必須 |
| 営利目的での利用 | 可 | 無断利用不可(要相談) | 無断利用不可(要相談) | 無断利用不可(要相談)※3 | 無断利用不可(要相談) |
| 非営利目的での利用 | 可 |  可 | 可 | 可 | 可 |　
| 改造したものの公開する際のライセンス継承範囲 | コードのみ | コードのみ※4 | 資材一式 | 資材一式 | 資材一式 |

※1 「事務所所属ライバー」、「ライバー事務所」、「個人事業主」、「法人」以外の利用者。
※2 ご自身の任意のタイミングで、SNSや配信を通じて本ツールを使っていること（本リポジトリへのリンクや、作者のSNS）を書いていただけるだけで大丈夫です。   
※3 事業収入250万円未満は可 
※4 ライバー事務所の力を借りずに、自力で編集したものに限る。

# 最後に
### 開発に対する思い
開発者自身もマイナーながら配信活動しています。  
正直、一人で配信・動画編集・宣伝・企画などすべてこなすのはとても大変です。  
マイナーなのでもちろん活動にほとんどお金をかけることができません。
もちろん人を雇うこともできません。  
今ではグループを組んで活動しようとしておりますが、  
それでも学業・仕事をしもっての活動なので  
なかなか理想通りにはことが進みません。  
そのような方の手助けに少しでもなればと思って作成しております。  

### バグや機能追加
バグや追加してほしい機能などあればissueやTwitterのDMでご連絡ください。  

個人で開発しているのですべての要望に答えられる訳ではありませんが、  
使ってくださっている方がいると、今後の活動・開発の励みになりますので  
何卒よろしくお願い申し上げます。  

Twitter：[オメガりん](https://twitter.com/omegarin02)   
配信チーム：flare(アカウント作成検討中)
