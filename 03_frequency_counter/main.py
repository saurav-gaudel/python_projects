from collections import Counter
import re

def frequency_counter(text:str)->list[tuple[str,int]]:
    lowered_text:str= text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()

def main()->None:
    text = input("Enter text:").strip()
    word_frequencies: list[tuple[str,int]]= frequency_counter(text)
    for word, count in word_frequencies:
        print(f"{word} : {count}")


if __name__== "__main__":
    main()
