"""
Extended Audio Generator - Monologue and Review style
Based on KT test real examples (1.txt, 2.txt)

Generates:
- Monologue texts (leadership, science, culture)
- Review/Commentary texts (films, books, places)
"""

import os
import sys
import numpy as np
import soundfile as sf
import torch

# Setup SoX path
sox_path = r"C:\Program Files (x86)\sox-14-4-2"
if os.path.exists(sox_path):
    print(f"[SETUP] Adding SoX to PATH: {sox_path}")
    os.environ["PATH"] += os.pathsep + sox_path

# Output directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================
# MONOLOGUE TEXTS (Single speaker, educational)
# ============================================

MONOLOGUES = {
    # Monologue 1: Great Leaders (based on 1.txt style)
    "monologue_leaders": {
        "speaker": "Ryan",
        "text": """Great leaders come in all shapes and sizes. They can be anyone from a company CEO to a soccer coach, a small business owner to a group discussion leader. While there are some natural leaders, most great leaders are not born that way. Instead, they learned how to be great over time. So what are these qualities that all great leaders share?

Great leaders are confident in their abilities and actions. They are not afraid of new challenges and stay calm when things get difficult. Once they decide to do something, they do it. While great leaders are confident, they are not arrogant. Confident leaders usually give comfort to those around them.

No one wants to work with people who are not excited about what they are doing. Great leaders are excited about what they do and want to share that feeling with others. Think about a soccer coach who is not excited about the sport. This kind of person hardly ever gets great results.

Great leaders care about other people and want to help them. When people need help, these leaders make difficult situations less challenging. Good communication skills are important for great leaders. They communicate their ideas clearly and listen carefully.

Great leaders have a goal in mind and do what they need to achieve it. Sony co-founder Akio Morita did not succeed the first time his company tried to sell its product, a rice cooker. It didn't cook the rice, it burnt it. They sold less than a hundred, but this did not stop Morita, as he went on to create a multi-billion dollar company.""",
    },
    # Monologue 2: Film Review (based on 2.txt style)
    "monologue_films": {
        "speaker": "Vivian",
        "text": """Welcome to the film review. Today, we're reviewing some of this week's newest films.

Let's start with the hit, Jungle Fever. This is an unusual one. Some of you may remember last year's TV documentary about a family of tigers in India. Well, this is a cartoon based on that program, and I can report it's great fun for people of any age.

Some of you will be excited to know that the actor Steve Willis is back on our screens. You'll remember him as an action hero, Marty, but in this new film, Call, he's actually a chef working in an Italian pizza takeaway shop in London. Actor Jennifer Peckary plays his manager, and romance is in the air.

Don't miss Swim, a comedy which takes a look at learning to swim as an adult. It's about a twenty-year-old man who wants to join in with his friends when they swim in the lake near his house. So he goes to the local pool to take lessons. Be prepared to laugh until it hurts!

Finally, we have Mountain Dreams, a beautiful documentary about climbers attempting to reach the summit of Mount Everest. The photography is stunning, and the personal stories of the climbers will inspire you.""",
    },
    # Monologue 3: University Life
    "monologue_university": {
        "speaker": "Ryan",
        "text": """Welcome to Cambridge University. I'm Professor Williams, and I'll be giving you a brief introduction to our institution today.

Cambridge University was founded in 1209, making it one of the oldest universities in the world. We currently have over 23,000 students from more than 140 countries. The university consists of 31 colleges, each with its own traditions and character.

Academic life here is centered around supervisions, which are small group teaching sessions with one or two students and a tutor. This personalized approach allows for deep discussion and individual attention that you won't find at larger institutions.

Our library system is one of the largest in the world, with over 15 million books across more than 100 libraries. The main University Library is a legal deposit library, meaning it receives a copy of every book published in the United Kingdom.

Students at Cambridge enjoy a balanced life. While academic work is demanding, there are numerous societies and clubs to join. The famous boat race against Oxford is held every spring on the River Thames. Many students also participate in theater, music, and sports.

If you have any questions about admissions or student life, please don't hesitate to ask during the tour.""",
    },
    # Monologue 4: Kazakhstan Culture
    "monologue_kazakhstan": {
        "speaker": "Vivian",
        "text": """Today I'd like to share some fascinating aspects of Kazakh culture and traditions.

Kazakhstan is the ninth largest country in the world, stretching from the Caspian Sea to the Altai Mountains. The country has been home to nomadic peoples for thousands of years, and this heritage continues to influence modern Kazakh culture.

The traditional Kazakh dwelling is the yurt, called a kiiz uy. These portable felt tents were perfect for the nomadic lifestyle and could be assembled or disassembled in just a few hours. Today, yurts are still used for celebrations and can be seen at festivals throughout the country.

Hospitality is extremely important in Kazakh culture. When guests arrive, they are traditionally offered kumys, a drink made from fermented mare's milk, and beshbarmak, which means five fingers because it's eaten with the hands. This dish consists of boiled meat served over flat noodles.

Music plays a central role in Kazakh traditions. The dombra, a two-stringed instrument, is found in almost every home. Traditional songs called kuis tell stories of nature, love, and historical events.

The Nauryz festival, celebrated on March 22nd, marks the spring equinox and the beginning of the new year. Families gather to enjoy traditional foods, games, and music. It's a time of renewal and hope for the coming year.""",
    },
    # Monologue 5: Technology and Innovation
    "monologue_technology": {
        "speaker": "Ryan",
        "text": """Good morning everyone. Today's lecture focuses on how technology is changing our world.

Over the past two decades, we've witnessed remarkable technological advances. The smartphone in your pocket has more computing power than the computers that sent astronauts to the moon. We can video call friends across the world instantly, something that seemed like science fiction just 30 years ago.

Artificial intelligence is perhaps the most significant development of our time. AI can now diagnose diseases, drive cars, and even create art. Machine learning algorithms process vast amounts of data to find patterns that humans might miss. In healthcare, AI is helping doctors detect cancer earlier and develop personalized treatment plans.

However, technology also presents challenges. Privacy concerns have grown as companies collect more personal data. The rise of social media has changed how we communicate, sometimes creating echo chambers where we only hear opinions similar to our own.

Looking forward, we can expect even more changes. Renewable energy technology is becoming more efficient, helping us address climate change. Virtual reality and augmented reality are creating new ways to learn and work. And quantum computing promises to solve problems that are currently impossible for traditional computers.

The key is to embrace these changes while being mindful of their impact on society. Technology should serve humanity, not the other way around.""",
    },
    # Monologue 6: Health and Wellness
    "monologue_health": {
        "speaker": "Vivian",
        "text": """Welcome to our weekly health program. Today we'll discuss some simple ways to improve your wellbeing.

Sleep is often overlooked, but it's essential for good health. Adults should aim for seven to nine hours per night. During sleep, your body repairs itself, and your brain consolidates memories. To improve sleep quality, try to go to bed at the same time each night and avoid screens for an hour before sleeping.

Physical activity is just as important. You don't need to run marathons or lift heavy weights. Even a 30-minute walk each day can reduce the risk of heart disease, diabetes, and depression. Find an activity you enjoy, whether it's swimming, dancing, or gardening. The best exercise is the one you'll actually do.

What you eat matters too. Try to include plenty of fruits, vegetables, and whole grains in your diet. Reduce processed foods and sugary drinks. Remember, it's about balance, not perfection. Occasional treats are fine as part of an overall healthy diet.

Don't forget about mental health. Stress affects both your mind and body. Simple practices like deep breathing, meditation, or spending time in nature can help manage stress. Stay connected with friends and family, too. Social relationships are strongly linked to happiness and longevity.

Finally, regular health check-ups can catch problems early when they're easier to treat. Talk to your doctor about recommended screenings for your age and health history.""",
    },
}


# ============================================
# AUDIO GENERATION
# ============================================


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


def generate_monologue(model, monologue_id: str):
    """Generate monologue audio."""
    if monologue_id not in MONOLOGUES:
        print(f"[ERROR] Monologue '{monologue_id}' not found!")
        return

    monologue = MONOLOGUES[monologue_id]
    speaker = monologue["speaker"]
    text = monologue["text"]

    print("\n" + "=" * 60)
    print(f"[START] Generating: {monologue_id}")
    print(f"   Speaker: {speaker}")
    print(f"   Length: {len(text)} characters")
    print("=" * 60)

    # Split text into paragraphs for better generation
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    all_audio = []
    sr = None

    for i, paragraph in enumerate(paragraphs, 1):
        print(f"  [AUDIO] Paragraph {i}/{len(paragraphs)}...")

        try:
            wavs, sample_rate = model.generate_custom_voice(
                text=paragraph,
                language="English",
                speaker=speaker,
                instruct="Natural reading pace, clear pronunciation, educational tone.",
            )
            all_audio.append(wavs[0])
            sr = sample_rate

            # Add 1 second pause between paragraphs
            if sr:
                pause = np.zeros(int(sr * 1.0))
                all_audio.append(pause)

        except Exception as e:
            print(f"  [ERROR] Failed to generate paragraph {i}: {e}")

    if not all_audio:
        print("[ERROR] No audio generated.")
        return

    # Concatenate all audio
    final_audio = np.concatenate(all_audio)

    # Save
    output_path = os.path.join(OUTPUT_DIR, f"{monologue_id}.wav")
    sf.write(output_path, final_audio, sr)

    duration = len(final_audio) / sr
    print(f"\n[OK] Saved: {output_path}")
    print(f"   Duration: {duration:.1f} seconds")


def main():
    """Main function."""
    print("\n" + "=" * 60)
    print("KT English Test - Monologue Audio Generator")
    print("=" * 60 + "\n")

    available = list(MONOLOGUES.keys())
    print("Available monologues:")
    for i, key in enumerate(available, 1):
        print(f"  {i}. {key}")
    print(f"  all - Generate ALL monologues")

    # Argument parsing
    if len(sys.argv) < 2:
        choice = input("\nEnter number or 'all': ").strip()
    else:
        choice = sys.argv[1]

    # Load model
    try:
        model = load_model()
    except Exception as e:
        print(f"\n[FATAL ERROR] Model loading failed: {e}")
        return

    if choice.lower() == "all":
        for mono_id in available:
            generate_monologue(model, mono_id)
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(available):
                generate_monologue(model, available[idx])
            else:
                print("[ERROR] Invalid number.")
        except ValueError:
            if choice in available:
                generate_monologue(model, choice)
            else:
                print("[ERROR] Invalid input.")

    print("\n" + "=" * 60)
    print("[DONE] Finished!")
    print(f"Audio files: {OUTPUT_DIR}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
