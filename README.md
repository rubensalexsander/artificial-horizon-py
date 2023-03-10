# artificial-horizon-py
Biblioteca que cria horizonte artificial para projetos em Python.

Passos:
- Estudar e resumir livro "Fundamentos da Matemática 3 - Trigonometria".
- Construir e disponibilizar biblioteca que resuma os conceitos de trigonometria do livro.
- Construir e disponibilizar biblioteca py-artificial-horizon que use a biblioteca citada a cima e que tenha suporte para Tkinter e PyGame.
- Descrever passos do projeto neste repositório.

# Idéia básica da biblioteca:
> horizon = instancia_do_objeto(center_place)

> horizon.set_angles(x, y, z)

No "loop de jogo":
> result = horizon.update(x, y, z)

"result" será uma array com diversos objetos "line" com seus pontos já definidos e poderão ser, facilmente escritos fazendo um loop for.

Será também possível, no momento da instância do objeto, passar um objeto "canvas" (se estiver usando Tkinter) ou "pygame.display" (se estiver usando PyGame). Dessa forma o horizonte artificial será escrito automaticamente no objeto repassado.

# Imagens de referância para o modelo do projeto (serão reproduzidas apenas as informações de giroscópio):

![ha1](https://user-images.githubusercontent.com/89158806/224062091-6abca9c8-db19-4894-a94b-1f9382140de4.png)

![ha2](https://user-images.githubusercontent.com/89158806/224064546-fdbdb779-8a98-44c8-aecd-e061db199c48.png)

![ha3](https://user-images.githubusercontent.com/89158806/224063969-9dd2bca7-63a0-440e-af16-165928e2968f.png)
