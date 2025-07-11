import pyaudio as pa
import wave as wv
from datetime import datetime

class AudioRecorder:      
    def __init__(self,chunk: int = 1024, rate: int = 16000, format: int = pa.paInt16, channel: int = 1):
        self.CHUNK = chunk
        self.RATE = rate
        self.FORMAT = format
        self.CHANNELS = channel
        self.FRAMES = []

    def record_audio(self, RECORD_SECONDS: int):    
        self.FRAMES = []
        audio = pa.PyAudio()
        
        stream = audio.open(
            channels=self.CHANNELS,
            input=True,
            rate=self.RATE,
            format=self.FORMAT,
            frames_per_buffer=self.CHUNK
            )

        print("Recording...")
 
        for _ in range(0,int(self.RATE/self.CHUNK * RECORD_SECONDS+1)):
            data = stream.read(self.CHUNK)
            self.FRAMES.append(data)
            
        print("Recorded")

        stream.stop_stream()
        stream.close()
        audio.terminate()

    def save_audio(self, OUTPUT_FILENAME: str = None) -> str:
        if OUTPUT_FILENAME:
            filename = f"{OUTPUT_FILENAME}.wav"
        else:
            timestamp = datetime.now().strftime("D_%d-%m-%Y_T_%H-%M-%S")
            filename = f"{timestamp}.wav"
        
        path = f"audio/recordings/{filename}"
                 
        wav = wv.open(path,"wb")
        wav.setnchannels(self.CHANNELS)
        audio = pa.PyAudio()
        sampwidth = audio.get_sample_size(self.FORMAT)
        audio.terminate()
        wav.setsampwidth(sampwidth)
        wav.setframerate(self.RATE)
        wav.writeframes(b''.join(self.FRAMES))
        wav.close()

        print(f"Saved to {filename}")
        
        return filename