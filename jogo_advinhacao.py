import time
import random
import textwrap
import os
import pyfiglet



# lore do jogo
def synopsis():
    synopsis = "Nesta história você assume o papel de um bobo da corte que foi injustamente acusado e sentenciado à morte " \
               "por um crime que não cometeu. Pela alegria e felicidade proporcionada à corte de Arvandoria nos seus " \
               "anos de serviço, o Rei Thalathir oferece uma chance de perdão, acerte o número secreto com apenas " \
               "algumas tentativas e sua vida será salva e poderá voltar a ser o bobo da corte real. No entanto, " \
               "se você falhar em acertar o número, será enforcado sem piedade. Sabendo da injustiça, " \
               "seu amigo Avidrak o mago do castelo, lhe presenteia com um amuleto mágico que lhe dará dicas sobre o " \
               "número secreto.Mas você terá que usar suas habilidades de dedução e lógica para salvar sua vida."

    text_width(synopsis)


def intro(player_name, attempts):
    intro = f"{player_name} caminhava com as mãos amarradas em frente ao seu corpo, escoltado por dois guardas com " \
            f"lanças. Eles atravessaram o salão principal do castelo de Arvandoria, onde a realeza recebe os convidados " \
            f"ilustres e sedia bailes majestosos. As paredes de pedra escura e as tapeçarias ricas em cores retratavam " \
            f"as histórias da linhagem real e dos grandes feitos dos heróis da nação. O chão de pedra polida refletia o " \
            f"brilho das tochas acesas ao longo do caminho.Finalmente, chegaram à grande porta dupla de carvalho, " \
            f"que levava ao trono de Thalathir. {player_name} inspirou profundamente sabendo que sua vida estava em jogo. " \
            f"Os guardas empurraram as portas e o conduziram até o trono, onde o rei estava sentado com uma expressão " \
            f"séria no rosto.'{player_name}, bobo da corte real, você foi acusado de um crime grave e será julgado aqui, " \
            f"nesse momento', disse o rei Thalathir, levantando-se do trono. Você é acusado de roubo à coroa. Como réu, " \
            f"você tem o direito de se defender. O que você tem a dizer em sua defesa?' {player_name} engoliu em seco e " \
            f"ajoelhou-se perante o rei. 'Vossa Majestade, eu sou inocente. Eu juro pelos meus anos de lealdade à corte e " \
            f"pelos Deuses que não cometi tal crime.'O rei acenou com a cabeça. 'Muito bem, {player_name}.Vou lhe " \
            f"oferecer uma chance de perdão. Aqui está o meu desafio: acerte o número entre 1 e 100 dentro deste " \
            f"envelope. Se você adivinhar o número em {attempts} tentativas, sua vida será poupada e voltará ao seu papel " \
            f"de bobo da corte. Se você falhar em adivinhar o número, sua sentença será cumprida.'{player_name} sentiu um " \
            f"arrepio percorrer sua espinha. Ele sabia que suas chances eram baixas. Mas antes que ele pudesse falar " \
            f"qualquer coisa, o mago Avidrak, amigo de longa data, apareceu do seu lado e cochichou em seu ouvido.'" \
            f"{player_name}, aqui está um amuleto mágico que o ajudará a adivinhar o número secreto', disse o mago, " \
            f"entregando um pequeno objeto em forma de lua crescente.{player_name} agradeceu ao amigo e escondeu o " \
            f"amuleto em seu bolso, esperando que o rei não tivesse notado.'Eu aceito seu desafio, Vossa Majestade', " \
            f"disse {player_name}, determinado a salvar sua vida.O rei sorriu satisfeito.'Muito bem, {player_name}. " \
            f"Comecemos o jogo.'"

    text_width(intro)


def final_1(guess, player_name):
    final_1 = f"{player_name} respirou fundo e usou o amuleto mágico que o amigo lhe havia dado. Ele sentiu uma " \
              f"sensação estranha percorrer seu corpo e um lampejo de confiança invadiu sua mente - o número " \
              f"secreto era {guess}, o mesmo número que o dia em que nasceu. {player_name} sentiu um sorriso se " \
              f"formar em seu rosto enquanto proferia: '{guess}!' O rei olhou para ele, surpreso, e depois olhou " \
              f"para um papel em suas mãos. 'Parabéns, {player_name}! Você acertou! A sua vida será poupada e " \
              f"você voltará ao seu papel de bobo da corte'. {player_name} mal podia acreditar no que havia " \
              f"acontecido, sentiu um alívio enorme e uma gratidão ainda maior pelo amigo mago que lhe concedera " \
              f"o amuleto mágico. Após a vitória no desafio proposto pelo rei Thalathir, {player_name} foi " \
              f"perdoado e recebeu o seu antigo papel como bobo da corte real de volta. A partir daquele momento, " \
              f"{player_name} se tornou mais cuidadoso e mais sábio em relação à sua vida. Ele aprendeu a ser " \
              f"grato pelas pessoas que o amavam e valorizavam, e a nunca mais se envolver em qualquer atividade " \
              f"suspeita. A sua vitória no desafio do rei Thalathir, juntamente com o seu amuleto mágico, " \
              f"o tornou um pouco famoso entre os cidadãos de Arvandoria. As pessoas passaram a se referir a ele " \
              f"como 'o bobo sortudo' e a lhe oferecer presentes em sinal de gratidão pela sua divertida " \
              f"companhia e pela sorte que ele trouxe ao reino. {player_name} também passou a ter mais respeito e " \
              f"admiração pelos magos e seus poderes. Ele se aproximou do mago Avidrak, que se tornou o seu amigo " \
              f"e mentor. Através da orientação de Avidrak, {player_name} começou a aprender mais sobre magia e " \
              f"se tornou um mago iniciante. Com o passar do tempo, {player_name} se tornou um membro valioso da " \
              f"corte real de Arvandoria. Ele entreteve a realeza e os convidados com suas habilidades divertidas " \
              f"e se tornou um conselheiro confiável do rei Thalathir. {player_name} se tornou conhecido por seu " \
              f"humor, inteligência e sabedoria, e sua presença foi sempre bem-vinda em qualquer evento " \
              f"importante do reino. Ao longo dos anos, {player_name} se apaixonou por uma bela dama da corte " \
              f"chamada Isadora, e os dois se casaram em uma cerimônia majestosa na presença do rei e da rainha. " \
              f"{player_name} e Isadora tiveram três filhos e, juntos, construíram uma vida feliz e próspera. " \
              f"{player_name} nunca mais teve problemas com a lei ou se envolveu em situações perigosas, " \
              f"e viveu o resto de seus dias como um homem sábio e respeitado no reino de Arvandoria. Ele foi " \
              f"lembrado por muitos anos como um exemplo de superação e de como as pessoas podem mudar suas vidas"
    text_width(final_1)


def final_2(guess, player_name):
    final_2 = f"{player_name} respirou fundo e usou o amuleto mágico que o amigo lhe havia dado. Ele sentiu um " \
              f"arrepio percorrer seu corpo e um lampejo de esperança invadir sua mente - o número secreto era" \
              f" {guess}. {player_name} encheu-se de confiança renovada e disse: '{guess}!'. O rei olhou para ele, " \
              f"sem expressão, e depois olhou para um papel em suas mãos. 'Sinto muito, {player_name}, " \
              f"mas sua resposta está incorreta. A sentença será cumprida.' O rei sinalizou para os guardas, " \
              f"que imediatamente agarraram {player_name} e o arrastaram para fora do salão. {player_name} gritou, " \
              f"implorando por misericórdia, mas sua voz foi abafada pelos gritos da multidão que se reunira do lado " \
              f"de fora. Os guardas o levaram até a praça da cidade, onde uma multidão eufórica o esperava. Ele foi " \
              f"jogado no centro da praça e amarrado a um poste. A multidão zombava e apedrejava-o, enquanto " \
              f"{player_name} tentava desesperadamente se libertar das cordas que o prendiam. Mas era tarde demais. " \
              f"Um homem raivoso se aproximou e brandiu uma espada, contra o bob da corte. O corpo de {player_name}" \
              f" caiu no chão, enquanto a multidão celebrava sua morte. O mago Avidrak assistiu a tudo em " \
              f"silêncio, impotente para salvar seu amigo. Ele viu como {player_name} implorou por misericórdia, " \
              f"e como seus pedidos foram ignorados. E, por fim, ele viu {player_name} morrer injustamente condenado " \
              f"por um crime que não cometeu. A morte de {player_name} seria esquecida em breve, como tantas outras " \
              f"que já haviam ocorrido naquele lugar. Avidrak chorou silenciosamente enquanto a multidão aplaudia e " \
              f"ria do último espetáculo de {player_name}. Ele sabia que nunca mais seria o mesmo depois de " \
              f"testemunhar a morte de seu amigo. Sabia que sempre carregaria consigo a dor da perda, e que nada " \
              f"jamais poderia curar a ferida que a morte de {player_name} deixou em seu coração."
    text_width(final_2)


#Funções visuais
def time_sleep():
    time.sleep(3)

def auto_type(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()


def text_width(text):
    wrapper = textwrap.TextWrapper(width=80)
    word_list = wrapper.wrap(text=text)
    for element in word_list:
        auto_type(element)


# Respostas
def invalid_input():
    print("")
    auto_type("Sem gracinhas, digite um valor válido")
    print("")



def guess_feedback(guess_type):
    if guess_type == "high":
        auto_type("Você errou! Você sente uma vibração fria percorrer seu corpo, indicando que o número secreto é menor "
                  "que o seu chute.")
    elif guess_type == "low":
        auto_type("Você errou! Uma onda de calor toma conta de você, indicando que o número secreto é maior que o "
                  "seu chute.")

def whats_your_guess():
    auto_type("Mostre sua astúcia e descubra o número de 1 a 100 protegido pela coroa:")


# Estruturas
def home():
    text = pyfiglet.figlet_format("Bem vindo ao \nReino de Arvandoria!",justify = "center", font="rectangles")
    print("-*" * 40)
    print(text)
    print("-*"*40)



def name():
    auto_type("Qual será seu nome de jogador?")
    player_name = input("")
    player_name = player_name.title()
    return player_name

def level(player_name):
    while True:
        auto_type(f"Em que nível você se atreve a jogar, {player_name}?")
        print("")
        auto_type("(1) Treino do Bobo da Corte")
        auto_type("(2) Desafio dos Cavaleiros")
        auto_type("(3) Julgamento do Dragão")
        print("")
        try:
            auto_type("Escolha o seu desafio:")
            level = int(input(""))
            if level == 1:
                attempts = 8
                break
            elif level == 2:
                attempts = 5
                break
            elif level == 3:
                attempts = 3
                break
            else:
                invalid_input()
                continue

        except ValueError:
            invalid_input()
            continue

    return attempts

def end_game():
    while True:
        print("\n")
        play_again = input("Deseja jogar novamente? (s/n)")
        print("")
        if play_again.lower() == "s":
            play_game()
        elif play_again.lower() == "n":
            print("Obrigado por jogar! Até a próxima!")
            break
        else:
            print("Por favor, digite 's' para jogar novamente ou 'n' para sair.")


def play_game():
    secret_number = random.randrange(1, 101)

    home()
    print("")
    synopsis()
    print("")
    player_name = name()
    attempts = level(player_name)
    os.system('cls')

    intro(player_name, attempts)


    for rodada in range(1, attempts + 1):
        time_sleep()
        os.system('cls')
        print("")
        auto_type("Tentativa {} de {}:".format(rodada, attempts))
        print("")

        while True:
            try:
                whats_your_guess()
                print()
                guess_str = input("")
                guess = int(guess_str)

                hit = guess == secret_number
                heigher = guess > secret_number
                lower = guess < secret_number
                
                if guess_str.isnumeric():
                    if (hit):   
                        os.system('cls')
                        final_1(guess, player_name)
                    else:
                        if (heigher):
                            guess_feedback("high")
                            os.system('cls')
                        elif (lower):
                            guess_feedback("low")
                            os.system('cls')


                    if (rodada == attempts):
                            os.system('cls')
                            final_2(guess, player_name)

                    if guess < 1 or guess > 100:
                        raise ValueError
                    break
                else:
                    raise ValueError
            except ValueError:
                print("")
                auto_type("Tentativa {} de {}:".format(rodada, attempts))
                invalid_input()
                continue
    
    

    

    end_game()


if (__name__ == "__main__"):
    play_game()
