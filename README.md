# Youtube To RSS CLI

Python program to convert a single or multiple youtube channel(s) URL to their respective RSS links.

# Installation

`git clone https://github.com/benarmstead/youtube-to-rss-cli/`

`cd youtube-to-rss-cli/src`

`python3 main.py`

# Commands

If no flag is passed then you will be taken to the CLI menu.

`-h` : Help screen.

`-u` : Enter URL(s) to convert, can take as many URL's as you wish.

`-f` : Enter filename which the URL's are stored in.
       These must be in the specific format shown below.

# Examples

`-u` example: 

`python3 main.py -u https://www.youtube.com/c/level1techs https://www.youtube.com/c/level1techs`

Returns: 

```
https://www.youtube.com/feeds/videos.xml?channel_id=UC4w1YQAJMWOz4qtxinq55LQ
https://www.youtube.com/feeds/videos.xml?channel_id=UC4w1YQAJMWOz4qtxinq55LQ
```

`-f` example: 

`python3 main.py -f urls.txt`

Contents of urls.txt:

```
https://www.youtube.com/c/level1techs
https://www.youtube.com/c/level1techs
```


Returns:

```
https://www.youtube.com/feeds/videos.xml?channel_id=UC4w1YQAJMWOz4qtxinq55LQ
https://www.youtube.com/feeds/videos.xml?channel_id=UC4w1YQAJMWOz4qtxinq55LQ
```
