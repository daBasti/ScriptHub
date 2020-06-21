# Cheatsheet for the youtube-dl Crunchyroll Extractor Module


To download Crunchyroll Premium content a valid browser session_id is needed  
To obtain it:  
  *  for Chrome: Log into Crunchyroll, open the Browser Console, go to "Application" -> "Cookies" -> "crunchyroll.com"  
     -> look for the "session_id" property and copy the value into the provided cookies.txt file

<br>

List the available video formats for a specific anime
```
youtube-dl "https://www.crunchyroll.com/a-certain-scientific-railgun/episode-1-super-powered-level-5-792607" \
  --no-check-certificate --list-formats
 ```
   *  Hint: "hardsub" in the "format code" means the subtitles are hard coded into the final file.  
  format codes without a "hardsub" don't contain any subtitles by default

choose a suitable format code
```
e.g. "adaptive_hls-audio-jaJP-hardsub-enUS-8104-2"
```


### Option 1
with hard coded subtitles
```
youtube-dl "https://www.crunchyroll.com/a-certain-scientific-railgun/episode-1-super-powered-level-5-792607" \
  --no-check-certificate -f adaptive_hls-audio-jaJP-hardsub-enUS-8104-2 --cookies cookies.txt
```

<br>

### Option 2
without hard coded subtitles

hint: use VLC or something else (manually enabling the subtitles is necessary)
Windows "Movies & TV" and "Windows Media Player" don't play nicely with these subtitles

first find which subtitle languages and formats are available
```
youtube-dl "https://www.crunchyroll.com/a-certain-scientific-railgun/episode-1-super-powered-level-5-792607" \
  --no-check-certificate --list-subs
```

download it with the desired subtitles
```
youtube-dl "https://www.crunchyroll.com/a-certain-scientific-railgun/episode-1-super-powered-level-5-792607" \
  --no-check-certificate -f adaptive_hls-audio-jaJP-8105-2 --sub-lang enUS --write-sub --sub-format ass --embed-subs \
  --cookies cookies.txt
```


  
