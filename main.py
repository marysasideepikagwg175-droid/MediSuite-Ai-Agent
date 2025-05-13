import os
from Agent import MedicalCodingAgent

def main():
    """Main entry point for the CLI."""
    # Read environment variables
    tesseract_cmd = os.getenv('TESSERACT_CMD', '/usr/bin/tesseract')  # Default for Linux
    poppler_path = os.getenv('POPPLER_PATH', '/usr/bin')  # Default for Linux
    openai_api_key = os.getenv('OPENAI_API_KEY', 'your-default-api-key')

    # Inject configurations into the MedicalCodingAgent
    agent = MedicalCodingAgent(
        tesseract_cmd=tesseract_cmd,
        poppler_path=poppler_path,
        openai_api_key=openai_api_key
    )
    agent.start_conversation()

if __name__ == "__main__":
    main()