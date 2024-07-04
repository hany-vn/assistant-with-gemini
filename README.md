# Voice Recognition and Synthesis Project

## Description
This project utilizes the SpeechRecognition library for speech recognition from users and the gTTS (Google Text-to-Speech) library for text-to-speech synthesis. It also incorporates other libraries such as playsound for audio playback, and google.generativeai for additional AI tasks.

## System Requirements
- Python 3.x
- Install the required libraries listed in the `requirements.txt` file using: `pip install -r requirements.txt`
- Internet connection is required to use Google Text-to-Speech and Google Generative AI services.

## Installation
1. Clone the project from the GitHub repository:
git clone https://github.com/hany-vn/assistant-with-gemini

css
Copy code
2. Navigate to the project directory:
cd your_project

markdown
Copy code
3. Install the necessary libraries:
pip install -r requirements.txt

vbnet
Copy code

## Usage
1. Run the `main.py` file to start the application.
2. The application will wait for the user to speak a sentence.
3. After the user finishes speaking, the application will recognize the speech and synthesize the spoken response.

## Customization
- You can change the language for speech recognition and synthesis by modifying parameters in the `main.py` file.
- You can also adjust the speech speed by editing the `speed` parameter in the `gTTS()` function.

## Disclaimer
- Using the SpeechRecognition library requires an Internet connection to utilize Google services. Ensure your computer is connected to the Internet when running the project.
- To avoid being blocked by Google's privacy policies, use the gTTS service responsibly and adhere to Google Text-to-Speech usage guidelines and terms.

## Author
This project is developed by [Hany](https://github.com/hany-vn).
