from PIL import Image

# Extended set of ASCII characters from darkest to lightest
ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def resize_image(image, new_width=80):
    """Resize image preserving aspect ratio"""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))


def image_to_grayscale(image):
    """Convert image to grayscale"""
    return image.convert("L")


def map_pixels_to_ascii(image):
    """Map each pixel to an ASCII char based on intensity"""
    pixels = image.getdata()
    chars = [ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels]
    return "".join(chars)


def convert_image_to_ascii(path, new_width=80):
    """Read an image and return its ASCII representation"""
    image = Image.open(path)
    image = resize_image(image, new_width)
    grayscale_image = image_to_grayscale(image)
    ascii_str = map_pixels_to_ascii(grayscale_image)
    ascii_lines = [
        ascii_str[i : i + new_width]
        for i in range(0, len(ascii_str), new_width)
    ]
    return "\n".join(ascii_lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert an image to ASCII art")
    parser.add_argument("path", help="Path to the image")
    parser.add_argument(
        "-w", "--width", type=int, default=80, help="Width of the ASCII output"
    )
    args = parser.parse_args()

    print(convert_image_to_ascii(args.path, args.width))
