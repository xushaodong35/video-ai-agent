import subprocess
import json
import os

VIDEO_INPUT = "input.mp4"

SCENES_FILE = "scenes.json"
STORYBOARD_FILE = "storyboard.json"
BLENDER_SCRIPT = "render.py"


def run_step1_extract():
    print("Step1: Extract scenes")
    os.system(f"python pipelines/video_to_scene.py {VIDEO_INPUT}")


def run_step2_storyboard():
    print("Step2: Build storyboard (AI analysis)")
    # 这里未来可以接 OpenAI / Codex API
    os.system("echo 'AI storyboard step placeholder'")


def run_step3_generate_blender():
    print("Step3: Generate Blender script")
    os.system("echo 'Blender script generated placeholder'")


def run_step4_render():
    print("Step4: Render video in Blender")
    # Blender执行命令（关键）
    os.system("blender -b scene.blend -P render.py")


def main():
    print("=== FULL PIPELINE START ===")

    run_step1_extract()
    run_step2_storyboard()
    run_step3_generate_blender()
    run_step4_render()

    print("=== DONE: OUTPUT VIDEO GENERATED ===")


if __name__ == "__main__":
    main()
