# pip install stegano
from stegano import exifHeader


def hide_payload(image_path, payload, output_path):
    try:
        secret = exifHeader.hide(image_path, output_path, payload)
        print("Payload successfully hidden in the image!")
    except Exception as e:
        print("Error:", e)


def extract_payload(image_path):
    try:
        secret = exifHeader.reveal(image_path)
        print("Extracted Payload:", secret.decode())
    except Exception as e:
        print("Error:", e)


# Example usage
image_path = "1.jpg"
payload = "Беги, за тобой выехали!"
output_path = "output_image_with_payload.jpg"


def main():
    # Hide payload
    hide_payload(image_path, payload, output_path)

    # Extract payload
    extract_payload(output_path)


if __name__ == '__main__':
    main()
