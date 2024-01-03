# 初めに
本リポジトリは、Live配信者や動画配信者のアシスタントをdiscordbotさせようと試みたコードが格納されている。

機能は、機能一覧に記載の通りである。

また、本READMEは、pythonを使ったことがある人、もしくはプログラミングの経験を有している人向けに記載しており、完全な初心者に対して配慮しきれていない部分があると思いますがご了承ください。

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
- 今後も追加予定

# 使い方
各機能の詳細は`doc/`をご確認ください。  
以下の説明に（google）と書かれている項目は、googleドライブにあるファイルを使用したい場合のみ行う。
1. [こちらのサイト](https://gafuburo.net/how-to-discordbot/)を参考にdiscord botを作成する。
2. [python](https://www.python.org/downloads/)をinstallする。
3. pipコマンドをinstallする。
4. （あとでgit cloneをする場合は）gitコマンドをinstallする。
5. 本リポジトリをclone or ダウンロードする。  
   - cloneの場合：
     - `git clone https://github.com/omegarin02/multi_task_assistant_for_discord.git`
     - `cd multi_task_assistant_for_discord`
   - ダウンロードの場合：
     - 画面右上の緑の`code`ボタンをクリックして、`donload zip`をクリックする。
     - zipファイルを展開する
     - 以降は、zipファイルを展開したフォルダ or ディレクトリで作業をする
6. `pip install -r requirements.txt`必用なライブラリをinstallする。
7. `./config/config_sample.json` を `./config/config.json`にコピーしてconfigファイルを作る※1
8. (google) [googleのドキュメント](https://developers.google.com/drive/api/quickstart/python?hl=ja)を参考に、「デスクトップアプリケーションの認証情報を承認する」までを行う。
9.  (google) 5で作った `client_secrets.json`はconfig配下に配置する
10. `python main.py`でボットを起動する。  
   (google)google driveを使用する場合は初めの１回だけ認証を求められる。その後は、認証情報が `config/saved_credentials.json`に格納される
11. discordで`/bot-help`と入力し、使い方と説明が表示されることを確認する。

## ※1 config.jsonのパラメータ説明
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

# 免責事項
本スクリプトは個人的な開発で作成されたものです。  
運用に際しては、必要最低限の動作確認しかしておりません。  
したがって、本スクリプトで生じた不利益については一切責任を負いませんのであらかじめご了承ください。


# ライセンス
ご利用の先は下記のクリエイティブ・コモンズのライセンスをお守りください。
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/omegarin02/multi_task_assistant_for_discord">multi_task_assistant_for_discord</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://twitter.com/omegarin02">Omegarin</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

**ライセンスの補足**
- 作品のクレジットを表示すること
  - 配信や自身のSNSで、本ツールを使っていること（本リポジトリへのリンクや、作者のSNS）を書いていただけるだけで大丈夫です。
- 営利目的での利用をしないこと
  - ただし、個人の利用の場合は営利目的でも利用可能とします。
  - Liver事務所に所属している人の使用や、会社や事業での使用で営利目的としている場合は全てNGです。ご利用の際は事前にご連絡ください。
- 元の作品と同じ組み合わせのCCライセンスで公開すること 
  - ご自由にスクリプト等を変えていただいて構いません。
  - 改変したコードを公開する際は、本ライセンスを継承してください。

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
バグや追加してほしい機能などあればissueに起票していただいてもよいですし、  
TwitterのDMでご連絡いただいても構いません。  

個人で開発しているのですべての要望に答えられる訳ではありませんが、  
使ってくださっている方がいると、今後の活動・開発の励みになりますので  
何卒よろしくお願い申し上げます。  


Twitter：[オメガりん](https://twitter.com/omegarin02)   
配信チーム：flare(アカウント作成検討中)