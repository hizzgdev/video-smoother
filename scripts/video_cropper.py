import cv2
from tqdm import tqdm
import time

def crop_video(input_path, output_path, x, y, width, height):
    """
    剪裁视频到指定大小

    :param input_path: 输入视频的文件路径
    :param output_path: 输出视频的文件路径
    :param x: 剪裁区域左上角的 x 坐标
    :param y: 剪裁区域左上角的 y 坐标
    :param width: 剪裁区域的宽度
    :param height: 剪裁区域的高度
    """
    # 记录开始时间
    start_time = time.time()

    # 打开输入视频文件
    cap = cv2.VideoCapture(input_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error opening video file")
        return

    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 获取视频的帧率
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 创建输出视频文件
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 创建进度条
    progress_bar = tqdm(total=total_frames, desc="Cropping frames", unit="frame")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 剪裁帧
        cropped_frame = frame[y:y + height, x:x + width]

        # 写入剪裁后的帧
        out.write(cropped_frame)

        # 更新进度条
        progress_bar.update(1)

    # 关闭进度条
    progress_bar.close()

    # 释放资源
    cap.release()
    out.release()

    # 记录结束时间并计算耗时
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"视频裁剪耗时: {elapsed_time:.2f} 秒")

if __name__ == "__main__":
    # 使用示例
    input_video_path = 'test_input_video.1.mp4'
    output_video_path = 'test_output_video.2.mp4'
    # 假设从 (100, 100) 位置开始，剪裁宽度为 300，高度为 200 的区域
    x = 0
    y = 250
    width = 886
    height = 1300

    crop_video(input_video_path, output_video_path, x, y, width, height)