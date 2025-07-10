import pyaudio as pa
import wave as wv

class AudioRecorder:      
    def __init__(self,chunk = 1024, rate = 44100, format = pa.paInt16, channel = 1):
        self.CHUNK = chunk
        self.RATE = rate
        self.FORMAT = format
        self.CHANNELS = channel
        self.FRAMES = []

    def record_audio(self, RECORD_SECONDS):    
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

    def save_audio(self, OUTPUT_FILENAME = None):
        from datetime import datetime
        if OUTPUT_FILENAME:
            filename = f"{OUTPUT_FILENAME}.wav"
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
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