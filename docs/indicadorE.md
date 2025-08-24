# Indicador de Confiança do Mercado Local (IFIX)

Mede a confiança do mercado brasileiro por meio do IFIX, avaliando se o desempenho diário foi melhor, igual ou pior em relação ao ritmo recente. O indicador varia de 0 a 100, funcionando como um termômetro da “temperatura” local.

## O que ele nos mostra
- Próximo de 0: confiança baixa, retornos aquém da média recente.
- Faixa intermediária: confiança estável, retornos dentro do padrão.
- Próximo de 100: confiança elevada, retornos acima do normal recente.

## Como é calculado
O score compara o retorno do dia do IFIX com a média dos últimos dias. Sobe quando o retorno supera a média recente e cai quando é inferior.

## Insumos e parâmetros
- Dado: close_price (fechamento diário do IFIX).
- Parâmetros típicos:
	- Janela do retorno médio (N): 3 dias.
	- Lookback de comparação histórica: ~30 dias (ajustável ao seu histórico).
