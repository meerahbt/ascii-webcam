import sys
import cv2
import numpy as np
from config import Config
from video_handler import VideoHandler
from ascii_converter import ASCIIConverter
from arabic_converter import ArabicConverter
from dithering_converter import DitheringConverter
import termios
import tty
import select

def is_key_pressed():
    dr, dw, de = select.select([sys.stdin], [], [], 0)
    return dr != []

def get_key():
    return sys.stdin.read(1)

def preprocess_frame(frame, terminal_size):
    # Get terminal dimensions
    cols, rows = terminal_size
    
    # Calculate dimensions preserving aspect ratio
    frame_height, frame_width = frame.shape[:2]
    terminal_ratio = cols / rows
    frame_ratio = frame_width / frame_height
    
    # In your working version, how exactly were you calculating height and width?
    # Let's see your original ASCIIConverter's resize logic
    
    # For now, using basic scaling
    new_width = cols
    new_height = rows
    
    small_frame = cv2.resize(frame, (new_width, new_height))
    small_frame = cv2.flip(small_frame, 1)
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    return gray

def main():
    config = Config()
    video_handler = VideoHandler()
    ascii_converter = ASCIIConverter()
    dithering_converter = DitheringConverter()
    arabic_converter = ArabicConverter()
    
    current_mode = "ascii"
    
    if not video_handler.start_capture(config.DEFAULT_DEVICE_ID):
        print("Error: Could not open video capture device")
        return
    
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        
        print("Starting video capture...")
        print("\nControls:")
        print("  'a' - ASCII mode")
        print("  'd' - Floyd-Steinberg dithering mode")
        print("  'o' - Ordered dithering mode")
        print("  'r' - Arabic mode")  # New control
        print("  'q' - Quit")
        
        while True:
            ret, frame = video_handler.read_frame()
            if not ret:
                print("Failed to grab frame")
                break
            
            # Get terminal size for each frame
            terminal_size = config.get_terminal_size()
            
            # Process frame
            processed_frame = preprocess_frame(frame, terminal_size)
            
            # Convert based on mode
            if current_mode == "ascii":
                converted_frame = ascii_converter.convert_to_blocks(processed_frame)
            elif current_mode == "dither":
                converted_frame = dithering_converter.convert_to_dither(processed_frame)
            elif current_mode == "arabic":  # New mode
                converted_frame = arabic_converter.convert_to_arabic(processed_frame)
            else:  # ordered_dither
                converted_frame = dithering_converter.convert_to_ordered_dither(processed_frame)

            # Update display
            config.clear_screen()
            
            # Get dimensions
            processed_height = len(converted_frame.split('\n'))
            
            sys.stdout.write(config.move_cursor(0, 0))
            sys.stdout.write(converted_frame)
            sys.stdout.write(config.move_cursor(0, processed_height))
            sys.stdout.write(f"Current mode: {current_mode}")
            sys.stdout.flush()
            
            if is_key_pressed():
                key = get_key()
                if key == 'q':
                    print("Quitting...")
                    break
                elif key == 'a':
                    current_mode = "ascii"
                elif key == 'd':
                    current_mode = "dither"
                elif key == 'o':
                    current_mode = "ordered_dither"
                elif key == 'r':
                    current_mode = "arabic"
    
    except (KeyboardInterrupt, Exception) as e:
        print(f"\nProgram interrupted: {str(e)}")
    
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        print("Cleaning up...")
        video_handler.release()

if __name__ == "__main__":
    main()