import cv2
import numpy as np
import time
import os
from datetime import datetime

class FaceDetectionSystem:
    def __init__(self):
        """Initialize the face detection system"""
        self.face_cascade = self.load_cascade()
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        
        self.video_cap = None
        self.face_count = 0
        self.total_faces_detected = 0
        self.start_time = time.time()
        
        # Create screenshots directory
        self.screenshot_dir = "face_detection_screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
    
    def load_cascade(self):
        """Load face cascade with error handling"""
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(cascade_path)
        
        if face_cascade.empty():
            print(f"❌ Error: Could not load cascade from {cascade_path}")
            print("Make sure OpenCV is properly installed: pip install opencv-python")
            exit(1)
        
        print("✅ Face cascade loaded successfully")
        return face_cascade
    
    def initialize_camera(self, camera_index=0):
        """Initialize camera with multiple fallback options"""
        for i in range(camera_index, camera_index + 3):
            print(f"🔍 Trying camera index {i}...")
            self.video_cap = cv2.VideoCapture(i)
            
            if self.video_cap.isOpened():
                # Test if camera actually works
                ret, test_frame = self.video_cap.read()
                if ret and test_frame is not None:
                    print(f"✅ Camera {i} initialized successfully")
                    
                    # Set camera properties for better quality
                    self.video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                    self.video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                    self.video_cap.set(cv2.CAP_PROP_FPS, 30)
                    
                    return True
                else:
                    self.video_cap.release()
            
        print("❌ Error: Could not access any camera")
        print("💡 Troubleshooting tips:")
        print("   - Check if camera is being used by another application")
        print("   - Check camera permissions in system settings")
        print("   - Try running as administrator")
        return False
    
    def detect_faces_and_features(self, frame, gray_frame):
        """Detect faces, eyes, and smiles"""
        faces = self.face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.05,  # More sensitive detection
            minNeighbors=6,    # Reduce false positives
            minSize=(50, 50),  # Larger minimum size
            maxSize=(400, 400), # Maximum face size
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        for (x, y, w, h) in faces:
            # Draw face rectangle with gradient effect
            cv2.rectangle(frame, (x-2, y-2), (x+w+2, y+h+2), (0, 255, 0), 3)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 200, 0), 1)
            
            # Region of interest for eyes and smile
            roi_gray = gray_frame[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
            # Detect eyes
            eyes = self.eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(20, 20)
            )
            
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
                cv2.circle(roi_color, (ex + ew//2, ey + eh//2), 5, (255, 255, 255), -1)
            
            # Detect smile (only in lower half of face)
            smile_roi = roi_gray[int(h*0.5):, :]
            smiles = self.smile_cascade.detectMultiScale(
                smile_roi,
                scaleFactor=1.7,
                minNeighbors=15,
                minSize=(20, 20)
            )
            
            # Add labels and info
            label_y = y - 10 if y > 30 else y + h + 25
            cv2.putText(frame, f'Face {len(faces)}', (x, label_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            if len(eyes) >= 2:
                cv2.putText(frame, '👀', (x, label_y - 25), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            
            if len(smiles) > 0:
                cv2.putText(frame, '😊 Smile!', (x, y + h + 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        return faces
    
    def add_ui_overlay(self, frame, faces):
        """Add informational overlay"""
        height, width = frame.shape[:2]
        
        # Semi-transparent overlay for stats
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 120), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        
        # Statistics
        runtime = int(time.time() - self.start_time)
        cv2.putText(frame, f'Faces detected: {len(faces)}', (20, 35), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, f'Total detected: {self.total_faces_detected}', (20, 55), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, f'Runtime: {runtime}s', (20, 75), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Controls info
        cv2.putText(frame, "Controls: 'q'-Quit | 's'-Screenshot | 'r'-Reset", 
                   (20, height-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Frame rate indicator
        fps_color = (0, 255, 0) if len(faces) > 0 else (255, 255, 255)
        cv2.circle(frame, (width-30, 30), 10, fps_color, -1)
    
    def save_screenshot(self, frame):
        """Save screenshot with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.screenshot_dir}/face_detection_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📷 Screenshot saved: {filename}")
    
    def run(self):
        """Main execution loop"""
        print("🚀 Starting Face Detection System...")
        print("=" * 50)
        
        if not self.initialize_camera():
            return
        
        print("\n▶️  Face detection started!")
        print("📋 Instructions:")
        print("   - Press 'q' to quit")
        print("   - Press 's' to take screenshot")
        print("   - Press 'r' to reset counters")
        print("   - Press ESC to exit")
        print("-" * 50)
        
        try:
            while True:
                ret, frame = self.video_cap.read()
                
                if not ret:
                    print("❌ Error: Could not read frame from camera")
                    break
                
                # Flip frame horizontally for mirror effect
                frame = cv2.flip(frame, 1)
                
                # Convert to grayscale for detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                # Apply histogram equalization for better detection
                gray = cv2.equalizeHist(gray)
                
                # Detect faces and features
                faces = self.detect_faces_and_features(frame, gray)
                
                # Update statistics
                if len(faces) > 0:
                    self.total_faces_detected += len(faces)
                
                # Add UI overlay
                self.add_ui_overlay(frame, faces)
                
                # Display the frame
                cv2.imshow('🎯 Advanced Face Detection System', frame)
                
                # Handle key presses
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord('q') or key == 27:  # 'q' or ESC
                    print("👋 Exiting...")
                    break
                elif key == ord('s'):  # Screenshot
                    self.save_screenshot(frame)
                elif key == ord('r'):  # Reset counters
                    self.total_faces_detected = 0
                    self.start_time = time.time()
                    print("🔄 Counters reset")
        
        except KeyboardInterrupt:
            print("\n⚡ Interrupted by user")
        
        except Exception as e:
            print(f"❌ An error occurred: {e}")
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.video_cap:
            self.video_cap.release()
        cv2.destroyAllWindows()
        
        runtime = int(time.time() - self.start_time)
        print(f"\n📊 Session Summary:")
        print(f"   Runtime: {runtime} seconds")
        print(f"   Total faces detected: {self.total_faces_detected}")
        print(f"   Screenshots saved in: {self.screenshot_dir}/")
        print("✅ Resources cleaned up successfully")

# Main execution
if __name__ == "__main__":
    try:
        detector = FaceDetectionSystem()
        detector.run()
    except Exception as e:
        print(f"❌ Failed to start face detection system: {e}")
        print("💡 Make sure you have opencv-python installed: pip install opencv-python")