import time
import random

# Preload sentences to avoid redundant function calls
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes perfect when learning to type fast.",
    "Speed and accuracy are key to efficient typing.",
    "Typing tests help improve your keyboard skills."
]

def get_random_sentence():
    return random.choice(SENTENCES)

def calculate_accuracy(user_input, sentence):
    if not user_input:
        return 0.0  # Avoid division errors

    correct_chars = sum(1 for a, b in zip(user_input, sentence) if a == b)
    return (correct_chars / max(len(sentence), len(user_input))) * 100

def typing_test():
    sentence = get_random_sentence()
    print("\nType the following sentence:")
    print(f"\033[1;34m{sentence}\033[0m")  # Blue bold text

    input("\nPress Enter when ready...")
    start_time = time.time()
    user_input = input("\nStart typing: ").strip()
    elapsed_time = max(time.time() - start_time, 0.01)  # Avoid divide-by-zero

    words_typed = len(user_input.split())
    wpm = (words_typed / elapsed_time) * 60 if words_typed > 0 else 0
    accuracy = calculate_accuracy(user_input, sentence)

    print("\nResults:")
    print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
    print(f"⌨️ Words per minute: {wpm:.2f}")
    print(f"🎯 Accuracy: {accuracy:.2f}%")

def main():
    print("Welcome to the Typing Speed Test!")
    while True:
        typing_test()
        if input("\nDo you want to try again? (y/n): ").strip().lower() != 'y':
            print("\nThanks for playing! Keep practicing. ✨")
            break

if __name__ == "__main__":
    main()

