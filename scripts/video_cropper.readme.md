# Video Cropper

`video_cropper.py` 是一个用于将视频剪裁到指定大小的 Python 脚本。它使用 OpenCV 库来处理视频，并使用 `tqdm` 库显示处理进度。

## 依赖安装
在运行此脚本之前，需要安装必要的 Python 库。可以使用以下命令进行安装：
```bash
pip install opencv-python tqdm
```

## 脚本功能
`crop_video` 函数负责将输入视频剪裁到指定的区域，并将结果保存到输出文件中。函数的参数如下：
- `input_path`: 输入视频的文件路径。
- `output_path`: 输出视频的文件路径。
- `x`: 剪裁区域左上角的 x 坐标。
- `y`: 剪裁区域左上角的 y 坐标。
- `width`: 剪裁区域的宽度。
- `height`: 剪裁区域的高度。

## 使用方法
### 直接修改脚本
可以直接修改脚本中的 `if __name__ == "__main__"` 部分来指定输入输出文件路径和剪裁区域。示例如下：
```python
if __name__ == "__main__":
    # 使用示例
    input_video_path = 'test_input_video.mp4'
    output_video_path = 'test_output_video.mp4'
    # 假设从 (100, 100) 位置开始，剪裁宽度为 300，高度为 200 的区域
    x = 100
    y = 100
    width = 300
    height = 200

    crop_video(input_video_path, output_video_path, x, y, width, height)
```

### 运行脚本
在终端中运行以下命令来执行视频剪裁操作：
```bash
python /<your-path>/video-smoother/scripts/video_cropper.py
```

## 注意事项
- 请确保输入视频文件存在，并且路径正确。
- 剪裁区域的坐标和尺寸必须在视频帧的有效范围内，否则可能会导致剪裁结果不符合预期。
- 输出文件的格式由 `cv2.VideoWriter` 中的 `fourcc` 参数决定，当前设置为 `mp4v`，即输出 MP4 格式的视频。
- 该脚本生成的视频没有声音 ，因为 OpenCV 主要处理视频的图像帧，不处理音频数据。如果需要保留音频，可能需要使用其他工具或库来处理。