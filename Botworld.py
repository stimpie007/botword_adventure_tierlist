import textwrap
from collections import defaultdict

tierlists = [
    {
        'source': "https://gameplayplan.com/botworld-adventure-tier-list/",
        'tiers': {
            'S': ["Ram", "Icicool", "Bouncer", "Thump", "Comet", "Tether", "Virus"],
            'A': ["Gyro", "Shuffle", "Bullseye", "Phantom", "Pluggie", "Brute", "Halo", "Mort", "Gusto", "InkJet",
                  "Nibbles", "Bigshot"],
            'B': ["Sheller", "Berserker", "Dune Bug", "K.O.", "Nozzle", "Froggy", "Slicer", "Chainer", "Longshot",
                  "Link", "Frosty", "Chomp", "Fork", "Pupil", "Rocketeer", "Bombee", "Hornet"],
            'C': ["Frostie", "Scatter", "Lobbie", "Slash", "Barrie", "Beat", "Bullwark", "Yanky", "Flamer"]
        }
    },
    {
        'source': "https://www.pocketgamer.com/botworld-adventure/tier-list/",
        'tiers': {
            'S': ["Backfire", "Ram", "Meteor", "Icicool", "Bouncer", "Thump", "Comet", "Tether", "Virus"],
            'A': ["Drill", "Gyro", "Shuffle", "Bullseye", "Phantom", "Pluggie", "Brute", "Halo", "Mort", "Gusto",
                  "InkJet", "Nibbles", "Bigshot"],
            'B': ["Sheller", "Berserker", "Dune Bug", "K.O.", "Nozzle", "Froggy", "Slicer", "Chainer", "Longshot",
                  "Link", "Frosty", "Chomp", "Fork", "Pupil", "Rocketeer", "Bombee", "Hornet"],
            'C': ["Frostie", "Scatter", "Lobbie", "Slash", "Barrie", "Beat", "Bullwark", "Yanky", "Flamer"]
        }
    },
    {
        'source': "https://ucngame.com/guides/botworld-adventure-tier-list/",
        'tiers': {
            'S': ["Icicool", "Ram", "Thump", "Dune Bug", "Mort"],
            'A': ["Bigshot", "Brute", "Chomp", "Hornet", "Virus"],
            'B': ["Barrie", "Berserker", "Bombee", "Fork", "Froggy", "Frosty", "Lobbie", "Nozzle", "Pupil", "Rocketeer",
                  "Yanky"],
            'C': ["Beat", "Bullwark", "Flamer", "K.O.", "Longshot", "Slash", "Chainer", "Pluggie", "Slicer", "Scatter"]
        }
    },
    {
        'source': "https://www.gosugamers.in/botworld-adventure-tier-list-best-bots-ranked/",
        'tiers': {
            'S': ["Comet", "InkJet", "Nibbles", "Bigshot", "Bullseye", "Virus", "Shuffle", "Thump", "Tether", "Gyro"],
            'A': ["Drill", "Ram", "Pluggie", "Phantom", "Gusto", "Mort", "Bouncer", "Brute", "Halo", "Icicool"],
            'B': ["Berserker", "Scatter", "Lobbie", "Sheller", "Flamer", "Bombee", "Fork", "Rocketeer", "Beat",
                  "Bullwark", "Yanky", "Hornet", "Dune Bug", "Pupil", "K.O."],
            'C': ["Nozzle", "Froggy", "Slash", "Chomp", "Longshot", "Link", "Frosty", "Slicer", "Frostie", "Chainer",
                  "Barrie"]
        }
    },
    {
        'source': "Custom 1",
        'tiers': {
            'S': ["Comet", "Ram", "Virus", "InkJet", "Tether", "Gyro", "Bigshot"],
            'A': ["Phantom", "Pluggie", "Drill", "Mort", "Bouncer"]
        }
    },
    {
        'source': "Custom 2",
        'tiers': {
            'S': ["Tether", "Comet", "Virus", "Mort", "Icicool", "Ram", "Thump"],
            'A': ["Bigshot", "Bouncer", "Gyro", "Brute", "InkJet", "Nibbles", "Bullseye", "Shuffle", "Pluggie", "Halo",
                  "Phantom", "Drill"]
        }
    }
]

rating_system = {'S': 5, 'A': 3, 'B': 1, 'C': 0}


def calculate_ratings(tierlists):
    bot_ratings = defaultdict(int)  # Initialize with default int value (0)

    # Loop through each tier list and assign ratings
    for tierlist in tierlists:
        for tier, bots in tierlist['tiers'].items():
            for bot in bots:
                bot_ratings[bot] += rating_system[tier]  # Directly add rating

    # Return sorted ratings
    return sorted(bot_ratings.items(), key=lambda item: item[1], reverse=True)


def print_top_bots(bot_ratings, top_n=10):
    print("Top 10 Bots:")
    for index, (bot, rating) in enumerate(bot_ratings[:top_n], start=1):
        print(f"{index}. {bot}: {rating}")


def print_all_bots(tierlists):
    all_bots = set()  # Use a set to avoid duplicates
    for tierlist in tierlists:
        for tier, bots in tierlist['tiers'].items():
            all_bots.update(bots)  # Add bots to the set

    wrapped_bots = textwrap.fill(", ".join(sorted(all_bots)), width=80)  # Set width for wrapping
    print("\nAll Bots:\n" + wrapped_bots)  # Use one print statement


def main():
    bot_ratings = calculate_ratings(tierlists)
    print_top_bots(bot_ratings)
    print_all_bots(tierlists)


if __name__ == "__main__":
    main()
