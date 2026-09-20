# scripts/test_datasets.py
from core.api_session import get_session
from core.brain_api import BrainAPIClient

# Giả định thư viện ace đã được đặt trong thư mục dự án theo cấu trúc: Alpha/ace/
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ace')))
import ace_lib 

def discover_metadata():
    session = get_session()
    api_client = BrainAPIClient(session)
    
    print("--- 1. Kiểm tra cấu hình CHN / TOP2000U qua HTTP API trực tiếp ---")
    chn_datasets = api_client.get_datasets(region="CHN", universe="TOP2000U")
    print(f"Tìm thấy {len(chn_datasets)} Datasets hợp lệ cho thị trường Trung Quốc.")
    if chn_datasets:
        print(f"Dataset mẫu: {chn_datasets[0].get('id')} - {chn_datasets[0].get('name')}")

    print("\n--- 2. Đối chiếu với thư viện ACE ---")
    # THEO QUY TẮC DỰ ÁN: Luôn ưu tiên dùng hàm của ACE nếu có sẵn. 
    # Cần đọc file ace_lib.py để đảm bảo truyền đúng tham số. 
    # Ví dụ giả định hàm get_datasets trong ace_lib nhận session làm tham số:
    try:
        ace_datasets = ace_lib.get_datasets(session, region="CHN", delay=1)
        print(f"ACE Library trả về {len(ace_datasets)} datasets.")
    except Exception as e:
        print(f"Lỗi khi gọi ACE (Cần mở thư mục ace/ace_lib.py để check chữ ký hàm): {e}")

if __name__ == "__main__":
    discover_metadata()