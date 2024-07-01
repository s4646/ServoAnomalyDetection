import os
from tqdm import tqdm
from pydub import AudioSegment

def main():
    directory = "data"
    counter = 0
    for label in range(2):
        for idx, audio_file in enumerate(os.listdir(f"{directory}/{label}/original")):
            print(f"label: {label}, file: {idx+1}")
            file = AudioSegment.from_file(f"{directory}/{label}/original/{audio_file}")
            length = len(file)//1000
            for second in tqdm(range(length)):
                chunk = file[second*1000:(second+1)*1000]
                chunk.export(f"{directory}/{label}/sample_{counter}.wav", format="wav")
                counter +=1

if __name__ == '__main__':
    main()