from app.record import AudioRecorder
        
if __name__ == "__main__":
    recorder = AudioRecorder()

    duration = int(input("Enter recording duration in seconds: "))
    recorder.record_audio(duration)

    name = input("Enter file name (or press Enter to auto-generate): ").strip()
    if name == "":
        recorder.save_audio()
    else:
        recorder.save_audio(name)
        
        