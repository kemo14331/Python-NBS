from setuptools import setup

setup(
    name="Python-NBS",                 # モジュールの名前
    version="1.0.0",              # モジュールのバージョン
    author="Kemo",             # モジュールの作者
    url="",                       # モジュールのホームページ
    description="A python library for reading NBS files",    # モジュールの説明(help(hello)で確認可能)
    install_requires=[],          # 依存パッケージ([pip install -e .]実行時に一緒にインストール)
    extras_require={
        "develop" : [],           # 拡張依存パッケージ([pip install -e . develop]実行時に一緒にインストール)
    }
)