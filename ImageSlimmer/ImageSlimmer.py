import os
from PIL import Image, ImageSequence, ImageDraw
# pip3 install Pillow

def compress_gif(infile, outfile, target_size_kb=250, resize_ratio=0.5, max_colors=64):
    """Compress GIF files by reducing resolution and color palette of each frame."""
    with Image.open(infile) as img:
        # Create a list to hold the resized and reduced color frames
        frames = []
        for frame in ImageSequence.Iterator(img):
            # Resize the frame
            new_size = (int(frame.width * resize_ratio), int(frame.height * resize_ratio))
            frame = frame.resize(new_size, Image.Resampling.LANCZOS)
            
            # Reduce colors
            frame = frame.quantize(colors=max_colors)
            
            frames.append(frame)

        # Save the frames to a temporary GIF file to estimate size
        temp_outfile = outfile + '_temp.gif'
        frames[0].save(
            temp_outfile, save_all=True, append_images=frames[1:], optimize=True, loop=0
        )
        
        # Check file size
        file_size_kb = os.path.getsize(temp_outfile) / 1024
        if file_size_kb > target_size_kb:
            print(f"Warning: Unable to compress {infile} to less than {target_size_kb} KB. Saving as is.")
        os.rename(temp_outfile, outfile)


def compress_image(infile, outfile, target_size_kb=100, quality=85):
    """Attempt to compress an image to below the target size."""
    with Image.open(infile) as img:
        # Special handling for GIFs, especially animated GIFs
        if img.format == 'GIF':
            compress_gif(infile, outfile, target_size_kb)
            return
        
        # For non-GIF images, proceed with compression
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")

        # Loop to reduce the file size
        while True:
            img.save(outfile, quality=quality)
            if os.path.getsize(outfile) <= target_size_kb * 1024:
                break
            else:
                quality -= 5  # Decrement quality to try further size reduction
                if quality < 10:  # Avoid reducing quality below a minimum threshold
                    break

def compress_images_in_folder(input_folder_path, output_folder_path, target_size_kb=100):
    """Compress all images within the specified folder and save them to the output folder."""
    for file in os.listdir(input_folder_path):
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()
        if file_extension in ('.png', '.jpg', '.jpeg', '.gif'):
            infile_path = os.path.join(input_folder_path, file)
            outfile_name = f"{filename}_compressed{file_extension}"
            outfile_path = os.path.join(output_folder_path, outfile_name)
            print(f"Compressing {infile_path} and saving to {outfile_path}")
            compress_image(infile_path, outfile_path, target_size_kb=target_size_kb)

# Paths to the input and output folders
input_folder_path = '/Users/lvshaomin/Desktop/EasyTool/ImageSlimmer/Input'
output_folder_path = '/Users/lvshaomin/Desktop/EasyTool/ImageSlimmer/Output'

# Run the compression function
compress_images_in_folder(input_folder_path, output_folder_path)
