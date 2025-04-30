import click
from pathlib import Path

from .config import load_config
from .db import get_connection, fetch_tables, fetch_columns, fetch_indexes
from .renderer import render_markdown

@click.command()
@click.option(
    '--config', '-c','config_path',
    default=Path('config.json'),
    show_default=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help='Path to config.json (copy from sample_config.json)'
)
@click.option(
    '--output', '-o','output_path',
    default=Path('output/schema.md'),
    show_default=True,
    type=click.Path(dir_okay=False, path_type=Path),
    help='Output Markdown file under output/'
)

def main(config_path: Path, output_path: Path):
    """
    MySQL のスキーマ情報を読み込んで Markdown ドキュメントを生成します。
    """
    # 設定読み込み
    cfg = load_config(config_path)

    # DB接続
    conn = get_connection(cfg)

    # テーブル情報取得
    tables = fetch_tables(conn)
    for tbl in tables:
        tbl['columns'] = fetch_columns(conn, tbl['Name'])
        tbl['indexes'] = fetch_indexes(conn, tbl['Name'])

    # Markdown生成
    md = render_markdown(tables)

    # ファイル書き出し
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md, encoding='utf-8')

    click.echo(f'Schema exported to {output_path}')

if __name__ == '__main__':
    main()