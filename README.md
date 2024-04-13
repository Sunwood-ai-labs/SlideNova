---
title: SlideNova
emoji: 🐠
colorFrom: indigo
colorTo: green
sdk: docker
pinned: false
license: mit
app_port: 8501
---



<p align="center">
<img src="https://media.githubusercontent.com/media/Sunwood-ai-labs/SlideNova/develop/docs/SlideNova_icon.png" width="100%">
<br>
<h1 align="center">SlideNova</h1>
<h3 align="center">
  ～Experience Slide-Making Reinvented～

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Sunwood-ai-labs/SlideNova)
[![GitHub Stars](https://img.shields.io/github/stars/Sunwood-ai-labs/SlideNova)](https://github.com/Sunwood-ai-labs/SlideNova)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/SlideNova)](https://github.com/Sunwood-ai-labs/SlideNova)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/SlideNova)](https://github.com/Sunwood-ai-labs/SlideNova)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/SlideNova?sort=date&color=red)](https://github.com/Sunwood-ai-labs/SlideNova)
</h3>
</p>

## 🚀 はじめに

SlideNovaは、Markdownからモダンで美しいスライドを簡単に作成できるWebアプリケーションです。
[Slidev](https://sli.dev/)を使用しており、スライドの生成はDockerコンテナ内で行われます。
Streamlitを使用した直感的なユーザーインターフェイスで、Markdownを入力するだけですぐにスライドを作成できます。

## 更新情報

### [2024/04/13] SlideNova v0.1.0 [リリースノート](https://github.com/Sunwood-ai-labs/SlideNova/releases/tag/v0.1.0)
- Markdownからスライド生成するWebアプリの公開
- Dockerを使った環境構築の自動化
- Streamlitによる直感的なユーザーインターフェイス
- スライドのダウンロード機能
- ドキュメントの拡充
- 開発環境の整備とGitHub Actionsの設定

## 🌟 主な特徴

- 📝 Markdownでスライド作成
- 🎨 Slidevを使用したモダンなスライドデザイン
- 🐳 Dockerによる環境構築の簡易化
- 🖥️ Streamlitによる使いやすいWebUI

## 📦 インストール

SlideNovaを使用するには、DockerとDocker Composeが必要です。以下の手順に従ってください。

1. このリポジトリをクローンします。

```bash
git clone https://github.com/Sunwood-ai-labs/SlideNova.git
```

2. プロジェクトディレクトリに移動します。

```bash
cd SlideNova
```

3. Docker Composeを使用してSlideNovaを起動します。

```bash
docker-compose up --build
```

4. ブラウザで `http://localhost:8502` を開きます。

## 🛠️ 使い方

1. Markdownエディタにスライドのコンテンツを入力します。
2. 「Generate Slides」ボタンをクリックします。
3. 生成されたスライドが表示されます。

## Develop command

```bash
yes | npx slidev export slides/demo.md --format png --output slides/out/ --dark
```

## 📖 ドキュメント

より詳細な情報は、[ドキュメント](docs/)を参照してください。

## 🤝 コントリビューション

コントリビューションは歓迎します！詳細は[コントリビューションガイド](CONTRIBUTING.md)を参照してください。

## 📜 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 📧 お問い合わせ

ご質問やご提案がありましたら、[Issue](https://github.com/Sunwood-ai-labs/SlideNova/issues)を作成してください。
