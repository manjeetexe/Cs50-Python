import os
import PIL.Image
import base64
import google.generativeai as genai
from dotenv import load_dotenv
import io

# Load environment variables (e.g., GEMINI_API_KEY)
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to convert an image to base64
def image_to_base64(image_path):
    with PIL.Image.open(image_path) as img:  # Open the image
        img = img.convert("RGB")  # Convert the image to RGB (if it's not already)
        buffered = io.BytesIO()  # Create a buffer to hold the image
        img.save(buffered, format="JPEG")  # Save the image to the buffer
        return base64.b64encode(buffered.getvalue()).decode('utf-8')  # Encode it to base64

# Convert the admin and captured images to base64
admin_image_base64 = image_to_base64('./admin/pht.jpg')  # Correct the relative path
captured_image_base64 = image_to_base64('./pht2.jpg')  # If the captured image is in the root folder     # Path to your captured image

# Prepare the images to be sent to Gemini API
image_send = [
    {"inlineData": {"data": captured_image_base64, "mimeType": "image/jpg"}},
    {"inlineData": {"data": admin_image_base64, "mimeType": "image/jpg"}}
]

# Send the images to the Gemini API for comparison
try:
    # Assuming 'generate_content' is the correct method (it may differ depending on the API)
    result = genai.generate_content(
        prompt="Compare these two images for authentication",
        images=image_send
    )
    
    # Print the response from Gemini
    print("Gemini Response:", result.response.text)

except Exception as e:
    print("Error sending images to Gemini:", e)