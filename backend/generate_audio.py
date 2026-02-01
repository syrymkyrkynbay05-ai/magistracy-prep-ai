"""
Qwen3-TTS арқылы КТ тесті үшін ағылшын тілі аудио диалогтарын генерациялау скрипті.

Қолдану:
1. pip install qwen-tts soundfile
2. python generate_audio.py
"""

import os
import soundfile as sf
from qwen_tts import Qwen3TTSModel
import torch

# Output directory
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize model
print("🔄 Loading Qwen3-TTS model...")
model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
    device_map="cuda:0" if torch.cuda.is_available() else "cpu",
    dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
)
print("✅ Model loaded!")

# ============================================
# DIALOGUE 1: Travel to Sydney
# ============================================
dialogue_1 = [
    {
        "speaker": "Ryan",  # Male
        "text": "Hi Sarah! I'm planning to visit Sydney next month. Since you're from there, could you give me some recommendations?",
    },
    {
        "speaker": "Vivian",  # Female
        "text": "Oh, that's wonderful! Sydney is beautiful. First, you absolutely must visit the Sydney Opera House. It's iconic!",
    },
    {
        "speaker": "Ryan",
        "text": "Yes, I've seen pictures. It looks amazing. What about beaches? I heard Bondi Beach is popular.",
    },
    {
        "speaker": "Vivian",
        "text": "Bondi is great, but it can be very crowded. If you want something quieter, try Manly Beach. You can take a ferry from Circular Quay.",
    },
    {
        "speaker": "Ryan",
        "text": "A ferry ride sounds fun! How long does it take?",
    },
    {
        "speaker": "Vivian",
        "text": "About thirty minutes, and the views of the harbour are spectacular. You'll pass right by the Opera House and the Harbour Bridge.",
    },
    {
        "speaker": "Ryan",
        "text": "Perfect! What about food? Any local dishes I should try?",
    },
    {
        "speaker": "Vivian",
        "text": "Definitely try a meat pie. It's a classic Australian snack. And for seafood, go to the Sydney Fish Market. It's the third largest in the world!",
    },
    {
        "speaker": "Ryan",
        "text": "That sounds delicious! One more question - what's the weather like in December?",
    },
    {
        "speaker": "Vivian",
        "text": "December is summer in Australia, so expect warm weather, around twenty-five to thirty degrees Celsius. Don't forget sunscreen!",
    },
]

# ============================================
# DIALOGUE 2: Birthday Party Planning
# ============================================
dialogue_2 = [
    {
        "speaker": "Vivian",  # Female - Birthday person
        "text": "Hey Tom! My birthday is coming up this Saturday. I want to celebrate with our friends. Any ideas for a venue?",
    },
    {
        "speaker": "Ryan",  # Male - Friend
        "text": "Happy early birthday! How about that new pizza place downtown? I heard it's really good.",
    },
    {
        "speaker": "Vivian",
        "text": "Hmm, I'm not really in the mood for pizza. What about something different?",
    },
    {
        "speaker": "Ryan",
        "text": "Well, there's also a nice burger restaurant on Main Street. They have a private room for parties.",
    },
    {
        "speaker": "Vivian",
        "text": "Oh, I love burgers! That sounds much better. Do they take reservations?",
    },
    {
        "speaker": "Ryan",
        "text": "Yes, I can call them today. How many people are you inviting?",
    },
    {
        "speaker": "Vivian",
        "text": "About fifteen, including us. Do you think they can accommodate that many?",
    },
    {
        "speaker": "Ryan",
        "text": "Their private room fits up to twenty people, so we should be fine. What time do you want to start?",
    },
    {
        "speaker": "Vivian",
        "text": "How about seven in the evening? That gives everyone time to finish work.",
    },
    {
        "speaker": "Ryan",
        "text": "Perfect! I'll make the reservation for seven o'clock on Saturday. Should I also order a birthday cake?",
    },
    {
        "speaker": "Vivian",
        "text": "Yes, please! Chocolate cake would be amazing. Thank you so much for helping me plan this!",
    },
    {
        "speaker": "Ryan",
        "text": "No problem! It's going to be a great party. I'll send everyone the details.",
    },
]


def generate_dialogue_audio(dialogue: list, output_name: str):
    """Generate audio for a complete dialogue and save as single file."""
    print(f"\n🎙️ Generating: {output_name}")

    all_audio = []
    sr = None

    for i, line in enumerate(dialogue):
        print(f"  [{i+1}/{len(dialogue)}] {line['speaker']}: {line['text'][:50]}...")

        wavs, sample_rate = model.generate_custom_voice(
            text=line["text"],
            language="English",
            speaker=line["speaker"],
            instruct="Natural conversational tone, clear pronunciation.",
        )

        all_audio.append(wavs[0])
        sr = sample_rate

        # Add small pause between speakers (0.3 seconds of silence)
        pause = [0.0] * int(sr * 0.3)
        all_audio.append(pause)

    # Concatenate all audio
    import numpy as np

    final_audio = np.concatenate(all_audio)

    # Save
    output_path = os.path.join(OUTPUT_DIR, f"{output_name}.mp3")
    sf.write(output_path, final_audio, sr)
    print(f"  ✅ Saved: {output_path}")

    return output_path


def generate_individual_lines(dialogue: list, output_prefix: str):
    """Generate audio for each line separately (for testing)."""
    print(f"\n🎙️ Generating individual lines: {output_prefix}")

    for i, line in enumerate(dialogue):
        print(f"  [{i+1}/{len(dialogue)}] {line['speaker']}: {line['text'][:40]}...")

        wavs, sr = model.generate_custom_voice(
            text=line["text"],
            language="English",
            speaker=line["speaker"],
            instruct="Natural conversational tone, clear pronunciation.",
        )

        output_path = os.path.join(OUTPUT_DIR, f"{output_prefix}_line_{i+1:02d}.wav")
        sf.write(output_path, wavs[0], sr)

    print(f"  ✅ All lines saved!")


if __name__ == "__main__":
    print("=" * 60)
    print("КТ Ағылшын Тілі - Аудио Диалог Генераторы")
    print("=" * 60)

    # Generate Dialogue 1: Sydney Travel
    generate_dialogue_audio(dialogue_1, "audio_dialogue_1_sydney")

    # Generate Dialogue 2: Birthday Party
    generate_dialogue_audio(dialogue_2, "audio_dialogue_2_birthday")

    print("\n" + "=" * 60)
    print("✅ Барлық аудио файлдар дайын!")
    print(f"📁 Орны: {OUTPUT_DIR}")
    print("=" * 60)
