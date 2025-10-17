import requests

# API 接口地址
url = "https://api.zetatechs.com/v1/chat/completions"

# 请求头（包含认证信息和数据格式）
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "  # 直接使用提供的 API 密钥
}

# 请求体数据（对话内容和模型参数）
data = {
    "model": "gpt-5-chat-latest",
    "messages": [
        {"role": "developer", "content": "你是一个有帮助的助手。"},
        {"role": "user", "content": "你好吗？"}
    ]
}

try:
    # 发送 POST 请求
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # 检查请求是否成功（如 404、500 等错误）

    # 打印 API 返回的响应结果（JSON 格式）
    print("API 响应结果：")
    print(response.json())

except requests.exceptions.RequestException as e:
    # 捕获并打印请求过程中的错误（如网络问题、认证失败等）

    print(f"请求出错：{e}")
