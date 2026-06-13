import json

class ProductSwapEngine:

    def __init__(self):
        self.rules = {
            "LED lamp": {
                "type": "light_source",
                "replace_strategy": "preserve_lighting + replace_mesh"
            }
        }

    def detect_product(self, vision_data):
        """
        从视觉分析中识别原产品
        """
        for scene in vision_data.get("scenes", []):
            product = scene["analysis"].get("product", "")
            if product:
                return product
        return None

    def create_swap_plan(self, original, target_product):
        """
        创建替换方案（核心商业逻辑）
        """
        return {
            "original_product": original,
            "target_product": target_product,
            "strategy": "mesh_replace + lighting_match + camera_lock",
            "constraints": [
                "keep lighting unchanged",
                "keep camera motion identical",
                "replace only object mesh"
            ]
        }

    def export(self, plan, output="product_swap.json"):
        with open(output, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)

        print("Swap plan saved:", output)


if __name__ == "__main__":
    engine = ProductSwapEngine()

    sample_vision = {
        "scenes": [
            {
                "analysis": {
                    "product": "LED lamp"
                }
            }
        ]
    }

    original = engine.detect_product(sample_vision)
    plan = engine.create_swap_plan(original, "YOUR_PRODUCT")

    engine.export(plan)
