from client import BatchedSpeechRecognitionPhonemeAlignerClient

def main():
    client = BatchedSpeechRecognitionPhonemeAlignerClient()
    res = client.transcribe_with_alignment('https://assets.genpark.ai/audio/medical_consultation.wav')
    print('ASR Job: ' + res['transcription_job_id'] + ' (' + str(res['audio_duration_seconds']) + 's audio)')
    print('CTranslate2 Speedup: ' + str(res['ctranslate2_speedup_factor']) + 'x | Words Aligned: ' + str(res['word_timestamps_aligned_count']))
    print('Phoneme Precision: ±' + str(res['phoneme_boundary_accuracy_ms']) + 'ms | Speakers: ' + str(res['diarized_speakers_count']))
    print('Transcript URL: ' + res['transcript_json_url'])

if __name__ == '__main__':
    main()
