def get_stats(stats):
    """Display S.P.E.C.I.A.L. stats."""
    print("=== Your S.P.E.C.I.A.L. ===")
    for stat, value in stats.items():
        print(f"{stat}: {value}")

if __name__ == "__main__":
    player = {
        'Strength': 5,
        'Perception': 6,
        'Endurance': 4,
        'Charisma': 3,
        'Intelligence': 7,
        'Agility': 5,
        'Luck': 5
    }
    get_stats(player)
