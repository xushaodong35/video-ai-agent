import cv2
import json
import os

def extract_frames(video_path, sample_rate=1):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    frames = []
    frame_id = 0
    success = True

    while success:
        success, frame = cap.read()

        if frame_id % int(fps * sample_rate) == 0:
            if success:
                frames.append({
                    "frame_id": frame_id,
                    "time": frame_id / fps
                })

        frame_id += 1

    cap.release()
    return frames


def build_scenes(frames):
    scenes = []

    for i in range(len(frames) - 1):
        scenes.append({
            "id": i,
            "start": frames[i]["time"],
            "end": frames[i+1]["time"],
            "description": "auto detected scene (placeholder)",
            "motion": "unknown"
        })

    return scenes


def main(video_path, output_path="scenes.json"):
    frames = extract_frames(video_path)
    scenes = build_scenes(frames)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(scenes, f, indent=2, ensure_ascii=False)

    print("Scene file generated:", output_path)


if __name__ == "__main__":
    # 示例
    video_path = "input.mp4"
    main(video_path)
