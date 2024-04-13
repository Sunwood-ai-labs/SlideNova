import streamlit as st
from marp import Marp
import base64
from io import BytesIO

def main():
    st.title("Marp Slide Generator")
    
    # マークダウン入力欄
    markdown_text = st.text_area("Enter your markdown text here:", height=400)
    
    if st.button("Generate Slides"):
        # Marpオブジェクトの作成
        marp = Marp()
        
        # マークダウンからスライドを生成
        slides = marp.convert(markdown_text)
        
        # スライドを画像に変換
        images = []
        for slide in slides:
            image_data = slide.render(format="png")
            images.append(image_data)
        
        # 画像を表示
        st.subheader("Generated Slides")
        for i, image in enumerate(images):
            st.image(image, caption=f"Slide {i+1}", use_column_width=True)
            
            # 画像をダウンロード可能なリンクとして提供
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:file/png;base64,{img_str}" download="slide_{i+1}.png">Download Slide {i+1}</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()