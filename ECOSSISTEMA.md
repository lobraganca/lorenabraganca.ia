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

## 1. Marca

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

## 2. Funil de vendas

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

## 3. Plataforma dos alunos (área de membros)

- Entrada por e-mail ou telefone
- **Acesso liberado sozinho** quando o pagamento aprova
- Aulas gravadas, materiais, prompts e modelos prontos
- Progresso: um passo a passo da construção da ferramenta, com checklist
- Comunidade **[a decidir: WhatsApp, Discord ou dentro da plataforma]**
- Vitrine dos projetos dos alunos (vira prova social para a próxima turma)
- Certificado
- **Painel da administração**: alunos, vendas, reembolsos, presença, números

## 4. Automação de mensagens

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

## 5. Suporte

- Perguntas frequentes (na página de vendas e na plataforma)
- **Assistente de IA** treinado no conteúdo da imersão, respondendo 24h e
  passando para uma pessoa quando não souber
- Canal humano, com prazo de resposta combinado
- **Reembolso**: compra online tem 7 dias de arrependimento por lei
  (CDC, art. 49). Processo claro e fácil, sem esconder.

## 6. Squad: quem faz o quê

Para cada papel: é uma pessoa ou um agente de IA, e com quais instruções.
**[a decidir]**

| Papel | Pessoa ou IA? |
|---|---|
| Copy (textos de venda e mensagens) | |
| Design (peças, slides) | |
| Social media | |
| Tráfego pago | |
| Edição de vídeo | |
| Suporte | |
| Técnico (páginas, plataforma, automações) | |

## 7. Base legal e operação

- Termos de uso e política de privacidade (LGPD)
- Consentimento para receber mensagens
- Nota fiscal e CNPJ
- Autorização de imagem, se gravar alunos
- Painel de números: pessoas na lista, conversão da página, vendas,
  reembolsos, presença no evento, quem concluiu a ferramenta

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

## Ordem de construção

1. **Fundação**: conversa, não código
2. **Branding book**
3. **Design system**
4. **Isca e página de captura**: a lista começa a crescer cedo
5. **Página de vendas e checkout**
6. **Automações de captação e venda**
7. **Plataforma dos alunos** com liberação automática do acesso
8. **Automações de entrega e do evento**
9. **Suporte e assistente de IA**
10. **Pós-imersão**: depoimentos, vitrine, continuidade

A lista cresce enquanto o resto é construído, e a plataforma só precisa
estar pronta no dia em que o primeiro aluno entra.
