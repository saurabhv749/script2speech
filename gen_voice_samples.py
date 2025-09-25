import os
from model import TTSModel
from utils import model_html, speaker_html

VOICE_SAMPLES_DIR = "voice_samples"
SAMPLE_SPEECH_TEXT = "Listen carefully.. the secret to success is persistence. The journey to greatness is long, but every step.. every challenge.. builds your strength."
DOCS_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voice Samples</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        audio { width: 100%; margin: 10px 0; }
        h2 { color: #333; }
    </style>
</head>
<body>
    <h1>Generated Voice Samples</h1>
"""
DOCS_CONTENT += f"<p><em>{SAMPLE_SPEECH_TEXT}</em></p>"

if not os.path.exists(VOICE_SAMPLES_DIR):
    os.makedirs(VOICE_SAMPLES_DIR)

balacoon = TTSModel()

speech_models = balacoon.get_model_names()

for model_name in speech_models:
    balacoon.set_model(model_name_str=model_name)
    speakers = balacoon.get_speakers(model_name_str=model_name)

    DOCS_CONTENT += model_html(model_name)
    for speaker in speakers:
        output_filename = model_name.replace("cpu.addon", "_" + speaker)
        output_filename += ".wav"
        output_path = os.path.join(VOICE_SAMPLES_DIR, output_filename)

        # rel path to audio file from docs/index.html
        sample_audio_path = "../" + output_path
        DOCS_CONTENT += speaker_html(speaker=speaker, file_path=sample_audio_path)

        balacoon.synthesize_audio(
            model_name_str=model_name,
            speaker_str=speaker,
            text_str=SAMPLE_SPEECH_TEXT,
            output_path=output_path,
        )

# update index.html
with open("docs/index.html", "w") as f:
    f.write(DOCS_CONTENT)
    f.write("</body></html>")
