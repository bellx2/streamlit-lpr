import streamlit as st
import requests

def detect_plate(token, f):
  api_url = "https://api.sensing-api.com/api/lpr-entry"
  url = "{0}?token={1}".format(api_url, token)
  file = {'image1': (f.name, f.getvalue(), 'image/jpeg')}

  r = requests.put(url,files=file)
  return r.json()

def main():
  st.title('EyeTech SensingAPI Demo')
  st.markdown('''
    [EyeTech SensingAPI](https://lpr.sensing-api.com)のTokenが必要です。
  ''')
  api_token = st.text_input('SensingAPI Token')
  col1, col2 = st.columns(2)
  detect_result = ""
  with col1:
    col1.header('画像')
    f = st.file_uploader(label='画像ファイル:',type=["jpg", "jpeg"], accept_multiple_files=False)
    st.write('Image Info: ', f)
    if f is not None:
      data = f.getvalue()
      st.image(data)
      detect_result = detect_plate(api_token, f)
      
  with col2:
    col2.header('検出結果')
    st.write(detect_result)

if __name__ == '__main__':
    main()