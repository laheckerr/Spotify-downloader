import ffmpeg
import os

ffmpeg_executable = "C:\Users\User.DESKTOP-J0NR9D8\Desktop\ffmpeg\ffmpeg.exe"  # Replace this with the full path to your ffmpeg executable

input_folder = input("enter path to the folder with mp3 files: ")
output_folder = input("enter path to the output folder: ")

def convert(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, acodec='aac', strict='experimental')
        .run(overwrite_output=True, cmd=ffmpeg_executable)  # Specify the ffmpeg executable path
    )

def batch_convert(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp3'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.m4a')
            convert(input_file, output_file)

def main():
    batch_convert(input_folder, output_folder)

if __name__ == "__main__":
    main()

