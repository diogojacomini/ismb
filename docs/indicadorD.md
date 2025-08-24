# Indicador de Atividade do Mercado

Mede a intensidade diária do mercado, avaliando se o dia foi fraco, normal ou forte em relação ao ritmo recente. Considera que retornos sem volume têm menos qualidade, enquanto movimentos acompanhados de volume elevado são mais representativos.

## O que ele nos mostra
- Próximo de 0: dia fraco, movimento abaixo do ritmo recente.
- Faixa intermediária: atividade em linha com os últimos dias.
- Próximo de 100: dia forte, acima do normal e sustentado por volume.


## Como é calculado
O score compara o retorno do dia com a média dos últimos dias e ajusta pelo volume negociado. Dias fortes têm retorno acima da média e bom volume; dias fracos, retorno baixo ou volume fraco.

## Insumos e parâmetros
- Dados: preço de fechamento diário e volume do IBOVESPA.
- Parâmetros típicos:
	- Janela do retorno médio (N): 3 dias.
	- Janela da média de volume: 30 dias.
	- Piso do fator de volume: 0,7 (evita penalização excessiva).
