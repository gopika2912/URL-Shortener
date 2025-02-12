import hashlib

def shorten_url(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]

if __name__ == "__main__":
    url = "https://example.com"
    print("Shortened URL:", shorten_url(url))
