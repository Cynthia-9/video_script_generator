import streamlit as st
from utils import generate_script

st.title("📽️ 视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥", type='password')
    st.markdown("[获得OpenAI API密钥](https://openai.com/blog/openai-api)")

subject = st.text_input("💡 请输入视频主题")
video_length = st.number_input("⏱️ 请输入视频大致时长（单位：分钟）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造性（数字越小说明脚本更严谨，数字越大说明脚本更多样）",
                       min_value=0.1, max_value=1.0, value=0.2, step=0.1)
submit = st.button('生成脚本')

if submit and not openai_api_key:
    st.info("请输入OpenAI API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit:
    with st.spinner("AI正在思考中..."):
        search_result, title, script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("脚本生成成功！")
    st.subheader("🔥 标题")
    st.write(title)
    st.subheader("✍️ 脚本")
    st.write(script)
    with st.expander("维基百科搜索结果 🤓"):
        st.info(search_result)
