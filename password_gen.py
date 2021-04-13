import random
import PySimpleGUI as sg
#pip install PySimpleGUI
import os
#pip install playsound
#from playsound import playsound


class PassGen:
    def __init__(self):
        sg.theme('Black')
        #playsound('musica.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
            sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuario', size=(10, 1)),
            sg.Input(key='Usuario',size=(20, 1))],
            [sg.Text('Quantidade de caracteres'),
            sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')],
        ]
        # Declarar Janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
        
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}, Usuario: {valores['Usuario']}, nova senha: {nova_senha}")
        print('Senha salva para o arquivo "senhas.txt"')



gen = PassGen()
gen.Iniciar()