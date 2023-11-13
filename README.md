# Google Sheets PDF Downloader

## Overview

This Python script is designed to download PDF files listed in a Google Sheet. It uses the Google Sheets API for authentication and gspread library to interact with Google Sheets.

## Features

- Downloads PDF files linked in a Google Sheet.
- Provides feedback on the download status.
- Handles errors gracefully and logs any issues encountered.

## Prerequisites

Before running the script, make sure you have the following:

1. **Google Sheets API Credentials:**
   - Create a service account on the [Google Cloud Console](https://console.cloud.google.com/).
   - Download the JSON key file for the service account and save it as `credentials.json`.
   - Share the Google Sheet with the email address mentioned in the service account.

2. **Python Dependencies:**
   - Install the required Python libraries using the following command:
     ```bash
     pip install gspread oauth2client requests
     ```

## Configuration

1. **Google Sheets URL:**
   - Replace the `sheet_url` variable with the actual URL of your Google Sheet.

2. **Running the Script:**
   - Execute the script using the following command:
     ```bash
     python script_name.py
     ```

## Usage

1. Run the script, and it will fetch the PDF links from the specified Google Sheet.
2. PDFs will be downloaded to the local directory.
3. The script will provide feedback on the download status, including any errors encountered.

## Notes

- Ensure the Google Sheet is shared with the service account mentioned in the `credentials.json` file.
- Make sure the provided Google Sheet URL is accessible.

## Contributing

Feel free to contribute to the project by opening issues or creating pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Replace `script_name.py` with the actual name of your Python script, and create a `LICENSE` file with the appropriate license information. Additionally, you may want to include a `requirements.txt` file if your script has specific version requirements for its dependencies.