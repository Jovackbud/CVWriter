from src.writer import write_cv, write_cover
from src.utils import get_file, extract_text_from_pdf
import joblib


cv_dir = 'data/cv'
cv_path = get_file(cv_dir)
cv_text = extract_text_from_pdf(cv_path)
jd_dir = 'data/jd'
jd_path = get_file(jd_dir)
jd_text = extract_text_from_pdf(jd_path)

new_cv = write_cv(cv_text, jd_text)
cover_letter = write_cover(new_cv, jd_text)

joblib.dump(cover_letter, 'data/reponse/cover_letter.txt')
joblib.dump(new_cv, 'data/reponse/cv.txt')
