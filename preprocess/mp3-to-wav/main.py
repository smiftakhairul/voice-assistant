import os, sys, pydub

mp3Path = str(input("Enter MP3 directory path or press Enter for default: ") or "files/mp3/")
wavPath = str(input("Enter WAV directory path or press Enter for default: ") or "files/wav/")

if not os.path.exists(mp3Path) or not os.path.exists(wavPath):
    print('Directory not found or incorrect!')
    sys.exit()

index = 0
for file in os.listdir(mp3Path):
    if file.endswith(".mp3"):
        index += 1
        print(f'(#{index}) Converting {file} ...')
        sound = pydub.AudioSegment.from_mp3(mp3Path + file)
        sound.export(wavPath + file.replace('.mp3', '.wav'), format = "wav")
        print("Success!")
        # os.remove(wavPath + file.replace('.mp3', '.wav'))