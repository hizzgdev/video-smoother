# Video Dimensions

`video_dimensions.py` 是一个借助 OpenCV 库获取指定视频文件宽度和高度的 Python 脚本。此脚本可帮助开发者快速获取视频的尺寸信息。

## 依赖安装
在运行该脚本前，需要安装 OpenCV 库。可使用以下命令进行安装：
```bash
pip install opencv-python
```

## 脚本功能
`get_video_dimensions` 函数是该脚本的核心，其功能为接收视频文件路径，读取视频并返回视频的宽度和高度。若视频文件无法打开，函数会输出错误信息并返回 `None`。

### 函数签名
```python
def get_video_dimensions(input_path):
```

### 参数说明
| 参数名     | 类型   | 描述                 |
|------------|--------|----------------------|
| `input_path` | 字符串 | 输入视频的文件路径 |

### 返回值
- 若视频成功打开，返回一个包含视频宽度和高度的元组 `(width, height)`。
- 若视频打开失败，返回 `(None, None)`。

## 使用方法

### 调用函数
你可以在其他 Python 脚本里导入并调用 `get_video_dimensions` 函数，示例如下：
```python
from video_dimensions import get_video_dimensions

video_path = 'your_video.mp4'
width, height = get_video_dimensions(video_path)
if width and height:
    print(f"视频宽度: {width} 像素")
    print(f"视频高度: {height} 像素")
else:
    print("未能获取视频尺寸信息。")
```

### 直接运行脚本
`video_dimensions.py` 脚本自带使用示例，你可直接在终端运行：
```bash
python /<your-path>/video-smoother/scripts/video_dimensions.py
```
运行前，请确保 `test_input_video.mp4` 文件存在，或者修改脚本里的 `input_video_path` 变量为实际的视频文件路径。

## 注意事项
- 请保证输入的视频文件路径正确，且文件存在。
- 若视频文件损坏或者格式不被 OpenCV 支持，函数将无法打开视频并输出错误信息。 