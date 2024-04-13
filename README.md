# Video2JPEG
 Video2JPEG is a Python utility that extracts frames from specified intervals of video files and saves them as JPEG images.
 
## Features
- Extract frames from any video supported by OpenCV.
- Define specific start and end times for frame extraction.
- Automatically create directories based on video names for organized storage.
- Customizable prefix for output image filenames.

## Prerequisites
To run Video2JPEG, you'll need:
- Python
- OpenCV library (Install with `pip install opencv-python`)

## Installation
Clone the repository:
```bash
git clone https://github.com/gfdfranco/Video2JPEG.git
cd Video2JPEG
```
## Usage
Run the script by specifying the path to your video, start and end times for frame extraction, and the output folder:
```bash
python video2jpeg.py --video_path "path_to_your_video.mp4" --start_time 10 --end_time 20 --output_folder "output_frames"
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - [Your Email](mailto:email@example.com)

Project Link: [https://github.com/yourusername/Video2JPEG](https://github.com/yourusername/Video2JPEG)

## Acknowledgements
- [OpenCV](https://opencv.org/)
