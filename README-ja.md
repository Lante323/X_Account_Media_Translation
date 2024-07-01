# Twitter Media Tweets Retweeter

このプロジェクトは、Twitterアーカイブからメディアツイートを抽出し、PythonとSeleniumを使用して別のアカウントから再度ツイートする方法を提供します。

## 目次

- [前提条件](#前提条件)
- [インストール](#インストール)
- [使用方法](#使用方法)
- [ライセンス](#ライセンス)

## 前提条件

- Python 3.x
- Selenium
- pandas
- Twitterアカウント
- 旧Twitterアカウントからエクスポートしたアーカイブファイル
- ChromeDriver

## インストール

1. **リポジトリをクローンする:**

   ```bash
   git clone https://github.com/yourusername/twitter-media-tweets-retweeter.git
   cd twitter-media-tweets-retweeter
   ```

1. **必要な Python パッケージをインストールする:**

   ```
   pip install -r requirements.txt
   ```

1. **ChromeDriver をダウンロードする:**

   [こちら](https://developer.chrome.com/docs/chromedriver/downloads?hl=ja)から Chrome のバージョンに合った ChromeDriver をダウンロードし、プロジェクトディレクトリに配置します。

## 使用方法

**Step 1: ステップ1: メディアツイートを抽出**
   1. Twitterアーカイブから取得したtweets.jsファイルをdataフォルダに配置します。
   1. ***'extract_media_tweets.py'*** スクリプトを実行してメディアツイートを抽出します:
      ```
      python extract_media_tweets.py
      ```
      これにより、抽出されたメディアツイートを含む ***'media_tweets.csv'*** ファイルが作成されます。

**Step 2: メディアツイートを再ツイート**

   1. ***'retweet_media_tweets.py'*** スクリプトを開き、以下の変数をTwitterの認証情報と ChromeDriver のパスに更新します:
      ```
      chrome_driver_path = 'path_to_your_chromedriver'
      twitter_username = 'your_username'
      twitter_password = 'your_password'
      ```

   1. ***'retweet_media_tweets.py'*** スクリプトを実行してメディアツイートを再ツイートします:
      ```
      python retweet_media_tweets.py
      ```

   1. 指示に従ってMFAコードを入力します。


## License

このプロジェクトは MITライセンス の下でライセンスされています。
詳細は [LICENSE](https://opensource.org/license/mit) ファイルを参照してください。
