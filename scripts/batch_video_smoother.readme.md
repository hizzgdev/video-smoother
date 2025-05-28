# Batch Video Smoother 脚本说明文档

## 概述
`batch_video_smoother.py` 是一个用于批量处理视频文件的 Python 脚本。它会遍历指定目录下的视频文件，利用 `video_smoother.py` 脚本中的 `VideoSmoother` 类对视频进行平滑处理，同时支持对视频进行裁剪操作。处理完成后的视频文件名会在原文件名后添加 `.out` 后缀。

## 依赖安装
在运行此脚本之前，需要安装必要的 Python 库，可以使用以下命令进行安装：
```bash
pip install opencv-python numpy tqdm
```
同时，要确保 `video_smoother.py` 脚本存在于项目中，因为 `batch_video_smoother.py` 会引用该脚本中的 `VideoSmoother` 类。

## 脚本功能
该脚本主要实现以下功能：
1. **批量处理视频**：遍历指定目录下的所有支持格式的视频文件，并对其进行处理。
2. **递归处理**：支持递归处理指定目录及其所有子目录下的视频文件。
3. **删除原始文件**：处理完成后，可选择删除原始视频文件。

## 命令行参数
| 参数名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `directory` | 字符串 | `.` | 要遍历的文件路径，默认为当前目录。示例：`/path/to/your/videos` |
| `--include-subdirs` | 无 | 无 | 是否包含子目录。若指定此参数，则会递归处理指定目录及其所有子目录下的支持格式文件。示例：`--include-subdirs` |
| `--delete-original` | 无 | 无 | 是否在处理完成后删除原始视频文件。若指定此参数，则处理完成后会删除原始文件。示例：`--delete-original` |

## 引用说明
`batch_video_smoother.py` 脚本引用了 `video_smoother.py` 中的 `VideoSmoother` 类。`VideoSmoother` 类封装了视频平滑处理的主要逻辑，其初始化方法的参数及主要方法的详细介绍可参考 [video_smoother.readme.md](video_smoother.readme.md)。

## 支持的视频格式
该脚本支持以下视频格式：
- `.mp4`
- `.mov`
- `.avi`
- `.mkv`
- `.flv`
- `.wmv`

## 使用方法
### 基本使用
在终端中运行以下命令，处理当前目录下的视频文件：
```bash
python /<your-path>/video-smoother/scripts/batch_video_smoother.py
```

### 处理指定目录下的视频文件
```bash
python /<your-path>/video-smoother/scripts/batch_video_smoother.py /path/to/your/videos
```

### 包含子目录
```bash
python /<your-path>/video-smoother/scripts/batch_video_smoother.py /path/to/your/videos --include-subdirs
```

### 处理完成后删除原始文件
```bash
python /<your-path>/video-smoother/scripts/batch_video_smoother.py /path/to/your/videos --delete-original
```

## 注意事项
- 请确保输入视频文件存在且路径正确，输出路径有写入权限。
- 裁剪参数 `crop_x`、`crop_y`、`crop_width` 和 `crop_height` 在脚本中已预设，如需修改可直接编辑 `batch_video_smoother.py` 文件。
- 调整 `still_time_threshold` 参数时，需要根据视频内容进行多次测试，以达到最佳的平滑效果。
- 该脚本生成的视频没有声音，因为 `VideoSmoother` 类主要处理视频的图像帧，不处理音频数据。如果需要保留音频，可能需要使用其他工具或库来处理。
```