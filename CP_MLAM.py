import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

demanda = np.random.normal(
    loc=500,       # média aproximada da demanda
    scale=70,      # desvio padrão
    size=120       # quantidade de dias analisados
)

demanda = np.round(demanda).astype(int)


media = np.mean(demanda)
desvio_padrao = np.std(demanda, ddof=1)


print("ANÁLISE DA DEMANDA")


print(f"Média da demanda: {media:.2f} unidades")
print(f"Desvio padrão: {desvio_padrao:.2f} unidades")




def distribuicao_normal(x, media, desvio):
    """
    Calcula a densidade da Distribuição Normal.
    """

    parte_1 = 1 / (desvio * np.sqrt(2 * np.pi))

    parte_2 = np.exp(
        -0.5 * ((x - media) / desvio) ** 2
    )

    return parte_1 * parte_2

x = np.linspace(
    media - 4 * desvio_padrao,
    media + 4 * desvio_padrao,
    500
)

y = distribuicao_normal(
    x,
    media,
    desvio_padrao
)

plt.figure(figsize=(12, 7))

plt.plot(
    x,
    y,
    linewidth=3,
    label="Distribuição Normal"
)

plt.axvline(
    media,
    linestyle="--",
    linewidth=2,
    label=f"Média = {media:.1f}"
)

plt.axvline(
    media + desvio_padrao,
    linestyle=":",
    linewidth=2
)

plt.axvline(
    media - desvio_padrao,
    linestyle=":",
    linewidth=2
)

plt.axvline(
    media + 2 * desvio_padrao,
    linestyle="-.",
    linewidth=1.5
)

plt.axvline(
    media - 2 * desvio_padrao,
    linestyle="-.",
    linewidth=1.5
)

plt.title(
    "Distribuição Normal da Demanda",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Demanda diária (unidades)", fontsize=13)
plt.ylabel("Densidade", fontsize=13)

plt.legend()
plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 7))

plt.plot(
    x,
    y,
    linewidth=3
)


plt.axvline(
    media,
    linestyle="--",
    linewidth=2
)


for numero in [1, 2, 3]:

    plt.axvline(
        media + numero * desvio_padrao,
        linestyle=":",
        linewidth=1.5
    )

    plt.axvline(
        media - numero * desvio_padrao,
        linestyle=":",
        linewidth=1.5
    )



plt.text(
    media,
    max(y) * 0.95,
    " MÉDIA (μ)",
    ha="center",
    fontsize=13
)

plt.text(
    media + desvio_padrao,
    max(y) * 0.50,
    "+1σ",
    ha="center",
    fontsize=12
)

plt.text(
    media - desvio_padrao,
    max(y) * 0.50,
    "-1σ",
    ha="center",
    fontsize=12
)

plt.title(
    "Média e Desvio Padrão",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Valor observado")
plt.ylabel("Densidade")

plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()

dias = np.arange(1, len(demanda) + 1)

plt.figure(figsize=(13, 7))

plt.plot(
    dias,
    demanda,
    marker="o",
    markersize=3,
    linewidth=1.5,
    label="Demanda diária"
)


plt.axhline(
    media,
    linestyle="--",
    linewidth=2,
    label=f"Média = {media:.0f}"
)


plt.axhline(
    media + desvio_padrao,
    linestyle=":",
    linewidth=1.5,
    label="+1 desvio padrão"
)

plt.axhline(
    media - desvio_padrao,
    linestyle=":",
    linewidth=1.5,
    label="-1 desvio padrão"
)

plt.title(
    "Exemplo: Demanda Diária de um Produto",
    fontsize=20,
    fontweight="bold"
)

plt.xlabel("Dias")
plt.ylabel("Quantidade vendida")

plt.legend()
plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()


z_score = (
    demanda - media
) / desvio_padrao


fora_do_padrao = np.abs(z_score) > 2


print("\n")
print("VALORES FORA DO PADRÃO")

print(
    f"Quantidade de valores fora do padrão: "
    f"{np.sum(fora_do_padrao)}"
)

if np.any(fora_do_padrao):

    print("\nDias identificados:")

    for dia, valor, z in zip(
        dias[fora_do_padrao],
        demanda[fora_do_padrao],
        z_score[fora_do_padrao]
    ):

        print(
            f"Dia {dia}: "
            f"{valor} unidades "
            f"(Z = {z:.2f})"
        )

else:

    print("Nenhum valor fora do padrão foi identificado.")


plt.figure(figsize=(13, 7))

plt.plot(
    dias,
    demanda,
    linewidth=1.5,
    label="Demanda"
)


plt.scatter(
    dias[fora_do_padrao],
    demanda[fora_do_padrao],
    s=80,
    label="Fora do padrão",
    zorder=5
)


plt.axhline(
    media,
    linestyle="--",
    linewidth=2,
    label=f"Média = {media:.0f}"
)


plt.axhline(
    media + 2 * desvio_padrao,
    linestyle=":",
    linewidth=1.5
)

plt.axhline(
    media - 2 * desvio_padrao,
    linestyle=":",
    linewidth=1.5
)

plt.title(
    "Identificação de Valores Fora do Comportamento Esperado",
    fontsize=19,
    fontweight="bold"
)

plt.xlabel("Dia")
plt.ylabel("Demanda")

plt.legend()
plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()


print("\n")
print("RESUMO")


print(f"Média da demanda: {media:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Maior demanda: {np.max(demanda)}")
print(f"Menor demanda: {np.min(demanda)}")

print(
    f"Valores fora do padrão: "
    f"{np.sum(fora_do_padrao)}"
)


print("\nAPLICAÇÕES:")

print("""
• Gestão de estoques
• Estoque de segurança
• Previsão de demanda
• Controle de qualidade
• Análise de prazos
• Identificação de padrões
• Identificação de valores fora do esperado"
• Apoio à tomada de decisões""")



print("\n")

print("DISTRIBUIÇÃO NORMAL + INTELIGÊNCIA ARTIFICIAL")


print("""
A Distribuição Normal ajuda a compreender o comportamento
dos dados.

A Inteligência Artificial e o Machine Learning podem utilizar
essas informações para:

• identificar padrões;
• detectar anomalias;
• analisar comportamentos;
• realizar previsões;
• auxiliar na tomada de decisões.
""")

