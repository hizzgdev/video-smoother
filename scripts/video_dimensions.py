import cv2

def get_video_dimensions(input_path):
    """
    获取视频的宽度和高度

    :param input_path: 输入视频的文件路径
    :return: 视频的宽度和高度
    """
    # 打开输入视频文件
    cap = cv2.VideoCapture(input_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error opening video file")
        return None, None

    # 获取视频的宽度和高度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 释放资源
    cap.release()

    return width, height

if __name__ == "__main__":
    # 使用示例
    input_video_path = 'test_input_video.mp4'
    width, height = get_video_dimensions(input_video_path)
    if width is not None and height is not None:
        print(f"视频的宽度: {width} 像素")
        print(f"视频的高度: {height} 像素")
