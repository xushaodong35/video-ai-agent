import json
import os

from agents.vision_agent import analyze_video
from pipelines.video_to_scene import main as extract_scenes


INPUT_VIDEO = "input.mp4"


def step1_extract(video):
    print("🟡 Step1: Extract scenes")
    extract_scenes(video)
    with open("scenes.json", "r", encoding="utf-8") as f:
        return json.load(f)


def step2_vision_analysis():
    print("🟡 Step2: AI vision understanding")

    dummy_frames = ["frame1", "frame2", "frame3"]
    from agents.vision_agent import analyze_video

    vision_data = analyze_video(dummy_frames)

    with open("vision.json", "w", encoding="utf-8") as f:
        json.dump(vision_data, f, indent=2, ensure_ascii=False)

    return vision_data


def step3_storyboard_merge(scenes, vision):
    print("🟡 Step3: Merge storyboard + vision")

    merged = {
        "scenes": scenes,
        "vision": vision,
        "product_swap": {
            "from": "LED lamp",
            "to": "YOUR_PRODUCT"
        }
    }

    with open("storyboard_final.json", "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    return merged


def step4_generate_blender_script():
    print("🟡 Step4: Generate Blender script")

    os.system("echo 'Generate Blender render script here' > render.py")


def step5_render():
    print("🟡 Step5: Render video in Blender")

    # 实际项目这里会调用 Blender
    os.system("blender -b scene.blend -P render.py")


def run_pipeline():
    print("🚀 AI AD FACTORY START")

    scenes = step1_extract(INPUT_VIDEO)
    vision = step2_vision_analysis()
    merged = step3_storyboard_merge(scenes, vision)

    step4_generate_blender_script()
    step5_render()

    print("🎬 DONE: AI GENERATED AD VIDEO READY")


if __name__ == "__main__":
    run_pipeline()
