from flask import Flask, request, jsonify
import os

from pipelines.run_full_factory import run

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/generate_ad", methods=["POST"])
def generate_ad():
    """
    🎬 商业入口：
    上传视频 + 产品 → 自动生成广告
    """

    video = request.files.get("video")
    product = request.form.get("product")

    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    print("Received video:", video_path)
    print("Target product:", product)

    # ===== 核心AI流水线 =====
    result = run(video_path, product)

    return jsonify({
        "status": "success",
        "message": "AI ad generated",
        "output": result
    })


@app.route("/health")
def health():
    return {"status": "ok", "system": "AI Ad Factory V1"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
