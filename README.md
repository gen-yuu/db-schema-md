# db-schema-md

## 概要
`db-schema-md` は、MySQL データベースのスキーマ（テーブル定義・カラム情報・インデックス情報）を **Markdown** 形式で自動出力するコマンドラインツールです。

主な特徴：
- CLI で簡単に実行可能
- Jinja2 テンプレートによる柔軟なレイアウトカスタマイズ
- テーブル一覧、カラム定義、インデックス情報をまとめて出力

## 動作確認環境
- **Python**: 3.7 以上
- **ライブラリ**:
  - click 8.x
  - Jinja2 3.x
  - mysql-connector-python 8.x
- **対応 OS**: macOS / Linux / Windows (WSL)

## 構成
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

## 注意事項
- `config.json` は **機密情報** を含むため、Git 管理対象から除外してください。
- `output/` ディレクトリ内のファイルは生成専用です。
- MySQL 接続情報や権限設定によっては、`SHOW TABLE STATUS` や `SHOW FULL COLUMNS` が実行できない場合があります。
- 大規模なデータベースでは実行に時間がかかる場合があります。

* outputディレクトリのsampleから始まるファイルを除く全てのファイル・ディレクトリ
* config.json
* packages（プロジェクト情報ではないがGit管理不要のため）

## 使用方法
1. リポジトリをクローン
   ```bash
   git clone https://github.com/yourname/db-schema-md.git
   cd db-schema-md
   ```
2. Python 環境を準備・依存インストール
   ```bash
   make setup
   ```
3. スキーマを Markdown に出力
   ```bash
   make run CONFIG=config.json OUTPUT=output/schema.md
   ```
4. 結果を確認
   ```bash
   cat output/schema.md
   ```

   ## sample (サンプルテーブル)
以下は出力例の一部です。

```markdown
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
```

---
