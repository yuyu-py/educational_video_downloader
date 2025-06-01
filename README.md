# YouTube動画ダウンロードツール

## プロジェクト内容
yt-dlpライブラリを使用してYouTube動画を効率的にダウンロードするツールです。動画品質の選択、ファイル形式の指定、字幕の自動取得など、様々なカスタマイズ機能を備えています。Pythonを使った動画処理技術とユーザーインターフェース設計を学習することを目的として実装しました。動作テストとしてInternet Archiveの教育動画も利用できます。

## プロジェクト構成
```
youtube_video_downloader/
├── video_downloader.py     # メインプログラム
├── requirements.txt        # 依存関係管理
├── README.md              # プロジェクト説明書
└── .gitignore             # Git除外ファイル設定
```

## 必要要件/開発環境
- **Python 3.7以上**
- **インターネット接続** (動画ダウンロードのため)
- **VSCode** (開発環境)
- **Git** (バージョン管理)
- **FFmpeg** (ファイル形式変換時に必要)

### 使用ライブラリ
- **yt-dlp 2025.5.22** 動画ダウンロード処理

## 機能
- **動画品質選択** 480p、720p、1080p、最高画質から選択可能
- **ファイル形式変換** MP4、AVI、MKV形式への変換対応
- **字幕自動取得** 利用可能な字幕ファイルの自動ダウンロード
- **メタデータ保存** 動画の詳細情報をJSONファイルで保存
- **ダウンロード進行表示** リアルタイムで進行状況を確認
- **エラーハンドリング** 接続エラーや不正URLへの対応
- **ファイルサイズ表示** ダウンロード前のサイズ確認機能
- **URL検証機能** 対応サイトの自動判別

## 実行方法

### 1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/youtube_video_downloader.git
cd youtube_video_downloader
```

### 2. 仮想環境の作成・アクティベート

**Windows**
```bash
python -m venv myenv
myenv\Scripts\activate
```

**macOS**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 4. プログラムの実行
```bash
python video_downloader.py
```

実行後、URL入力画面が表示されます。
YouTubeのURLを入力して動画をダウンロードできます。
停止するには 'q' を入力してください。

## 使用例
動作テスト用として以下のURLで確認できます。
```
https://archive.org/details/BigBuckBunny_124
```

## 対応サイト
- YouTube (youtube.com, youtu.be)
- Internet Archive (archive.org)

## ダウンロードファイル
動画ファイルは「downloads」フォルダに保存されます。
設定により以下のファイルが生成されます。
- 動画ファイル (.mp4, .avi, .mkv等)
- 動画情報ファイル (.info.json)
- 字幕ファイル (.vtt, .srt等)

## 開発者
YuYu