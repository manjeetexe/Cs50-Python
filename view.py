import cv2

def capture_image():

    cap = cv2.VideoCapture(1)
    
 
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    while True:
    
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('Camera Feed - Press "c" to capture', frame)

      
        if cv2.waitKey(1) & 0xFF == ord('c'):
            captured_image_path = 'pht2.jpg'
            cv2.imwrite(captured_image_path, frame)
            print(f"Image captured and saved as {captured_image_path}")
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return captured_image_path

image_path = capture_image()