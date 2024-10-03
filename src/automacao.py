import pyautogui
import time
import threading
from typing import Tuple, List, Optional

# Variável global para controle de parada do programa
stop_program = False

def clicar_em_coordenadas(coordenadas: List[Optional[Tuple[int, int]]]) -> None:
    """
    Recebe uma lista de coordenadas e clica em cada uma delas, com um intervalo de 1.5 segundos.
    Se uma coordenada for None, imprime um aviso.
    """
    for coord in coordenadas:
        if coord is not None:
            try:
                pyautogui.click(coord)
                time.sleep(1.5)
            except Exception as e:
                print(f"Erro ao clicar na coordenação {coord}: {e}")
        else:
            print("Coordenação não encontrada.")

def localizar_botao(imagem_botao: str, confidence: float = 0.8) -> Optional[Tuple[int, int]]:
    """
    Localiza o centro de um botão na tela, baseado em uma imagem fornecida, repetindo até
    encontrar ou até que o programa seja parado.
    """
    while not stop_program:
        try:
            botao_pos = pyautogui.locateCenterOnScreen(imagem_botao, confidence=confidence)
            if botao_pos is not None:
                return botao_pos
            time.sleep(1.5)
        except Exception as e:
            print(f"Erro ao localizar botão {imagem_botao}: {e}")
    return None

def mover_para_posicao_1_e_scroll() -> None:
    """
    Move o cursor para a posição de um botão específico e realiza um scroll para baixo.
    """
    posicao1 = localizar_botao('src/assets/botoes/posicao1.png')
    if posicao1 is not None:
        pyautogui.moveTo(posicao1)
        pyautogui.scroll(-1000)

def executar_perda_colisao() -> None:
    """
    Executa uma sequência de ações específicas para perda de colisão.
    Identifica botões através de imagens e realiza interações automatizadas na tela.
    """
    primeiroClick = (1880, 642)
    segundoClick = (1751, 767)
    imagens_botoes = [
        'src/assets/botoes/botao3_perda_colisao.png',
        'src/assets/botoes/botao4_perda_colisao.png',
        'src/assets/botoes/botao5_perda_colisao.png',
        'src/assets/botoes/botao6_perda_colisao.png'
    ]
    passo_atual = 0
    while not stop_program:
        try:
            # Etapa inicial com dois cliques e scroll na tela
            if passo_atual == 0:
                clicar_em_coordenadas([primeiroClick, segundoClick])
                time.sleep(1.5)
                pyautogui.moveTo(1913, 536)
                pyautogui.scroll(-1000)
                time.sleep(0.5)
                pyautogui.scroll(-1000)
                passo_atual += 1
            # Loop sobre as imagens de botões e ações associadas
            for idx, img in enumerate(imagens_botoes):
                if passo_atual == idx + 1:
                    botao = localizar_botao(img, confidence=0.9)
                    if botao is not None:
                        clicar_em_coordenadas([botao])
                        pyautogui.moveTo(1034, 179)
                        if img == 'src/assets/botoes/botao4_perda_colisao.png':
                            passo_atual += 1
                        elif img == 'src/assets/botoes/botao5_perda_colisao.png':
                            pyautogui.write("Ao arquivo, aguardando novos fatos.")
                            passo_atual += 1
                        elif img == 'src/assets/botoes/botao6_perda_colisao.png':
                            passo_atual += 1
                        else:
                            passo_atual += 1
                    else:
                        print(f"Erro ao localizar {img}, retornando ao passo anterior.")
                        passo_atual = max(0, passo_atual - 1)
                        time.sleep(2)
            if passo_atual >= len(imagens_botoes) + 1:
                time.sleep(4)
                passo_atual = 0
        except Exception as e:
            print(f"Erro: {e}. Retornando ao início.")
            passo_atual = 0
            time.sleep(4)

def executar_estelionato() -> None:
    """
    Executa uma sequência de ações específicas para o caso de estelionato.
    Similar à função executar_perda_colisao, mas com diferentes botões e mensagens.
    """
    primeiroClick = (1880, 642)
    segundoClick = (1751, 767)
    imagens_botoes = [
        'src/assets/botoes/botao3_estelionato.png',
        'src/assets/botoes/botao4_estelionato.png',
        'src/assets/botoes/botao5_estelionato.png',
        'src/assets/botoes/botao6_estelionato.png'
    ]
    passo_atual = 0
    while not stop_program:
        try:
            # Etapa inicial com dois cliques e scroll na tela
            if passo_atual == 0:
                clicar_em_coordenadas([primeiroClick, segundoClick])
                time.sleep(1.5)
                pyautogui.moveTo(1913, 536)
                pyautogui.scroll(-1000)
                time.sleep(0.5)
                pyautogui.scroll(-1000)
                passo_atual += 1
            # Loop sobre as imagens de botões e ações associadas
            for idx, img in enumerate(imagens_botoes):
                if passo_atual == idx + 1:
                    botao = localizar_botao(img, confidence=0.9)
                    if botao is not None:
                        clicar_em_coordenadas([botao])
                        if img == 'src/assets/botoes/botao4_estelionato.png':
                            pyautogui.moveTo(1034, 179)
                            passo_atual += 1
                        elif img == 'src/assets/botoes/botao5_estelionato.png':
                            pyautogui.moveTo(1034, 179)
                            pyautogui.write("Aguardando representação/requerimento da vítima.")
                            passo_atual += 1
                        elif img == 'src/assets/botoes/botao6_estelionato.png':
                            passo_atual += 1
                        else:
                            passo_atual += 1
                    else:
                        print(f"Erro ao localizar {img}, retornando ao passo anterior.")
                        passo_atual = max(0, passo_atual - 1)
                        time.sleep(2)
            if passo_atual >= len(imagens_botoes) + 1:
                time.sleep(4)
                passo_atual = 0
        except Exception as e:
            print(f"Erro: {e}. Retornando ao início.")
            passo_atual = 0
            time.sleep(4)
