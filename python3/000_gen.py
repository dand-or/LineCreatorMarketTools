from PIL import Image
import zipfile
import os
import shutil

print("--start--")
# パスコードオフ画像なければ複製する
if(not os.path.exists("./i_14.png")):
    shutil.copy("./i_12.png", "./i_14.png")
if(not os.path.exists("./i_16.png")):
    shutil.copy("./i_12.png", "./i_16.png")
if(not os.path.exists("./i_18.png")):
    shutil.copy("./i_12.png", "./i_18.png")

# トリミング系
img = Image.open("./i_01.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_01.png", quality=95)
img = Image.open("./i_02.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_02.png", quality=95)
img = Image.open("./i_29.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_29.png", quality=95)
img = Image.open("./i_30.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_30.png", quality=95)
img = Image.open("./i_03.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_03.png", quality=95)
img = Image.open("./i_04.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_04.png", quality=95)
img = Image.open("./i_05.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_05.png", quality=95)
img = Image.open("./i_06.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_06.png", quality=95)
img = Image.open("./i_07.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_07.png", quality=95)
img = Image.open("./i_08.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_08.png", quality=95)
img = Image.open("./i_25.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_25.png", quality=95)
img = Image.open("./i_26.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_26.png", quality=95)
img = Image.open("./i_09.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_09.png", quality=95)
img = Image.open("./i_10.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_10.png", quality=95)
img = Image.open("./i_27.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_27.png", quality=95)
img = Image.open("./i_28.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_28.png", quality=95)
img = Image.open("./i_31.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_31.png", quality=95)
img = Image.open("./i_32.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_32.png", quality=95)
img = Image.open("./i_33.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_33.png", quality=95)
img = Image.open("./i_34.png")
img_crop = img.crop((0, 19, 128, 131)).save("./a_34.png", quality=95)

# リサイズ系
### main -> ios_thumbnail
img = Image.open("./main.png")
img_resize = img.resize((200, 284))
img_resize.save("./ios_thumbnail.png")
### main -> android_thumbnail
img = Image.open("./main.png")
img_resize = img.resize((136, 202))
img_resize.save("./android_thumbnail.png")
### main -> store_thumbnail
img = Image.open("./main.png")
img_resize = img.resize((198, 278))
img_resize.save("./store_thumbnail.png")
### a_21 -> i_21
img = Image.open("./a_21.png")
img_resize = img.resize((240, 240))
img_resize.save("./i_21.png")
### a_20 -> i_20
img = Image.open("./a_20.png")
img_resize = img.resize((240, 240))
img_resize.save("./i_20.png")
### i_12 -> a_12
img = Image.open("./i_12.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_12.png")
### i_13 -> a_13
img = Image.open("./i_13.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_13.png")
### i_14 -> a_14
img = Image.open("./i_14.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_14.png")
### i_15 -> a_15
img = Image.open("./i_15.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_15.png")
### i_16 -> a_16
img = Image.open("./i_16.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_16.png")
### i_17 -> a_17
img = Image.open("./i_17.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_17.png")
### i_18 -> a_18
img = Image.open("./i_18.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_18.png")
### i_19 -> a_19
img = Image.open("./i_19.png")
img_resize = img.resize((116, 116))
img_resize.save("./a_19.png")
# ### a_22 -> i_22
# img = Image.open("./a_22.png")
# img_resize = img.resize((1482, 1334))
# img_resize.save("./i_22.png")


# zip作成
zip = zipfile.ZipFile("./items.zip", "w")
zip.write("a_01.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_02.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_03.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_04.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_05.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_06.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_07.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_08.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_09.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_10.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_12.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_13.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_14.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_15.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_16.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_17.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_18.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_19.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_20.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_21.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_22.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_23.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_24.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_25.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_26.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_27.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_28.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_29.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("a_30.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("android_thumbnail.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_01.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_02.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_03.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_04.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_05.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_06.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_07.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_08.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_09.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_10.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_12.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_13.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_14.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_15.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_16.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_17.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_18.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_19.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_20.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_21.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_22.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_25.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_26.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_27.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_28.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_29.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_30.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_31.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_32.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_33.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("i_34.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("ios_thumbnail.png", compress_type=zipfile.ZIP_DEFLATED)
zip.write("store_thumbnail.png", compress_type=zipfile.ZIP_DEFLATED)
zip.close()
print("--end😄--")
