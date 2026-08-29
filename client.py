class BatchedSpeechRecognitionPhonemeAlignerClient:
    def transcribe_with_alignment(self, audio_file_url='https://assets.genpark.ai/audio/earnings_call_q2.wav', compute_vad=True):
        return {
            'transcription_job_id': 'whx_asr_9918',
            'audio_duration_seconds': 342.5,
            'ctranslate2_speedup_factor': 8.4,
            'word_timestamps_aligned_count': 940,
            'phoneme_boundary_accuracy_ms': 12,
            'diarized_speakers_count': 3,
            'transcript_json_url': 'https://transcripts.genpark.ai/asr/9918.json'
        }
