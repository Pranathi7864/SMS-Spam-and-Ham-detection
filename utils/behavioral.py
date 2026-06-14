from collections import Counter

def get_symbol_ratio(text):
    if not text:
        return 0

    counts = Counter(text)
    total = len(text)

    spam_symbols = ['!', '$', '#', '*']
    symbol_ratio = sum(counts[s] for s in spam_symbols if s in counts) / total

    return symbol_ratio