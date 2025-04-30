# table-definition-generator

## 概要
`db-schema-md` は，MySQL データベースのスキーマ（テーブル定義・カラム情報・インデックス情報）を **Markdown** 形式で自動出力するコマンドラインツールです．

## 目次
- [動作確認環境](#動作確認環境)
- [ディレクトリ構成](#ディレクトリ構成)
- [インストール](#インストール)
- [使い方](#使い方)
- [設定](#設定)
- [オプション一覧](#オプション一覧)
- [サンプル](#出力例)
- [貢献](#貢献)
- [ライセンス](#ライセンス)


## 動作確認環境
- **Python**: 3.7 以上
- **ライブラリ**:
  - click 8.x
  - Jinja2 3.x
  - mysql-connector-python 8.x
- **OS**: macOS Sonoma ver14.6/ Ubuntu 22.04

## ディレクトリ構成
```
your-project/
├── Makefile                    # セットアップ・実行用タスク
├── requirements.txt            # Python 依存パッケージ一覧
├── config_sample.json          # サンプル設定ファイル(DB情報)
├── config.json                 # 実際に使用する設定ファイル(※Git管理対象外)
├── src/
│   └── schema_md/              # パッケージ本体
│       ├── __init__.py
│       ├── __main__.py         # `python -m schema_md` エントリポイント
│       ├── cli.py              # CLI 定義（click）
│       ├── config.py           # 設定ファイル読み込み
│       ├── db.py               # DB 接続／情報取得
│       ├── renderer.py         # Markdown 出力ロジック(Jinja2)
│       └── templates/
│           └── schema.md.jinja # Markdown テンプレート
├── output/                     # 出力先ディレクトリ(※Git管理対象外)
│   └── schema.md               # 生成された Markdown
└── README.md                   # プロジェクト概要（本ファイル）
```

## インストール
リポジトリをクローンしたら，Makefile の setup ターゲットを使って必要な環境構築を行います．
```bash
# 1. リポジトリをクローン
git clone https://github.com/yourname/db-schema-md.git
cd db-schema-md

# 2. Makefile で仮想環境作成＆依存インストール
make setup

# 3. 動作確認
make run CONFIG=config.json OUTPUT=output/schema.md
```
- make setup
  - .venv ディレクトリに仮想環境を作成
  - requirements.txt→依存インストール
  - pip install -e . で CLI コマンドを登録
- make run
  - .venv をアクティベートして schema-md コマンドを呼び出し

※ PyPI への公開は未実施ですので，`pip install db-schema-md`はまだ使えません．

## 使い方
リポジトリをセットアップした後は，以下のコマンドで実際にスキーマの Markdown 出力ができます

A. Makefile 経由
```bash
# output/schema.md に出力
make run CONFIG=config.json OUTPUT=output/schema.md
```
B.直接 CLI を呼び出す
```bash
# デフォルト設定を使う場合
schema-md

# 設定ファイル・出力先を個別に指定する場合
schema-md \
  --config path/to/config.json \
  --output path/to/output.md
```

### 主なオプション一覧

| オプション         | 説明                             | デフォルト       | 
| ------------------ | -------------------------------- | ---------------- | 
| -c, --config PATH  | JSON 形式の設定ファイルのパス    | config.json      | 
| -o, --output PATH  | 生成する Markdown ファイルのパス | output/schema.md | 
| -h, --help         | ヘルプメッセージを表示           |                  | 

### ヘルプの確認
CLI の詳細な使い方やオプションは --help でいつでも確認できます．
```bash
schema-md --help

Usage: schema-md [OPTIONS]

Options:
  -c, --config PATH   Path to config.json (default: config.json)
  -o, --output PATH   Output Markdown file (default: output/schema.md)
  -h, --help          Show this message and exit.
```

### 注意事項
- `config.json` は **機密情報** を含むため，Git 管理対象から除外してください．
- `output/` ディレクトリ内のファイルは生成専用です．
- MySQL 接続情報や権限設定によっては，`SHOW TABLE STATUS` や `SHOW FULL COLUMNS` が実行できない場合があります．
- 大規模なデータベースでは実行に時間がかかる場合があります．


## 出力例
以下は出力例の一部です．

## sample (サンプルテーブル)

| 論理名        | 物理名    | 型                                                           | キー制約 | Null制約 | その他制約                                   |
|:-------------:|:---------:|:------------------------------------------------------------:|:-------:|:-------:|:--------------------------------------------:|
| ID            | id        | int unsigned                                                 | PRI     | NO      | auto_increment                              |
| カラム1       | column1   | int                                                          | MUL     | NO      |                                              |
| 文字列カラム2 | column2   | varchar(50)                                                  |         | YES     |                                              |
| 日時          | column3   | datetime                                                     | MUL     | YES     |                                              |
| カテゴリー    | category  | enum(<br>  'INFO',<br>  'WARN',<br>  'ALERT'<br>)           |         | YES     |                                              |
| 作成日時      | created_at| datetime                                                     |         | YES     | DEFAULT_GENERATED                           |
| 更新日時      | updated_at| datetime                                                     |         | YES     | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |

| インデックス名         | 対象カラム名  | 複合キーのキー順序 |
|:---------------------:|:------------:|:-----------------:|
| PRIMARY               | id           | 1                 |
| Sample_INDEX          | column1      | 1                 |
| Sample_INDEX2         | column3      | 1                 |
|                       | column2      | 2                 |

## 貢献
このプロジェクトへのご協力ありがとうございます．
以下の手順に沿って Pull Request を送ってください．

### 1. Issue を立てる
- バグ報告や機能要望はまず Issue を作成してください．
- タイトルと本文に**再現手順**，**環境情報**（OS，Python バージョン）をお書きください．

### 2. Fork & ブランチ作成
```bash
git clone https://github.com/yourname/db-schema-md.git
cd db-schema-md
git checkout -b feature/your-feature
```
### 3. コミット & Push
- コミットメッセージは Conventional Commits 形式で
```bash
git add .
git commit -m "feat(cli): add verbose logging"
git push origin feature/your-feature
```
### 4. Pull Request を作成
- GitHub 上で “Compare & pull request” をクリックし，変更内容の説明を追加．
### 5. レビュー・マージ
- メンテナーがレビュー後，マージします

## ライセンス
`db-schema-md` は [MIT ライセンス](LICENSE) のもとで公開されています．  
詳細はリポジトリルートの [LICENSE](LICENSE) ファイルをご覧ください．