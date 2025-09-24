import os
from model import TTSModel

VOICE_SAMPLES_DIR = "voice_samples"
SAMPLE_SPEECH_TEXT = "Listen carefully... the secret to success is persistence. The journey to greatness is long, but every step... every challenge... builds your strength."
README_CONTENT = """# Script2speech
python script to generate audio files from a text file
using `balacoon_tts`

works on CPU, Linux only

### SETUP
```
git clone  https://github.com/saurabhv749/script2speech.git
cd script2speech

conda create -n tts python=3.11
conda init bash
conda activate tts
pip install -r requirements.txt
```

### Generate voice samples
This will also update `README.md` file
```
python gen_voice_samples.py
```
"""

balacoon = TTSModel()

speech_models = balacoon.get_model_names()
voice_samples = []

for model_name in speech_models:
    balacoon.set_model(model_name_str=model_name)
    speakers = balacoon.get_speakers(model_name_str=model_name)
    for speaker in speakers:
        output_filename = model_name.replace("cpu.addon", "_" + speaker)
        voice_sample_name = output_filename
        output_filename += ".wav"
        output_path = os.path.join(VOICE_SAMPLES_DIR, output_filename)
        # add sample
        voice_samples.append((voice_sample_name, output_path))

        balacoon.synthesize_audio(
            model_name_str=model_name,
            speaker_str=speaker,
            text_str=SAMPLE_SPEECH_TEXT,
            output_path=output_path,
        )

# update README
with open("README.md", "w") as f:
    f.write(README_CONTENT)
    f.write("\n\n")
    f.write("## Voice Samples\n")
    # add samples in a table
    f.write("| Model_Speaker | Audio Sample |\n")
    for voice_sample_name, output_path in voice_samples:
        f.write(
            f"| {voice_sample_name} | <audio controls><source src='{output_path}' type='audio/wav'></audio> |\n"
        )
