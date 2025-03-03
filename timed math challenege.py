import time
import random

def load_sentences():
    return [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an amazing programming language.",
        "Practice makes perfect when learning to type fast.",
        "Speed and accuracy are key to efficient typing.",
        "Typing tests help improve your keyboard skills."
    ]

def get_random_sentence(sentences):
    return random.choice(sentences)

def typing_test():
    sentences = load_sentences()
    sentence = get_random_sentence(sentences)
    print("\nType the following sentence:")
    print(f"\033[1;34m{sentence}\033[0m")  # Blue bold text
    
    input("\nPress Enter when ready...")
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    wpm = (words_typed / elapsed_time) * 60 if elapsed_time > 0 else 0
    
    accuracy = sum(1 for a, b in zip(user_input, sentence) if a == b) / max(len(sentence), 1) * 100
    
    print("\nResults:")
    print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
    print(f"⌨️ Words per minute: {wpm:.2f}")
    print(f"🎯 Accuracy: {accuracy:.2f}%")

def main():
    print("Welcome to the Typing Speed Test!")
    while True:
        typing_test()
        again = input("\nDo you want to try again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Keep practicing. ✨")
            break

if __name__ == "__main__":
    main()
