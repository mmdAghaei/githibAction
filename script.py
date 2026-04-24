import io
import zipfile
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

WEBHOOK_URL = "https://mmdaghaei.runflare.run/webhook-test/ef6241a8-68f3-40bf-a6f6-712482e45e1e"
SITE_URL = "https://google.com"

def download_page_and_assets(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    assets = {}

    # CSS
    for tag in soup.find_all("link", rel="stylesheet"):
        href = tag.get("href")
        if href:
            asset_url = urljoin(url, href)
            assets[href] = requests.get(asset_url).content

    # JS
    for tag in soup.find_all("script"):
        src = tag.get("src")
        if src:
            asset_url = urljoin(url, src)
            assets[src] = requests.get(asset_url).content

    # Images
    for tag in soup.find_all("img"):
        src = tag.get("src")
        if src:
            asset_url = urljoin(url, src)
            assets[src] = requests.get(asset_url).content

    return html, assets


def build_zip_in_memory(html, assets):
    mem_zip = io.BytesIO()

    with zipfile.ZipFile(mem_zip, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("index.html", html)
        for path, content in assets.items():
            z.writestr(path, content)

    mem_zip.seek(0)
    return mem_zip


# Download
html, assets = download_page_and_assets(SITE_URL)

# Build ZIP in RAM
zip_file = build_zip_in_memory(html, assets)

# Send to webhook
requests.post(
    WEBHOOK_URL,
    files={"file": ("website.zip", zip_file, "application/zip")}
)

print("DONE!")
