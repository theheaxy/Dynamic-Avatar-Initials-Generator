from PIL import Image, ImageDraw, ImageFont
import os

# # List of color hex codes - you can add or remove colors as needed..
colors = ["#9b59b6","#34495e", "#16a085", "#27ae60", "#2980b9", "#8e44ad", "#2c3e50", "#f1c40f", "#e67e22", "#e74c3c", "#95a5a6", "#f39c12", "#d35400", "#c0392b", "#bdc3c7", "#7f8c8d"]

# Calculate the initials from the name - update the 'name' variable with your specific name.
name = "MRill.org"
initials = name.split(' ')[0][0].upper() + name.split(' ')[1][0].upper()

# Calculate the index for the color
char_index = ord(initials[0]) - 65
color_index = char_index % len(colors)
background_color = colors[color_index]

# Image size and other parameters
avatar_width = 300
avatar_height = 300
font_size = avatar_width // 2
font = ImageFont.truetype("arial.ttf", font_size)  # You can use a different font file here

# Create a new image
image = Image.new('RGB', (avatar_width, avatar_height), color=background_color)
draw = ImageDraw.Draw(image)

# Calculate text position
text_bbox = draw.textbbox((0, 0), initials, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
position = ((avatar_width - text_width) // 2, (avatar_height - text_height) // 2 - 10)

# Draw initials onto the image
draw.text(position, initials, fill="#FFFFFF", font=font)

# Define the output directory - You can change this path if desired; the directory will be created if it doesn't exist.
output_directory = "Dynamic-Avatar-Initials-Generator/image-exports"
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist
output_file_path = os.path.join(output_directory, "avatar_initials.png")

# Save the image
image.save(output_file_path)

print(f"Avatar image with initials successfully saved as PNG: {output_file_path}")
