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
- 今後も追加予定

# セットアップの方法
## Windows(簡単版)
1. [こちらのサイト](https://gafuburo.net/how-to-discordbot/)を参考にdiscord botを作成する。
2. [python](https://www.python.org/downloads/)をinstallする。
3. Releaseから最新版Source code(zip)をダウンロードする
4. chatGPTを使うのであれば、openaiからOPENAIのAPIkeyを取得する。
   - 他の方の記事ですが参考→[OpenAIのAPIキーの発行手順](https://auto-worker.com/blog/?p=6988#:~:text=%E3%82%82%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82-,OpenAI%E3%81%AEAPI%E3%82%AD%E3%83%BC%E3%81%AE%E7%99%BA%E8%A1%8C%E6%89%8B%E9%A0%86,-%E3%81%9D%E3%81%93%E3%81%A7%E3%80%81OpenAI%E3%81%AE)
5. google driveを使うのであれば、[Googleのドキュメント](https://developers.google.com/drive/api/quickstart/python?hl=ja)を参考に、「Googleclientライブラリをインストールする」の手前の手順までやる
   - サービスアカウントを使う場合は[こちら参照]()
6. init.batをダブルクリック
7. change-bot-setting.batをダブルクリックし、画面の指示に従って入力をする（※1）
8. start.batをダブルクリックしてbotを起動する(※2)
  - 画面が１つ立ち上がって、「ログインしました」と最後に書かれていればOKです。
  - この画面は閉じないでください

※1 画面の詳細は、「botの設定方法.pdf」をご覧ください

## Windows(git command利用版)
1. [こちらのサイト](https://gafuburo.net/how-to-discordbot/)を参考にdiscord botを作成する。
2. [python3](https://www.python.org/downloads/)をinstallする。
3. `git clone -b ${Release_Tag} https://github.com/omegarin02/multi_task_assistant_for_discord.git`
4. `pip install -r requirements.txt`
5. `python3 config/config_maker.py`
6. 画面の指示に従って入力をする（※1,※2）
7. botを起動する
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
ご利用の先は下記のクリエイティブ・コモンズのライセンスをお守りください。
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/omegarin02/multi_task_assistant_for_discord">multi_task_assistant_for_discord</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://twitter.com/omegarin02">Omegarin</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

**ライセンスの補足**
- 作品のクレジットを表示すること
  - ご自身の任意のタイミングで、SNSや配信を通じて本ツールを使っていること（本リポジトリへのリンクや、作者のSNS）を書いていただけるだけで大丈夫です。
- 営利目的での利用をしないこと
  - ただし、個人利用の場合は営利目的でも利用可能とします。（連絡不要です）
  - Liver事務所に所属している方の使用や、会社や事業の営利目的とした使用の場合、本リポジトリのコードをそのまま利用することは全てNGです。ご利用の際は事前にご相談ください。
    - ただし、改造して独自のツールを別途作る場合は使用可能とします。改造したツールを使用する場合でも、必ず本リポジトリのコードをベースに開発したことをSNSや配信にて明言してください。
- 元の作品と同じ組み合わせのCCライセンスで公開すること 
  - 改変したコードや資材を公開する際は、本ライセンスを継承してください。
    - ただし、個人利用の場合は、ライセンスの継承はコードのみで良いです。デモ用の資材などがもしあったとしても、継承は任意です。
    - Liver事務所に所属している方の使用や、会社や事業の営利目的とした使用の場合、デモ用資材一式とコードを公開し、資材とコードの全てに対してライセンスを継承してください。

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
