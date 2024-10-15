# Hand Detection Projects

This repository contains several projects that utilize hand detection techniques for various interactive applications. All projects are built using functions from the **PoseEstimation Project**, providing a robust framework for hand tracking and gesture recognition using mediapipe library.

## Projects Overview

### 1. Hand Detecting Project
A basic project focused on detecting hands in video or image streams. The main features include:

- Detecting hand landmarks in real-time.
- Tracking hand movements for further processing in other projects.

### 2. VolumeHandController Project
This project allows you to control your computer's volume using hand gestures. Key functionalities include:

- Increasing or decreasing the volume by moving your hand up or down.
- Real-time tracking of hand gestures for seamless control.
- Integration with your system’s volume control.

### 3. FingerCountingProject
A project that counts the number of fingers held up and provides visual feedback. Core features include:

- Real-time counting of fingers raised.
- A visual representation of the detected fingers.
- Can be used in various applications that require finger tracking for user input.

### 4. VirtualPainter Project
An interactive painting tool that allows you to draw on the screen using your fingers. Key features include:

- **Drawing with Fingers**: Use your index finger to paint on the video feed.
- **Color Switching**: Raise your middle and index fingers together to change the paint color.
- **Eraser Tool**: Use the rubber tool by activating a specific gesture (e.g., a fist).
- **Real-Time Interaction**: Draw in real-time with seamless hand gesture recognition.

## Dependencies

All projects in this folder share similar dependencies:

- TensorFlow / PyTorch (for deep learning models)
- OpenCV (for real-time video processing)
- NumPy (for numerical computations)
- Other dependencies can be found in `requirements.txt`.

## Usage

### Hand Detecting Project

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Hand_Detection.git
    ```
2. Navigate to the `Hand_Detecting` folder and run the detection script:
    ```bash
    python hand_detect.py --input your_input_video.mp4
    ```

### VolumeHandController Project

1. Ensure the **Hand Detecting Project** is set up and functioning.
2. Navigate to the `VolumeHandController` folder and control your system volume using hand gestures:
    ```bash
    python volume_controller.py --input your_live_video_feed
    ```

### FingerCountingProject

1. Make sure the **Hand Detecting Project** is properly set up.
2. Navigate to the `FingerCountingProject` folder and start finger counting:
    ```bash
    python finger_counter.py --input your_live_video_feed
    ```

### VirtualPainter Project

1. Ensure the **Hand Detecting Project** is working correctly.
2. Navigate to the `VirtualPainter` folder and begin painting:
    ```bash
    python virtual_painter.py --input your_live_video_feed
    ```

You can change colors by raising your middle and index fingers and switch to the rubber tool when necessary.
