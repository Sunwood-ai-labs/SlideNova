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
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/SlideNova?color=orange)](https://github.com/Sunwood-ai-labs/SlideNova)
</h3>
</p>

## 🚀 はじめに

[SlideNova](https://github.com/Sunwood-ai-labs/SlideNova/blob/develop/docs/SlideNova.md)は、生成AIを活用することを前提とした革新的なMarkdownベースのスライド作成Webアプリケーションです。生成AIとの連携により、効率的かつ高品質なスライド作成を実現します。

## 更新情報

### [2024/04/14] SlideNova v0.6.0 [リリースノート](https://github.com/Sunwood-ai-labs/SlideNova/releases/tag/v0.6.0)
- [Hugging Face Spacesでのアプリ公開](https://huggingface.co/spaces/MakiAi/SlideNova)
- スライドのダウンロード機能の改善
- ユーザーインターフェイスの改善
- ドキュメントの拡充とリンクの最適化
- 開発環境の改善とGitHub Actionsの設定
- プロジェクトアイコンの追加とREADMEの見た目の向上

### [2024/04/13] SlideNova v0.1.0 [リリースノート](https://github.com/Sunwood-ai-labs/SlideNova/releases/tag/v0.1.0)
- Markdownからスライド生成するWebアプリの公開
- Dockerを使った環境構築の自動化
- Streamlitによる直感的なユーザーインターフェイス
- スライドのダウンロード機能
- ドキュメントの拡充
- 開発環境の整備とGitHub Actionsの設定
- 
## ✨ 主な特徴

- 📝 **Markdownでのスライド作成**: Markdownの簡潔で直感的な記法を使ってスライドのコンテンツを作成できます。
- 🎨 **モダンなスライドデザイン**: Slidevを使用することで、洗練されたデザインのスライドを生成できます。
- 🐳 **Dockerによる環境構築の簡易化**: Dockerを活用し、複雑な環境設定なしですぐに使い始められます。
- 🖥️ **使いやすいWebUI**: Streamlitを採用した直感的なWebインターフェイスで、スムーズなスライド作成が可能です。
- 💾 **スライドのダウンロード**: 作成したスライドをPDFまたは画像形式でダウンロードできます。

## 🚀 はじめに

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

1. Markdownエディタにスライドのコンテンツを入力します。Markdownの記法に従って、見出し、箇条書き、画像、コードブロックなどを使用してスライドを構成します。

2. 「Generate Slides」ボタンをクリックすると、入力したMarkdownに基づいてスライドが生成されます。

3. 生成されたスライドが表示されます。スライドのデザインやレイアウトは自動的に最適化されます。

4. 必要に応じて、スライドをPDFまたは画像形式でダウンロードすることができます。

### 使用例

- サンプルのMarkdownファイル: [`slides/demo.md`](slides/demo.md)
- サンプルのスライド画像: [`slides/sample`](slides/sample)

## 📖 ドキュメント

より詳細な情報や[SlideNova]の機能については、[ドキュメント](https://github.com/Sunwood-ai-labs/SlideNova/blob/develop/docs/SlideNova.md)を参照してください。

## 🤝 コントリビューション

SlideNovaはオープンソースプロジェクトであり、コミュニティからのコントリビューションを歓迎しています。バグ報告、機能リクエスト、プルリクエストなどを通じて、SlideNovaの改善にご協力ください。詳細は[コントリビューションガイド](CONTRIBUTING.md)を参照してください。

## 📜 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 📧 お問い合わせ

ご質問やご提案がありましたら、[Issue](https://github.com/Sunwood-ai-labs/SlideNova/issues)を作成してください。フィードバックは常に歓迎です！

プレゼンテーションの未来を切り拓く SlideNova で、あなたのアイデアに命を吹き込みましょう！✨