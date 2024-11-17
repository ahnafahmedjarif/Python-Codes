"""Let's download a web """

import os
import requests

# URL of the webpage
url = "https://example.com"

# Fetch the webpage content
response = requests.get(url)

# Define the directory to save the file
save_dir = "webpages"
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Define the file name and save path
file_name = "webpage.html"
file_path = os.path.join(save_dir, file_name)

# Save the webpage content
with open(file_path, "w", encoding="utf-8") as file:
    file.write(response.text)

print(f"Webpage downloaded successfully and saved at {file_path}")