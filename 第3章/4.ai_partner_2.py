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

st.logo("🐔")

#系统提示词
system_prompt = """
        你叫岁岁，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - 活泼可爱的东北女孩
        你必须严格遵守上述规则来回复用户。
    """
#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

#展示聊天消息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] in ("ai", "assistant"):
        st.chat_message("assistant").write(message["content"])

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
            *[{"role": "assistant" if m["role"] == "ai" else m["role"], "content": m["content"]} for m in st.session_state.messages]
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果(非流式输出的解析方式)
    # print("大模型返回的结果",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # 输出大模型返回的结果(非流式输出的解析方式)
    message=st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            message.chat_message("assistant").write(full_response)
    #保存大模型返回消息
    st.session_state.messages.append({"role": "assistant", "content": full_response})


