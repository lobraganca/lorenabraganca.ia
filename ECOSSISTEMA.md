# Ecossistema da Imersão: mapa geral

> Documento vivo. Primeiro pensamos tudo; depois construímos por partes,
> na ordem do fim desta página. Cada decisão tomada é anotada aqui, e o que
> ainda está aberto fica marcado como **[a decidir]**.

## A ideia em uma frase

Uma imersão em que a pessoa sai com a **própria ferramenta funcionando**,
construída com IA, sem precisar saber programar. **[a confirmar]**

---

## O caminho da pessoa, do começo ao fim

Todo o ecossistema serve a este caminho. Cada peça existe porque alguém
passa por uma dessas etapas.

| Etapa | O que a pessoa vive | O que precisamos construir |
|---|---|---|
| **Descobre** | vê um conteúdo seu | perfil, conteúdo, link da bio |
| **Se interessa** | pega algo de graça e entra na lista | isca gratuita, página de captura |
| **Aquece** | recebe conteúdo antes das vendas | sequência de mensagens, aulas ou lives |
| **Compra** | lê a oferta e paga | página de vendas, checkout, recuperação de carrinho |
| **Entra** | recebe o acesso na hora | liberação automática, boas-vindas, primeiros passos |
| **Participa** | vive a imersão | evento ao vivo, plataforma, materiais, comunidade, suporte |
| **Conclui** | sai com a ferramenta pronta | certificado, vitrine dos projetos, pedido de depoimento |
| **Continua** | dá o próximo passo | oferta de continuidade, indicação |

---

## 0. Fundação: decide tudo o resto

Nada dos blocos seguintes começa sem isto. A cor da marca depende de quem
é o público; a página de vendas depende da promessa; o cronograma inteiro
é contado de trás para frente a partir da data.

- **Para quem é**, e para quem não é **[a decidir]**
- **A promessa**: o que exatamente a pessoa tem pronto no último dia **[a decidir]**
- **Formato**: online ao vivo? Quantos dias? Horários? A gravação fica? **[a decidir]**
- **Preço** e condições (parcelas, Pix, lote de abertura) **[a decidir]**
- **Nome da imersão** **[a decidir]**
- **Data do evento** **[a decidir]**

## 1. O produto: a imersão em si

A peça mais importante, e a que faltava na primeira versão deste mapa.
Todo o resto é embalagem e entrega; isto é o que a pessoa compra.

- **Método**: o passo a passo que leva alguém do zero à ferramenta no ar
- **Programa dia a dia**: o que se aprende e o que se constrói em cada dia
- **Projeto guiado**: todos constroem uma ferramenta-modelo junto com você,
  ou cada um constrói a própria ideia? **[a decidir]** (o modelo é mais
  seguro para iniciante; a ideia própria vende mais)
- **Materiais**: prompts, modelos prontos, checklists, glossário sem jargão
- **Nivelamento**: turma com gente de níveis diferentes; quem nunca abriu
  um computador para isso precisa de um caminho, quem já sabe precisa de um
  desafio
- **Requisitos, escritos na página de vendas**: computador (celular não
  basta para construir), internet, e **quanto a pessoa vai gastar com
  ferramentas de IA** além do ingresso. Surpresa com custo depois da compra
  vira pedido de reembolso.
- **Pré-imersão**: contas criadas e tudo instalado ANTES do primeiro dia,
  com checklist e vídeo curto. Sem isso, o primeiro dia inteiro vai embora
  em "não consegui entrar".
- **Segurança na ferramenta do aluno**: iniciante construindo com IA costuma
  deixar dados de outras pessoas expostos sem perceber. Foi exatamente o
  que aconteceu no Ei com os telefones dos candidatos. Isto precisa ser
  aula, não rodapé.
- **Sucesso medido**: quantos alunos terminam com a ferramenta no ar. É o
  número que vira prova na próxima turma.

## 2. Marca

**Branding book**
- Posicionamento: por que você, e não outra pessoa, para ensinar isto
- Sua história (o Ei Emprego é prova real: um app no ar, na loja, com usuários)
- Tom de voz: palavras que usamos e palavras que não usamos
- Logo e variações
- Paleta de cores, tipografia, estilo de foto e de ícone
- Aplicações: post, story, capa de aula, slide, certificado

**Design system**
- É o branding book virado código: cores, fontes, espaçamentos, botões,
  cartões, formulários
- Um só, usado nas páginas de venda **e** na plataforma dos alunos
- Lição do Ei: todo arquivo de marca sai de **uma fonte única**, gerado
  por um comando. Nenhuma imagem de marca é editada à mão.

## 3. Funil de vendas

- **Isca gratuita**: aula, mini-desafio ou uma ferramentinha pronta que a
  pessoa usa na hora (combina com o tema) **[a decidir]**
- **Página de captura**
- **Sequência de aquecimento** até a abertura
- **Página de vendas**: promessa, para quem é e para quem não é, o que sai
  pronto, programa dia a dia, quem é você, provas, bônus, preço, garantia
  e perguntas frequentes
- **Checkout**: Pix e cartão parcelado
- **Order bump e upsell**: o que se oferece junto e logo depois da compra **[a decidir]**
- **Recuperação**: carrinho abandonado, Pix gerado e não pago
- **Medição**: pixel (Meta, Google) e links rastreados, para saber de onde
  vem cada venda

## 4. Plataforma dos alunos (área de membros)

- Entrada por e-mail ou telefone
- **Acesso liberado sozinho** quando o pagamento aprova
- Aulas gravadas, materiais, prompts e modelos prontos
- Progresso: um passo a passo da construção da ferramenta, com checklist
- Comunidade **[a decidir: WhatsApp, Discord ou dentro da plataforma]**
- Vitrine dos projetos dos alunos (vira prova social para a próxima turma)
- Certificado
- **Painel da administração**: alunos, vendas, reembolsos, presença, números

## 5. Automação de mensagens

Canais: e-mail e WhatsApp.

| Momento | Mensagem |
|---|---|
| Entrou na lista | boas-vindas e entrega da isca |
| Aquecimento | conteúdo até a abertura |
| Abertura | "está aberto", com o link |
| Fechamento | últimas horas |
| Não concluiu a compra | carrinho abandonado, Pix pendente |
| Comprou | acesso, primeiros passos, grupo |
| Antes do evento | lembretes: 1 dia, 1 hora, "estamos ao vivo" |
| Durante | material do dia, tarefa do dia |
| Depois | gravação, pesquisa, pedido de depoimento, próxima oferta |

Atenção: WhatsApp automatizado precisa da **API oficial** (da Meta ou de
um provedor). Automatizar um número comum pode fazer o WhatsApp bloqueá-lo.

## 6. Suporte

- Perguntas frequentes (na página de vendas e na plataforma)
- **Assistente de IA** treinado no conteúdo da imersão, respondendo 24h e
  passando para uma pessoa quando não souber
- Canal humano, com prazo de resposta combinado
- **Reembolso**: compra online tem 7 dias de arrependimento por lei
  (CDC, art. 49). Processo claro e fácil, sem esconder.

## 7. Squad: quem faz o quê

**Decidido: pessoas e agentes de IA, juntos.**

A regra que organiza os dois: **a IA produz, uma pessoa aprova tudo o que
vai a público ou mexe com dinheiro.** Nenhum texto de venda, mensagem em
massa ou reembolso sai sem alguém olhar.

**Agentes de IA** (proposta; cada um ganha um arquivo de instruções na
pasta `agentes/`, que serve tanto aqui quanto num Projeto do Claude):

| Agente | O que faz | Quem aprova |
|---|---|---|
| Guardiã da marca | revisa tudo contra o branding book: tom, palavras, cores | Lorena |
| Copy | página de vendas, e-mails, mensagens de WhatsApp | Lorena |
| Conteúdo | roteiros, legendas, calendário de posts | Lorena ou social media |
| Suporte | responde alunos 24h e passa para uma pessoa quando não sabe | suporte humano |
| Técnico | constrói páginas, plataforma e automações (Claude Code) | Lorena |
| Números | relatório semanal: lista, vendas, conversão, presença | Lorena |

**Pessoas** (proposta):

| Papel | Por que pessoa, e não IA |
|---|---|
| **Lorena** | visão, conteúdo, aulas ao vivo, aprovação final |
| **Monitores da imersão** | quem constrói a primeira ferramenta trava em detalhe técnico, e trava ao vivo. Alguém precisa olhar a tela da pessoa. Referência: 1 monitor para cada 20 a 30 alunos. Ex-alunos viram monitores nas próximas turmas. |
| **Suporte e comunidade** | recebe o que o agente de suporte não resolve, modera a comunidade |
| **Tráfego pago** | mexe com dinheiro de anúncio todo dia |
| **Edição de vídeo** | pode usar IA, mas uma pessoa entrega |
| **Contabilidade e jurídico** | nota fiscal, termos, LGPD |

Os agentes também são conteúdo: mostrar o próprio squad de IA trabalhando
é demonstração do que a imersão ensina. **[a decidir: se entra no programa]**

## 8. Base legal e operação

- Termos de uso e política de privacidade (LGPD)
- Consentimento para receber mensagens
- Nota fiscal e CNPJ
- Autorização de imagem, se gravar alunos
- Painel de números: pessoas na lista, conversão da página, vendas,
  reembolsos, presença no evento, quem concluiu a ferramenta

## 9. O evento ao vivo

- Onde acontece: Zoom, Meet, YouTube fechado, presencial **[a decidir]**
- Salas separadas para os monitores atenderem quem travou
- Ensaio técnico antes, com o squad inteiro
- Plano B: internet reserva, alguém que assume a transmissão se a sua cair
- Gravação de cada dia, na plataforma no mesmo dia

## 10. Financeiro

- Custos: taxas do Mercado Pago (parcelado custa mais), impostos, anúncios,
  monitores, ferramentas, o próprio tempo
- **Ponto de equilíbrio**: quantas vendas pagam a turma
- Meta de vendas e de pessoas na lista para chegar nela
- Reserva para reembolsos e contestação de cartão

## 11. Depois da imersão

- A ferramenta do aluno **continua de pé** depois que a imersão acaba? Quem
  ele chama quando quebrar? **[a decidir: comunidade, plano de continuidade,
  mentoria]**
- Lista de espera da próxima turma
- Indicação e afiliados: aluno que indica ganha algo **[a decidir]**
- Ex-alunos viram monitores e depoimentos

## 12. Riscos e plano B

| Se acontecer | O que fazemos |
|---|---|
| Mercado Pago recusa ou trava | segundo meio de pagamento pronto |
| WhatsApp bloqueia o número | API oficial desde o início; e-mail como segundo canal |
| Uma ferramenta de IA muda de preço ou de tela no meio da turma | materiais com data, e aula que ensina o raciocínio, não só o botão |
| Poucas vendas | turma piloto primeiro (ver abaixo), antes de investir no ecossistema inteiro |

---

## Decisões técnicas (recomendação, a confirmar)

- **Página de vendas e plataforma próprias**, no mesmo código e com o
  mesmo design system. É a prova viva do que a imersão ensina: "isto aqui
  eu construí com o mesmo método".
- **Supabase + Vercel + Mercado Pago**, a mesma base que já funciona no
  Ei Emprego. **Projeto Supabase novo e separado**: nada deste ecossistema
  mora no banco do Ei.
- **Endereço na internet**: não existe domínio terminado em `.ia`. As
  opções são `lorenabraganca.ai`, `lorenabraganca.com.br` ou um subdomínio
  como `ia.lorenabraganca.com.br`. **[a decidir]**

---

## Turma piloto: validar antes de construir tudo (recomendação)

Construir o ecossistema inteiro antes de a primeira pessoa passar pela
imersão é apostar tudo num programa que ninguém testou. A proposta:

- **Turma piloto** pequena (10 a 20 pessoas), preço de lançamento, com o
  mínimo: link de pagamento, Zoom, grupo e uma pasta de materiais
- Enquanto ela acontece, o ecossistema completo vai sendo construído
- A piloto devolve o que nenhum planejamento dá: onde as pessoas travam,
  quanto tempo cada parte leva de verdade, **depoimentos reais e
  ferramentas reais no ar** para a página de vendas da turma grande

**[a decidir]**

---

## Ordem de construção

1. **Fundação**: conversa, não código
2. **O produto**: método, programa, materiais, pré-imersão
3. **Branding book**
4. **Design system**
5. **Isca e página de captura**: a lista começa a crescer cedo
6. **Página de vendas e checkout**
7. **Automações de captação e venda**
8. **Plataforma dos alunos** com liberação automática do acesso
9. **Automações de entrega e do evento**
10. **Suporte e assistente de IA**
11. **Pós-imersão**: depoimentos, vitrine, continuidade

A lista cresce enquanto o resto é construído, e a plataforma só precisa
estar pronta no dia em que o primeiro aluno entra.
