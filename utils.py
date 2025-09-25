import wave


# Audio utils
def audio_samples_to_file(sample_rate, samples, filename):
    with wave.open(filename, "w") as fp:
        fp.setparams((1, 2, sample_rate, len(samples), "NONE", "NONE"))
        fp.writeframes(samples)


# HTML Template utils
def voice_sample_html(file_path: str):
    return f"""
    <audio controls>
        <source src="{file_path}" type="audio/wav">
        Your browser does not support the audio element.
    </audio>"""


def model_html(model_name: str):
    return f"""<h2>{model_name}</h2>"""


def speaker_html(speaker: str, file_path: str):
    return f"""<p>{speaker}</p>""" + voice_sample_html(file_path)
