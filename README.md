# Twitter Media Tweets Retweeter
This project provides a method to extract media tweets from a Twitter archive and retweet them from another account using Python and Selenium.
* [README.md for Japanese](https://github.com/Lante323/X_Account_Media_Translation/blob/develop/README-ja.md)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequisites

- Python 3.x
- Selenium
- pandas
- Export old X(Twitter) Accouct CSV file
- A Twitter account with MFA
- ChromeDriver

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:Lante323/X_Account_Media_Translation.git
   cd X_Account_Media_Translation
   ```

1. **Install the required Python packages:**

   ```
   pip install -r requirements.txt
   ```

1. **Download ChromeDriver:**

   Download the ChromeDriver that matches your Chrome version from [here](https://developer.chrome.com/docs/chromedriver/downloads?hl=en) and place it in your project directory.

## Usage

**Step 1: Extract Media Tweets**

   1. Place your tweets.js file from the Twitter archive in the data folder.
   1. Run the ***'extract_media_tweets.py'*** script to extract media tweets:
      ```
      python extract_media_tweets.py
      ```
      This will create a ***'media_tweets.csv'*** file containing the extracted media tweets.

**Step 2: Retweet Media Tweets**

   1. Open the ***'retweet_media_tweets.py'*** script and update the following variables with your Twitter credentials and ChromeDriver path:
      ```
      chrome_driver_path = 'path_to_your_chromedriver'
      twitter_username = 'your_username'
      twitter_password = 'your_password'
      ```

   1. Run the ***'retweet_media_tweets.py'*** script to retweet the media tweets:
      ```
      python retweet_media_tweets.py
      ```

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more details.
