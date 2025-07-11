import whisper
class Transcriber:  
    def __init__(self, MODEL: str = "turbo", AUDIO_FILE: str = None):
        self.model = whisper.load_model(MODEL)
        self.audio_file = AUDIO_FILE
        
    def transcribe(self) -> dict:
        path = f"audio/recordings/{self.audio_file}"
        result = self.model.transcribe(path)
        print("Transcription Complete")
        return result
    
    def get_transcript_name(self) -> str:
        return self.audio_file.rsplit(".",1)[0]
    def save_transcript(self,result: dict):
        path = f"audio/transcripts/{self.get_transcript_name()}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        