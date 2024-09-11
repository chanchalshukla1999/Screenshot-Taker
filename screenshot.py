import pyscreenshot

# To capture the screen
image = pyscreenshot.grab(bbox=(10,10,500,500))

# Show the captured screenshot
image.show()

# To save image
image.save("py.png")