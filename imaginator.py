import csv, tempfile, zipfile

from tkinter import Tk, Frame, Button, filedialog, messagebox
from pathlib import Path
from utils import download, zipdir


class Imaginator(Frame):

    def __init__(self, app: Tk):
        Frame.__init__(self, app)

        self.app = app
        self.button = Button(self, text="Selecione a planilha", command=self.run, width=50, height=15)

        self.button.pack()
        self.pack()

    def run(self):
        try:
            source = filedialog.askopenfilename(title="Selecione a planilha", initialdir=Path.home())

            if not source:
                return

            source_path = Path(source)

            with tempfile.TemporaryDirectory() as tempdir:
                with open(source) as stream:
                    reader = csv.reader(stream)

                    for ID, *images in reader:
                        for i, url in enumerate(images):
                            if url:
                                name = f'{ID}_{i}.png'
                                download(url, tempdir, name)

                destination = filedialog.askdirectory(title="Selecione onde salvar o arquivo ZIP", initialdir=Path.home())

                if not destination:
                    destination = Path.home()

                with zipfile.ZipFile(f'{destination}/Imagens {source_path.stem}.zip', 'w') as output:
                    zipdir(tempdir, output)
        except Exception as error:
            messagebox.showerror("Imaginator", error)

        self.app.destroy()
