import random
# Uma lista com os ensinamentos do Zen Budista

zen_teachings = {
    1: " A mente é tudo. O que você pensa, você se torna. ",
    2: " A paz vem de dentro, não a procure á sua volta. ",
    3: " O desapego não é não possuir nada, mas não ser possuído por nada. ",
    4: " Dharma: cumprir o dever sem apego aos frutos do trabalho. ",
    5: " Conheça a si mesmo e você conhecerá o universo. ",
    6: " Perseverança é a chave para a iluminação.",
    7: "Encontre a beleza na simplicidade da vida.",

}
def gerar_insight():
    # A função random.choice escolhe um item aleatório da lista
    frase_do_dia = random.choice(zen_teachings)

    print("-" * 30)
    print("🕉️ MOMENTO ZEN DA SARAH")
    print("-" * 30)
    print(f"\nReflexão para agora:{frase_do_dia}\n")
    print("-" * 30)

    if __name__ == "__main__":
        gerar_insight()
