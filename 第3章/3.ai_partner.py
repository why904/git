import streamlit as st
import os
from openai import OpenAI

#设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

st.logo("./res/logo.png")

#系统提示词
system_prompt = "你是一名可爱的AI助理,你叫岁岁,请你用温柔的语气回答用户问题，请用中文回答问题。"
#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
#展示聊天消息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "ai":
        st.chat_message("ai").write(message["content"])

# 创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
#消息输入框
prompt=st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(prompt)
    #保存用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互#调用大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("大模型返回的结果",response.choices[0].message.content)
    st.chat_message("ai").write(response.choices[0].message.content)
    #保存大模型返回消息
    st.session_state.messages.append({"role": "ai", "content": response.choices[0].message.content})
