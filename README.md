## Tweetscraper Mailing Service
Efficiently generates a twitter newsletter from your chosen twitter handle.
Supports tweet filters such as date-posted and can apply a limit of tweets per newsletter.
Email service functionality to designate email addresses to deliver newletter to.

## Technologies
Project is created with:
Python 3.10.6
Python-docx: 0.8.11
Tweet-capture: 0.1.3
Pillow 9.3.0

## Setup
To use this project on Windows, need to download libraries:
```
> pip install python-docx
> pip install tweet-capture
> pip install pillow
```
Next, this project only supports the sender's email to be a Gmail account for the mailing service. A Gmail account will need to be created/used. Need to have 2-step verification active and then an "App Password" generated in the Gmail account settings. In my "settings.py" there is a designated place to put your email and this "App Password" to be used.

## Usage
In my "settings.py", there are three options for tweet filteration currently. The twitter handle of desired account, date to give range of allowed tweet range, and the specified number of tweets per newsletter. Run in terminal:
```
> python scraper.py
```
