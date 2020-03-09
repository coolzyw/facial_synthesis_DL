from PIL import Image
import os


def crop_image(filename, row, col):
    im = Image.open(filename)
    width, height = im.size
    # Setting the points for cropped image
    row_step = height / row
    col_step = width / col
    top = 0
    label = 0
    for i in range(0, row):
        left = 0
        dir = "crop/person{}".format(i)
        os.mkdir(dir)
        for j in range(0, col):
            right = left + col_step
            bottom = top + row_step

            # Cropped image of above dimension
            # (It will not change orginal image)
            im1 = im.crop((left, top, right, bottom))

            # Shows the image in image viewer
            im1.save("{}/style{}.jpg".format(dir, str(j)))

            left += col_step

        top += row_step
        label += 1


def main():
    filename = "output/output.jpeg"
    crop_image(filename, 16, 6)


if __name__ == "__main__":
    main()