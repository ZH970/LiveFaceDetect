import time
import face_recognition
import cv2
# import matplotlib.pyplot


# 获取系统摄像头数据
def display_camera_stream(camera_id):
    cap = cv2.VideoCapture(camera_id,cv2.CAP_DSHOW)
    if not cap.isOpened():
        print('Error: Cannot open camera.')
        return None

    # 读取一帧图像
    ret, frame = cap.read()

    if not ret:
        print('Error: Cannot read frame.')
        print("Capture failed")
        return None

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    # cv2.namedwindow("Camera", cv2.WINDOW_NORMAL)
    # 开始显示摄像头流
    start_time = time.time()
    while (time.time() - start_time) < 1000: # 10s
        # 读取一帧图像
        ret, frame = cap.read()
        # 缩小图像
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # 将BGR图像转换为RGB图像
        rgb_small_frame = small_frame[:, :, ::-1]

        # 检测人脸
        face_locations = face_recognition.face_locations(rgb_small_frame)
        for top, right, bottom, left in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # 检杳是否成功读取到图像
        if not ret:
            print("无法从摄像头读取图像")
            break


        # 显示图像
        cv2.imshow("Camera", frame)
        # 如果按下"q"键，则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放摄像头资源
    cap.release()
    # 关闭所有 OpenCV窗口
    cv2.destroyAllwWindows()

    # 开始捕获视频
    # start_time = time.time()
    # while (time.time() - start_time) < 10:
    #     ret, frame = cap.read()
    #     if not ret:
    #         print("Capture failed")
    #         break
    #     out.write(frame)
    #     cv2.imshow('frame', frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break


# while True:
#     frame = cap_camera_ima()
#     # 压缩图片
#     # frame = cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)))
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1):
#         break

# hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# matplotlib.pyplot.hist(image.ravel(), 256, [0, 256])
# matplotlib.pyplot.show()

# 调用函数显示摄像头流
display_camera_stream(0)
# 拆分通道
# b, g, r = cv2.split(image)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)

cv2.waitKey()
