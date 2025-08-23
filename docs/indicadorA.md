# Indicador de Risco de Crédito

Este indicador traduz o equilíbrio entre medo e confiança do mercado. Ao unir o comportamento recente da oscilação dos preços com o desempenho observado, ele sintetiza o “apetite por risco” do dia.

## O que ele nos mostra
- Próximo de 0: predomínio de cautela e aversão ao risco.
- Faixa intermediária: mercado em modo neutro, sem sinais fortes de estresse ou euforia.
- Próximo de 100: ambiente de maior confiança e tomada de risco.

## Por que isso é útil
- Ajuda a calibrar exposição a ativos de risco ao longo do tempo.
- Oferece um termômetro simples para comunicar condições de mercado.
- Complementa a leitura de preço com um sinal de “sentimento” agregado.

## Como é calculado (resumo)
O indicador combina o retorno diário do Ibovespa e sua volatilidade recente:

- Retorno do dia: log_ret_t = ln(close_t / close_{t-1})
- Volatilidade: EWMA dos retornos (21 dias, α=0,94)
- Score final: mistura o retorno e o risco, reescalado para 0–100

Retornos acima do típico e menor volatilidade elevam o score (maior apetite a risco); o oposto reduz o score.

## Insumos e parâmetros
- Dados: preços de fechamento diários do Ibovespa (close).
- Parâmetros típicos:
  - Janela para média/desvio dos retornos: 21 dias.
  - EWMA da volatilidade: janela 21, α=0,94 (ajuste conforme seu histórico).
  - Pesos: w_ret=0,6 e w_vol=0,4 (ajuste conforme sua preferência de sensibilidade).
