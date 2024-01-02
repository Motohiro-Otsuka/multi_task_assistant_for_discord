# scheduler機能説明
大きく下記の４つの機能を有する
- スケジュール画像の自動生成 (schedule-print)
- スケジュールの変更(schedule-edit)
- スケジュールの確認(schedule-show)
- スケジュール画像のグリッド表示(schedule-grid)

また、本機能を実行するためには次のファイルが必要
- スケジュールが書かれたエクセルファイル
- 時刻や日付の文字画像
- 配信コンテンツの文字画像 or 画像
- 配信サイトの画像
※この辺は、sampleに含まれているファイルをご覧ください。


## スケジュール画像の自動生成 (schedule-print)

ディスコード上で`/schedule-print`で呼び出す。
呼び出されると、config.jsonで指定したファイルから
スケジュール画像を作成し、チャットに張り付ける。
文字の配置や、画像などはcofingから調整する。

## スケジュールの変更(schedule-edit)
ディスコード上で`/schedule-edit`で呼び出す。
呼び出されると、現在のスケジュールをエクセルファイルから読み取って
スレッド上に返信します。
変更したい日付を送信すると、その日のスケジュールだけが返信されるので
その内容をコピーしたうえで、変更後の内容を送信してください。
自動的に、エクセルファイルに内容が反映されます。
※日付変更は未対応

## スケジュールの確認(schedule-show)
ディスコード上で`/schedule-show`で呼び出す。
呼び出されると、現在のスケジュールをエクセルファイルから読み取って
スレッド上に返信します。

## スケジュール画像のグリッド表示(schedule-grid)
ディスコード上で`/schedule-grid`で呼び出す。
呼び出されると、スケジュール画像のベースとなる画像にグリッド線を引いて
スレッド上に返信します。
黄色い線は50px、赤い線は100pxごとに引かれています。

# 設定項目の説明
configで設定する値は下記の通り
```json
"live_scheduler":{
    "use":true,#task/scheduler.pyを読み込んでよい場合はtrue,ダメなときはfalse
    "googleDrive":true,#googleドライブと連携するときはture,連携しないときはfalse
    "commands":{
        "schedule-print":{
            "discription":"スケジュール画像を生成する",
            "use":true #スケジュール画像の生成機能を使う場合はtrue,ダメなときはfalse
        },
        "schedule-grid":{
            "discription":"スケジュール画像にグリッド線を入れた画像を生成する。主にデバッグ用。（黄：10px, 赤：50px）",
            "use":true #スケジュール画像にグリッド線を引く機能を使う場合はtrue,ダメなときはfalse
        },
        "schedule-show":{
            "discription":"現在登録されているスケジュールを表示する",
            "use":true #現在のスケジュールを確認する機能を使う場合はtrue,ダメなときはfalse
        },
        "schedule-edit":{
            "discription":"現在登録されているスケジュールを変更する",
            "use":true #現在のスケジュールを変更する機能を使う場合はtrue,ダメなときはfalse
        }
    },
    "files":{
        "icons":{ #毎回配信者が変わるような場合はその人たちの名前と画像を列挙する
            "ライバーさんの名前":"googleDrive共有リンク or local file path"
        },
        "contents":{ #配信内容の画像 or 文字画像のファイルを列挙する
            "スプラ":"googleDrive 共有リンクor local file path",
            "雑談":"googleDrive 共有リンクor local file path"
        },
        "platform":{ #配信サイト画像ファイルを列挙する
            "YouTube":"googleDrive 共有リンクor local file path",
            "ミラティブ":"googleDrive 共有リンクor local file path",
            "ツイキャス":"googleDrive 共有リンクor local file path",
            "ニコ生":"googleDrive 共有リンクor local file path"
        },
        "number_img":{ #数字の文字画像をのファイルを列挙する
            "0":"googleDrive 共有リンクor local file path",
            "1":"googleDrive 共有リンクor local file path",
            "2":"googleDrive 共有リンクor local file path",
            "3":"googleDrive 共有リンクor local file path",
            "4":"googleDrive 共有リンクor local file path",
            "5":"googleDrive 共有リンクor local file path",
            "6":"googleDrive 共有リンクor local file path",
            "7":"googleDrive 共有リンクor local file path",
            "8":"googleDrive 共有リンクor local file path",
            "9":"googleDrive 共有リンクor local file path",
            ":":"googleDrive 共有リンクor local file path"
        },
        "format":"googleDrive 共有リンクor local file path",#配信スケジュール画像のベースとなるパスを張り付ける
        "schedule":"googleDrive 共有リンクor local file path",#配信スケジュールが書かれているエクセルファイルのパスを張り付ける
        "tmp_dir_path":"tmp"
    },
    "grid":{
        "column_size":{#カラムサイズや文字サイズを定義する
            "day":{#日付１文字あたりのサイズ（xが幅、yが高さ)
                "x":30,
                "y":70
            },
            "time":{#時刻１文字あたりのサイズ（xが幅、yが高さ)
                "x":20,
                "y":70
            },
            "content":{#配信内容の画像のサイズ（xが幅、yが高さ)
                "x":340,
                "y":70
            },
            "liver":{#配信者の画像のサイズ（xが幅、yが高さ)
                "x":78,
                "y":70
            },
            "platform":{#配信サイトの画像のサイズ（xが幅、yが高さ)
                "x":130,
                "y":70
            }
        },
        "column_first_point":{#各カラムの１行目の左上の座標の定義
            "day":{
                "x":95,
                "y":145
            },
            "time":{
                "x":170,
                "y":145
            },
            "content":{
                "x":280,
                "y":145
            },
            "liver":{
                "x":620,
                "y":145
            },
            "platform":{
                "x":930,
                "y":145
            }
        }
    }
}
```
※設定する際は、#記号も含めて、それ以降の1行は記載しないこと。（正常にjsonが読み込めない）