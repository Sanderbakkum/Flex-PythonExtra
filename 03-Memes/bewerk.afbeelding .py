from PIL import Image

afbeelding = Image.open("Foto.jpg")

afbeelding.show()

breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuw_afmeting = (helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuw_afmeting)

kleinere_afbeelding.save('Kleinere_Foto.jpg')
