from PIL import Image, ImageEnhance 


im = Image.open("images/moon_rocks_1.jpg")
enhancer = ImageEnhance.Contrast(im)
enhanced_im = enhancer.enhance(4.0)
enhanced_im.save("output/moon_rocks_1.png")


im2 = Image.open("images/moon_rocks_2.jpg")
enhancer2 = ImageEnhance.Contrast(im2)
enhanced_im2 = enhancer2.enhance(4.0)
enhanced_im2.save("output/moon_rocks_2.png")


im3 = Image.open("images/moon_rocks_3.jpg")
enhancer3 = ImageEnhance.Contrast(im3)
enhanced_im3 = enhancer3.enhance(4.0)
enhanced_im3.save("output/moon_rocks_3.png")


im4 = Image.open("images/moon_rocks_4.jpg")
enhancer4 = ImageEnhance.Contrast(im4)
enhanced_im4 = enhancer4.enhance(4.0)
enhanced_im4.save("output/moon_rocks_4.png")


im5 = Image.open("images/moon_rocks_5.jpg")
enhancer5 = ImageEnhance.Contrast(im5)
enhanced_im5 = enhancer5.enhance(4.0)
enhanced_im5.save("output/moon_rocks_5.png")