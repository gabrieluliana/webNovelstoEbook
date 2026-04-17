import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


# Define a simple class for novel data
class NovelData:
    def __init__(self):
        self.url = ""
        self.numChapters = 0
# Create an instance
novelData = NovelData()


def getData(novelData):
    novelData.url = urlEntry.get()
    novelData.numChapters = numEntry.get()

    print(f"dento do get URL: {novelData.url}, Number of Chapters: {novelData.numChapters}")
    root.destroy()

root = ttk.Window(size=(500, 300), title="WebNovel to eBook", themename="darkly")
ttk.Style().configure("TButton", font="Helvetica 14")  # NOTE:

## Initial screen to collect URL and number of chapters to download ##########
rframe = ttk.Frame(root, padding=5)
rframe.pack(fill=BOTH, expand=YES)

urlLabel = ttk.Labelframe(master=rframe, text="First Chapter URL", padding=10)
urlLabel.pack(fill=BOTH, pady=(10, 5), expand=YES)

urlEntry = ttk.Entry(urlLabel)
urlEntry.pack(fill=X, padx=10)
urlEntry.focus()

numLabel = ttk.Labelframe(master=rframe, text="Number of Chapters", padding=10)
numLabel.pack(fill=BOTH, pady=(10, 5), expand=YES)

def validate_input(P):
    # P is the value that the text will have if the change is allowed
    if P == "":
        return True  # Allow clearing the box
    if P.isdigit() and len(P) <= 3:
        return True  # Allow if it's all digits and max 3 characters
    return False     # Otherwise, reject the change

#register the validation function and get the validation command
vcmd = (rframe.register(validate_input), '%P')

#create the entry widget with the validation command for only numbers, with max lenght of 3
numEntry = ttk.Entry(numLabel, validate='key', validatecommand=vcmd)
numEntry.pack(fill=X, padx=10)


btnframe = ttk.Frame(master=rframe, padding=(5, 0))
btnframe.pack(anchor='center', expand=YES)

b1 = ttk.Button(
    btnframe,
    text="Start",
    bootstyle=SUCCESS,
    command=lambda: getData(novelData)
)
b1.pack(side=LEFT, padx=10, pady=10)

b2 = ttk.Button(btnframe,
    text="Exit",
    bootstyle=SECONDARY,
    command=lambda: root.destroy()
)
b2.pack(side=LEFT, padx=10, pady=10)

root.mainloop()


## Second show infos and wait completion ##########

root = ttk.Window(size=(800, 600), title="Building your eBook...", themename="darkly")
ttk.Style().configure("TButton", font="Helvetica 14")  # NOTE:

print("Data collected, building your eBook...")
print(f"Finalizando - URL: {novelData.url}, Number of Chapters: {novelData.numChapters}")
xframe = ttk.Frame(root, padding=5)
xframe.pack(anchor='center', fill=BOTH, expand=YES)

waitTxt = ttk.Label(xframe, text="Building your eBook, please wait...", font="Helvetica 16")
waitTxt.pack(pady=20)

fictionTitle = "Example Fiction Title"
waitTxt = ttk.Label(xframe, text=fictionTitle, font="Helvetica 16")
waitTxt.pack(pady=10)

coverImg = Image.open("./covers/cover_img.jpg")
# coverImg.show()
print(f"Format: {coverImg.format}, Size: {coverImg.size}, Mode: {coverImg.mode}") 
coverImg = coverImg.resize((250, 400))
coverObj = ImageTk.PhotoImage(coverImg)
coverLabel = ttk.Label(xframe, image=coverObj)
coverLabel.pack(pady=20)

root.mainloop()

# for i in range(1, numChapters + 1):
    
#     chapterTitle = str(soup.h1)
#     chapterText = str(soup.find('div', class_='chapter-content'))
#     chapterText = chapterTitle + chapterText

#     print(f"{i} - {soup.h1.text}")
#     ficChapter = xml2epub.create_chapter_from_string(chapterText, url=url, title=soup.h1.text, strict=False)
#     book.add_chapter(ficChapter)

#     time.sleep(0.6)
#     try:
#         soup = getNextChapter(soup)
#     except:
#         print("There is no next chapter")
#         print(f"book finished with {i} chapters")
#         break