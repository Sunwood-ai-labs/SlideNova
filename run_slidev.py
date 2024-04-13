# run_slidev.py
import os
import subprocess

# Slideを格納するディレクトリを指定
slide_dir = "./slides"

# Slideのエントリーポイントを指定
slide_entry = "slides.md"

# slidevコマンドを実行してスライドを開発モードで起動
# subprocess.run(["npx", "slidev", slide_entry])

# slidevコマンドを実行してスライドをビルド
subprocess.run(["npx", "slidev", "build", slide_entry])