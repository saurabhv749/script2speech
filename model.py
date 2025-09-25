import os
import logging
from balacoon_tts import TTS
from huggingface_hub import snapshot_download

from utils import audio_samples_to_file

LOCAL_DIR = "tts_models"
MYTTS = None


class TTSModel:
    def __init__(self):
        self.repo_id = "balacoon/tts"
        self.models = []
        self.cur_model = ""
        self.model_to_speakers = dict()
        self.max_length = 1024

        self.download_models()

    def download_models(self):
        snapshot_download(
            repo_id=self.repo_id,
            allow_patterns=["*_cpu.addon"],
            local_dir=LOCAL_DIR,
        )
        # filter models that are downloaded
        self.models = [f for f in os.listdir(LOCAL_DIR) if "cpu.addon" in f]

    def get_model_names(self):
        return self.models

    def set_model(self, model_name_str: str):
        """
        gets value from `model_name`. either
        uses cached list of speakers for the given model name
        or loads the addon and checks what are the speakers.
        """
        model_path = os.path.join(LOCAL_DIR, model_name_str)
        if self.cur_model != model_name_str:
            global MYTTS
            MYTTS = TTS(model_path)
            speakers = MYTTS.get_speakers()
            self.model_to_speakers[model_name_str] = speakers
            self.cur_model = model_name_str

    def get_speakers(self, model_name_str: str):
        if model_name_str not in self.model_to_speakers:
            self.set_model(model_name_str)

        speakers = self.model_to_speakers[model_name_str]
        return speakers

    def get_all_speakers(self):
        return self.model_to_speakers

    def synthesize_audio(
        self, text_str: str, model_name_str: str, speaker_str: str, output_path: str
    ):
        """
        gets utterance to synthesize from `text` Textbox
        and speaker name from `speaker` dropdown list.
        speaker name might be empty for single-speaker models.
        Synthesizes the waveform and updates `audio` with it.
        """
        if not text_str or not model_name_str or not speaker_str or not output_path:
            logging.info("text, model name, speaker or output_path are not provided")
            return None

        if len(text_str) > self.max_length:
            logging.info(f"{text_str[:50]} has length over 1024 trimming.....")
            # truncate the text
            text_str = text_str[: self.max_length]
        samples = MYTTS.synthesize(text_str, speaker_str)
        sampling_rate = MYTTS.get_sampling_rate()
        audio_samples_to_file(
            sample_rate=sampling_rate, samples=samples, filename=output_path
        )
