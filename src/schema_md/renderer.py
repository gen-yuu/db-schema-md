from typing import List, Dict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

# テンプレートディレクトリを指定
template_dir = Path(__file__).parent / "templates"
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(["jinja"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


def render_markdown(tables: List[Dict]) -> str:
    """
    テーブル／カラム／インデックス情報のリストを受け取り、
    Jinja2 テンプレートを用いて Markdown ドキュメント文字列を返します。

    :param tables: SHOW TABLE STATUS → SHOW FULL COLUMNS → SHOW INDEX を結合した構造
    :return: Markdown 形式の文字列
    """
    template = env.get_template("schema.md.jinja")
    return template.render(tables=tables)