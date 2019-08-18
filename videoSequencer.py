import cv2
import os


def get_videos(vid_dir):
    videos = []
    vid_path = ''
    for file in os.listdir(vid_dir):
        filename = os.fsdecode(file).replace(' ', '')
        vid_path = os.path.join(vid_dir, filename)
        videos.append({
            'vid_name': filename.split('.')[0],
            'vid_path': vid_path
        })
    return videos

def extract_frames(videos, output_dir):
    first_frame = None
    last_frame = None
    for video in videos:
        vidcap = cv2.VideoCapture(video['vid_path'])
        success, first_frame = vidcap.read()
        frame_count = vidcap.get(7)
        vidcap.set(1, frame_count - 1)
        success, last_frame = vidcap.read()
        cv2.imwrite(os.path.join(output_dir, video['vid_name'] + 'first_frame.jpg'), first_frame)
        cv2.imwrite(os.path.join(output_dir, video['vid_name'] + 'last_frame.jpg'), last_frame)
        vidcap.release()

def main():
    input_dir = os.path.join(os.getcwd(), 'videos')
    output_dir = os.path.join(os.getcwd(), 'frames')

    videos = get_videos(input_dir)
    extract_frames(videos, output_dir)

    print('extraction complete')

if __name__ == '__main__':
    main()