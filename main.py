from random import choice

while True:
    slowa = [
        ("Ręka, ramię", "Arm"),
        ("Oko", "Auge"),
        ("Brzuch", "Bauch"),
        ("Noga", "Bein"),
        ("Stopa", "Fuß"),
        ("Twarz", "Gesicht"),
        ("Włosy", "Haar"),
        ("Szyja) gardło", "Hals"),
        ("Dłoń", "Hand"),
        ("Skóra", "Haut"),
        ("Głowa", "Kopf"),
        ("Ciało", "Körper"),
        ("Warga", "Lippe"),
        ("Żołądek", "Magen"),
        ("Usta", "Mund"),
        ("Nos", "Nase"),
        ("Ucho", "Ohr"),
        ("Plecy", "Rücken"),
    ]

    while slowa:
        pl, de = choice(slowa)
        if input(f"{pl}: ") == de:
            print("✅ Na wozie")
            slowa.remove((pl, de))
        else:
            print("❌ W obozie")