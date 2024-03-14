from PIL import Image
 
def convert_to_pixel_art(input_path, output_path, pixel_size):
    # Open the image
    img = Image.open(input_path)
 
    # Resize the image to make pixels more prominent
    img = img.resize(
        (img.width // pixel_size, img.height // pixel_size),
        resample=Image.NEAREST
    )
 
    # Convert the image to 8-bit mode
    img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
 
    # Save the result
    img.save(output_path)
 
# Example usage
input_image_path = "Assets/sample.jpg"
output_image_path = "Assets/sample_pixel.png"
pixel_size = 30  # Adjust this based on your preference
 
convert_to_pixel_art(input_image_path, output_image_path, pixel_size)