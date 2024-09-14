import streamlit as st
import epubtranslator 
from epubtranslator import LANGUAGES, TranslatorEngine
import tempfile
import os



def main():
    st.markdown("[![100pa.com](https://www.100pa.com/images/logo.png)](https://100pa.com/)")
    st.title("🌉 Epub Translator")
    st.write("Select epub file and target language to translate the file.")

    file = st.file_uploader("Select epub file", type=["epub"])
    if file is not None:
        with tempfile.NamedTemporaryFile(suffix=".epub", delete=False) as tmp:
            tmp.write(file.getvalue())
            tmp.flush()
            file_path = tmp.name
        lang = st.selectbox("Select your target language", list(LANGUAGES.values()), index=list(LANGUAGES.values()).index("polish")) # default polish
        # lang = st.selectbox("Wybierz język docelowy", list(LANGUAGES.values()))
        lang_code = [k for k, v in LANGUAGES.items() if v == lang][0]

        if st.button("Translate"):
            translator = epubtranslator.TranslatorEngine()
            translator.dest_lang = lang_code
            translator.start(file_path)

            translated_file_path = os.path.splitext(file_path)[0] + "_translated.epub"
            with open(translated_file_path, "rb") as f:
                st.download_button("Download translated file", f, file_name=os.path.basename(translated_file_path))

if __name__ == "__main__":
    main()