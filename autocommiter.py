import os
import random
import time
import google.generativeai as genai
from datetime import datetime

# Configure the Gemini API client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the model to use
model = genai.GenerativeModel("gemini-2.5-flash")  # Ensure this model is available

# Define the commit message template
commit_message_template = """
feat: Add new module for decentralized identity (DID) system

- Implemented a module for a decentralized identity (DID) system on a dedicated Layer 3 (L3) blockchain.
- The module includes functionalities for DID creation, verification, and resolution.
- Integrated with existing blockchain infrastructure to ensure seamless interoperability.
"""

# Define the directory for storing generated files
modules_dir = "modules"

# Ensure the modules directory exists
os.makedirs(modules_dir, exist_ok=True)

def generate_commit():
    """Generate a commit by creating a new Python file and committing it."""
    # Generate a unique filename based on the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"feat_did_system_{timestamp}.py"
    filepath = os.path.join(modules_dir, filename)

    # Generate content using the Gemini model
    try:
        response = model.generate_content(
            contents=commit_message_template
        )
        content = response.text.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        return

    # Write the generated content to the new Python file
    with open(filepath, "w") as f:
        f.write(content)

    # Log the commit
    with open("log.txt", "a") as log:
        log.write(f"Committed {filename} at {datetime.now()}\n")

    print(f"Generated and committed {filename}")

def main():
    """Main loop to generate commits at random intervals."""
    while True:
        generate_commit()
        # Sleep for a random interval between 1 to 6 hours
        sleep_time = random.randint(3600, 21600)
        print(f"Sleeping for {sleep_time / 3600:.2f} hours...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
