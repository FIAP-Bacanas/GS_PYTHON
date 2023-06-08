def exibir_menu():
  print("=== MENU ===")
  print("1. Início")
  print("2. Produtos")
  print("3. Vídeos")
  print("4. Saiba mais")
  print("5. Sobre nós")


def iniciar():
  print("Bem vindo ao nosso site")


def exibir_produtos():
  print("=== PRODUTOS ===")
  print("1. Tomate")
  print("2. Cebola")
  print("3. Pepino")
  print("4. Chuchu")
  print("5. Rastelo")
  print("6. Adubo")
  print("7. Terra")
  print("8. Luva de proteção")


# venda de produtos
def comprar_produto(produto):
  print("Você selecionou o", produto)


def pagina_produto():
  while True:
    exibir_produtos()
    opcao = input("Selecione um produto (1-8) ou 'q' para sair: ")
    if opcao == 'q':
      break
    elif opcao in ['1', '2', '3', '4', '5', '6', '7', '8']:
      produtos = [
        'Tomate', 'Cebola', 'Pepino', 'Chuchu', 'Rastelo',
        'Adubo', 'Terra', 'Luva de proteção'
      ]
      indice = int(opcao) - 1
      comprar_produto(produtos[indice])
    else:
      print("Opção inválida. Por favor, selecione novamente.")


def exibir_video():
    print("=== MENU DE VÍDEOS ===")
    print("1. Categoria 1")
    print("2. Categoria 2")
    print("3. Categoria 3")
    print("4. Categoria 4")

def assistir_video(categoria, video):
    print(f"Você está assistindo ao vídeo da {categoria}: {video}")

def pagina_videos():
    while True:
        exibir_video()
        opcao = input("Selecione uma categoria (1-4) ou 'q' para sair: ")
        if opcao == 'q':
            break
        elif opcao in ['1', '2', '3', '4']:
            categoria = f"Categoria {opcao}"
            videos = {
                '1': ['Vídeo 1A', 'Vídeo 1B', 'Vídeo 1C'],
                '2': ['Vídeo 2A', 'Vídeo 2B', 'Vídeo 2C'],
                '3': ['Vídeo 3A', 'Vídeo 3B', 'Vídeo 3C'],
                '4': ['Vídeo 4A', 'Vídeo 4B', 'Vídeo 4C']
            }
            exibir_videos(videos[opcao], categoria)
        else:
            print("Opção inválida. Por favor, selecione novamente.")

def exibir_videos(videos, categoria):
    print(f"=== Vídeos da {categoria} ===")
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video}")
    print()

    opcao = input("Selecione um vídeo (1-3) ou 'q' para voltar: ")
    if opcao == 'q':
        return
    elif opcao in ['1', '2', '3']:
        indice = int(opcao) - 1
        assistir_video(categoria, videos[indice])
    else:
        print("Opção inválida. Por favor, selecione novamente.")

# Pagina saiba mais
def exibir_pagina_artigos():
  print("=== Artigos ===")
  print("1. ONU")
  print("2. Agricultura Urbana")
  print("3. Importancia da Agricultura")
  print("4. Sustentabilidade")
  print()


def exibir_artigo(titulo):
  print("===", titulo, "===")
  if titulo == "ONU":
    print("A Cartilha da ONU 2030 para agricultura promove o desenvolvimento sustentável no setor agrícola. Destaca a importância da produção de alimentos de forma ambientalmente consciente, o acesso equitativo a recursos agrícolas, o apoio aos agricultores familiares, a redução do desperdício de alimentos e o fortalecimento da resiliência agrícola diante das mudanças climáticas.")
  elif titulo == "Agricultura Urbana":
    print("A agricultura urbana é uma prática que envolve o cultivo de alimentos nas áreas urbanas. Ela traz diversos benefícios, como o acesso a alimentos frescos e saudáveis, a redução da pegada ambiental, o fortalecimento da comunidade e a criação de espaços verdes em ambientes urbanos densos. Promove a sustentabilidade e a segurança alimentar local.")
  elif titulo == "Importancia da Agricultura":
    print("A agricultura desempenha um papel vital na sociedade, fornecendo alimentos essenciais para a população global. Além disso, impulsiona economias, cria empregos e contribui para o desenvolvimento rural. A agricultura sustentável também preserva os recursos naturais, promove a segurança alimentar e fortalece a resiliência diante dos desafios climáticos.")
  elif titulo == "Sustentabilidade":
    print("A sustentabilidade é fundamental para garantir o equilíbrio entre o desenvolvimento humano e a preservação do meio ambiente. Envolve ações que visam suprir as necessidades atuais sem comprometer as gerações futuras. Promover a eficiência energética, a conservação dos recursos naturais e a adoção de práticas ambientalmente responsáveis são pilares essenciais da sustentabilidade.")
  print()
 


def pagina_artigos():
  while True:
    exibir_pagina_artigos()
    opcao = input("Selecione um artigo (1-4) ou 'q' para sair: ")
    if opcao == 'q':
      break
    elif opcao == '1':
      exibir_artigo("ONU")
    elif opcao == '2':
      exibir_artigo("Agricultura Urbana")
    elif opcao == '3':
      exibir_artigo("Importancia da Agricultura")
    elif opcao == '4':
      exibir_artigo("Sustentábilidade")
    else:
      print("Opção inválida. Por favor, selecione novamente.")


# Sobre nos pagina
def exibir_sobre_nos(nome, idade, ocupacao):
  print("=== Sobre Nós ===")
  print("Nome:", nome)
  print("Idade:", idade)
  print("Ocupação:", ocupacao)
  print()


def pagina_sobre_nos():
  pessoas = [{
    'nome': 'Eduardo Pielich',
    'idade': 18,
    'ocupacao': 'Engenheiro de Software'
  }, {
    'nome': 'David Dennuci',
    'idade': 18,
    'ocupacao': 'Engenheiro de Software'
  }, {
    'nome': 'Igor Tellini',
    'idade': 18,
    'ocupacao': 'Engenheiro de Software'
  }, {
    'nome': 'João Rodrigo Nogueira',
    'idade': 18,
    'ocupacao': 'Engenheiro de Software'
  }, {
    'nome': 'Victor Hugo Andrade',
    'idade': 18,
    'ocupacao': 'Engenheiro de Software'
  }]

  for pessoa in pessoas:
    exibir_sobre_nos(pessoa['nome'], pessoa['idade'], pessoa['ocupacao'])


def menu():
  while True:
    exibir_menu()
    opcao = input("Selecione uma opção (1-5): ")
    if opcao == '1':
      iniciar()
    elif opcao == '2':
      pagina_produto()
    elif opcao == '3':
      pagina_videos()
    elif opcao == '4':
      pagina_artigos()
    elif opcao == '5':
      pagina_sobre_nos()
    else:
      print("Opção inválida. Por favor, selecione novamente.")

iniciar()
menu()
