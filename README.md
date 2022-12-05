## Voice Assistant
**Text-to-Speech** from `.xlsx` files and generate `.mp3` or `.wav` audio files using `python`. This program uses api from [Google Translate](https://translate.google.com/) for tts. You can also choose `gTTs` python library.

### Directory Structure
    .
    ├── ...
    ├── preprocess
    │   ├── mp3-to-wav
    │   │   ├── files               # default location
    │   │   │   ├── mp3
    │   │   │   └── wav
    │   │   └── main.py             # mp3 to wav conversion
    │   └── text-to-speech
    │   │   ├── files               # default location
    │   │   │   ├── mp3
    │   │   │   └── xlsx
    │   │   └── main.py             # read xlsx columns & convert text to mp3
    └── ...

### Procedures
1. ```git clone```
2. Provide the directory path of `.xlsx`, `.mp3` and `.wav` files through input. You can hit `Enter` to use default path (default: `{project-path}/files/{xlsx & mp3 & wav}`).
3. Run the program and get your output in folder (mp3 or wav).

### Requirements
1. If you're using **linux/osx**, make sure `ffmpeg` installed in system.
2. `openpyxl`
3. `pydub`
4. `gTTs`
