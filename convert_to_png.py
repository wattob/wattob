"""
PDF to PNG Converter

Usage:
    This script converts a PDF file to a PNG image, renames it, and saves it to a specified folder.

How to Run:
    1. Install required dependencies: pip install pdf2image
    2. Update the 'pdf_path', 'output_folder', and 'output_png_name' variables in the __main__ section.
    3. Run the script.

Purpose:
    This script is designed to convert a PDF document to a PNG image, allowing for customization
    of the output file name and location.

Note:
    Make sure to have 'poppler' installed on your system, as it is required by pdf2image.

"""

from pdf2image import convert_from_path
import os

def convert_pdf_to_png(pdf_path, output_folder, output_png_name):
    # Extracting the PDF file name without the extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Convert PDF to PNG
    images = convert_from_path(pdf_path, fmt='png', output_folder=output_folder)

    # Close the file to avoid the PermissionError
    images[0].close()

    # Remove the existing PNG file if it exists
    existing_png_path = os.path.join(output_folder, f"{output_png_name}.png")
    if os.path.exists(existing_png_path):
        os.remove(existing_png_path)

    # Rename the generated PNG file using the custom naming convention
    output_path = os.path.join(output_folder, f"{output_png_name}.png")
    os.rename(images[0].filename, output_path)

    # Return the list of generated PNG filenames (in this case, just one)
    return [output_path]

if __name__ == "__main__":
    # Path to the input PDF file
    pdf_path = "resume/resume.pdf"

    # Output folder for the PNG file
    output_folder = "resume/"

    # Desired name for the output PNG file
    output_png_name = "resume_preview"

    # Convert PDF to PNG
    png_files = convert_pdf_to_png(pdf_path, output_folder, output_png_name)

    print(f"Conversion successful. PNG file saved in {output_folder}:")
    for png_file in png_files:
        print(png_file)
