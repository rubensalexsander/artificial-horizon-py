
# artificial-horizon-py
Biblioteca que cria horizonte artificial para projetos em Python.

Passos:
- Estudar e resumir livro "Fundamentos da Matemática 3 - Trigonometria". ✅
- Construir e disponibilizar biblioteca py-artificial-horizon que tenha suporte para Tkinter e PyGame. ✅
- Descrever passos do projeto neste repositório. ✅

# Idéia básica da biblioteca:
- Instanciar o objeto:

> horizon = ArtificialHorizon(vortex, size)

*(vortex:Ponto central do instrumento, size: Tamanho do instrumento)*

*Atributo tk_canvas: Recebe um objeto do tipo "Canvas", da biblioteca Tkinter, em que escreve o horizonte automaticamente quando o método "horizon.update()" é chamado.*

*Atributo pygame_display: Recebe um objeto do tipo "pygame.display", da biblioteca Pygame, em que escreve o horizonte automaticamente quando o método "horizon.update()" é chamado.*


- Atualizar no "loop de jogo":

> horizon_lines = horizon.update(angle_value)

"horizon_lines" será uma array que contém outras arrays que são linhas que devem ser desenhadas na tela fazendo um loop for.

    horizon_lines[0] -> [ponto1, ponto2]

Uma linha pode ser definida por 2 pontos.

    

    horizon_lines[0][0] -> [10, 20] (Valores hipotéticos de um dos pontos da linha)

Caso já tenha passado o atributo tk_canvas ou pygame_display, não será nessessário armazenar as linhas na variável "horizon_lines":

> horizon.update(angle_value)

# Imagens de referância para o modelo do projeto (serão reproduzidas apenas as informações de giroscópio):

![ha1](https://user-images.githubusercontent.com/89158806/224062091-6abca9c8-db19-4894-a94b-1f9382140de4.png)

![ha3](https://user-images.githubusercontent.com/89158806/224063969-9dd2bca7-63a0-440e-af16-165928e2968f.png)

# Resultados:

- Primeira versão:

[Screencast from 2023-03-10 11-31-47.webm](https://user-images.githubusercontent.com/89158806/224342671-4f923eca-90cc-48aa-9bd3-333cb903c19c.webm)

- Segunda versão: 

*Adicionado blur na atualização do ângulo que deixa a atualização mais suave.*

*Adicionado text que descreve o ângulo do objeto.*

*Outras modificações*

[Screencast from 2023-03-10 23-19-02.webm](https://user-images.githubusercontent.com/89158806/224460282-9708025c-ab3c-4ff3-a1fc-94791316bd6e.webm)

*O horizonte no resultado foi utilizado em um projeto de robótica privado que monitora sensores de um arduino pela porta serial e utiliza C++.*

- Terceira versão:

*Adicionado eixo x.*

[Screencast from 2023-03-13 18-05-19.webm](https://user-images.githubusercontent.com/89158806/224832443-1b812237-da87-4367-8e88-acf45553ff89.webm)


