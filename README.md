# プロジェクト名

## 概要
ここにプロジェクトの概要を記述してください。プロジェクトの目的や主な機能、利用技術などを簡潔に紹介します。

## データセットの準備
このプロジェクトで使用するデータセットはGoogle Driveに保存されています。以下の手順に従ってアクセスし、必要なデータをダウンロードしてください。

1. Google Driveの[共有リンク](https://docs.google.com/spreadsheets/d/1qYi2QqqIt4TG9KMEnDJVIep0rgVt1QS6/edit?usp=sharing&ouid=106553213312574087716&rtpof=true&sd=true)にアクセスします。
2. 必要なファイルを選択し、ローカル環境にダウンロードします。
3. `python-template/dataset`に格納します。

## 環境構築
このプロジェクトは `pyenv` と `pip` を使用してPython環境を構築します。以下の手順に従って環境をセットアップしてください。

```bash
# Pythonバージョンのインストール
pyenv install 3.11.0
pyenv global 3.11.0

# 仮想環境の作成
python -m venv myenv

# 仮想環境の有効化
source myenv/bin/activate

# 必要なパッケージのインストール
pip install -r requirements.txt
```

### 環境変数の設定
`.env.sample`に記載する
```
OPENAI_API_KEY=your-api-key
```
利用する際には、`.env.sample`をコピーして`.env`ファイルを作成する。

#### pythonコードで読み込む場合
```python
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

# os.environを用いて環境変数を表示させる
print(os.environ['API_KEY'])
```

## 実行方法
プロジェクトをローカルで実行する方法を記述します。
```bash
# メインスクリプトを実行
python main.py
```

## テストの実行
このプロジェクトでは ruff を使用してコードの静的解析を行います。以下の手順に従ってテストを実行してください。
```bash
# テストの実行
ruff check

# 自動整形する場合
ruff check --fix
```

## ブランチのルール
- 絶対にmainにpushしないこと。
- developブランチからfeature、hotfixのブランチを作成する


| ブランチ名   | 役割                         | 派生元    | マージ先        |
|----------|----------------------------|---------|--------------|
| `main` | 公開するものを置くブランチ       | -       | ここのブランチの環境でリリース |
| `develop` | 開発中のものを置くブランチ      | `main` | `main`     |
| `release` | 次にリリースするものを置くブランチ | `develop` | `develop`, `master` |
| `feature-*` | 新機能開発中に使うブランチ   | `develop` | `develop`    |
| `hotfix-*` | 公開中のもののバグ修正用ブランチ | `main`  | `develop`, `main` |

### ブランチ名の例
1. feature-名前-機能名
2. feature-takahashi-login
3. hotfix-sato-userlist

### ブランチの作成方法
```bash
# リモートレポジトリをクローンする
git clone git@github.com:aice-co-jp/python-template.git
cd python-template

# developブランチに移動する
git checkout develop

# レポジトリを作成する 
git checkout -b feature-takahashi-login
```

### 変更内容をpushするまで
```bash
# 変更内容を確認する
git status

# 変更内容をリモートに反映させたいファイルを選択する（複数ある場合はスペースで区切ってaddする。全て反映させたい場合はadd -A）
git add main.py

# 変更内容を保存する（コミットメッセージは変更内容をトラックしやすい内容で記載する）
git commit -m "initial commit"

# 変更内容をリモートへ反映させる
git push origin python-template