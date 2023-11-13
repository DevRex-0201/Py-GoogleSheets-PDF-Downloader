import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import os

# Set up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

# Google Sheet URL (replace this with your actual Google Sheets URL)
sheet_url = "https://docs.google.com/spreadsheets/d/1kGYjUElJEwLNmShkAfYFnVnYgm0GAdqCvl4X-Uh0yOw/edit?usp=sharing"

# Open the Google Sheet using its URL
sheet = client.open_by_url(sheet_url).sheet1

# Get all PDF links from the Google Sheet
pdf_links = sheet.col_values(1)  # Assuming PDF links are in the first column

# Download PDFs
for link in pdf_links:
    if link.endswith('.pdf'):
        print("ok")
        try:
            response = requests.get(link, stream=True)
            filename = os.path.basename(link)  # Extract filename from the URL
            if os.path.exists(filename):
                filename = f"{os.path.splitext(filename)[0]}_{str(hash(link))[:5]}.pdf"
            with open(filename, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)
            print(f"Downloaded: {filename}")
        except requests.RequestException as e:
            print(f"Failed to download {link}: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")
