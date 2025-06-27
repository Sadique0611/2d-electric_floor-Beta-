from utils.pdf_to_image import pdf_to_image
from utils.detect import run_detection

pdf_file = "input/floorplan.pdf"
model_file = "model/best.pt"
output_image = "output/result.png"
images = pdf_to_image(pdf_file, "floorplan.pdf")
first_page_image = images[0] 
run_detection(first_page_image, model_file, output_image)
