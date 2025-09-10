import requests # type: ignore
import os
from urllib.parse import urlparse
import uuid

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    

    urls = input("Please enter one or more image URLs (separated by commas): ").split(",")

   
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

   
    saved_files = set()

    for url in urls:
        url = url.strip()
        if not url:
            continue
        
        try:
            
            response = requests.get(url, timeout=10)
            response.raise_for_status() 

          
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type:
                print(f"✗ Skipped (not an image): {url}")
                continue

           
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename or "." not in filename:
                ext = content_type.split("/")[-1] if "/" in content_type else "jpg"
                filename = f"image_{uuid.uuid4().hex}.{ext}"

            
            if filename in saved_files:
                print(f"✗ Skipped duplicate: {filename}")
                continue

            
            filepath = os.path.join(folder, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)

            saved_files.add(filename)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
