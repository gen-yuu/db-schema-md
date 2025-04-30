"""
schema_md パッケージのエントリポイント。
python -m schema_md でこのモジュールが実行され、cli.main() が呼び出されます。
"""

from .cli import main

if __name__ == "__main__":
    main()