import os
import shutil

# Thư mục chứa 50 thư mục con
source_folder = 'C:\\Users\\84375\\Downloads\\dataset'

# Thư mục đích
destination_folder = 'D:\\DoAn\\DoAn2\\ThamKhao\\MiAI_Image_Search\\dataset'

# Khởi tạo biến đếm để đổi tên ảnh
counter = 1

# Duyệt qua tất cả các thư mục con
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # Đường dẫn đến file gốc
        source_path = os.path.join(root, file)
        # Đường dẫn đến file mới
        new_filename = f"{counter:04}.jpg"  # đổi đuôi file tùy vào định dạng
        destination_path = os.path.join(destination_folder, new_filename)
        # Sao chép file
        shutil.copy(source_path, destination_path)
        # Tăng biến đếm
        counter += 1
        # Điều kiện dừng khi đến file thứ 1000
        if counter > 1500:
            break
    # Điều kiện dừng khi đã đến file thứ 1000
    if counter > 1500:
        break
