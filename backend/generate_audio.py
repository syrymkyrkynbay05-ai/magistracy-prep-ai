"""
Qwen3-TTS audio dialogue generator for KT English test.

Usage:
    python generate_audio.py 1      # Dialogue 1 (Sydney Travel)
    python generate_audio.py 10     # Dialogue 10 (Restaurant)
    python generate_audio.py all    # All 10 dialogues
"""

import os
import sys
import numpy as np
import soundfile as sf
import torch

# ============================================
# SETUP SOX PATH
# ============================================
sox_path = r"C:\Program Files (x86)\sox-14-4-2"
if os.path.exists(sox_path):
    print(f"[SETUP] Adding SoX to PATH: {sox_path}")
    os.environ["PATH"] += os.pathsep + sox_path

# Output directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================
# ALL DIALOGUES (1-10)
# ============================================

DIALOGUES = {
    1: [  # Sydney Travel
        {
            "speaker": "Ryan",
            "text": "Hi Sarah! I'm planning to visit Sydney next month. Since you're from there, could you give me some recommendations?",
        },
        {
            "speaker": "Vivian",
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
        {"speaker": "Ryan", "text": "A ferry ride sounds fun! How long does it take?"},
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
    ],
    2: [  # Birthday Party
        {
            "speaker": "Vivian",
            "text": "Hey Tom! My birthday is coming up this Saturday. I want to celebrate with our friends. Any ideas for a venue?",
        },
        {
            "speaker": "Ryan",
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
    ],
    3: [  # University Library
        {
            "speaker": "Ryan",
            "text": "Excuse me, I'm looking for a book on Microeconomics. The catalog says it should be here.",
        },
        {
            "speaker": "Vivian",
            "text": "Let me check for you. Yes, it's in the Economics section, row 4B. But it looks like the last copy was checked out this morning.",
        },
        {
            "speaker": "Ryan",
            "text": "Oh no, really? I have an exam on Monday and I really need it. Is there any other way to access it?",
        },
        {
            "speaker": "Vivian",
            "text": "Well, we do have an electronic version available. You can access it through the university portal with your student ID.",
        },
        {
            "speaker": "Ryan",
            "text": "That would be perfect! Do I need a special password?",
        },
        {
            "speaker": "Vivian",
            "text": "Just your regular student login. Also, the library is open 24 hours during exam week if you want to study here.",
        },
        {
            "speaker": "Ryan",
            "text": "That's good to know. Are the study rooms available to book?",
        },
        {
            "speaker": "Vivian",
            "text": "Yes, but they fill up fast. You should book at least two days in advance online.",
        },
    ],
    4: [  # Shopping Return
        {
            "speaker": "Vivian",
            "text": "Good morning. I'd like to return this sweater I bought yesterday.",
        },
        {
            "speaker": "Ryan",
            "text": "Good morning, ma'am. Is there anything wrong with the item?",
        },
        {
            "speaker": "Vivian",
            "text": "It's a bit too small. I tried it on at home and the sleeves are too short.",
        },
        {"speaker": "Ryan", "text": "I understand. Do you have the receipt with you?"},
        {"speaker": "Vivian", "text": "Yes, here it is. I haven't removed the tags."},
        {
            "speaker": "Ryan",
            "text": "Perfect. Would you like to exchange it for a larger size, or would you prefer a refund?",
        },
        {
            "speaker": "Vivian",
            "text": "Do you have it in a medium size? This one is a small.",
        },
        {
            "speaker": "Ryan",
            "text": "Let me check our inventory... Yes, we have one medium left in blue. Would you like to try it on first?",
        },
        {"speaker": "Vivian", "text": "Yes, please. Where are the fitting rooms?"},
        {"speaker": "Ryan", "text": "Just to your right, behind the jeans section."},
    ],
    5: [  # Job Interview
        {
            "speaker": "Ryan",
            "text": "Welcome, Ms. Johnson. Please take a seat. I've reviewed your resume and it looks very impressive.",
        },
        {
            "speaker": "Vivian",
            "text": "Thank you, Mr. Smith. I was very excited to see this opening at your company.",
        },
        {
            "speaker": "Ryan",
            "text": "Tell me, what was your main responsibility in your last role?",
        },
        {
            "speaker": "Vivian",
            "text": "I managed a team of five software developers. We were responsible for maintaining the company's main e-commerce platform.",
        },
        {
            "speaker": "Ryan",
            "text": "That's exactly the kind of experience we're looking for. How do you handle tight deadlines?",
        },
        {
            "speaker": "Vivian",
            "text": "I prioritize tasks and communicate clearly with my team. If necessary, I'm willing to put in extra hours to ensure the project succeeds.",
        },
        {"speaker": "Ryan", "text": "Good to hear. Do you have any questions for us?"},
        {
            "speaker": "Vivian",
            "text": "Yes, I was wondering what the typical career path looks like for this position?",
        },
    ],
    6: [  # Doctor Appointment
        {
            "speaker": "Vivian",
            "text": "Good morning, Doctor. I haven't been feeling well lately.",
        },
        {"speaker": "Ryan", "text": "I see. Can you describe your symptoms?"},
        {
            "speaker": "Vivian",
            "text": "I have a persistent headache and I feel very tired all the time. It's been about three days.",
        },
        {"speaker": "Ryan", "text": "Do you have a fever or a cough?"},
        {"speaker": "Vivian", "text": "No fever, but a slight dry cough at night."},
        {
            "speaker": "Ryan",
            "text": "Okay. Let me check your blood pressure... It's a bit high. Have you been under a lot of stress recently?",
        },
        {
            "speaker": "Vivian",
            "text": "Yes, actually. work has been very demanding this month.",
        },
        {
            "speaker": "Ryan",
            "text": "Stress can definitely cause these symptoms. I'm going to prescribe you some rest and plenty of fluids. Stay home for two days.",
        },
        {
            "speaker": "Vivian",
            "text": "Thank you, Doctor. Should I take any medication?",
        },
        {
            "speaker": "Ryan",
            "text": "Just something for the headache if it gets too bad. Come back in a week if you don't feel better.",
        },
    ],
    7: [  # Asking Directions
        {
            "speaker": "Ryan",
            "text": "Excuse me, could you help me? I'm trying to find the City Art Museum.",
        },
        {
            "speaker": "Vivian",
            "text": "Sure! You're actually quite close. Go straight down this street for two blocks.",
        },
        {"speaker": "Ryan", "text": "Okay, straight for two blocks. Then what?"},
        {
            "speaker": "Vivian",
            "text": "When you see the large post office on the corner, turn left. The museum will be on your right side, opposite the park.",
        },
        {
            "speaker": "Ryan",
            "text": "Is it within walking distance, or should I take a bus?",
        },
        {
            "speaker": "Vivian",
            "text": "It's only about a ten-minute walk. But if you prefer, numbers 45 and 52 stop right in front of it.",
        },
        {
            "speaker": "Ryan",
            "text": "I think I'll walk, the weather is nice today. Thanks for your help!",
        },
        {"speaker": "Vivian", "text": "You're welcome! Enjoy the exhibition."},
    ],
    8: [  # Renting Apartment
        {
            "speaker": "Vivian",
            "text": "Hello, I'm calling about the apartment for rent on Baker Street.",
        },
        {
            "speaker": "Ryan",
            "text": "Yes, the two-bedroom unit. It's still available. Would you like some information about it?",
        },
        {"speaker": "Vivian", "text": "Yes, please. Does the rent include utilities?"},
        {
            "speaker": "Ryan",
            "text": "The rent includes water and heating, but electricity and internet are separate.",
        },
        {
            "speaker": "Vivian",
            "text": "Okay, that sounds reasonable. Is there a parking space included?",
        },
        {
            "speaker": "Ryan",
            "text": "Yes, there is one assigned parking spot in the underground garage. Are there any pets?",
        },
        {"speaker": "Vivian", "text": "I have a small cat. Is that allowed?"},
        {
            "speaker": "Ryan",
            "text": "Usually we don't allow pets, but for a small cat we can make an exception with an additional deposit.",
        },
        {"speaker": "Vivian", "text": "That's great. When can I come to see it?"},
        {
            "speaker": "Ryan",
            "text": "I'm showing it tomorrow at 2 PM. Does that work for you?",
        },
    ],
    9: [  # Sports Club
        {
            "speaker": "Ryan",
            "text": "Hi, I'm interested in joining the gym. Can you tell me about your membership options?",
        },
        {
            "speaker": "Vivian",
            "text": "Certainly! We have two main plans. The Basic plan is $30 a month and includes access to all equipment.",
        },
        {"speaker": "Ryan", "text": "And the other plan?"},
        {
            "speaker": "Vivian",
            "text": "The Premium plan is $50. It includes unlimited group classes like yoga and spinning, plus access to the swimming pool.",
        },
        {
            "speaker": "Ryan",
            "text": "The pool sounds tempting. Are there towels provided?",
        },
        {
            "speaker": "Vivian",
            "text": "Yes, with the Premium plan we provide fresh towels and a private locker.",
        },
        {"speaker": "Ryan", "text": "Is there a contract, or can I cancel anytime?"},
        {
            "speaker": "Vivian",
            "text": "It's a month-to-month contract, you just need to give us 30 days notice before cancelling.",
        },
        {
            "speaker": "Ryan",
            "text": "Sounds fair. I'll go with the Premium plan. Can I start today?",
        },
        {
            "speaker": "Vivian",
            "text": "Absolutely! Just fill out this form and we'll get your key card ready.",
        },
    ],
    10: [  # Ordering Food
        {"speaker": "Vivian", "text": "Good evening, are you ready to order?"},
        {
            "speaker": "Ryan",
            "text": "Yes, I think so. For the starter, I'd like the tomato soup, please.",
        },
        {"speaker": "Vivian", "text": "Excellent choice. And for the main course?"},
        {
            "speaker": "Ryan",
            "text": "I'm torn between the grilled salmon and the steak. Which one do you recommend?",
        },
        {
            "speaker": "Vivian",
            "text": "The salmon is very fresh today, it came in this morning. It's served with roasted vegetables.",
        },
        {
            "speaker": "Ryan",
            "text": "That sounds perfect. I'll have the salmon then. Does it contain any nuts? I have an allergy.",
        },
        {
            "speaker": "Vivian",
            "text": "No, it's completely nut-free. Would you like anything to drink with that?",
        },
        {
            "speaker": "Ryan",
            "text": "Just a glass of white wine, please. The house white is fine.",
        },
        {"speaker": "Vivian", "text": "Very well. I'll bring your drink right away."},
    ],
}


def load_model():
    """Load Qwen3-TTS model."""
    from qwen_tts import Qwen3TTSModel

    print("[INFO] Loading Qwen3-TTS model...")

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    dtype = torch.float32
    print(f"   Device: {device}")

    model = Qwen3TTSModel.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
        device_map=device,
        dtype=dtype,
    )
    print("[OK] Model loaded!\n")
    return model


def generate_single_line(model, speaker: str, text: str, line_num: int, total: int):
    """Generate audio for a single line."""
    short_text = text[:60] + "..." if len(text) > 60 else text
    print(f"  [AUDIO] [{line_num}/{total}] {speaker}: {short_text}")

    wavs, sr = model.generate_custom_voice(
        text=text,
        language="English",
        speaker=speaker,
        instruct="Natural conversational tone, clear pronunciation.",
    )
    return wavs[0], sr


def generate_dialogue(model, dialogue_id: int):
    """Generate complete dialogue audio."""
    if dialogue_id not in DIALOGUES:
        print(f"[ERROR] Dialogue {dialogue_id} not found!")
        return

    dialogue = DIALOGUES[dialogue_id]
    output_name = f"dialogue_{dialogue_id}"

    print("\n" + "=" * 60)
    print(f"[START] Generating Dialogue {dialogue_id}")
    print("=" * 60)

    all_audio = []
    sr = None
    total = len(dialogue)

    for i, line in enumerate(dialogue, 1):
        try:
            audio, sample_rate = generate_single_line(
                model, line["speaker"], line["text"], i, total
            )
            all_audio.append(audio)
            sr = sample_rate

            # 0.5 second pause between speakers
            if sr:
                pause = np.zeros(int(sr * 0.5))
                all_audio.append(pause)
        except Exception as e:
            print(f"  [ERROR] Failed to generate line {i}: {e}")

    if not all_audio:
        print("[ERROR] No audio generated.")
        return

    # Concatenate all audio
    final_audio = np.concatenate(all_audio)

    # Save
    output_path = os.path.join(OUTPUT_DIR, f"{output_name}.wav")
    sf.write(output_path, final_audio, sr)

    duration = len(final_audio) / sr
    print(f"\n[OK] Saved: {output_path}")
    print(f"   Duration: {duration:.1f} seconds")


def main():
    """Main function."""
    print("\n" + "=" * 60)
    print("KT English Test - Audio Dialogue Generator (1-10)")
    print("=" * 60 + "\n")

    # Argument parsing
    if len(sys.argv) < 2:
        print("Usage:")
        print(
            "  python generate_audio.py <number>   # Generate specific dialogue (1-10)"
        )
        print("  python generate_audio.py all        # Generate ALL dialogues")
        print()
        choice = input("Enter number (1-10) or 'all': ").strip()
    else:
        choice = sys.argv[1]

    # Load model
    try:
        model = load_model()
    except Exception as e:
        print(f"\n[FATAL ERROR] Model loading failed: {e}")
        return

    if choice.lower() == "all":
        for i in range(1, 11):
            generate_dialogue(model, i)
    else:
        try:
            dial_id = int(choice)
            generate_dialogue(model, dial_id)
        except ValueError:
            print("[ERROR] Invalid input. Use a number 1-10 or 'all'.")

    print("\n" + "=" * 60)
    print("[DONE] Finished!")
    print(f"Audio files: {OUTPUT_DIR}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
