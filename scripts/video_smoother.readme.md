# VideoSmoother 脚本说明文档

## 概述
`video_smoother.py` 是一个基于 Python 编写的视频处理脚本，借助 OpenCV 库实现视频平滑处理功能。其核心原理是通过比较相邻视频帧之间的差异，跳过差异小于设定阈值的连续帧，以此减少视频中的静止画面，使视频更加流畅。同时，该脚本还支持对视频进行裁剪操作。

## 依赖安装
在运行此脚本之前，需要安装必要的 Python 库，可以使用以下命令进行安装：
```bash
pip install opencv-python numpy tqdm
```

## 类与方法介绍

### `VideoSmoother` 类
该类封装了视频平滑处理的主要逻辑，以下是其初始化方法及各个参数的详细介绍：

```python
class VideoSmoother:
    def __init__(self, input_path, output_path, threshold=300000, still_time_threshold=1.0, crop=False, crop_x=0, crop_y=0, crop_width=None, crop_height=None, progress_desc=None):
```

#### 参数说明
| 参数名               | 类型    | 默认值      | 描述                                                                                                                         |
|----------------------|---------|-------------|------------------------------------------------------------------------------------------------------------------------------|
| `input_path`         | 字符串  | 无          | 输入视频文件的路径，必须提供有效的视频文件路径，如 `'test_input_video.mp4'`。                                                |
| `output_path`        | 字符串  | 无          | 处理后输出视频文件的路径，指定输出视频的保存位置和文件名，如 `'test_output_video.mp4'`。                                      |
| `threshold`          | 整数    | 300000      | 相邻帧差异的阈值，用于判断两帧之间的差异程度。当两帧差异的像素灰度值总和小于该阈值时，认为这两帧为静止帧。值越大，越容易将连续帧视为静止帧。该参数理论最大值为视频帧的像素总数乘以 255，但在实际应用中，通常不需要这么大的值。你可以通过试验不同的 threshold 值，找到最适合你视频的数值。一般来说，较小的 threshold 值会让脚本更敏感，更容易将帧标记为静止帧；较大的值则相反。|
| `still_time_threshold` | 浮点数  | 1.0         | 静止画面的时间阈值（单位：秒）。当连续静止帧的时长超过该阈值时，这些帧将被跳过。例如，设置为 2.0 表示连续静止 2 秒以上的帧会被跳过。 |
| `crop`               | 布尔值  | `False`     | 是否对视频进行裁剪操作。设置为 `True` 时启用裁剪功能，设置为 `False` 则不进行裁剪。                                          |
| `crop_x`             | 整数    | 0           | 裁剪区域左上角的 x 坐标，仅在 `crop` 为 `True` 时有效。                                                                      |
| `crop_y`             | 整数    | 0           | 裁剪区域左上角的 y 坐标，仅在 `crop` 为 `True` 时有效。                                                                      |
| `crop_width`         | 整数或 `None` | `None`    | 裁剪区域的宽度，仅在 `crop` 为 `True` 时有效。若设置为 `None`，则使用原始视频的宽度。                                        |
| `crop_height`        | 整数或 `None` | `None`    | 裁剪区域的高度，仅在 `crop` 为 `True` 时有效。若设置为 `None`，则使用原始视频的高度。                                        |
| `progress_desc`      | 字符串  | `None`      | 进度条的描述信息。若提供该参数，进度条将显示该描述；若为 `None`，则使用输入文件的文件名作为描述。                            |

### 主要方法
- `process_video()`: 处理视频的主方法，调用该方法即可开始视频处理流程，包括打开输入视频、获取视频信息、创建输出视频、处理视频帧等操作。

## 使用方法

### 示例代码
```python
if __name__ == "__main__":
    input_video_path = 'test_input_video.mp4'
    output_video_path = 'test_output_video.mp4'
    crop = True
    crop_x = 0
    crop_y = 0
    crop_width = 100
    crop_height = 100
    video_smoother = VideoSmoother(input_video_path, output_video_path, still_time_threshold=2.0, crop=crop, crop_x=crop_x, crop_y=crop_y, crop_width=crop_width, crop_height=crop_height)
    video_smoother.process_video()
```

### 步骤说明
1. **设置参数**：根据需求设置输入输出视频路径、阈值、裁剪参数等。
2. **创建 `VideoSmoother` 实例**：使用设置好的参数创建 `VideoSmoother` 类的实例。
3. **调用 `process_video()` 方法**：调用实例的 `process_video()` 方法开始处理视频。
4. **查看结果**：处理完成后，在指定的输出路径查看处理后的视频文件。

## 注意事项
- 请确保输入视频文件存在且路径正确，输出路径有写入权限。
- 裁剪参数 `crop_x`、`crop_y`、`crop_width` 和 `crop_height` 需根据视频实际尺寸合理设置，避免超出视频帧范围。
- 调整 `threshold` 和 `still_time_threshold` 参数时，需要根据视频内容进行多次测试，以达到最佳的平滑效果。
- 该脚本生成的视频没有声音 ，因为 OpenCV 主要处理视频的图像帧，不处理音频数据。如果需要保留音频，可能需要使用其他工具或库来处理。