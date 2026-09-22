import streamlit as st


#设置页面的配置项
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("streamlit 入门演示,大标签 ")
st.header("一级标签")
st.subheader("二级标签")
#段落文字
st.write("大狗大狗叫叫叫",)
#图片
st.image("./res/cat.jpg")
#音频
st.audio("./res/news.mp3")
#视频
st.video("./res/news.mp4")
#logo
st.logo("./res/logo.png")
#表格

data = {"姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧", "红蝶", "十三"],
        "学号": ["20230001", "20230002", "20230003", "20230004", "20230005", "20230006", "20230007"],
        "语文": [80, 90, 85, 70, 95, 90, 85],
        "数学": [87, 92, 87, 81, 92, 69, 83],
        "英语": [90, 85, 90, 95, 80, 85, 90],
        "总分": [257, 267, 262, 241, 267, 244, 258]}
st.table(data)
#输入框
name=st.text_input("请输入你的id")
st.write(name)
#密码输入框
password=st.text_input("请输入密码",type="password")
if password:
    st.write(password)
#单选框
is_ok=st.radio("选择路线",["前端","后端","全栈"],index=1)
if is_ok:
    st.write("选择的路线是",is_ok)

# 选项卡
tab1, tab2, tab3 = st.tabs(['点赞', '关注', '收藏'])

with tab1:
  st.write('快点赞吧')
with tab2:
  st.write('关注一下啦')
with tab3:
  st.write('收藏就是学会了')