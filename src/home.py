import streamlit as st
import json

def import_config_file(file):
    '''
    侧边栏配置导入
    '''
    if file is not None:
        content = file.read()
        try:
            # 解析JSON数据
            json_data = json.loads(content)
            st.success("load config success")
        except Exception as e:
            st.error("load config error:{}".format(e))
        st.session_state.base_url = json_data.get("base_url")
        st.session_state.api_key = json_data.get("api_key")

def home():
    st.title("🏠AI皮肤检测")
    st.caption("Please fill in the parameters in the sidebar before using, or import the parameters by uploading a file.")

    if "base_url" not in st.session_state:
        st.session_state['base_url'] = "https://api.openai.com/v1"
    
    if "api_key" not in st.session_state:
        st.session_state['api_key'] = ""

    #通过上传配置的方式导入base_url和api_key
    uploaded_file = st.sidebar.file_uploader("uploaded config", type="json")
    if uploaded_file is not None:
        import_config_file(uploaded_file)

    ## 输入方式
    st.session_state.base_url = st.sidebar.text_input('Base URL', st.session_state.base_url)
    st.session_state.api_key =  st.sidebar.text_input('API Key',st.session_state.api_key, type='password')

    option = st.radio("change language:", ("En", "Zh"),horizontal=True,index=1)
    if option == "Zh":
        st.markdown(
                """

                **探索肌肤的奥秘，AI皮肤检测引领智能护肤新潮流**

                在这个科技飞速发展的时代，我们对美的追求也变得更加精准和高效。AI皮肤检测技术，以其前所未有的智能分析能力，为您的肌肤健康保驾护航。

                **【智能分析】**  
                采用最前沿的人工智能算法，我们的AI皮肤检测系统能够深入分析您的肌肤状况，从毛孔、纹理到色素沉淀，每一个细节都不放过。

                **【个性化推荐】**  
                基于您的皮肤检测结果，我们提供个性化的护肤建议和产品推荐，确保您的护肤方案既科学又符合个人需求。

                **【持续追踪】**  
                通过持续的皮肤检测，您可以清晰地看到肌肤状况的改善过程，让您的护肤之旅更加透明和有据可依。

                **【便捷操作】**  
                只需简单的操作，即可在家中享受专业的皮肤检测服务，无需繁琐的预约和等待，一切尽在指尖。

                **欢迎体验，开启智能护肤新篇章！**

                """
            )
        st.markdown(
                """
                ## 使用说明
                * 请在侧边栏填写`API Key`，如果没有请在[openai官网](https://platform.openai.com/account/api-keys)获取，如果需要使用代理，请修改`base_url`\n
                * 也可以通过导入json文件自动填充，格式如下：\n
                    ```json
                    {
                        "base_url" : "https://xxx",
                        "api_key" : "sk-xxxx" 
                    }
                    ```
                * 接下来在侧边栏选择需要使用的页面。
                ---------------------------------------------------------
                """
            )
    elif option == "En":
            st.markdown(
            """

            **Unveil the Mysteries of Your Skin with AI Skin Analysis, Leading the New Trend of Smart Skin Care**

            In this era of rapid technological advancement, our pursuit of beauty has become more precise and efficient. AI skin analysis technology, with its unprecedented intelligent analytical capabilities, is here to safeguard your skin health.

            **[Smart Analysis]**

            Using cutting-edge artificial intelligence algorithms, our AI skin analysis system can deeply analyze your skin condition, from pores, texture to pigmentation, leaving no detail unexamined.

            **[Personalized Recommendations]**

            Based on your skin analysis results, we provide personalized skincare advice and product recommendations, ensuring that your skincare plan is both scientific and tailored to your individual needs.

            **[Continuous Tracking]**

            Through continuous skin analysis, you can clearly see the improvement process of your skin condition, making your skincare journey more transparent and evidence-based.

            **[Convenient Operation]**

            With simple operations, you can enjoy professional skin analysis services at home, without the hassle of appointments and waiting, everything is at your fingertips.

            Welcome to experience a new chapter in smart skincare!

            ---------------------------------------------------------

            ## Instructions for use
            * Please fill in the `API Key` in the sidebar. If you don't have one, you can obtain it from the [OpenAI website](https://platform.openai.com/account/api-keys). If you need to use a proxy, please modify the `base_url`.
            * You can also automatically populate the fields by importing a JSON file with the following format:
            ```json
            {
                "base_url" : "https://xxx",
                "api_key" : "sk-xxxx" 
            }
            ```
            * Next, select the desired page from the sidebar.

            """
        )
if __name__ == "__main__":
    home()