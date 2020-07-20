from bs4 import BeautifulSoup

class GarticProfilePage:
    name = ""
    status = ""
    picture = ""
    phrase = ""

    def __init__(self, rawPageData):
        soup = BeautifulSoup(rawPageData, 'lxml')

        internoConteudo = soup.find("div", class_="internoConteudo")
        self.name = internoConteudo.contents[6]
        self.status = internoConteudo.contents[-1]

        self.picture  = soup.find("div", id="contornoFotoPerfil").find("img").attrs["src"]

        self.phrase = soup.find("div", class_="frasePerfil").find("div").contents[2]