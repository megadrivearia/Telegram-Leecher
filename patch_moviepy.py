"""
This script fixes MoviePy SyntaxWarnings (Python 3.12)
so you don't need to edit site-packages manually.
"""

import os

# File paths
ffmpeg_reader = "/usr/local/lib/python3.12/dist-packages/moviepy/video/io/ffmpeg_reader.py"
sliders = "/usr/local/lib/python3.12/dist-packages/moviepy/video/io/sliders.py"
config = "/usr/local/lib/python3.12/dist-packages/moviepy/config_defaults.py"

def patch_ffmpeg_reader():
    if os.path.exists(ffmpeg_reader):
        with open(ffmpeg_reader, "r") as f:
            code = f.read()
        code = code.replace("re.search('\\d+x\\d+'", "re.search(r'\\d+x\\d+'")
        code = code.replace("re.search('\\d+$'", "re.search(r'\\d+$'")
        with open(ffmpeg_reader, "w") as f:
            f.write(code)
        print("✅ Patched ffmpeg_reader.py")

def patch_sliders():
    if os.path.exists(sliders):
        with open(sliders, "r") as f:
            code = f.read()
        code = code.replace("if event.key is 'enter'", "if event.key == 'enter'")
        with open(sliders, "w") as f:
            f.write(code)
        print("✅ Patched sliders.py")

def patch_config():
    if os.path.exists(config):
        with open(config, "r") as f:
            code = f.read()
        code = code.replace(
            r"C:\Program Files\ImageMagick-6.8.8-Q16\magick.exe",
            r"C:\\Program Files\\ImageMagick-6.8.8-Q16\\magick.exe"
        )
        with open(config, "w") as f:
            f.write(code)
        print("✅ Patched config_defaults.py")

if __name__ == "__main__":
    patch_ffmpeg_reader()
    patch_sliders()
    patch_config()
    print("🎉 All MoviePy patches applied successfully")
