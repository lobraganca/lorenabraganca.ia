# lorenabraganca.ia: o que uma sessão nova precisa saber

Projeto de Lorena Bragança: a imersão **Ferramentaria** (R$ 97, sexta 29/01
das 18h às 22h e sábado 30/01 das 8h às 12h, 2027), a **mentoria** de
R$ 2.997 e o site **lorenabraganca.com.br**.

**Este repositório não tem nada a ver com o Ei Emprego** (repositório
Nuvem-Lorena), a não ser a experiência. Banco, Vercel e domínio próprios.
Nunca ligar este site ao Supabase do Ei.

## Onde está cada coisa

| Arquivo | O que é |
|---|---|
| `ECOSSISTEMA.md` | o mapa de tudo, com cada decisão e a data dela. Leia primeiro. |
| `site/` | o site: HTML estático, sem etapa de montagem. `site/vercel.json` |
| `site/estilos/tokens.css` | **a fonte da verdade** de cores, letras e espaços |
| `site/estilos/componentes.css` | as peças: botões, rótulos, cartões, onda, formulário |
| `site/design-system.html` | a vitrine do design system |
| `scripts/gerar-previa.py` | transforma uma página do site em prévia para publicar como Artifact |
| `marca/` | briefing, identidade e peças do Claude Design (PDFs) |
| `trilha/`, `cronometro/`, `area-de-membros/planta/` | código das páginas publicadas como Artifact |

## Páginas publicadas (Artifacts)

- Trilha de aceleração (progresso no banco da página): https://claude.ai/artifact/1NhcuyV66r2fBr5yzeGDMq
- Cronômetro da apresentação: https://claude.ai/artifact/8KmbDVpwgENm1vT7R5N36Z
- Planta da Ferramenta: https://claude.ai/artifact/UN5HXRpwqWgQJmDXtConty
- Prévia do site: https://claude.ai/artifact/41M1V1ofufT4nDvu5mWewJ
- Design system: https://claude.ai/artifact/1cNDAfL7WTPay2D1zKsHzC

O código de cada uma é copiado para este repositório a cada mudança.

## Regras da marca que já custaram retrabalho

- **Texto branco sobre o azul-piscina é proibido** (contraste 2,6). O botão
  principal é piscina-500 com texto marinho (6,3).
- Toda cor nova entra em `tokens.css` com o contraste **calculado**.
- Letras: Fraunces (títulos; itálico só na palavra em destaque) e Figtree
  (texto e botões). Kalnia, Ms Madi, Bricolage e Atkinson saíram em 27/09.
- O site é claro e leve: ela recusou a versão com faixas marinho ("muito carregado").
- Não usar "Claude" no nome de produto nem em @: é marca de outra empresa.
- Não afirmar nada sobre ela que ela não confirmou. Ela vê tudo no celular.
- **Não citar o app do Ei Emprego** nos textos públicos (pedido dela em 27/09).

## Como a dona trabalha

Lorena usa celular, escreve em português, manda print e pede curto.
Responder em português sem jargão, dizer o que não foi verificado, e
anotar cada decisão dela no `ECOSSISTEMA.md` com a data.
