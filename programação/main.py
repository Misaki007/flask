from flask import Flask, render_template, request, session
from classes import Perfil
import os

app = Flask(__name__)

app.secret_key = "LGBSDGKYW#TBRjGJKikejhrg"

app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static/images")

pet1 = Perfil("Rex", "Rex é um adorável labrador amarelo de três anos. Ele é um entusiasta por natureza, sempre pronto para uma corrida no parque ou um mergulho na piscina. Rex é um grande amante de bolas, e ele pode passar horas brincando de buscar. Ele também é muito gentil e adora crianças, fazendo dele o melhor amigo da família.", "Maria", "pet1.jpg")

pet2 = Perfil("Luna", "Luna é uma gata persa de pelagem branca e longa. Ela é uma princesa peluda que adora ser mimada. Luna é a melhor companhia para noites aconchegantes no sofá, onde ela ronrona suavemente enquanto recebe carinho. Ela é um pouco tímida com estranhos, mas uma vez que você a conquista, você terá uma amiga fiel para a vida toda.", "João", "pet2.jpg")

pet3 = Perfil("Max", "Max é um vira-lata de cinco anos de idade que Ana resgatou de um abrigo. Ele tem uma energia interminável e é um entusiasta de esportes. Os seus passeios no parque são verdadeiras aventuras, e ele é conhecido por fazer amigos caninos em todos os lugares que vai. Max é um ótimo cão de guarda, mas também um parceiro de brincadeira leal.", "Ana", "pet3.jpeg")

pet4 = Perfil("Bella", "Bella é uma pequena chihuahua de pelo longo e olhos grandes. Ela é uma verdadeira princesa de colo e adora ser carregada por Pedro. Ela é um pouco tímida em relação a outros cães, mas se sente à vontade com outros chihuahuas. Bella também gosta de usar roupas elegantes e laços cor-de-rosa no cabelo.", "Pedro", "pet4.jpg")

pet5 = Perfil("Simba", "Simba é um gato siamês extremamente vocal. Ele adora ser o centro das atenções e não hesita em expressar suas opiniões com seus miados altos. Simba é um caçador nato, e seus brinquedos favoritos são penas e ratos de pelúcia. Ele é um gato curioso e adora explorar cada canto da casa.", "Carla", "pet5.jpeg")

pet6 = Perfil("Thor", "Thor é um labrador preto de dois anos de idade. Ele é um cachorro ativo e adora passar o tempo ao ar livre. Suas brincadeiras favoritas incluem pegar a bolinha e nadar no lago. Thor é conhecido por sua natureza amigável e por sua proteção. Mesmo com seu tamanho imponente, ele é um cachorro gentil e amoroso.", "Rafael", "pet6.jpg")

pet7 = Perfil("Daisy", "Daisy é uma coelhinha da raça Holland Lop de orelhas caídas. Ela tem uma pelagem macia e é muito fofa. Ela adora passar o tempo pulando e explorando o jardim. Daisy também é uma comilona e não resiste a cenouras frescas. Ela é uma coelhinha curiosa e brincalhona que traz muita alegria para a vida de Sofia.", "Sofia", "pet7.jpeg")

pet8 = Perfil("Rocky", "Rocky é um bulldog inglês de quatro anos de idade. Ele é um verdadeiro molosso, mas tem um coração doce. Rocky é um mestre em cochilar, especialmente no sofá. Ele é um verdadeiro cão de sofá e adora passar o tempo relaxando com sua família. Rocky também é conhecido por seu ronco alto, que sempre faz todos rirem.", "Diego", "pet8.jpg")

pet9 = Perfil("Nala", "Nala é uma cacatua das Filipinas muito falante e colorida. Ela adora cantar músicas alegres e imitar os sons que ouve em casa. Nala é uma ave curiosa e adora interagir com sua família humana. Ela é uma verdadeira artista quando se trata de entretenimento, e todos na casa adoram sua companhia.", "Isabela", "pet9.jpg")

pet10 = Perfil("Oliver", "Oliver é um gato preto de pelagem brilhante. Ele é um caçador nato e passa horas perseguindo moscas e brincando com pássaros de brinquedo. Oliver também é um gato independente que gosta de explorar o mundo ao seu redor. Ele é muito ágil e adora subir em móveis altos.", "Laura", "pet10.jpeg")

pet11 = Perfil("Charlie", "Charlie é um papagaio colorido e extravagante. Ele adora cantar e falar com seu dono, Gabriel. Charlie é um verdadeiro showman e sempre faz uma entrada triunfal na sala. Ele conhece várias palavras e frases e gosta de surpreender com suas habilidades linguísticas.", "Gabriel", "pet11.jpeg")

pet12 = Perfil("Daisy", "Daisy é uma tartaruga de estimação que adora nadar no seu pequeno aquário. Ela tem uma casca brilhante e gosta de relaxar nas pedras e tomar sol. Daisy é uma tartaruga tranquila e paciente que traz uma sensação de calma e serenidade para a vida de Lucas.", "Lucas", "pet12.jpg")







Perfis = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10]

@app.route("/")
def home():
    if "login" not in session:
        session["login"] = False

    return render_template("index.html", Perfis=Perfis)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        if request.form["nome"] == "usuario" and request.form["senha"] == "usuario":
            session["login"] = True
            return render_template("dashboard.html", Perfis=Perfis)
        else:
            return render_template("warning.html")
    elif request.method == "GET" and session["login"] == True:
        return render_template("dashboard.html", Perfis=Perfis)
    else:
        return render_template("warning.html")

@app.route("/curtidas/<nome_antigo>", methods=["GET"])
def curtidas(nome_antigo):
    for perfil in Perfis:
        if perfil.nome == nome_antigo:
            perfil_antigo = perfil
            break
    perfil_antigo.curtidas += 1
    return render_template("index.html", Perfis=Perfis)

@app.route("/logout")
def logout():
    if "login" in session:
        session["login"] = False

    return render_template("index.html", Perfis=Perfis)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():

    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        dono = request.form["dono"]
        imagem = request.files.get("imagem") 
        perfil = Perfil(nome, descricao, dono, imagem.filename)
        Perfis.append(perfil)



    return render_template("dashboard.html", Perfis=Perfis)


@app.route("/editar/<nome_antigo>", methods=["GET", "POST"])
def editar(nome_antigo):
    
    

    for perfil in Perfis:
        if perfil.nome == nome_antigo:
            perfil_antigo = perfil
            break

    if request.method == "POST":

        
        perfil_antigo.nome = request.form["nome"]
        perfil_antigo.descricao = request.form["descricao"]
        perfil_antigo.dono = request.form["dono"]
        if request.files["foto"]:
            imagem = request.files.get("foto")
            perfil_antigo.imagem_path = imagem.filename

        return render_template("dashboard.html", Perfis=Perfis)
    else:
        return render_template("editar.html", perfil=perfil_antigo)

@app.route("/excluir/<nome_antigo>", methods=["GET", "POST"])
def excluir(nome_antigo):

    for perfil in Perfis:
        if perfil.nome == nome_antigo:
            Perfis.remove(perfil)
    return render_template("dashboard.html", Perfis=Perfis)


if __name__ == '__main__':
    app.run(debug=True)     
