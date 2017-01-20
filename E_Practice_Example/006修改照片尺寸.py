import os


def reset_images_size(dir_path=None):
     if dir_path is None:
         return

     for root, dirs, files in os.walk(dir_path):
         for path in files:
             if path.startswith("."):
                 continue

             file_path = os.path.join(root, path)
             image = imager.open_image(file_path)
             if image is not None:
                 new_image = imager.reset_image_size(image, 640, 1136)
                 imager.save(new_image, file_path)