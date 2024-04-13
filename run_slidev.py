# run_slidev.py
import os
import subprocess


# slidevコマンドを実行してスライドをビルド
subprocess.run(["npx slidev export slides/demo.md --format png --output slides/out/ --dark -t"])