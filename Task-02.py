from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    # Convert the image to a numpy array
    img_array = np.array(img, dtype=np.uint8)
    
    # Encrypt the image by adding the key to each pixel value and using modulo 256
    encrypted_array = (img_array.astype(np.int32) + key) % 256
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    
    # Save the encrypted image
    encrypted_img.save('encrypted_image.png')
    print('Image encrypted and saved as encrypted_image.png')

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    # Convert the image to a numpy array
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)
    
    # Decrypt the image by subtracting the key from each pixel value and using modulo 256
    decrypted_array = (encrypted_array.astype(np.int32) - key) % 256
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    
    # Save the decrypted image
    decrypted_img.save('decrypted_image.png')
    print('Image decrypted and saved as decrypted_image.png')

# Main function to handle user input
def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    image_path = input("Enter the image path: ")
    key = int(input("Enter the key (an integer value): "))
    
    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
