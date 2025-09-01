#take image and audio and make video where image is still and audio plays
import subprocess
import os

def create_video():
    # Remove output file if it exists to avoid the overwrite prompt
    if os.path.exists('output.mp4'):
        os.remove('output.mp4')
        
    command = [
        'ffmpeg',
        '-loop', '1',  # Loop the image
        '-i', 'nano-banana-no-bg-2025-08-28T12-42-25.jpg',  # Input image
        '-i', 'रिच_डैड_पुअर_डैड__पैसे_की_सोच_बदलने_वाले_7_सिद्धांत_और_वित्तीय_आज़ादी_का_रास्ता.m4a',  # Input audio file
        '-c:v', 'libx264',  # Video codec
        '-tune', 'stillimage',  # Optimize for still image
        '-c:a', 'aac',  # Audio codec
        '-b:a', '192k',  # Audio bitrate
        '-shortest',  # Match the duration of the audio
        '-pix_fmt', 'yuv420p',  # Pixel format for better compatibility
        'English_emergency_fund_building.mp4'
    ]
    
    try:
        subprocess.run(command, check=True)
        print("Video created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_video()