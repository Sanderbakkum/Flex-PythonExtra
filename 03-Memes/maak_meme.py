from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

print("De afbeelding is " + str(breedte)+" pixel breed en " + str(hoogte) + " hoog")

lettertype = ImageFont.truetype("impact.ttf", 40)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "When your code\nisn't working."

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekst_breedte=" + str(tekst_breedte) + ", tekst_hoogte" + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2
tekengebied.multiline_text((tekst_x-50,tekst_y-50), tekst, font=lettertype, fill=(0,0,0))
tekengebied.multiline_text((tekst_x-52,tekst_y-52), tekst, font=lettertype, fill=(255,255,255))
achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
