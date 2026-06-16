import json
import os
import requests

# 1. Setup Configuration
API_KEY = "sd_f3e71e7186ac98dc29e93ab4a678d621" 
ENDPOINT = "https://api.supadata.ai/v1/transcript"

# 2. Hard-Technical Data Targets (No marketing fluff, pure engineering breakdowns)
videos = {
    "elias_dabbas_python_data_science_seo": "https://www.youtube.com/watch?v=DwKw3YRLDEI",
    "programmatic_seo_nextjs_engine_guide": "https://www.youtube.com/watch?v=290Ytj96vL4"
}

output_dir = "research/youtube-transcripts"
os.makedirs(output_dir, exist_ok=True)

# 3. Request Loop
for name, url in videos.items():
    print(f"Requesting API transcript data for: {name}...")
    headers = {"x-api-key": API_KEY}
    params = {"url": url}

    try:
        response = requests.get(ENDPOINT, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if "content" in data:
                file_path = os.path.join(output_dir, f"{name}.txt")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(data["content"]))
                print(f"✅ Saved transcript to {file_path}")
        else:
            print(f"❌ Failed for {name}: Status Code {response.status_code} - {response.text}")
    except Exception as e:
        print(f"💥 Error requesting {name}: {str(e)}")