# Indicador de Sentimento da Mídia

Este indicador capta o “humor” das notícias econômicas do dia, analisando o tom dos títulos (positivo, negativo ou neutro) para resumir o clima informacional predominante.

## O que ele nos mostra
- Próximo de 0: predominância de notícias com tom mais negativo.
- Faixa intermediária: equilíbrio entre notícias positivas e negativas.
- Próximo de 100: predominância de tom positivo nas manchetes.

## Como é calculado
O score é calculado pela média do sentimento das manchetes do dia, normalizado para a escala 0–100. Quanto maior o score, mais positivo o clima informacional; quanto menor, mais negativo.

## Insumos e parâmetros
- Dados: títulos/manchetes do dia (fontes financeiras acompanhadas pelo pipeline).
- Parâmetros típicos:
	- Mínimo de manchetes/dia para cálculo: 5 (abaixo disso, trate como confiança baixa ou carregue leitura anterior).
	- Suavização opcional: média móvel 3–5 dias.
	- Dicionários/polaridade: revisar termos específicos do mercado brasileiro para melhor acurácia.
