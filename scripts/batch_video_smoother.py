import os
import argparse

from video_smoother import VideoSmoother

# 定义 OpenCV 支持的视频文件格式列表
SUPPORTED_FORMATS = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']

# 解析命令行参数
parser = argparse.ArgumentParser(
    description='此脚本用于批量处理视频文件，对指定目录下支持的视频文件进行处理，可选择是否包含子目录。处理后的视频文件名会在原文件名后添加 .out 后缀。',
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument('directory', type=str, nargs='?', default='.',
                    help='要遍历的文件路径，默认为当前目录。\n示例: /path/to/your/videos')
parser.add_argument('--include-subdirs', action='store_true',
                    help='是否包含子目录。若指定此参数，则会递归处理指定目录及其所有子目录下的支持格式文件。\n示例: --include-subdirs')
parser.add_argument('--delete-original', action='store_true',
                    help='是否在处理完成后删除原始视频文件。若指定此参数，则处理完成后会删除原始文件。\n示例: --delete-original')
args = parser.parse_args()

# 获取命令行参数
directory = args.directory
include_subdirs = args.include_subdirs
delete_original = args.delete_original

# 获取所有支持格式的文件
video_files = []
if include_subdirs:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in SUPPORTED_FORMATS:
                video_files.append(os.path.join(root, file))
else:
    for file in os.listdir(directory):
        file_ext = os.path.splitext(file)[1].lower()
        if file_ext in SUPPORTED_FORMATS and os.path.isfile(os.path.join(directory, file)):
            video_files.append(os.path.join(directory, file))

total = len(video_files)

# 遍历所有支持格式的文件
for index, input_video_path in enumerate(video_files, start=1):
    # 生成输出文件名
    output_video_path = os.path.splitext(input_video_path)[0] + '.out.mp4'

    # 初始化裁剪参数
    crop_x = 0
    crop_y = 250
    crop_width = 886
    crop_height = 1300
    still_time_threshold = 1

    # 生成进度条描述信息
    file_name = os.path.basename(input_video_path)
    progress_desc = f"[{index}/{total}] {file_name}"

    # 初始化 VideoSmoother 实例并设置 progress_desc 参数
    video_smoother = VideoSmoother(
        input_video_path, 
        output_video_path, 
        still_time_threshold=still_time_threshold, 
        crop=True, 
        crop_x=crop_x, 
        crop_y=crop_y, 
        crop_width=crop_width, 
        crop_height=crop_height,
        progress_desc=progress_desc
    )

    # 处理视频
    video_smoother.process_video()

    # 如果设置了删除原始文件，则删除
    if delete_original:
        try:
            os.remove(input_video_path)
            print(f"已删除原始文件: {input_video_path}")
        except Exception as e:
            print(f"删除文件 {input_video_path} 时出错: {e}")