import subprocess

def create_video():
    command = [
        'ffmpeg',
        '-loop', '1',  # Loop the image
        '-i', 'ChatGPT Image Aug 26, 2025, 10_26_20 AM.png',  # Input image
        '-i', 'Stock_Investing__2025_Guide.mp4',  # Input audio file
        '-c:v', 'libx264',  # Video codec
        '-tune', 'stillimage',  # Optimize for still image
        '-c:a', 'aac',  # Audio codec
        '-b:a', '192k',  # Audio bitrate
        '-shortest',  # Match the duration of the audio
        '-pix_fmt', 'yuv420p',  # Pixel format for better compatibility
        'output.mp4'
    ]
    
    subprocess.run(command, check=True)

if __name__ == "__main__":
    create_video()
