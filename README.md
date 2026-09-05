# 📊 Exercícios de Z-Score em Python

Repositório desenvolvido como parte das atividades acadêmicas da **FATEC São José dos Campos — Prof. Jessen Vidal**, com o objetivo de praticar conceitos de **Z-Score e análise estatística utilizando Python**.

A lista de exercícios foi proposta pelo professor **Carlos Feichas** para que nós, estudantes, pudéssemos compreender melhor como o Z-Score pode ser utilizado na análise e interpretação de dados, indo além do simples cálculo matemático.

---

## 🎯 Sobre a lista

Os exercícios foram elaborados para trabalhar diferentes aplicações do **Z-Score**, utilizando situações progressivamente mais próximas de problemas reais.

A proposta não é apenas calcular um valor de Z-Score, mas também **interpretar o que esse resultado representa dentro do contexto dos dados**.

Entre os conceitos e ferramentas trabalhados estão:

- 📐 Cálculo de Z-Score;
- 📊 Média e desvio-padrão;
- ➕ Valores acima e abaixo da média;
- 🔎 Identificação de valores que merecem investigação;
- 🐍 Implementação dos conceitos em Python;
- 🧮 Utilização de **NumPy**;
- 🐼 Manipulação de dados com **Pandas**;
- 📋 Classificação de dados a partir do Z-Score;
- 📦 Utilização de DataFrames;
- 📈 Comparação entre **IQR** e Z-Score;
- 🔐 Aplicação do conceito em uma pequena análise de eventos de segurança.

A lista também reforça uma ideia importante: um valor considerado incomum **não deve ser automaticamente removido**. A identificação de um possível outlier é apenas um indicativo de que aquele dado merece ser investigado.

---

## 📚 Exercícios

A lista é composta por **10 exercícios**, cada um explorando uma aplicação ou interpretação diferente do Z-Score:

| # | Tema |
|---|---|
| 01 | Distância em passos de desvio-padrão |
| 02 | Acima ou abaixo da média? |
| 03 | Qual leitura é mais incomum? |
| 04 | Latência de uma API |
| 05 | Monitoramento de CPU com classificação |
| 06 | O mesmo valor em dois contextos |
| 07 | Função de interpretação |
| 08 | Z-Score em um DataFrame |
| 09 | Comparação entre IQR e Z-Score |
| 10 | Mini análise de eventos de segurança |

Os primeiros exercícios trabalham principalmente a interpretação do Z-Score, enquanto os seguintes introduzem aplicações utilizando Python, NumPy e Pandas. A atividade termina relacionando a análise estatística com um cenário de **segurança da informação**. 
---

## 📂 Estrutura do repositório

As respostas e implementações dos exercícios estão disponíveis na pasta:

```text
Exercicios/
```

A organização do projeto é, portanto:

```text
.
├── Exercicios/
│   ├── 01_Distancia_em_passos_desvio_padrao.py
│   ├── 02_Acima_ou_abaixxo_da_media.py
│   └── ...
└── Exercicios_ZScore_Python.pdf
└── README.md
```

> **As respostas dos exercícios estão na pasta `Exercicios`.**

---

## 🧠 O que é Z-Score?

De forma geral, o **Z-Score** indica quantos desvios-padrão um determinado valor está distante da média de um conjunto de dados.

A fórmula utilizada é:

```text
             valor - média
Z = ───────────────────────────
             desvio-padrão
```

Isso permite transformar valores que possuem escalas diferentes em uma medida comum de distância em relação à média.

Por exemplo, um Z-Score positivo indica que o valor está acima da média, enquanto um Z-Score negativo indica que está abaixo dela. Um Z-Score igual a zero significa que o valor está exatamente na média.

A lista utiliza **|Z| > 3** como uma regra prática para indicar valores que merecem investigação. Isso não significa, porém, que todo valor identificado dessa maneira seja necessariamente um erro ou deva ser removido.

---

## 🔎 Da estatística para situações reais

Uma das partes interessantes da atividade é observar como o conceito pode ser aplicado fora de exemplos puramente matemáticos.

Ao longo dos exercícios, o Z-Score é utilizado para analisar situações como:

- 🌡️ temperaturas;
- 🌐 latência de APIs;
- 💻 utilização de CPU;
- 👥 diferentes grupos de dados;
- 📊 requisições de usuários;
- 🔐 eventos relacionados à segurança.

Dessa forma, a atividade busca mostrar que estatística pode ser uma ferramenta para **encontrar comportamentos que fogem do padrão e levantar hipóteses sobre o que está acontecendo nos dados**.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **NumPy**
- **Pandas**

As bibliotecas são utilizadas conforme solicitado nos exercícios, mantendo o foco na compreensão dos conceitos e na interpretação dos resultados.

---

## 🎓 Contexto acadêmico

**Instituição:** FATEC São José dos Campos — Prof. Jessen Vidal  
**Professor:** Carlos Feichas  
**Tema:** Z-Score e análise de dados  
**Linguagem:** Python

Este repositório foi criado com fins **educacionais**, servindo como registro e material de estudo dos exercícios realizados durante a disciplina.

---

## 💭 Considerações

Mais do que chegar a um número, os exercícios procuram desenvolver a capacidade de **olhar para os dados e entender o que eles estão dizendo**.

Um Z-Score elevado pode indicar algo incomum, mas o significado desse comportamento depende do contexto. Por isso, a interpretação é uma parte essencial da análise — o cálculo por si só não encerra o processo.

> **Calcular é apenas o começo. Entender o que o resultado significa é a parte mais importante da análise.**

---

### 👨‍💻 Desenvolvido para fins acadêmicos

**FATEC São José dos Campos — Prof. Jessen Vidal**  
**Professor: Carlos Feichas**

*Repositório destinado ao estudo e prática de conceitos de estatística aplicada com Python.*
