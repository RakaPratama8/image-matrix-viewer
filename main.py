import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io


def main():
    st.title("Image Matrix Viewer")
    st.markdown(
        """
        :red[Muhamad Raka Pratama, 50422956]
        """
    )
    img_uploaded = st.file_uploader("Upload your image here!", type=["jpg", "jpeg", "png"],
                                    accept_multiple_files=False)
    
    column1, column2 = st.columns(2)
    if img_uploaded:
        img_bytes = img_uploaded.read()
        img = Image.open(io.BytesIO(img_bytes))
        img = img.convert('RGB')
        img_np = np.asarray(img)
        
        table_datas = []
        for i in range(img_np.shape[0]):
            datas = []
            for j in range(img_np[0].shape[0]):
                datas.append(','.join(map(str, img_np[i][j])))
            table_datas.append(datas)
        
        st.dataframe(table_datas)
        
        with column1:
            st.image(img_np, caption=f"{img_uploaded.name}", width="content")
        with column2:
            x, y = st.number_input("Input x value", step=1, min_value=0, max_value=img_np.shape[0]-1), st.number_input("Input y value", step=1, min_value=0, max_value=img_np.shape[0]-1)
            
            if x >= 0 and y >= 0:
                st.text(
                    f"Selected element :\n{img_np[x][y]}"
                )
            
if __name__ == "__main__":
    main()
