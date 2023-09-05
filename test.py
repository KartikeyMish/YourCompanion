import struct
import wave
from pvrecorder import PvRecorder

recorder = PvRecorder(device_index=-1, frame_length=512)
audio = []


try:
    recorder.start()
    while True:
        frame = recorder.read()
        audio.extend(frame)
except KeyboardInterrupt:
    recorder.stop()
    with wave.open("/", 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))
finally:
    recorder.delete()
