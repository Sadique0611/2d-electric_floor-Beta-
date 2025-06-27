from pdf2image import convert_from_path
import os

def pdf_to_image(pdf_path, output_folder):
    pages = convert_from_path(pdf_path, 300)
    os.makedirs(output_folder, exist_ok=True)
    image_paths = []
    for i, page in enumerate(pages):
        img_path = os.path.join(output_folder, f"page_{i+1}.png")
        page.save(img_path, "PNG")
        image_paths.append(img_path)
    return image_paths