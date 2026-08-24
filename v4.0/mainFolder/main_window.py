import tkinter as tk
import json
import math
from player import player
from beast import get_enemy
from engine import playerNormalAttack, playerPowerAttack
from ai import enemyAI

class VorrexApp:
    def __init__(self, window):
        self.window = window
        self.BG = "#1a1a2e"
        self.ACCENT = "#e94560"
        self.ACCENT2 = "#00b4d8"
        self.TEXT = "#eaeaea"
        window.config(bg=self.BG)
        self.player = player
        self.is_enemy_defended = False

        self.show_start_screen()

    def clear_screen(self):
        for w in self.window.winfo_children():
            w.place_forget()

    def make_button(self, parent, text, command, relx, rely, **kwargs):
        button = tk.Button(
            parent,
            text=text,
            fg=self.ACCENT,
            bg=self.BG,
            activeforeground=self.ACCENT,
            activebackground=self.BG,
            command=command,
            **kwargs
        )
        button.place(relx=relx, rely=rely, anchor="center")
        button.bind("<Enter>", lambda e: self.on_enter(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))
        return button

    def on_enter(self, button):
        button.config(
                background="#222238",
                foreground="#da3551",
                bd=3,
                highlightbackground="white",
                relief="sunken",
                highlightthickness=2
            )

    def on_leave(self, button):
        button.config(
                background=self.BG,
                foreground=self.ACCENT,
                bd=2,
                highlightbackground="SystemButtonFace",
                relief="raised",
                highlightthickness=1
        )

    def close_program(self):
        self.window.destroy()

    def show_start_screen(self):
        global main_name, tagline, main_play_btn, main_quit_btn

        self.clear_screen()
        
        # Main Title Name

        main_name = tk.Label(
            self.window,
            text="VORREX",
            fg=self.ACCENT,
            bg=self.BG,
            font=("Impact", 66, "underline")
        )
        main_name.place(relx=0.5, rely=0.09, anchor="center")

        # Sub-Title(tagline) below Main Title

        tagline = tk.Label(
            self.window,
            text="Every Move Costs!",
            fg=self.TEXT,
            bg=self.BG,
            font=("Impact", 48, "bold")
        )
        tagline.place(relx=0.5, rely=0.26, anchor="center")

        # Play Button

        main_play_btn = self.make_button(
            self.window,
            text="Play",
            font=("Impact", 24),
            width=8,
            height=1,
            padx=60,
            pady=4,
            command=self.show_mode_select,
            relx=0.5,
            rely=0.48
        )

        # Quit Button

        main_quit_btn = self.make_button(
            self.window,
            text="Quit",
            font=("Impact", 24),
            width=8,
            height=1,
            padx=61,
            pady=4,
            command=self.close_program,
            relx=0.5,
            rely=0.68
        )

    def show_mode_select(self):
        global main_box, select_mode_title, back_btn_main, classic_mode_button

        # Erasing the main menu

        self.clear_screen()

        # The White Border around the main contents

        main_box = tk.Frame(
                self.window,
                bd=3,
                highlightbackground="white",
                highlightthickness=2,
                bg=self.BG,
                height=480,
                width=930
            )
        main_box.place(relx=0.5, rely=0.5, anchor="center")

        # Back Button

        def on_back_btn():
            self.clear_screen()
            main_name.place(relx=0.5, rely=0.09, anchor="center")
            tagline.place(relx=0.5, rely=0.26, anchor="center")
            main_play_btn.place(relx=0.5, rely=0.48, anchor="center")
            main_quit_btn.place(relx=0.5, rely=0.68, anchor="center")

        back_btn_main = self.make_button(
                self.window,
                text="Back",
                padx=14,
                font=("Impact", 14),
                relx=0.09,
                rely=0.04,
                command=on_back_btn
            )

        select_mode_title = tk.Label(
                self.window,
                text="Select Gamemode",
                font=("Impact", 44, "bold"),
                bg=self.BG,
                fg=self.TEXT
            )
        select_mode_title.place(relx=0.5, rely=0.18, anchor="center")

        classic_mode_button = self.make_button(
                self.window,
                text="Classic",
                width=45,
                padx=0,
                pady=8,
                font=("Impact", 20),
                relx=0.5,
                rely=0.46,
                command=self.show_classic_screen
            )

    def show_classic_screen(self):
        global enemy_atk_label, enemy_health_label, enemy_name_label

        self.clear_screen()
        main_box.place(relx=0.5, rely=0.5, anchor="center")

        classic_title = tk.Label(
            self.window,
            text="Classic",
            font=("Impact", 58, "underline"),
            fg=self.TEXT,
            bg=self.BG,
            activebackground=self.BG,
            activeforeground=self.TEXT
        )

        classic_title.place(relx=0.5, rely=0.17, anchor="center")

        player_card = tk.Frame(
            self.window,
            bg=self.ACCENT2,
            highlightthickness=3,
            highlightbackground="#0c8aa3",
            height="90",
            width="470"
        )

        player_card.place(relx=0.32, rely=0.4, anchor="center")

        player_name_label = tk.Label(
            player_card,
            text="PLAYER",
            bg=self.ACCENT2,
            fg=self.BG,
            font=("Impact", 20)
        )
        player_name_label.place(relx=0.05, rely=0.28, anchor="w")

        stat_divider = tk.Frame(player_card, bg=self.BG, height=2, width=440)
        stat_divider.place(relx=0.05, rely=0.52, anchor="w")

        player_health_label = tk.Label(
            player_card,
            text="HP  100",
            bg=self.ACCENT2,
            fg=self.BG,
            font=("Impact", 15)
        )
        player_health_label.place(relx=0.05, rely=0.75, anchor="w")

        player_atk_label = tk.Label(
            player_card,
            text="ATK  25",
            bg=self.ACCENT2,
            fg=self.BG,
            font=("Impact", 15)
        )
        player_atk_label.place(relx=0.6, rely=0.75, anchor="w")

        start_btn = self.make_button(
            self.window,
            text="Start",
            command=self.reveal_enemy,
            font=("Impact", 22),
            padx=62,
            pady=0,
            rely=0.4,
            relx=0.76
        )

        vs_label = tk.Label(
            self.window,
            text="VS",
            fg=self.TEXT,
            bg=self.BG,
            font=("Impact", 22, "bold")
        )
        vs_label.place(relx=0.49, rely=0.55, anchor="center")

        enemy_card = tk.Frame(
            self.window,
            bg=self.ACCENT,
            highlightthickness=3,
            highlightbackground="#ac3c4f",
            height="90",
            width="470"
        )

        enemy_card.place(relx=0.68, rely=0.7, anchor="center")

        enemy_name_label = tk.Label(
            enemy_card,
            text="BEAST",
            bg=self.ACCENT,
            fg=self.BG,
            font=("Impact", 20)
        )
        enemy_name_label.place(relx=0.05, rely=0.28, anchor="w")

        enemy_divider = tk.Frame(enemy_card, bg=self.BG, height=2, width=440)
        enemy_divider.place(relx=0.05, rely=0.52, anchor="w")

        enemy_health_label = tk.Label(
            enemy_card,
            text="HP  ???",
            bg=self.ACCENT,
            fg=self.BG,
            font=("Impact", 15)
        )
        enemy_health_label.place(relx=0.05, rely=0.75, anchor="w")

        enemy_atk_label = tk.Label(
            enemy_card,
            text="ATK  ???",
            bg=self.ACCENT,
            fg=self.BG,
            font=("Impact", 15)
        )
        enemy_atk_label.place(relx=0.6, rely=0.75, anchor="w")

        def on_back_btn():
            self.clear_screen()

            main_box.place(relx=0.5, rely=0.5, anchor="center")
            select_mode_title.place(relx=0.5, rely=0.18, anchor="center")
            back_btn_main.place(relx=0.09, rely=0.04, anchor="center")
            classic_mode_button.place(relx=0.5, rely=0.46, anchor="center")

        back_btn = self.make_button(
            self.window,
            text="Back",
            padx=14,
            font=("Impact", 14),
            relx=0.09,
            rely=0.04,
            command=on_back_btn
        )

    def reveal_enemy(self):
        self.enemy = get_enemy()

        enemy_name_label.config(text=self.enemy["enemy_name"])
        enemy_health_label.config(text=f'HP  {self.enemy["enemy_init_health"]}')
        enemy_atk_label.config(text=f'ATK  {self.enemy["enemy_atk"]}')

        self.window.after(2000, self.show_classic_main)

    def show_classic_main(self):
        global battle_enemy_health_label, battle_player_health_label
        global player_bar_canvas, player_bar_fill, enemy_bar_canvas, enemy_bar_fill
        global battle_screen_frame

        self.clear_screen()

        self.enemy["enemy_energy"] = self.enemy.get("enemy_energy", 100)

        screen = tk.Frame(
                self.window,
                bd=3,
                highlightbackground="white",
                highlightthickness=2,
                bg=self.BG,
                height=300,
                width=920
            )
        screen.place(relx=0.5, rely=0.34, anchor="center")
        battle_screen_frame = screen

        bar_width = 380
        bar_height = 22

        # Player row: name/HP text above a bar
        battle_player_health_label = tk.Label(
            screen,
            text=f'You  HP: {self.player["player_health"]}',
            bg=self.BG,
            fg=self.ACCENT2,
            font=("Impact", 18)
        )
        battle_player_health_label.place(relx=0.5, rely=0.08, anchor="center")

        player_bar_canvas = tk.Canvas(
            screen, width=bar_width, height=bar_height,
            bg="#0d0d1a", highlightthickness=1, highlightbackground=self.ACCENT2
        )
        player_bar_canvas.place(relx=0.5, rely=0.22, anchor="center")
        player_bar_fill = player_bar_canvas.create_rectangle(
            0, 0, bar_width, bar_height, fill=self.ACCENT2, width=0
        )

        # Enemy row: name/HP text above a bar
        battle_enemy_health_label = tk.Label(
            screen,
            text=f'{self.enemy["enemy_name"]}  HP: {self.enemy["enemy_health"]}',
            bg=self.BG,
            fg=self.ACCENT,
            font=("Impact", 18)
        )
        battle_enemy_health_label.place(relx=0.5, rely=0.42, anchor="center")

        enemy_bar_canvas = tk.Canvas(
            screen, width=bar_width, height=bar_height,
            bg="#0d0d1a", highlightthickness=1, highlightbackground=self.ACCENT
        )
        enemy_bar_canvas.place(relx=0.5, rely=0.56, anchor="center")
        enemy_bar_fill = enemy_bar_canvas.create_rectangle(
            0, 0, bar_width, bar_height, fill=self.ACCENT, width=0
        )

        self.refresh_hp_bars()

        normal_atk_btn = self.make_button(
            self.window,
            text="Normal Attack",
            command=self.player_normal_attack,
            relx=0.32,
            rely=0.77,
            font=("Impact", 24)
        )

        power_atk_btn = self.make_button(
            self.window,
            text="Power Attack",
            command=self.player_power_attack,
            relx=0.68,
            rely=0.77,
            font=("Impact", 24)
        )

    def player_normal_attack(self):
        dmg, self.enemy["enemy_health"], self.player["player_xp"], self.is_enemy_defended = playerNormalAttack(
            self.enemy["enemy_health"], self.player["player_xp"], self.is_enemy_defended
        )
        self.show_damage_popup(enemy_side=True, amount=math.ceil(dmg / 10) if dmg else 0)
        self.after_player_turn()

    def player_power_attack(self):
        dmg, self.enemy["enemy_health"], self.player["player_energy"], self.player["player_xp"], self.is_enemy_defended = playerPowerAttack(
            self.enemy["enemy_health"], self.player["player_energy"], self.player["player_xp"], self.is_enemy_defended
        )
        self.show_damage_popup(enemy_side=True, amount=math.ceil(dmg / 10) if dmg else 0)
        self.after_player_turn()

    def after_player_turn(self):
        self.update_battle_labels()

        if self.enemy["enemy_health"] <= 0:
            self.end_battle(won=True)
            return

        # Enemy turn
        is_player_defended = False
        health_before = self.player["player_health"]
        enemy_dmg, self.player["player_health"], self.enemy["enemy_energy"], is_player_defended, self.is_enemy_defended, self.player["player_xp"] = enemyAI(
            self.enemy["enemy_health"],
            self.player["player_health"],
            self.enemy.get("enemy_energy", 100),
            self.player["player_energy"],
            0,
            0,
            is_player_defended,
            self.is_enemy_defended,
            self.player["player_xp"],
            self.enemy["enemy_init_health"]
        )
        self.enemy["enemy_energy"] = self.enemy.get("enemy_energy", 100)

        taken = health_before - self.player["player_health"]
        if taken > 0:
            self.show_damage_popup(enemy_side=False, amount=taken)

        self.update_battle_labels()

        if self.player["player_health"] <= 0:
            self.end_battle(won=False)

    def refresh_hp_bars(self):
        bar_width = 380

        enemy_frac = max(0, self.enemy["enemy_health"]) / self.enemy["enemy_init_health"]
        enemy_frac = min(1, max(0, enemy_frac))
        enemy_bar_canvas.coords(enemy_bar_fill, 0, 0, bar_width * enemy_frac, 22)

        player_frac = max(0, self.player["player_health"]) / self.player["player_init_health"]
        player_frac = min(1, max(0, player_frac))
        player_bar_canvas.coords(player_bar_fill, 0, 0, bar_width * player_frac, 22)

    def show_damage_popup(self, enemy_side, amount):
        if amount <= 0:
            return

        rely = 0.56 if enemy_side else 0.22
        popup = tk.Label(
            battle_screen_frame,
            text=f"-{amount}",
            bg=self.BG,
            fg="#ff4d4d",
            font=("Impact", 16)
        )
        popup.place(relx=0.85, rely=rely, anchor="center")
        self.window.after(700, popup.destroy)

    def update_battle_labels(self):
        battle_enemy_health_label.config(
            text=f'{self.enemy["enemy_name"]}  HP: {max(0, self.enemy["enemy_health"])}'
        )
        battle_player_health_label.config(
            text=f'You  HP: {max(0, self.player["player_health"])}'
        )
        self.refresh_hp_bars()

    def end_battle(self, won):
        self.clear_screen()

        if won:
            self.player["player_xp"] += 20
            msg = f'You defeated {self.enemy["enemy_name"]}!! VICTORY!! 🏆'
        else:
            msg = f'{self.enemy["enemy_name"]} defeated you!! DEFEAT!! 😞'

        self.save_progress()

        result_label = tk.Label(
            self.window,
            text=msg,
            bg=self.BG,
            fg=self.TEXT,
            font=("Impact", 26),
            wraplength=800
        )
        result_label.place(relx=0.5, rely=0.4, anchor="center")

        menu_btn = self.make_button(
            self.window,
            text="Back to Menu",
            command=self.show_start_screen,
            font=("Impact", 20),
            padx=20,
            pady=4,
            relx=0.5,
            rely=0.6
        )

    def save_progress(self):
        xp = self.player["player_xp"]
        level = self.player["player_level"]

        if xp >= 100:
            xp -= 100
            level += 1

        data = {"level": level, "experience": xp}
        try:
            with open("save.json", "w") as f:
                json.dump(data, f, indent=4)
        except OSError:
            pass
