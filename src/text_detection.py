import cv2
import os
import pytesseract
import easyocr
import pytesseract
from PIL import Image

# Ensure output directory exists
os.makedirs("frames", exist_ok=True)

# Load Video
video = cv2.VideoCapture("input.mp4")

if not video.isOpened():
    print("Error: Could not open video file.")
else:
    success, frame = video.read()
    count = 0

    while success:
        frame_path = f"frames/frame_{count}.jpg"
        cv2.imwrite(frame_path, frame)
        success, frame = video.read()
        count += 1

    video.release()
    print(f"Extracted {count} frames successfully.")



image = cv2.imread("frames/frame_86.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Save preprocessed image for debugging (optional)
cv2.imwrite("processed.png", gray)

# Perform OCR using pytesseract
text = pytesseract.image_to_string(gray)

print("Extracted Text:")
print(text)


'''# OCR Processing on First Frame
image_path = "frames/frame_86.jpg"
image = cv2.imread(image_path)

# Preprocess Image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Tesseract OCR
text = pytesseract.image_to_string(thresh)
print("Detected Text:", text)

# EasyOCR
reader = easyocr.Reader(['en'])
results = reader.readtext(image)
print("EasyOCR Results:", results)'''


# from googletrans import Translator

# translator = Translator()
# translated_text = translator.translate("Welcome", dest="es").text
# print("Translated Text:", translated_text)
