import streamlit as st
import os
from resume_parser import resume_parser

def main():
    st.title("Lets Summarize your resume!")
    # File uploader widget
    uploaded_file = st.file_uploader("Upload a .pdf or .docx file", type=["pdf", "docx"])
    # The pyresparser we will send these to only accepts pdf and docx

    if uploaded_file is not None:
        st.success("File successfully uploaded!")

        if st.button("Parse My Resume"):            # When we hit the parse button
            export_file(uploaded_file)              # First, the resume will be uploaded to our local directory
            file_content = get_file_path(uploaded_file)     # Second we will get the relative path to our file in the directory
            result = resume_parser(file_content)            #----# After getting the path, we call the resume_parser function from 
            
            st.write("Below is your Parsed Result:")
            st.write(result)



# function to get the file path
def get_file_path(uploaded_file):
    save_path = "uploaded_resume"               # Choose a folder to save the file
    os.makedirs(save_path, exist_ok=True)       # create a directory for the file path if it doesn't exist
    file_path = os.path.join(save_path, uploaded_file.name)     # joining the folder directory with the file name
    return file_path


# function to export the file to a certain file path
def export_file(uploaded_file):
    file_path = get_file_path(uploaded_file)
    with open(file_path, "wb") as f:                            # based on the directory above, we will write the uploaded file
        f.write(uploaded_file.getbuffer())
    return st.success(f"Successfully saved {uploaded_file.name} to uploaded_resume.")   # we return success message to user
    


if __name__ == "__main__":
    main()