# Video2JPEG
Video2JPEG is a Python utility that extracts frames from specified intervals of video files and saves them as JPEG images. This tool is especially useful for creating datasets for machine learning or simply extracting moments from videos for analysis.

## Features
- Extract frames from any video file supported by OpenCV.
- Automatically calculate frame intervals based on specified time intervals.
- Automatically create directories based on video names for organized storage.
- Customizable prefix for output image filenames.

## Prerequisites
To run Video2JPEG, you'll need:
- Python
- OpenCV library

Install OpenCV using pip:
```bash
pip install opencv-python
```

## Installation
Clone the repository:
```bash
git clone https://github.com/gfdfranco/Video2JPEG.git
cd Video2JPEG
```
## Usage
Run the script by specifying the path to your video, start and end times for frame extraction, and the output folder:
```bash
python video2jpeg.py --video "path_to_your_video.mp4" --interval 2 --prefix "image"
```

## Contributing
Contributions are welcome!

## License
Distributed under the MIT License.
