def to_upper(text: str) -> str:
    return text.upper()

def count_words(text: str) -> int:
    return len(text.split())

if __name__ == "__main__":
    print("Upper:", to_upper("hello"))
    print("Word Count:", count_words("hello world"))
