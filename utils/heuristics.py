import math
import re
import requests
from collections import Counter
import tldextract
from utils.behavioral import get_symbol_ratio


# -------- ENTROPY --------
def calculate_entropy(text):
    if not text:
        return 0

    urls = re.findall(r'http[s]?://\S+', text)
    target = urls[0] if urls else text

    probs = [n / len(target) for n in Counter(target).values()]
    return -sum(p * math.log2(p) for p in probs)


# -------- UNMASK SHORT LINKS --------
def get_final_destination(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=3)
        return response.url
    except:
        return url


# -------- MAIN FEATURE FUNCTION --------
def get_technical_features(text):

    TRUSTED_BRANDS = [
        "amazon", "google", "paypal", "microsoft",
        "apple", "facebook", "instagram",
        "bank", "icici", "hdfc", "sbi"
    ]

    DANGEROUS_TLDS = ['cc', 'xyz', 'top', 'tk', 'ml', 'ga', 'cf', 'gq', 'online']
    SENSITIVE_WORDS = ['login', 'verify', 'account', 'security', 'update', 'banking']

    entropy = calculate_entropy(text)
    digit_count = sum(c.isdigit() for c in text)
    has_url = int(bool(re.search(r'(https?://|www\.)', text)))
    length = len(text)

    urls = re.findall(
        r'(?:https?://|www\.)\S+|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(?:/\S*)?',
        text
    )

    final_url = ""
    risky_tld = 0
    phish_score = 0
    impersonation_score = 0

    symbol_ratio = get_symbol_ratio(text)

    if urls:
        final_url = get_final_destination(urls[0])
        ext = tldextract.extract(final_url)

        domain_full = ext.domain.lower()
        subdomain_full = ext.subdomain.lower()

        # --- Impersonation Detection ---
        for brand in TRUSTED_BRANDS:
            if brand in subdomain_full and brand not in domain_full:
                impersonation_score += 2

        # --- Risky TLD ---
        if ext.suffix in DANGEROUS_TLDS:
            risky_tld = 1

        # --- Sensitive Words in URL ---
        for word in SENSITIVE_WORDS:
            if word in final_url.lower():
                phish_score += 1

    return {
        "entropy": entropy,
        "digit_count": digit_count,
        "has_url": has_url,
        "length": length,
        "risky_tld": risky_tld,
        "phish_score": phish_score,
        "impersonation_score": impersonation_score,
        "symbol_ratio": symbol_ratio,
        "final_url": final_url
    }