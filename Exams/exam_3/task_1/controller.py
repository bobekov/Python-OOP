from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    SUSTENANCE_TYPES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        find_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                find_players.append(player.name)
        return f"Successfully added: {', '.join(find_players)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next((p for p in self.players if p.name == player_name), None)
        supply = next((s for s in reversed(self.supplies) if s.__class__.__name__ == sustenance_type), None)

        if sustenance_type in self.SUSTENANCE_TYPES and player is not None:
            if sustenance_type == "Food":
                if supply is None:
                    raise Exception("There are no food supplies left!")
            if sustenance_type == "Drink":
                if supply is None:
                    raise Exception("There are no drink supplies left!")

            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            player.stamina += supply.energy
            if player.stamina > 100:
                player.stamina = 100
                player.need_sustenance = False
            self.supplies.remove(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next(p for p in self.players if p.name == first_player_name)
        player2 = next(p for p in self.players if p.name == second_player_name)
        if player1.stamina <= 0 and player2.stamina <= 0:
            return f"Player {player1.name} does not have enough stamina.\n" \
                   f"Player {player2.name} does not have enough stamina."
        if player1.stamina <= 0:
            return f"Player {player1.name} does not have enough stamina."
        if player2.stamina <= 0:
            return f"Player {player2.name} does not have enough stamina."

        if player1.stamina < player2.stamina:
            player2.stamina -= player1.stamina * 0.5
            player1.stamina -= player2.stamina * 0.5
            if player2.stamina <= 0:
                player2.stamina = 0
                return f"Winner: {player1.name}"
            elif player1.stamina <= 0:
                player1.stamina = 0
                return f"Winner: {player2.name}"
            else:
                if player1.stamina < player2.stamina:
                    return f"Winner: {player2.name}"
                return f"Winner: {player1.name}"

        player1.stamina -= player2.stamina * 0.5
        player2.stamina -= player1.stamina * 0.5
        if player2.stamina <= 0:
            player2.stamina = 0
            return f"Winner: {player1.name}"
        elif player1.stamina <= 0:
            player1.stamina = 0
            return f"Winner: {player2.name}"
        else:
            if player1.stamina < player2.stamina:
                return f"Winner: {player2.name}"
            return f"Winner: {player1.name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0

        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(player.__str__())
        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)









