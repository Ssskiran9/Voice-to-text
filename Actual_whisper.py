
import torch
from transformers import pipeline

whisper = pipeline("automatic-speech-recognition", "openai/whisper-large-v3", torch_dtype=torch.float16, device="cuda:0")

transcription = whisper("C:\\Users\\saiki\\Downloads\\Voice 014.mp3")  # replace the mp3 file

print(transcription["text"])

#read roadmap of whisper 