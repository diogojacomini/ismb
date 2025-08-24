# Indicador de Retorno do Mercado (Ibovespa)

Resume como o desempenho recente do Ibovespa se compara ao seu padrão histórico, considerando também a força do volume de negociações.

## O que ele nos mostra
- Próximo de 0: desempenho fraco em relação ao histórico recente.
- Faixa intermediária: retorno dentro do padrão.
- Próximo de 100: desempenho acima do esperado para o período.

## Como é calculado
O score é calculado a partir do retorno diário do Ibovespa, comparado ao seu padrão histórico (média e desvio dos últimos dias) e ajustado pela força do volume negociado. Resultados altos indicam desempenho acima do normal e bem suportado por volume; baixos indicam desempenho fraco.

## Insumos e parâmetros
- Dados: close (fechamento) e volume diários do Ibovespa.
- Parâmetros típicos:
  - Janela para média/desvio do retorno: 21 dias.
  - Janela para média de volume: 30 dias.
  - Piso do fator de volume: 0,7.
