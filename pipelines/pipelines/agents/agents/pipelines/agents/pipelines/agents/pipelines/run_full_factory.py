import os
import json

from pipelines.video_to_scene import main as extract_scenes
from agents.vision_agent import analyze_video
from agents.product_swap_engine import ProductSwapEngine


INPUT_VIDEO = "input.mp4"
TARGET_PRODUCT = "your_product.obj"


def step1(video):
    print("🚀 Step1: Scene Extraction")
    extract_scenes(video)

    with open("scenes.json", "r", encoding="utf-8") as f:
        return json.load(f)


def step2():
    print("🚀 Step2: Vision AI Analysis")

    dummy_frames = ["frame1", "frame2", "frame3"]
    return analyze_video(dummy_frames)


def step3(vision_data):
    print("🚀 Step3: Product Swap Engine")

    engine = ProductSwapEngine()

    original = engine.detect_product(vision_data)
    plan = engine.create_swap_plan(original, "NEW_PRODUCT")

    engine.export(plan)
    return plan


def step4():
    print("🚀 Step4: Blender Generation")

    os.system("echo 'generate blender script here' > render.py")


def step5():
    print("🚀 Step5: Render Video")

    os.system("blender -b scene.blend -P render.py")


def run():
    print("===================================")
    print("🏭 AI AD FACTORY V3 STARTING")
    print("===================================")

    scenes = step1(INPUT_VIDEO)
    vision = step2()
    swap = step3(vision)

    step4()
    step5()

    print("===================================")
    print("🎬 DONE: NEW AD VIDEO GENERATED")
    print("===================================")


if __name__ == "__main__":
    run()
