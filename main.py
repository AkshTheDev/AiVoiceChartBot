from app.record import AudioRecorder
from app.transcribe import Transcriber
        
if __name__ == "__main__":
    recorder = AudioRecorder()

    duration = int(input("Enter recording duration in seconds: "))
    recorder.record_audio(duration)

    name = input("Enter file name (or press Enter to auto-generate): ").strip()
    if name == "":
        filename = recorder.save_audio()
    else:
        filename = recorder.save_audio(name)
    
    transcriber = Transcriber(AUDIO_FILE=filename)
    result = transcriber.transcribe()
    transcriber.save_transcript(result)    
        