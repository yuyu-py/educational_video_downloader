import yt_dlp
import os


class VideoDownloader:
    def __init__(self):
        self.download_path = "downloads"
        self.setup_download_directory()
        
    def setup_download_directory(self):
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
            print(f"ダウンロードフォルダ '{self.download_path}' を作成しました")
        else:
            print(f"ダウンロードフォルダ '{self.download_path}' を使用します")
            
    def get_custom_download_options(self, quality_format, file_format):
        options = {
            'format': quality_format,
            'noplaylist': True,
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s',
            'writeinfojson': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
        }
        
        if file_format != 'any':
            options['postprocessors'] = [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': file_format,
            }]
        
        return options
    
    def download_video_with_options(self, url, quality_format, file_format):
        try:
            options = self.get_custom_download_options(quality_format, file_format)
            
            with yt_dlp.YoutubeDL(options) as downloader:
                print(f"\n動画情報を取得中: {url}")
                info = downloader.extract_info(url, download=False)
                
                print(f"タイトル: {info.get('title', '不明')}")
                print(f"再生時間: {self.format_duration(info.get('duration', 0))}")
                print(f"ファイルサイズ: {self.format_filesize(info.get('filesize', 0))}")
                
                if self.display_settings(quality_format, file_format):
                    print("\nダウンロードを開始します...")
                    downloader.download([url])
                    print("ダウンロードが完了しました")
                    self.show_downloaded_files(info.get('title', 'unknown'))
                else:
                    print("ダウンロードをキャンセルしました")
                
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            
    def format_duration(self, seconds):
        if not seconds:
            return "不明"
        
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        
        if hours > 0:
            return f"{hours}時間{minutes}分{seconds}秒"
        elif minutes > 0:
            return f"{minutes}分{seconds}秒"
        else:
            return f"{seconds}秒"
        
    def run(self):
        print("=== Internet Archive教育動画ダウンローダー ===")
        print("教育動画のURLを入力してください")
        print("例: https://archive.org/details/BigBuckBunny_124")
        print()
        
        while True:
            url = input("動画URL（終了する場合は 'q' を入力）: ").strip()
            
            if url.lower() == 'q':
                print("プログラムを終了します")
                break
            
            if not url:
                print("URLを入力してください")
                continue
            
            if not self.validate_url(url):
                print("有効なURLを入力してください")
                continue
            
            quality_format = self.select_quality()
            file_format = self.select_format()
            
            self.download_video_with_options(url, quality_format, file_format)
            print()
            
    def validate_url(self, url):
        valid_domains = ['archive.org', 'youtube.com', 'youtu.be']
        return any(domain in url for domain in valid_domains)
    
    def select_quality(self):
        print("\n=== 動画品質を選択してください ===")
        quality_options = {
            '1': {'format': 'best[height<=480]', 'description': '480p (標準画質)'},
            '2': {'format': 'best[height<=720]', 'description': '720p (高画質)'},
            '3': {'format': 'best[height<=1080]', 'description': '1080p (フルHD)'},
            '4': {'format': 'best', 'description': '最高画質（サイズ大）'}
        }
        
        for key, value in quality_options.items():
            print(f"{key}. {value['description']}")
        
        while True:
            choice = input("選択番号を入力してください (1-4): ").strip()
            if choice in quality_options:
                return quality_options[choice]['format']
            print("無効な選択です。1-4の番号を入力してください。")
            
    def select_format(self):
        print("\n=== ファイル形式を選択してください ===")
        format_options = {
            '1': {'ext': 'mp4', 'description': 'MP4形式（汎用性が高い）'},
            '2': {'ext': 'avi', 'description': 'AVI形式（高品質）'},
            '3': {'ext': 'mkv', 'description': 'MKV形式（高機能）'},
            '4': {'ext': 'any', 'description': 'オリジナル形式（変換なし）'}
        }
        
        for key, value in format_options.items():
            print(f"{key}. {value['description']}")
        
        while True:
            choice = input("選択番号を入力してください (1-4): ").strip()
            if choice in format_options:
                return format_options[choice]['ext']
            print("無効な選択です。1-4の番号を入力してください。")
    
    def display_settings(self, quality_format, file_format):
        print("\n=== 現在の設定 ===")
        print(f"動画品質: {quality_format}")
        print(f"ファイル形式: {file_format}")
        print(f"保存先: {self.download_path}/")
        print("追加機能: 動画情報・字幕も同時ダウンロード")
        
        confirm = input("\nこの設定でダウンロードしますか？ (y/n): ").strip().lower()
        return confirm == 'y' or confirm == 'yes'
    
    def format_filesize(self, size_bytes):
        if not size_bytes:
            return "不明"
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def show_downloaded_files(self, title):
        print(f"\n=== ダウンロード完了ファイル ===")
        for filename in os.listdir(self.download_path):
            if title.replace(" ", "_") in filename or title in filename:
                filepath = os.path.join(self.download_path, filename)
                filesize = os.path.getsize(filepath)
                print(f"・{filename} ({self.format_filesize(filesize)})")
    
def main():
    downloader = VideoDownloader()
    downloader.run()


if __name__ == "__main__":
    main()