import cv2
import os
import argparse


def extract_frames(video_path, interval, image_prefix):
    """
    Extract frames from the specified video at given intervals and save them
    with a specified prefix.

    Parameters:
    video_path (str): The full path to the video file.
    interval (float): Time interval in seconds between frames to capture.
    image_prefix (str): Prefix for naming the extracted images.
    """
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = f"{video_name}_images"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)

    current_frame = 0
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if current_frame % frame_interval == 0:
                frame_name = os.path.join(
                    output_folder,
                    f"{image_prefix}_{video_name}_frame_{frame_count}.jpg"
                )
                cv2.imwrite(frame_name, frame)
                print(f"Extracted {frame_name}")
                frame_count += 1
            current_frame += 1
        else:
            break

    cap.release()
    print("Finished extracting frames.")


def main():
    """
    Main function to parse arguments and call the frame extraction function.
    """
    parser = argparse.ArgumentParser(
        description="Extract frames from video at regular intervals.")
    parser.add_argument("--video", type=str, required=True,
                        help="Path to the input video file.")
    parser.add_argument("--interval", type=float, required=True,
                        help="Interval in seconds between frames to capture.")
    parser.add_argument("--prefix", type=str, required=True,
                        help="Prefix for the output image files.")

    args = parser.parse_args()

    extract_frames(args.video, args.interval, args.prefix)


if __name__ == "__main__":
    main()
