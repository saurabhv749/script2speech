# Script2speech
python script to generate audio files from a text file
using `balacoon_tts`

> works on CPU, Linux only

> Don't use multiple dots (... or ....+)

### SETUP
```
git clone  https://github.com/saurabhv749/script2speech.git
cd script2speech

conda create -n tts python=3.10
conda init bash
conda activate tts
pip install -r requirements.txt
```

### Run the script

```
python app.py --file _script.txt_ --model_name "en_us_hifi92_light_cpu.addon" --speaker "92"
```
this will output dialogues to _audios/_ folder

### Generate voice samples
This will also update `index.html` file
```
python gen_voice_samples.py
```

### Voice Samples

For direct previews, visit the [script2speech voice samples](https://saurabhv749.github.io/script2speech/).