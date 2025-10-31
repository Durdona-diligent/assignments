def calculate_experience_points(game_mode, missions_completed, difficulty):
    xp_per_mission = 0
    if game_mode == "campaign":
        if difficulty == "easy":
            xp_per_mission = 50
        elif difficulty  == "normal":
            xp_per_mission = 85
        elif difficulty == "hard":
            xp_per_mission = 150
    if game_mode == "multiplayer":
        if difficulty == "easy":
            xp_per_mission = 30
        elif difficulty == "normal":
            xp_per_mission = 55
        elif difficulty == "hard":
            xp_per_mission = 95
    if game_mode == "tutorial":
        if difficulty == "easy":
            xp_per_mission = 15
        if difficulty == "normal":
            xp_per_mission = 25
        if difficulty == "hard":
            xp_per_mission = 40    
    total_xp = xp_per_mission * missions_completed
    return total_xp
def calculate_skill_rating(play_hours, baseline_score, current_score):
    expected_score = 1000 + (play_hours * 100)
    score_range = expected_score - baseline_score
    skill_percentage = (current_score - baseline_score) / score_range * 100
    return skill_percentage
def determine_player_rank(skill_percent):
    if  skill_percent < 50:
        return "Bronze Rank"
    elif skill_percent < 60:
        return "Silver Rank"
    elif skill_percent < 70:
        return "Gold Rank"
    elif skill_percent < 85:
        return "Platinum Rank"
    else:
        return "Diamond Rank"
def calculate_reward_coins(xp_points, missions, rank_bonus):
    base_coins = xp_points * 0.05 + missions * 2
    final_coins = base_coins * rank_bonus
    return round(final_coins, 1)
def needs_practice_mode(gaming_days, total_missions, avg_skill):
    if gaming_days >= 6 and avg_skill < 50:
        return True
    elif total_missions < 100 and avg_skill < 60:
        return True
    elif gaming_days >= 4 and avg_skill < 40:
        return True
    else:
        return False
def generate_achievement_summary(player_name, game_mode, missions, difficulty, play_hours, baseline_score, current_score, gaming_days):
    print("========================================")
    print("Achievement Summary for: ", player_name)
    print("----------------------------------------")
    print("Game Mode: ", game_mode)
    print("Missions Completed: ", missions)
    print("Difficulty: ", difficulty)
    xp_points = calculate_experience_points(game_mode, missions, difficulty)
    print("Experience Points: ", xp_points)
    skill_percent = calculate_skill_rating(play_hours, baseline_score, current_score)
    print("Skill Analysis:")
    print("  Play Hours: ", play_hours, "Baseline: ", baseline_score, "Current Score: ", current_score)
    print("  Skill Rating: ", round(skill_percent, 1), "%")
    player_rank = determine_player_rank(skill_percent)
    print("  Player Rank: ", player_rank)
    if player_rank == "Bronze Rank":
        bonus = 0.5
    elif player_rank == "Silver Rank":
        bonus = 1.0
    elif player_rank == "Gold Rank":
        bonus = 1.2
    elif player_rank == "Platinum Rank":
        bonus = 1.5
    elif player_rank == "Diamond Rank":
        bonus = 1.8    
    coins = calculate_reward_coins(xp_points, missions, bonus)
    print("Reward Coins: ", coins)
    print("Gaming Days: ", gaming_days)
    practice = needs_practice_mode(gaming_days, missions, skill_percent)
    if practice:
        print("Practice Mode Needed: Yes")
    else:
        print("Practice Mode Needed: No")
print("GAMING ACHIEVEMENT TRACKER")
generate_achievement_summary("Phoenix", "campaign", 45, "hard", 3, 800, 1150, 3)
generate_achievement_summary("Storm", "multiplayer", 60, "normal", 5, 900, 1300, 5)
generate_achievement_summary("Echo", "tutorial", 30, "easy", 8, 850, 950, 7)