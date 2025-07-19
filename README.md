# Veo AI Video Generator

This project is a simple web application that allows users to generate videos using Google's Veo AI model. The app is built with [Streamlit](https://streamlit.io/) and leverages the Google Generative AI API to create videos from user prompts.

## Features
- Enter a text prompt to generate a video using Veo AI
- Download the generated video
- Simple and interactive web interface

## Requirements
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)

## Setup
1. **Clone the repository:**
   ```bash
   git clone [<your-repo-url>](https://github.com/saimsajidirl/Veo_deo-Generation)
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API key:**
   - Create a `.env` file in the project root with the following content:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```
   - Replace `your_google_api_key_here` with your actual API key from Google.

## Running the App
Start the Streamlit app with:
```bash
streamlit run main.py
```

Then open the provided local URL in your browser.

## Usage
1. Enter a descriptive prompt for the video you want to generate.
2. Click the "Generate Video" button.
3. Wait for the video to be generated (this may take a minute).
4. Watch the video in the app and download it if desired.

## Notes
- Make sure your Google API key has access to the Veo AI video generation model.
- The app currently generates one video per prompt with a 16:9 aspect ratio and does not allow person generation.

## License
MIT 
