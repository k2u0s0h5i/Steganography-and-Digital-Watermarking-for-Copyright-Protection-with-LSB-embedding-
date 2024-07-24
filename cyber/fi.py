import cv2 
import numpy as np 
import random 

# Embedding function 
def embed(): 
    # img1 and img2 are the two input images 
    img1=cv2.imread('cover_img.jpeg') 
    img2=cv2.imread('water.jpg') 
    
    for i in range(img2.shape[0]): 
        for j in range(img2.shape[1]): 
            for l in range(3): 
                # v1 and v2 are 8-bit pixel values of img1 and img2 respectively 
                v1=format(img1[i][j][l], '08b') 
                v2=format(img2[i][j][l], '08b') 
                
                # Taking 4 MSBs of each image 
                v3=v1[:4]+v2[:4] 
                
                img1[i][j][l]=int(v3, 2) 
    
    cv2.imwrite('embed_img.png', img1) 
    print("Embedded completed. The embedded image is saved as 'embed_img.png'.") 

# extraction function 
def extract(): 
    # Encrypted image 
    img=cv2.imread('embed_img.png') 
    width=img.shape[0] 
    height=img.shape[1] 
    
    # img1 and img2 are two blank images 
    img1=np.zeros((width, height, 3), np.uint8) 
    img2=np.zeros((width, height, 3), np.uint8) 
    
    for i in range(width): 
        for j in range(height): 
            for l in range(3): 
                v1=format(img[i][j][l], '08b') 
                v2=v1[:4]+chr(random.randint(0, 1) + 48)*4
                v3=v1[4:]+chr(random.randint(0, 1) + 48)*4
                
                # Appending data to img1 and img2 
                img1[i][j][l]=int(v2, 2) 
                img2[i][j][l]=int(v3, 2) 
    
    # These are two images produced from the encrypted image 
    cv2.imwrite('ex_cover.png', img1) 
    cv2.imwrite('ex_water.png', img2) 
    print("extraction completed. The extracted images are saved as 'ex_cover.png' and 'ex_water.png'.") 


def main():
    choice=input("Enter 'e' for embedding or 'd' for extraction: ").strip().lower()
    
    if choice == 'e':
        embed()
    elif choice == 'd':
        extract()
    else:
        print("Invalid choice. Please enter 'e' for embedding or 'd' for extracting.")

# Driver's code 
if __name__ == "__main__":
    main()
