import cv2
import os

def find_similar_images(folder_path, min_similarity=0.8):
    image_files = os.listdir(folder_path)
    num_images = len(image_files)

    similar_images = []

    for i in range(num_images):
        img1_path = os.path.join(folder_path, image_files[i])
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)

        for j in range(i+1, num_images):
            img2_path = os.path.join(folder_path, image_files[j])
            img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

            height, width = img1.shape

            # Minimum image size for comparison
            min_size = (20, 20)

            if height >= min_size[0] and width >= min_size[1]:
                result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
                _, similarity, _, _ = cv2.minMaxLoc(result)

                if similarity >= min_similarity:
                    similar_images.append((image_files[i], image_files[j], similarity))

    similar_images.sort(key=lambda x: x[2], reverse=True)
    return similar_images

# Klasör yolunu masaüstünden alın
folder_path = os.path.expanduser("C:\Users\EXCALIBUR\Desktop\ALGORTIMA_ANALIZI_ODEV_SOURCES")

# Benzerlik eşiği (isteğe bağlı olarak değiştirilebilir)
minimum_similarity = 0.8

similar_images = find_similar_images(folder_path, minimum_similarity)

for img1, img2, similarity in similar_images:
    print(f"{img1} ve {img2} görselleri birbirine % {similarity * 100} oranında benzemektedir.")

