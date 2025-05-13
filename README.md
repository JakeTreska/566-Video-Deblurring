🚀 Real-Time Video Deblurring with Deep Learning

This project explores the development of real-time video deblurring models using custom lightweight architectures inspired by NAFNet, with the ultimate goal of deployment in edge-computing environments like drones and surveillance systems.

📌 Overview

Traditional state-of-the-art (SOTA) deblurring models such as NAFNet achieve excellent results, but their massive size makes them impractical for real-time applications. Our solution: build significantly smaller models that trade off only a modest amount of accuracy for massive gains in inference speed.

🧠 Model Summary

| Model      | Parameters | FPS (GPU) | SSIM Improvement | Laplacian Score Increase |
|------------|------------|-----------|------------------|---------------------------|
| Small      | 1.7M       | 100+ FPS  | +1–3%            | +31%                      |
| Medium     | 5M         | 35+ FPS   | +1–3%            | +17.3%                    |
| Large      | 14M        | 20+ FPS   | +1–3%            | +11.4%                    |
| NAFNet     | 68.7M      | 1–2 FPS   | +14.05%          | +189%                     |


📌 SSIM = Structural Similarity Index
📌 Laplacian = Edge sharpness metric used for visual fidelity evaluation
Although the NAFNet model achieves significantly higher SSIM and Laplacian scores, it is too computationally expensive for real-time deployment, running at just 1–2 FPS. In contrast, our small model runs at over 100 FPS on most GPUs, making it ideal for live video processing.

🎯 Key Highlights

Architecture: All models use a multi-scale residual design (inspired by NAFNet) and vary only in the number of residual blocks.
Losses: Combined SSIM and L1 loss to balance perceptual quality and pixel-level fidelity.
Preprocessing: Used Sobel filters and image normalization for noise suppression and edge enhancement.


🖼️ Visual Results

Figure: Canny Filtered Outputs (Left → Right):

Blurred Input → Small Model → Medium → Large → Ground Truth
Noticeable improvement in edge density and sharpness across all custom models.


🚁 Drone Footage Fine-Tuning

To evaluate real-world performance, we fine-tuned the smallest model on aerial drone footage (VisDrone dataset):

Metric	Improvement
SSIM	~20% ↑
Laplacian Score	Significant edge recovery shown visually
Visual Example Layout:

Row 1: Blurred drone images
Row 2: Output from fine-tuned model
Row 3: Ground truth sharp images
These results demonstrate the model’s ability to generalize to real-world motion blur, particularly in fast-moving aerial scenes.


🔭 Future Work

Incorporate selective deblurring (e.g., use Laplacian variance to skip already-sharp frames).
Explore transformer-based models for global context learning.
Add an object detection module (e.g., YOLO) post-deblurring for downstream tasks.
Expand training with real blurry/clear datasets like GoPro or REDS.


👥 Team
Jake Treska
Anurag Bapat
Swaminathan Chellappa
Yongchen Lin
Monika Yadav
