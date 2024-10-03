import pyautogui
import time
import threading
from typing import Tuple, List, Optional

stop_program = False

def clicar_em_coordenadas(coordenadas: List[Optional[Tuple[int, int]]]) -> None:
    """Clique nas coordenadas especificadas."""
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
    """Localiza o botão na tela."""
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
    """Move para a posição 1 e realiza o scroll."""
    posicao1 = localizar_botao('/assets/botoes/posicao1.png')
    if posicao1 is not None:
        pyautogui.moveTo(posicao1)
        pyautogui.scroll(-1000)

import time

import time

def executar_perda_colisao() -> None:
    """Executa as ações de Perda-Colisão."""
    primeiroClick = (1880, 642)
    segundoClick = (1751, 767)
    imagens_botoes = [
        'assets/botoes/botao3_perda_colisao.png',  
        'assets/botoes/botao4_perda_colisao.png',  
        'assets/botoes/botao5_perda_colisao.png',  
        'assets/botoes/botao6_perda_colisao.png'  
    ]

    # Estado para controlar qual passo está sendo executado
    passo_atual = 0

    while not stop_program:
        try:
            # Executa os cliques iniciais
            if passo_atual == 0:
                clicar_em_coordenadas([primeiroClick, segundoClick])
                time.sleep(1.5)
                pyautogui.moveTo(1913, 536)
                pyautogui.scroll(-1000)
                time.sleep(0.5)
                pyautogui.scroll(-1000)
                passo_atual += 1

            # Processa cada botão em ordem
            for idx, img in enumerate(imagens_botoes):
                if passo_atual == idx + 1:
                    botao = localizar_botao(img, confidence=0.9)
                    if botao is not None:
                        clicar_em_coordenadas([botao])
                        pyautogui.moveTo(1034, 179)  # Movimento padrão após clicar no botão

                        # Verifica e executa as ações específicas dos botões
                        if img == 'assets/botoes/botao4_perda_colisao.png':  # Botão 2
                            pass  # Ação específica pode ser adicionada aqui, se necessário
                            passo_atual += 1
                        elif img == 'assets/botoes/botao5_perda_colisao.png':  # Botão 3
                            pyautogui.write("Ao arquivo, aguardando novos fatos.")  # Mensagem específica do botão 3
                            passo_atual += 1
                        elif img == 'assets/botoes/botao6_perda_colisao.png': 
                            passo_atual += 1
                        else:
                            passo_atual += 1
                    else:
                        # Se o botão não for encontrado, volta ao passo anterior
                        print(f"Erro ao localizar {img}, retornando ao passo anterior.")
                        passo_atual = max(0, passo_atual - 1)
                        time.sleep(2)

            # Reinicia a sequência após concluir todos os passos
            if passo_atual >= len(imagens_botoes) + 1:
                time.sleep(4)  # Pausa de 4 segundos antes de reiniciar o loop
                passo_atual = 0  # Reseta para recomeçar o loop

        except Exception as e:
            print(f"Erro: {e}. Retornando ao início.")
            passo_atual = 0
            time.sleep(4)




def executar_estelionato() -> None:
    """Executa as ações de Estelionato."""
    primeiroClick = (1880, 642)
    segundoClick = (1751, 767)
    imagens_botoes = [
        'assets/botoes/botao3_estelionato.png',  
        'assets/botoes/botao4_estelionato.png',  
        'assets/botoes/botao5_estelionato.png',  
        'assets/botoes/botao6_estelionato.png'  
    ]

    # Estado para controlar qual passo está sendo executado
    passo_atual = 0

    while not stop_program:
        try:
            # Executa os cliques iniciais
            if passo_atual == 0:
                clicar_em_coordenadas([primeiroClick, segundoClick])
                time.sleep(1.5)
                pyautogui.moveTo(1913, 536)
                pyautogui.scroll(-1000)
                time.sleep(0.5)
                pyautogui.scroll(-1000)
                passo_atual += 1

            # Processa cada botão em ordem
            for idx, img in enumerate(imagens_botoes):
                if passo_atual == idx + 1:
                    botao = localizar_botao(img, confidence=0.9)
                    if botao is not None:
                        clicar_em_coordenadas([botao])

                        # Verifica e executa as ações específicas dos botões
                        if img == 'assets/botoes/botao4_estelionato.png':
                            pyautogui.moveTo(1034, 179)  # Moveto após o botão 4
                            passo_atual += 1
                        elif img == 'assets/botoes/botao5_estelionato.png':
                            pyautogui.moveTo(1034, 179)  # Moveto após o botão 5
                            pyautogui.write("Aguardando representação/requerimento da vítima.")
                            passo_atual += 1
                        elif img == 'assets/botoes/botao6_estelionato.png':
                            passo_atual += 1
                        else:
                            passo_atual += 1
                    else:
                        # Se o botão não for encontrado, volta ao passo anterior
                        print(f"Erro ao localizar {img}, retornando ao passo anterior.")
                        passo_atual = max(0, passo_atual - 1)
                        time.sleep(2)

            # Reinicia a sequência após concluir todos os passos
            if passo_atual >= len(imagens_botoes) + 1:
                time.sleep(4)
                passo_atual = 0  # Reseta para recomeçar o loop

        except Exception as e:
            print(f"Erro: {e}. Retornando ao início.")
            passo_atual = 0
            time.sleep(4)

