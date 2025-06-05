import streamlit as st
from PIL import Image
import os

def home_page():
    st.title("许世晨")
    st.markdown("中共党员")
    
    # 获取项目根目录（通过向上一级目录计算）
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    
    # 左右分栏布局：左侧联系信息，右侧照片
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # 联系信息
        st.markdown(
            """
            <div class="contact-info">
                <strong>电话:</strong> 13668802266<br>
                <strong>邮箱:</strong> <a href="mailto:xushichen2024@163.com">xushichen2024@163.com</a><br>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # 个人简介
        st.markdown("### 个人简介")
        st.markdown("""
        香港中文大学市场营销硕士在读，中山大学本科。具备丰富的跨行业实习经验，涵盖品牌策划、国际交流及市场研究领域。擅长数据分析、多模态内容创作及跨部门协作，拥有国家级/省级科研项目成果。
        """)
        
    with col2:
        # 显示个人照片
        try:
            # 构建图片的绝对路径
            photo_path = os.path.join(root_dir, "static", "images", "ximage.jpg")
            
            # 检查文件是否存在
            if not os.path.exists(photo_path):
                raise FileNotFoundError(f"图片文件不存在: {photo_path}")
                
            image = Image.open(photo_path)
            # 将 use_column_width 替换为 use_container_width 
            st.image(image, caption="许世晨", width=200, use_container_width=True)
        except FileNotFoundError as e:
            st.error(f"❌ 图片未找到: {str(e)}")
            st.info("请确保:")
            st.info("1. 图片文件名为 `ximage.jpg`")
            st.info("2. 图片位于项目根目录下的 `static/images/` 文件夹中")
        except Exception as e:
            st.error(f"❌ 加载图片失败: {str(e)}")
            st.info("可能的原因:")
            st.info("1. 图片文件损坏")
            st.info("2. 没有读取文件的权限")
            st.info("3. 图片格式不支持 (请使用JPEG/PNG格式)")
    
    # 简历下载按钮
    st.markdown("### 📄 下载简历")
    try:
        # 构建简历的绝对路径
        resume_path = os.path.join(root_dir, "static", "docs", "resume.pdf")
        
        # 检查文件是否存在
        if not os.path.exists(resume_path):
            raise FileNotFoundError(f"简历文件不存在: {resume_path}")
            
        with open(resume_path, "rb") as f:
            st.download_button(
                "下载PDF简历",
                f.read(),
                "许世晨-简历.pdf",
                "application/pdf",
                key="resume_download"
            )
    except FileNotFoundError as e:
        st.error(f"❌ 简历未找到: {str(e)}")
        st.info("请确保:")
        st.info("1. 简历文件名为 `resume.pdf`")
        st.info("2. 简历位于项目根目录下的 `static/docs/` 文件夹中")
    except Exception as e:
        st.error(f"❌ 加载简历失败: {str(e)}")
        st.info("可能的原因:")
        st.info("1. 简历文件损坏")
        st.info("2. 没有读取文件的权限")

if __name__ == "__main__":
    home_page()