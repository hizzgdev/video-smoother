# Video Smoother 脚本目录文档

本目录包含多个用于视频处理的 Python 脚本，以下是对各个脚本及其功能的简要介绍，点击脚本名称可查看对应的详细文档。

## 脚本列表

### 1. `video_smoother.py`
- **功能**：对单个视频文件进行处理，可根据相邻帧之间的差异阈值，跳过静止帧，实现视频平滑处理。同时支持视频裁剪功能。
- **文档**：[VideoSmoother 脚本说明文档](video_smoother.readme.md)

### 2. `batch_video_smoother.py`
- **功能**：该脚本主要用于批量处理视频文件。它能遍历指定目录下所有支持格式的视频文件，并对其进行处理。同时支持递归处理指定目录及其子目录下的视频文件，处理完成后还可选择删除原始视频文件。
- **文档**：[Batch Video Smoother 脚本说明文档](batch_video_smoother.readme.md)

### 3. `video_cropper.py`
- **功能**：将输入视频剪裁到指定的区域，并将结果保存到输出文件中。使用 OpenCV 库处理视频，`tqdm` 库显示处理进度。需要注意的是，生成的视频没有声音。
- **文档**：[Video Cropper 文档](video_cropper.readme.md)

### 4. `video_dimensions.py`
- **功能**：借助 OpenCV 库获取指定视频文件的宽度和高度。若视频文件无法打开，会输出错误信息并返回 `None`。
- **文档**：[Video Dimensions 脚本文档](video_dimensions.readme.md)

## 依赖安装
不同脚本所需的依赖库有所不同，具体安装命令可查看对应脚本的文档。以下是各脚本依赖安装的汇总：
- **`batch_video_smoother.py` 和 `video_smoother.py`**：
  ```bash
  pip install opencv-python numpy tqdm
  ```
- **`video_cropper.py`**：
  ```bash
  pip install opencv-python tqdm
  ```
- **`video_dimensions.py`**：
  ```bash
  pip install opencv-python
  ```