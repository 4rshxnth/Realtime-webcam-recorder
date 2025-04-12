# 🎥 OpenCV Video Recorder with Python

A lightweight, real-time webcam video recorder built using Python and OpenCV. This tool captures video from your default webcam and saves it as an `.avi` file with live preview support.

---

## 📌 About

**This project is ideal for beginners, developers, or researchers looking to:**

- Capture webcam feeds for ML/DL dataset generation
- Record sessions for computer vision experiments
- Build simple video tools or surveillance utilities

The video is encoded using the **XVID** codec and saved at 640x480 resolution, 20 FPS.

---

## ⚙️ Installation

**1. Clone the Repository**

```bash
git clone https://github.com/your-username/opencv-video-recorder-py.git
cd opencv-video-recorder-py
```


**2. Set Up Python Environment**

Make sure **Python 3.x** is installed. Then install **OpenCV** :

```bash
pip install opencv-python
```
---
## 🚀 How to Use
**Run the script:**
```bash
python record_video.py
```

A window will pop up showing your webcam feed in real-time.

Press `'s'` to stop recording at any time.

The video will be saved as `output.avi` in the current directory.

---

## 📂 Output

**After successful execution, the following file is generated:**

`output.avi` – The recorded webcam video

This file can be played using any media player like VLC, or processed further using Python/OpenCV tools.

---

## 🧩 Features

🎥 Real-time webcam capture

💾 Saves video locally as .avi

⚡ Efficient and fast with minimal dependencies

🖥️ Live preview window

⌨️ Simple hotkey interaction ('s' to stop)

---

## 🔧 Customization Tips

**You can tweak these in `record_video.py`:**

Resolution → (640, 480) → change for HD or low-res

FPS → 20.0 → increase/decrease based on your system's capacity

Codec → 'XVID' → switch to 'MJPG' or 'MP4V' for different formats

---

## 📜 License

This project is released under the MIT License. 

Feel free to use, modify, and share.

---

## 🙋 Support & Contributions

Pull requests, issues, and forks are welcome.

If you find this useful, give the repo a ⭐ and share your feedback.
