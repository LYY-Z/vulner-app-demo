import requests

def fetch_example():
    """一个简单的函数，演示requests库的使用"""
    try:
        response = requests.get('https://api.github.com')
        print(f"Status Code: {response.status_code}")
        # 简单地打印部分响应内容来证明库在工作
        print("Request successful!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    fetch_example()
