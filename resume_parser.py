from pyresparser import ResumeParser
import warnings
#please use data_practise env

def resume_parser(file_path):
    warnings.filterwarnings("ignore", category=UserWarning)
    parsed_result = ResumeParser(file_path).get_extracted_data()
    return parsed_result
