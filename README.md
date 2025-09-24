# Script2speech
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


## Voice Samples
| Model | Speaker | Audio Sample |
| en_us_cmuartic_jets_cpu.addon | aew | <audio controls><source src='./voice_samples/en_us_cmuartic_jets__aew.wav' type='audio/wav'></audio> |
