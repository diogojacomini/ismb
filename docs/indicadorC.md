# Indicador de Volatilidade do Mercado

Mede o nível de nervosismo do mercado ao observar o quanto os preços têm oscilado recentemente no Brasil (Ibovespa) e como essas oscilações se alinham ao humor externo (IVVB11).

## O que ele nos mostra
- Próximo de 0: mercado tenso, oscilações elevadas, maior aversão a risco.
- Faixa intermediária: mercado em equilíbrio, oscilações dentro do padrão histórico.
- Próximo de 100: mercado calmo, oscilações contidas, maior previsibilidade.

## Como é construído (visão simples)
O indicador faz uma média ponderada da oscilação recente do Ibovespa, da amplitude diária dos preços e do sinal externo do IVVB11. O resultado é convertido para a escala 0–100, onde valores baixos indicam mais volatilidade e altos mais estabilidade.

## Como é calculado
O cálculo usa médias móveis e normalizações dos dados diários do Ibovespa e IVVB11, combinando volatilidade, amplitude e sinal externo em um único score. Quanto maior o score, mais estável o mercado; quanto menor, mais volátil.

## Insumos e parâmetros
- Dados: séries diárias do Ibovespa (close, high, low) e IVVB11 (close).
- Parâmetros típicos:
  - EWMA: janela 21, α=0,94.
  - ATR: janela 14 (EMA ou média simples).
  - Pesos (exemplo): w1=0,5; w2=0,3; w3=0,2.
