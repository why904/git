import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

from streamlit import session_state

#设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#保存会话信息的函数
def save_session():
    session_data = {
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages,
        "nick_name": st.session_state.nick_name,
        "character": st.session_state.character
    }
    # 存会话的文件夹sessions
    if not os.path.exists("sessions"):
        os.makedirs("sessions")
    # 保存会话数据到文件夹sessions
    with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话的标识
def generate_session_name():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

#加载所有会话信息
def load_sessions():
    sessions_list = []
    if os.path.exists("sessions"):
        file_list=os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                file_slice = filename[:-5]
                sessions_list.append(file_slice)
    return sessions_list



#大标题
st.title("AI智能伴侣")
st.logo("🐔")
#系统提示词
system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """
#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "岁岁"
if 'character' not in st.session_state:
    st.session_state.character = "活泼开朗的雷州姑娘"
#会话标识current_session
if 'current_session' not in st.session_state:
    st.session_state.current_session = generate_session_name()  # 时间戳标识
#展示聊天消息
st.text(f"会话名称:{st.session_state.current_session}")
for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#侧边栏的添加
with st.sidebar:
    st.title("AI控制面板")
    # 保存会话信息按钮
    if st.button("新建会话",width="stretch",icon="✏️"):#按钮
        # 1.保存当前会话信息
        save_session()
        # 2.创建新会话
        # st.button(session, width="stretch", icon="📝")  # 按钮
        # st.button("", type="primary", width="stretch", icon="❌️")


    #伴侣信息面板
    st.write("----------------")
    st.subheader("AI智能伴侣信息")
    #伴侣信息保存按钮
    if st.button("保存伴侣信息",width="stretch",icon="💾"):
        save_session()
    # 昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    character = st.text_area("性格",placeholder="请输入性格",value=st.session_state.character)
    if character:
        st.session_state.character = character

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
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.character)},
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
    message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            message.chat_message("assistant").write(full_response)
    #保存大模型返回消息
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    #保存会话信息
    save_session()

