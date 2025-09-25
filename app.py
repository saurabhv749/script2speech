import os
import re
from model import TTSModel

SPEECH_OUTPUT_DIR = "audios"

if not os.path.exists(SPEECH_OUTPUT_DIR):
    os.makedirs(SPEECH_OUTPUT_DIR)

balacoon = TTSModel()


def generate_audio(dialogue: str, tts_model: str, speaker: str, output_file: str):
    balacoon.set_model(model_name_str=tts_model)
    balacoon.synthesize_audio(
        model_name_str=tts_model,
        speaker_str=speaker,
        text_str=dialogue,
        output_path=output_file,
    )


if __name__ == "__main__":
    # replaced sys.argv parsing with argparse
    import argparse

    parser = argparse.ArgumentParser(description="Script to Speech TTS application")
    parser.add_argument("--file", help="Path to the script file (.txt) with dialogues")
    parser.add_argument("--model_name", help="TTS model name")
    parser.add_argument("--speaker", help="Speaker to use")
    args = parser.parse_args()

    os.makedirs(SPEECH_OUTPUT_DIR, exist_ok=True)

    with open(args.file, "r", encoding="utf-8") as f:
        dialogues = f.readlines()

    for i, dialogue in enumerate(dialogues, start=1):
        dialogue = dialogue.strip()
        if not dialogue:
            continue
        safe_text = re.sub(r"[^A-Za-z0-9_]", "_", dialogue[:20])
        output_file = os.path.join(SPEECH_OUTPUT_DIR, f"{i:03d}_{safe_text}.wav")
        generate_audio(dialogue, args.model_name, args.speaker, output_file)
        print(f"Generated audio: {output_file}")
