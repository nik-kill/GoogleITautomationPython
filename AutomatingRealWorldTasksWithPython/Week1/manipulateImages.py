from PIL import Image
import  os

for file in os.listdir("images"):
    loc = "images/"+file
    if Image.open(loc):
      im = Image.open(loc)
      new = im.rotate(270).resize((128,128))
#    f = file.split(".")
#    f[-1] = "jpeg"
#    file = ".".join(f)
      newPath = "/opt/icons/"+file
      new = new.convert("RGB")
      new.save(newPath,"JPEG")
