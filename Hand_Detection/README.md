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

- Mediapipe (google's library for detection)
- OpenCV (for real-time video processing)
- NumPy (for numerical computations)
- os (for images used in project)
- ctypes, comtypes, pycaw (for volume controller)
- math (for math operations)
