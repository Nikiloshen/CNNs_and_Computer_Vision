# CNNs and Computer Vision

This repository contains two interrelated projects utilizing Convolutional Neural Networks (CNNs) for computer vision tasks:

1. **PoseEstimation Project** - A deep learning project designed to detect human poses using computer vision techniques.
2. **AiTrainerProject** - A real-time AI-based trainer that identifies working muscles during exercises and analyzes movement dynamics. The project builds on the PoseEstimation Project's functionality for precise muscle detection and movement evaluation.

## Projects Overview

### 1. PoseEstimation Project
This project focuses on estimating human poses from video or image input using a CNN-based model. Key functionalities include:

- Detecting key points of the human body (e.g., joints).
- Tracking body movements and identifying pose changes.
- Providing real-time feedback on body positions.

The PoseEstimation Project serves as the foundational tool for the **AiTrainerProject**, offering pose detection capabilities that are crucial for analyzing physical activity.

### 2. AiTrainerProject
The **AiTrainerProject** uses the pose estimation functionality to create an AI trainer that tracks which muscles are active during exercises. Core features include:

- **Real-Time Muscle Detection**: Identifies which muscles are engaged during physical exercises.
- **Exercise Analysis**: Evaluates form, posture, and movement to provide insights on exercise effectiveness.
- **Feedback Mechanism**: Provides real-time guidance to improve exercise performance by analyzing body movements.

The AiTrainerProject integrates the functions from the PoseEstimation Project to deliver an accurate, real-time AI trainer that can be used in various fitness applications.

## Dependencies

Both projects require the following libraries and frameworks:

- TensorFlow / PyTorch (for deep learning and CNN-based models)
- OpenCV (for image processing)
- NumPy (for numerical operations)
- Other dependencies can be found in `requirements.txt`.

## Usage

### PoseEstimation Project

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CNNs-and-Computer-Vision.git
    ```
2. Navigate to the `PoseEstimation` folder and run the pose estimation model on a sample video or image:
    ```bash
    python pose_estimation.py --input your_input_video.mp4
    ```

### AiTrainerProject

1. First, ensure the **PoseEstimation Project** is properly set up.
2. Navigate to the `AiTrainerProject` folder and start real-time analysis:
    ```bash
    python ai_trainer.py --input your_live_video_feed
    ```

The AI Trainer will provide feedback on which muscles are engaged and offer real-time guidance.
