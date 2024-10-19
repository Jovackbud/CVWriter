from src.utils import extract_text_from_pdf, get_cv_files
from src.writer import write_cv, write_cover
import joblib

cv_directory = 'dataset/cv'  # create the folder
cv_file = get_cv_files(cv_directory)
cv = extract_text_from_pdf(cv_file)

jd = input('Paste the job description here: ')

new_cv = write_cv(cv, jd)
cover_letter = write_cover(new_cv, jd)

joblib.dump(cover_letter, 'cover_letter.docx')
joblib.dump(cv, 'cv.docx')
