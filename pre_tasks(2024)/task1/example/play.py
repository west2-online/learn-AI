from __future__ import annotations
import copy
import random
import sys

import pokemon


def valid_choice(choice, range):
    # 判断输入的选择是否合法
    return choice.isdigit() and 1 <= int(choice) <= range


class Play:
    def __init__(self, all_pokemon) -> None:
        self.all_pokemon = all_pokemon
        self.player_team = []
        self.computer_team = []
        self.current_player_pokemon = None
        self.current_computer_pokemon = None
        self.turn = 0

    def player_choose_pokemon_team(self, pokemon_to_choose: list, num=1):
        # 玩家选择队伍中的Pokemon
        print(f"Choose {num} pokemon for your team:")
        pokemon_to_choose = copy.copy(pokemon_to_choose)
        index = 0
        while len(self.player_team) < num:
            self.print_pokemon_list(pokemon_to_choose)
            choice = input(f"Select your pokemon {index} by number: ")
            if valid_choice(choice, len(pokemon_to_choose)):
                self.player_team.append(pokemon_to_choose.pop(int(choice) - 1))
                index += 1
            else:
                print("Invalid choice, please select a valid Pokemon")
        print("Here is your pokemon team:")
        self.print_pokemon_list(self.player_team)

    def computer_choose_pokemon_team(self, pokemon_to_choose: list, num=1):
        # 电脑选择对战的队伍
        print(f"Your opponent is choosing {num} pokemon")
        self.computer_team.extend(random.sample(pokemon_to_choose, num))
        print("Here is your opponent's team:")
        self.print_pokemon_list(self.computer_team)

    def print_pokemon_list(self, pokemon_list):
        # 打印Pokemon列表
        for i, p in enumerate(pokemon_list, 1):
            print(f"{i}: {p}")

    def player_choose_pokemon(self):
        # 玩家选择当前战斗的Pokemon
        print("Your Team:")
        self.print_pokemon_list(self.player_team)
        while True:
            choice = input("Select your pokemon to battle by number:")
            if valid_choice(choice, len(self.player_team)):
                chosen_pokemon = self.player_team[int(choice) - 1]
                if chosen_pokemon.alive is True:
                    print(f"You choosed {chosen_pokemon.name}")
                    self.current_player_pokemon = chosen_pokemon
                    return chosen_pokemon  # 返回选择的Pokemon
                else:
                    print(f"{chosen_pokemon.name} has fainted! Choose another Pokemon!")
            else:
                print("Invalid choice, please select a valid Pokemon")

    def computer_choose_pokemon(self):
        # 电脑随机选择一个存活的Pokemon
        available_pokemon = [p for p in self.computer_team if p.alive is True]
        chosen_pokemon = random.choice(available_pokemon)
        print(f"Your opponent choosed {chosen_pokemon}")
        self.current_computer_pokemon = chosen_pokemon
        return chosen_pokemon  # 返回选择的Pokemon

    def game_finished(self):
        # 游戏结束
        sys.exit()

    def check_game_status(self):
        # 检查游戏状态，判断玩家或电脑是否失败
        is_player_fail = all(pokemon.alive is False for pokemon in self.player_team)
        is_computer_fail = all(pokemon.alive is False for pokemon in self.computer_team)
        if is_player_fail and is_computer_fail:
            print("All your and opponent's Pokemon have fainted. The game is tied.")
            self.game_finished()
        elif not is_player_fail and is_computer_fail:
            print("All computer's Pokemon have fainted. You win!")
            self.game_finished()
        elif is_player_fail and not is_computer_fail:
            print("All your Pokemon have fainted. You lose!")
            self.game_finished()

        if not self.current_player_pokemon.alive:
            self.player_choose_pokemon()
        if not self.current_computer_pokemon.alive:
            self.computer_choose_pokemon()

    def player_use_skills(self):
        # 玩家选择技能
        print("Choose the skill your pokemon to use")
        skills = self.current_player_pokemon.skills
        for i, skill in enumerate(skills, 1):
            print(f"{i}: {skill}")
        choice = input("Select the skill you want to use by number:")
        if valid_choice(choice, len(skills)):
            player_skill = self.current_player_pokemon.skills[int(choice) - 1]
            self.current_player_pokemon.use_skill(
                player_skill, self.current_computer_pokemon
            )
        else:
            print("Invalid choice, please select a valid Skill")

    def computer_use_skills(self):
        # 电脑随机选择技能
        computer_skill = random.choice(self.current_computer_pokemon.skills)
        self.current_computer_pokemon.use_skill(
            computer_skill, self.current_player_pokemon
        )

    def battle_round_begin(self):
        # 回合开始
        self.current_player_pokemon.begin()
        self.current_computer_pokemon.begin()
        self.check_game_status()

    def battle_round(self):
        # 回合进行
        print(
            f"\n{self.current_player_pokemon.name} vs {self.current_computer_pokemon.name}"
        )
        self.player_use_skills()
        self.computer_use_skills()
        self.check_game_status()

    def run(self):
        # 游戏主循环
        self.player_choose_pokemon_team(self.all_pokemon)
        self.computer_choose_pokemon_team(self.all_pokemon)

        print("Choose Your First Pokemon to battle")
        self.current_player_pokemon = self.player_choose_pokemon()
        self.current_computer_pokemon = self.computer_choose_pokemon()

        while True:
            self.battle_round_begin()
            self.battle_round()


if __name__ == "__main__":
    pokemon1 = pokemon.Bulbasaur()
    all_pokemon = [pokemon1]
    play = Play(all_pokemon)
    play.run()
