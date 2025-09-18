import cv2
import pytesseract
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties for the TTS engine to avoid pauses between lines
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to split text into smaller parts for continuous reading
def split_text(text, chunk_size=200):
    chunks = []
    chunk = ""
    words = text.split()
    for word in words:
        if len(chunk) + len(word) <= chunk_size:
            chunk += word + " "
        else:
            chunks.append(chunk)
            chunk = word + " "
    if chunk:
        chunks.append(chunk)
    return chunks

# Function to read text from live camera feed and convert it to speech continuously
def read_live_feed_and_speak():
    # Open the default camera (0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale for better text recognition
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use Tesseract OCR to recognize text
        text = pytesseract.image_to_string(gray)

        # Split the text into smaller parts for continuous reading
        text_chunks = split_text(text)

        # Convert each chunk to speech and read continuously
        for chunk in text_chunks:
            engine.say(chunk)
            engine.runAndWait()

        # Display the frame with recognized text
        cv2.imshow('Frame', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to read text from the live camera feed and speak it continuously
read_live_feed_and_speak()