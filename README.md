# Test M3U8 Playlists
This repository contains a series of tricky playlists known to cause issues in some software.

## Test Playlists
| URL                 | Description    |
|---------------------|----------------|
| [a.m3u8][3]         | A playlist with a reference to another playlist as the last item. |
| [recursive.m3u8][2] | A playlist with a reference to itself as the last item. |
| [absolute.m3u8][4]  | A playlist with absolute paths for the items. |
| [hls.m3u8][1]       | A playlist containing two MP3 files which is [valid according to the spec][5]. |

## Test Configuration
All tests can be performed using a local static server, for example by running
`python http.server 5000`. The only exception is the HLS playlist which requires a specific MIME
type `application/vnd.apple.mpegurl` which can be configured by running `python server.py` or,
alternatively, using the Github Pages server directly at this URL:
https://owahltinez.github.io/m3u8test/playlist/hls.m3u8.

[1]: https://owahltinez.github.io/m3u8test/playlist/hls.m3u8
[2]: https://raw.githubusercontent.com/owahltinez/m3u8test/main/playlist/recursive.m3u8
[3]: https://raw.githubusercontent.com/owahltinez/m3u8test/main/playlist/a.m3u8
[4]: https://raw.githubusercontent.com/owahltinez/m3u8test/main/playlist/absolute.m3u8
[5]: ./validation_data.json