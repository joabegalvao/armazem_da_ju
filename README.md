# Armazém da Ju | Landing page

Página única, estática, em HTML, CSS e JavaScript puro. Não há etapa de build
nem dependências de execução: basta servir a pasta.

## Como visualizar

```bash
# na raiz do projeto
python3 -m http.server 4175
# abra http://localhost:4175
```

Qualquer servidor estático funciona (Nginx, Apache, Netlify, Vercel, Hostinger).
Publique `index.html` e a pasta `assets/`. A pasta `tools/` não precisa ir para
o servidor.

### Materiais de origem

Os arquivos enviados pelo cliente ficam reunidos na pasta
`materiais-de-origem/`, que não faz parte do repositório: ela existe só na
pasta local do projeto e é ignorada pelo git. As imagens que o site usa já
estão prontas em `assets/img`.

```
materiais-de-origem/
  logo/          ju_essencias.jpg
  fotos/         as cinco fotos da loja e dos produtos
  avaliacoes/    fotos de perfil de quem avaliou
  dados.txt      contatos, links e texto das avaliações
```

Só é preciso ter os originais para rodar `tools/optimize-images.py`, ou seja,
para trocar ou reprocessar uma foto.

| Arquivo de origem | Conteúdo | Usado em |
| --- | --- | --- |
| `logo/ju_essencias.jpg` | Logo, 150 x 150 px | cabeçalho, rodapé, ícones e imagem de compartilhamento |
| `fotos/foto-163336-tratada.png` | Bandeja com a linha artesanal | hero e imagem de compartilhamento |
| `fotos/foto-163437-tratada.png` | Frascos de vidro "Alfa Ômega" | para criar |
| `fotos/foto-163401-tratada.png` | Mesa com sais de banho e sabonetes | saboaria artesanal |
| `fotos/foto-163156-tratada.png` | Vitrine de Natal | saboaria artesanal |
| `fotos/foto-163345-tratada.png` | Cantinho da loja | a loja |
| `avaliacoes/Ely_Melo.png`, `Claudia_Regina.png`, `Michelle_Almeida.png` | Fotos de perfil, 72 x 72 px | avaliações |
| `dados.txt` | Contatos, links e avaliações | textos da página |

## Repositório

| Item | Valor |
| --- | --- |
| Endereço | `git@github.com:joabegalvao/armazem_da_ju.git` |
| Página | https://github.com/joabegalvao/armazem_da_ju |
| Visibilidade | pública (conferida em 28/09/2026) |
| Branch | `main` |

O repositório guarda só o que o site precisa para funcionar e ser mantido:
`index.html`, `assets/`, `tools/`, `README.md` e `.gitignore`.

```bash
git clone git@github.com:joabegalvao/armazem_da_ju.git
```

Um clone novo abre e publica o site normalmente. Só não roda o script de
imagens, que depende da pasta `materiais-de-origem/`.

## Dados do cliente

Dados recebidos em 28/09/2026 e usados na página.

| Dado | Valor |
| --- | --- |
| Nome | Armazém da Ju |
| Segmento | Essências, fragrâncias e extratos, além de materiais para artesanato |
| Produto principal | Essências e fragrâncias |
| Público | Mulheres e pessoas interessadas em artesanato |
| Endereço | Avenida Brasil, 4383, sala 2, Maringá, PR |
| WhatsApp e fixo | (44) 3034-9904 |
| Instagram | https://www.instagram.com/armazemdajuessencias/ |
| Facebook | https://www.facebook.com/ArmazemJuArtesanatos/ |

### Avaliações como foram recebidas

Texto original, antes de qualquer correção.

- **Ely Melo:** Excelente local para vc comprar suas essências, que são de
  primeira qualidade. Também é um local onde vc encontra de tudo para seu
  artesanato.
- **Claudia Regina:** A loja é linda, e o atendimento muito bom.
- **Michelle Almeida:** Tem muitas embalagens lindas e acessórios para velas..
  gostei muito da loja

## Estratégia

| Definição | Decisão |
| --- | --- |
| Proposta de valor | Um só lugar para quem cria e para quem presenteia: essências, fragrâncias, extratos e materiais de artesanato, mais uma linha de saboaria artesanal com a marca da casa |
| Principal objeção | "Será que tem a essência ou o material que eu preciso, e é de qualidade?" |
| Conversão prioritária | Conversa no WhatsApp, para perguntar antes de ir à loja |
| Ação secundária | Visitar a loja na Avenida Brasil |
| Ação de apoio | Seguir o Instagram @armazemdajuessencias |

## Seções da página

| Ordem | Seção | Âncora | Conteúdo |
| --- | --- | --- | --- |
| 1 | Cabeçalho | | Logo, navegação e CTA de WhatsApp. Fixo no topo |
| 2 | Hero | `#inicio` | Proposta de valor, CTA principal e três fatos (endereço, telefone, marca própria) |
| 3 | Para criar | `#para-criar` | Seis categorias de produtos para quem faz artesanato |
| 4 | Saboaria artesanal | `#saboaria` | A linha própria, com a lista de produtos e duas fotos |
| 5 | A loja | `#a-loja` | O ambiente e a frase da placa na parede |
| 6 | Avaliações | `#avaliacoes` | Três depoimentos de clientes, um em destaque |
| 7 | Onde fica | `#onde-fica` | Dois caminhos: WhatsApp ou visita à loja |
| 8 | Chamada final | | WhatsApp e Instagram |
| 9 | Rodapé | | Contato, atendimento e redes sociais |

Componente de apoio: botão flutuante de WhatsApp, no canto inferior direito,
em todas as telas.

## Estrutura de arquivos

```
index.html                 conteúdo e SEO
assets/css/styles.css      estilos (tokens de cor e tipografia no topo)
assets/js/main.js          menu e revelação na rolagem
assets/img/                imagens otimizadas (geradas pelo script)
assets/fonts/              EB Garamond e Mulish (arquivos locais)
tools/optimize-images.py   gera assets/img a partir dos originais
materiais-de-origem/       arquivos do cliente (só na pasta local, fora do git)
```

## Como atualizar o conteúdo

| O que mudar | Onde |
| --- | --- |
| Textos, endereço, telefone | `index.html` (seções comentadas) |
| Número e mensagem do WhatsApp | `index.html`: procure por `wa.me/` (8 ocorrências). O texto vem depois de `?text=`, com espaços escritos como `%20` e acentos codificados |
| Telefone | `index.html`: seção "Onde fica", rodapé e bloco JSON-LD no `<head>` |
| Cores e fontes | `assets/css/styles.css`, bloco `:root` |
| Categorias de "Para criar" | copie um bloco `<li class="supply">` |
| Produtos da linha artesanal | `index.html`, lista `soap__tags` |
| Fotos | substitua o original, ajuste a lista `PHOTOS` em `tools/optimize-images.py` e rode o script |
| Foto com faixa na borda | acrescente o arquivo à lista `CROPS` do script (esquerda, topo, direita, base, em pixels) e rode o script |
| Avaliações | `index.html`, seção "AVALIAÇÕES". Fotos de perfil: lista `AVATARS` do script |

Há três mensagens de WhatsApp, conforme o ponto da página:

| Onde | Mensagem |
| --- | --- |
| Cabeçalho, hero, "Onde fica", chamada final, rodapé e botão flutuante | Olá! Vi o site do Armazém da Ju e quero saber mais sobre as essências e os produtos. |
| Seção "Para criar" | Olá! Vi o site do Armazém da Ju e quero saber se vocês têm uma essência ou um material que procuro. |
| Seção "Saboaria artesanal" | Olá! Vi o site do Armazém da Ju e quero saber mais sobre a linha de saboaria artesanal. |

Para gerar as imagens (requer Pillow e a pasta `materiais-de-origem/`):

```bash
python3 tools/optimize-images.py
```

Se a proporção de uma foto mudar, atualize `width` e `height` da tag `<img>`
correspondente no `index.html`, para não haver salto de layout.

### Título do hero

O título tem duas linhas, e o tamanho da letra é calculado para que cada uma
caiba na coluna em qualquer tela. Se o texto mudar, confira a quebra em 320 px
e em 900 px de largura. A regra está em `.hero__title`, no `styles.css`.

### Cache do navegador

Os arquivos de estilo e script são chamados com versão: `styles.css?v=1` e
`main.js?v=1`. Ao alterar um deles, aumente o número no `index.html` para que
os visitantes recebam a versão nova.

## Identidade visual

| Token | Cor | Origem |
| --- | --- | --- |
| `--ink` | `#1E1B07` | contorno e letras do logo |
| `--butter` | `#FEF8AA` | fundo do rótulo do logo |
| `--butter-100` | `#FFFBD6` | amarelo do logo clareado, fundo da seção de avaliações |
| `--paper` | `#FFFCF0` | fundo claro da página |
| `--linen` | `#F1E9D6` | juta e linho que aparecem nas fotos |
| `--rose` | `#A63D57` | rosa dos rótulos e das flores dos produtos |
| `--line`, `--ink-soft`, `--paper-soft` | `#D6CCB0`, `#595238`, `#CBC4A6` | linhas e textos secundários |
| `--whatsapp` | `#25D366` | verde oficial do WhatsApp, usado só no botão flutuante |

Tipografia: EB Garamond (títulos, com itálico nos destaques) e Mulish (textos).

Elementos que vêm da marca e da loja:

- Foto do hero em arco, com filete escuro em volta, como o topo curvo e o
  contorno do rótulo do logo.
- Itálico nos destaques dos títulos, que retoma a letra caligráfica do logo.
- Plaquinha com moldura dupla na seção "A loja", referência à placa de madeira
  que aparece na foto.
- Botões arredondados e etiquetas em forma de pílula, no lugar de cantos retos.

### Tratamento do logo

O arquivo recebido (`logo/ju_essencias.jpg`) tem 150 x 150 px, e o rótulo ocupa
140 x 83 px. Nada foi redesenhado. O script amplia a imagem, recorta a margem
vazia e torna transparente o fundo branco em volta do rótulo.

O logo só aparece sobre fundo claro (cabeçalho e rodapé). Em fundo escuro o
contorno some, porque tem quase a mesma cor.

Por ser pequeno, o logo fica levemente desfocado em telas de alta densidade. A
página o exibe com no máximo 140 px de largura para reduzir o efeito.

### Tratamento das fotos

As cinco fotos têm cerca de 1100 px de largura. O script gera versões de 480,
800 e 1000 px, com compressão mais forte na maior, que só é usada em telas de
alta densidade.

## Decisões de conteúdo

- Só foram usados dados fornecidos: nome, segmento, endereço, telefone, redes
  sociais, fotos e avaliações. Não há métricas, prêmios, preços ou promessas
  inventadas.
- "Marca própria" foi tratada como a linha de saboaria artesanal, porque o
  logo traz "Saboaria Artesanal" e as fotos mostram produtos com rótulo da
  casa.
- As seis categorias de "Para criar" vêm de duas fontes: essências,
  fragrâncias, extratos e materiais para artesanato estão no briefing;
  embalagens e acessórios para velas são citados na avaliação de Michelle
  Almeida.
- Os produtos da linha artesanal foram listados a partir das fotos. Só entraram
  os nomes legíveis nos rótulos (sabonete líquido, creme para a pele, óleo
  hidratante, sal de banho) e os itens reconhecíveis (sabonetes decorados e
  velas).
- A frase abaixo do nome no logo não foi usada, porque é ilegível no arquivo
  recebido.
- A foto de Natal aparece com legenda que a identifica como vitrine de Natal,
  para não parecer a vitrine do ano todo.
- Avaliações: as palavras são as enviadas pelo cliente. Na de Ely Melo, "vc"
  foi escrito por extenso ("você"), duas vezes. Na de Michelle Almeida, a
  pontuação foi corrigida ("velas.. gostei muito da loja" para "velas. Gostei
  muito da loja."). A de Claudia Regina está como recebida.
- As fotos de perfil de Ely Melo e Michelle Almeida trazem um selo laranja com
  estrela, que já vem no arquivo recebido.
- Avaliações sem estrelas e sem citação de fonte, porque nota e origem não
  foram informadas.
- A página não promete entrega, porque não foi informado se a loja envia
  pedidos. O WhatsApp é apresentado como canal para tirar dúvidas e confirmar
  disponibilidade.
- Não há formulário, porque não existe destino de envio definido.
- Não há seção de perguntas frequentes, por falta de dados sobre horários,
  formas de pagamento e entrega.
- O ícone do botão flutuante é escuro sobre o verde, e não branco, para manter
  contraste suficiente.

## Testes realizados

Executados em 28/09/2026, em Chromium automatizado (Playwright).

- Revisão visual das capturas de tela: página inteira em 390 e 1440 px,
  primeira dobra em 320, 768 e 1024 px.
- Sem rolagem horizontal e com o título do hero em duas linhas nos tamanhos
  320, 360, 390, 600, 640, 768, 820, 900, 1024, 1200, 1366, 1440 e 1920 px.
- Sem erros de console e sem imagens quebradas.
- 39 verificações automáticas aprovadas: menu no celular (toque, Esc, toque
  fora, foco), âncoras, botão flutuante de WhatsApp (posição, nome acessível,
  sem cobrir o texto do rodapé), revelação na rolagem, link de pular para o
  conteúdo, foco visível, destino e atributos de todos os links, mensagens do
  WhatsApp, hierarquia de títulos e atributos das imagens.
- Página utilizável sem JavaScript.
- Animações desligadas quando o sistema pede movimento reduzido.
- Contraste AA em todos os textos (mínimo de 5,07:1).
- Carga inicial no celular de 682 KB, medida no pior caso (tela de densidade
  3x), sem saltos de layout (CLS 0). Página inteira: 840 KB.

Não testado: Safari, Firefox e aparelhos físicos. Dos links externos, foi
conferido apenas o endereço, não o conteúdo de destino. Isso inclui o
WhatsApp: não foi verificado se o número responde.

## Histórico de ajustes

| Ajuste | Arquivos |
| --- | --- |
| Versão inicial da página | todos |
| Materiais de origem reunidos em `materiais-de-origem/`, fora do repositório | `tools/optimize-images.py`, `.gitignore`, `README.md` |

## Créditos e licenças

- Fotos, logo, avaliações e fotos de perfil: fornecidos pelo cliente.
- EB Garamond e Mulish: SIL Open Font License 1.1, obtidas do Google Fonts e
  hospedadas localmente.
- Ícones: desenhados para este projeto. Ícone do WhatsApp: Simple Icons (CC0).

## Pendências que dependem do cliente

- Logo em vetor (SVG, AI ou PDF) ou em alta resolução. É a pendência que mais
  afeta o acabamento.
- Confirmar que o número fixo (44) 3034-9904 recebe mensagens pelo WhatsApp.
- Conferir a lista de produtos da linha artesanal e os nomes corretos de cada
  um.
- Confirmar se as seis categorias de "Para criar" descrevem bem o que a loja
  vende, e se há outras que mereçam destaque.
- Informar se a loja faz entregas ou envia pedidos. Em caso positivo, a página
  pode dizer isso.
- Esclarecer o que são os frascos "Alfa Ômega": produto da casa, encomenda
  personalizada ou item de revenda. Hoje a legenda só descreve a foto.
- Horários de funcionamento e formas de pagamento.
- Domínio de publicação, para completar `og:image` com URL absoluta e adicionar
  `link rel="canonical"`.
- Origem das avaliações (por exemplo, o link do perfil no Google), caso se
  queira citar a fonte, e autorização dos clientes para uso de nome e foto.
- Fotos de produtos fora da época de Natal, para substituir a vitrine de Natal
  se a página for usada o ano todo.
- Fotos de perfil das avaliações têm 72 x 72 px. Ficam nítidas no tamanho usado
  (48 px), mas não podem ser ampliadas.
