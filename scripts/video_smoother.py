import cv2
import numpy as np
from tqdm import tqdm
import os

class VideoSmoother:
    def __init__(self, input_path, output_path, threshold=300000, still_time_threshold=1.0, crop=False, crop_x=0, crop_y=0, crop_width=None, crop_height=None, progress_desc=None):
        self.input_path = input_path
        self.output_path = output_path
        self.threshold = threshold
        self.still_time_threshold = still_time_threshold
        self.crop = crop
        self._crop_x = crop_x
        self._crop_y = crop_y
        self._crop_width = crop_width
        self._crop_height = crop_height
        self._cap = None
        self._out = None
        self._fps = None
        self._total_frames = None
        self._crop_width_final = None
        self._crop_height_final = None
        # 新增参数，用于存储进度条描述信息
        self.progress_desc = progress_desc

    def _open_input_video(self):
        """打开输入视频文件并检查是否成功打开"""
        self._cap = cv2.VideoCapture(self.input_path)
        if not self._cap.isOpened():
            print("Error opening video file")
            return False
        return True

    def _get_video_info(self):
        """获取视频的相关信息，并根据 crop 参数决定是否使用剪裁尺寸"""
        self._total_frames = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self._fps = self._cap.get(cv2.CAP_PROP_FPS)
        original_width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if self.crop:
            if self._crop_width is None:
                self._crop_width = original_width
            if self._crop_height is None:
                self._crop_height = original_height
        else:
            self._crop_width = original_width
            self._crop_height = original_height
            self._crop_x = 0
            self._crop_y = 0

        self._crop_width_final = self._crop_width
        self._crop_height_final = self._crop_height

    def _create_output_video(self):
        """创建输出视频文件"""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._out = cv2.VideoWriter(self.output_path, fourcc, self._fps, (self._crop_width_final, self._crop_height_final))

    def _process_frame(self, frame):
        """根据 crop 参数决定是否剪裁当前帧"""
        if self.crop:
            return frame[self._crop_y:self._crop_y + self._crop_height_final, self._crop_x:self._crop_x + self._crop_width_final]
        return frame

    def _check_frame_diff(self, prev_frame, frame):
        """计算相邻帧之间的差异，并检查是否小于阈值"""
        diff = cv2.absdiff(prev_frame, frame)
        diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff_sum = np.sum(diff_gray)
        return diff_sum <= self.threshold

    def _create_progress_bar(self):
        """创建进度条，优先使用用户提供的描述信息，否则使用输入文件的文件名作为描述信息"""
        if self.progress_desc:
            desc = self.progress_desc
        else:
            file_name = os.path.basename(self.input_path)
            desc = f"Processing {file_name}"
        return tqdm(total=self._total_frames, desc=desc, unit="frame")

    def _close_progress_bar(self, progress_bar):
        """关闭进度条"""
        if progress_bar:
            progress_bar.close()

    def _update_progress_bar(self, progress_bar):
        """更新进度条"""
        if progress_bar:
            progress_bar.update(1)

    def _process_video_frames(self):
        """处理视频帧的主要逻辑"""
        progress_bar = self._create_progress_bar()
        still_frame_threshold = int(self.still_time_threshold * self._fps)

        ret, prev_frame = self._cap.read()
        if not ret:
            print("Error reading first frame")
            self._cap.release()
            return

        prev_frame = self._process_frame(prev_frame)
        still_frame_count = 0
        frames_to_skip = []

        while True:
            ret, frame = self._cap.read()
            if not ret:
                break

            frame = self._process_frame(frame)

            if self._check_frame_diff(prev_frame, frame):
                still_frame_count += 1
                frames_to_skip.append(frame)
            else:
                if still_frame_count < still_frame_threshold:
                    for f in frames_to_skip:
                        self._out.write(f)
                self._out.write(frame)
                still_frame_count = 0
                frames_to_skip = []

            prev_frame = frame
            self._update_progress_bar(progress_bar)

        if still_frame_count < still_frame_threshold:
            for f in frames_to_skip:
                self._out.write(f)

        self._close_progress_bar(progress_bar)

    def process_video(self):
        if not self._open_input_video():
            return

        self._get_video_info()
        self._create_output_video()

        self._process_video_frames()

        self._cap.release()
        self._out.release()


if __name__ == "__main__":
    input_video_path = 'test_input_video.mp4'
    output_video_path = 'test_output_video.mp4'
    crop = False
    crop_x = 0
    crop_y = 0
    crop_width = 100
    crop_height = 100
    video_smoother = VideoSmoother(input_video_path, output_video_path, still_time_threshold=2.0, crop=True, crop_x=crop_x, crop_y=crop_y, crop_width=crop_width, crop_height=crop_height)
    video_smoother.process_video()
