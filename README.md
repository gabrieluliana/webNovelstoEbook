
# Web Novels to Ebook

---

## Proposta

Esse programa foi desenvolvido para facilitar a leitura pessoal de light novels disponiveis e publicadas pelos proprios autores em plataformas como [Royal Road](https://www.royalroad.com/home), o software pode ser utilizado para coletar os capitulos da série que você deseja e transformá-los em um eBook com formato `.EPUB` em seguida você pode enviar para seu dispositivo Kindle ou outro leitor de ebooks.

### :loudspeaker: ALERTA IMPORTANTE :loudspeaker:

Sempre procure e dê preferência ao livro original do autor se ele já estiver disponível, além de você estar ajudando financeiramente e dando publicidade ao autor muitos erros de formatação, continuidades e outros erros de escrita são corrigidos e melhorados na versão oficial, além disso, o autor tem o direito de escolher como ele quer que seu livro seja lido, seja em um site ou em um formato de ebook, respeite a escolha do autor.

Esse programa não tem como intuíto e motivação a pirataria, ele é apenas uma ferramenta para facilitar a leitura de livros que já estão disponíveis gratuitamente, ou para aqueles que querem ler offline sem depender de uma conexão com a internet.

Por isso, sempre que possível, procure o livro original do autor e apoie o trabalho dele, seja comprando seus livros, assinando seu Patreon, fazendo doações para o autor e para o site onde as obras são publicadas ou compartilhando o link para o site onde ele está disponível.

:warning: **É estritamente proibido utilizar esse programa para coletar, distribuir ou vender livros de dos autores reais para seu próprio benefício** :warning:

---

## Executando Localmente

Clone o projeto

```bash
  git clone https://github.com/gabrieluliana/royalroadScrapperToKindle
```

vá para o diretório do projeto

```bash
  cd my-project
```

ative o ambiente virtual

```bash
  pipenv shell
```

instale as dependências

```bash
  pipenv install
```

Execute o arquivo

```bash
  pipenv run python main.py
```

## Exemplo de uso

### Livro: :book: [Mother of Learning](https://amzn.to/4coNVyA) - Domagoj Kurmaic :book:

Esse livro é um dos meus favoritos, ele já está disponível para a venda pelo proprio autor na loja da [Amazon](https://amzn.to/4coNVyA) e audiobook na [Audible](https://www.audible.com.br/pd/Mother-of-Learning-Arc-1-Audiolivro/B0BTGB7VPS?tag=gazouli-20&source_code=ASSGB149080119000H&share_location=pdp).

E ainda está disponível no [Royal Road](https://www.royalroad.com/fiction/21220/mother-of-learning), então vamos utilizá-lo como exemplo para mostrar como o programa funciona.

O programa irá solicitar a URL do capitulo inicial a partir do qual voce deseja coletar o livro que você deseja coletar, aqui eu utilizo o capitulo 1 do livro, mas você pode escolher qualquer outro capitulo para iniciar a coleta, o programa irá coletar os capitulos seguintes a partir do capitulo inicial que você escolher.

```bash
https://www.royalroad.com/fiction/21220/mother-of-learning/chapter/301778/1-good-morning-brother
```

**Em seguida insira quantos capitulos deseja**, você pode escolher um número especifico ou colocar um numero mais alto, caso acabe os capitulos disponíveis o programa irá coletar apenas os capitulos disponiveis e gerar o ebook normalmente.

Nesse caso do livro Mother of Learning, existem 109 capitulos disponiveis no Royal Road, mas eu coloquei o numero 120 para coletar todos os capitulos disponíveis.

```bash
  120
```

 O programa irá coletar todos os capitulos e gerar um arquivo `[nome_do_livro].EPUB` no diretório ``\books\`` do projeto.

## Opcional - Alterando a formatação do Ebook

Utilizando o [Calibre](https://calibre-ebook.com/) edite o ebook e adicione suas preferencias de formatação de texto.

Eu utilizo como padrão um arquivo `styles.css` linkado com todos os capitulos com o seguinte código

```css
@charset "utf-8";

p, span {
 text-align: justify;
 line-height: 1em; 
 margin-bottom: 0.7em;
 margin-top: 0;
 text-indent: 2em;
}
```

## Casos aplicados Funcionando

- :star2: [Royal Road](royalroad.com) - Intuito inicial do projeto

 Casos pontuais em que utilizei variações do código para coletar livros de outros sites, mas o foco principal é o Royal Road, onde a maioria dos livros que eu leio estão disponíveis.

- [Worm - Web Series](https://parahumans.wordpress.com/)

- [Novelight](https://novelight.net/)

## Direitos Autorais

Esse programa é de código aberto e pode ser utilizado por qualquer pessoa, mas é importante lembrar que ele deve ser utilizado apenas para coletar livros que estão disponíveis gratuitamente e não para coletar livros de autores reais para distribuição ou venda sem a permissão do autor.
