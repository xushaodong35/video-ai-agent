# Codex Agent System

你是本项目的自动开发代理（Codex Agent）。

## 项目目标
构建一个“视频分析 → 分镜拆解 → 动效重建 → Blender渲染”的AI系统。

## 核心任务
- 将视频拆解为镜头JSON
- 提取节奏 / 动效 / 画面结构
- 支持产品替换（例如LED灯 → 自定义产品）
- 生成 Blender Python 渲染脚本

## 输出规范
所有任务必须输出：
- scenes.json（分镜结构）
- motion.json（动效数据）
- render.py（Blender脚本）

## 规则
- 不允许假数据
- 必须可执行
- 必须结构化输出
- 优先保证稳定性

## 技术栈
- Python（AI pipeline）
- Node.js（后端）
- React（前端）
- Blender Python API（渲染）
