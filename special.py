def get_stats(stats):
    """Display S.P.E.C.I.A.L. stats."""
    print("=== Your S.P.E.C.I.A.L. ===")
    for stat, value in stats.items():
        print(f"{stat}: {value}")

def level_up(stats, stat):
    """Increase a S.P.E.C.I.A.L. stat by 1."""
    if stat in stats:
        if stats[stat] < 10:
            stats[stat] += 1
            return f"{stat} increased to {stats[stat]}!"
        return f"{stat} is already at maximum (10)!"
    return f"Unknown stat: {stat}"


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
