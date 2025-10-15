import re
import tldextract

# Common suspicious patterns (expandable)
SUSPICIOUS_KEYWORDS = [
    "login", "verify", "account", "secure", "update", "password", "bank", "paypal", "alert", "invoice"
]

def extract_urls(text):
    """Extract all URLs from email text"""
    url_pattern = r'(https?://[^\s]+)'
    return re.findall(url_pattern, text)

def is_suspicious_url(url):
    """Analyze URL for phishing indicators"""
    domain_info = tldextract.extract(url)
    domain = f"{domain_info.domain}.{domain_info.suffix}"

    # Rule 1: If there's too many dots or hyphens
    if url.count('.') > 4 or '-' in domain:
        return True, "Too many subdomains or hyphens"

    # Rule 2: Keyword check
    if any(keyword in url.lower() for keyword in SUSPICIOUS_KEYWORDS):
        return True, "Contains phishing-related keywords"

    # Rule 3: Non-standard domain (e.g., .xyz, .top, .click)
    if domain_info.suffix in ["xyz", "top", "click", "link"]:
        return True, "Suspicious top-level domain"

    return False, "Looks normal"

def analyze_urls(text):
    """Return list of suspicious URLs"""
    urls = extract_urls(text)
    suspicious = []
    for url in urls:
        flag, reason = is_suspicious_url(url)
        if flag:
            suspicious.append({"url": url, "reason": reason})
    return suspicious