import enum
from typing import List, Optional

import data.requirements.requirements as requirements


class RequirementType(enum.Enum):
    """
    This a type of requirement. Note that this is a enum, but it has two member variables. These member variables
    are used to keep track of identifiers that can be used in the Paths.yml file. The other member variable is used to
    be able to create instances of requirements that implement the abstract Requirement class.
    """

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, identifiers: [], requirement):
        # Identifiers that can be used in the Paths.yml
        self.config_identifiers: List[str] = identifiers

        # Class that is used to create a new instance of the implemented requirement
        self.requirement_class: "Requirement" = requirement

    @staticmethod
    def get_requirement_from_identifier(identifier: str) -> Optional["RequirementType"]:
        """
        Find an instance of a RequirementType for a given identifier

        :param identifier: Identifier to look up
        :return: the corresponding RequirementType or None if none was matching
        """
        requirement: "RequirementType"
        for requirement in RequirementType:
            if identifier in requirement.config_identifiers:
                return requirement
        return None

    # Define requirement types
    IN_GROUP_REQUIREMENT = ["in group"], requirements.InGroupRequirement
    ASKYBLOCK_LEVEL_REQUIREMENT = ["askyblock level"], requirements.ASkyBlockLevelRequirement
    ACIDISLAND_LEVEL_REQUIREMENT = ["acidisland level"], requirements.AcidIslandLevelRequirement
    ADVANCEMENT_REQUIREMENT = ["has advancement"], requirements.AdvancementRequirement
    ANIMALS_BRED_REQUIREMENT = ["animals bred"], requirements.AnimalsBredRequirement
    AURELIUM_SKILLS_MANA_REQUIREMENT = ["aurelium skills mana"], requirements.AureliumSkillsManaRequirement
    AURELIUM_SKILLS_SKILL_REQUIREMENT = ["aurelium skills skill level"], requirements.AureliumSkillsSkillRequirement
    AURELIUM_SKILLS_STAT_REQUIREMENT = ["aurelium skills stat level"], requirements.AureliumSkillsStatRequirement
    AURELIUM_SKILLS_XP_REQUIREMENT = ["aurelium skills xp"], requirements.AureliumSkillsXPRequirement
    ACTIVE_PATHS_REQUIREMENT = ["active paths"], requirements.AutorankActivePathsRequirement
    COMPLETED_PATHS_REQUIREMENT = ["completed paths"], requirements.AutorankCompletedPathsRequirement
    BATTLE_LEVELS_KDR_REQUIREMENT = ["battlelevels kdr"], requirements.BattleLevelsKDRRequirement
    BATTLE_LEVELS_KILLSTREAK_REQUIREMENT = ["battlelevels killstreak"], requirements.BattleLevelsKillStreakRequirement
    BATTLE_LEVELS_KILLS_REQUIREMENT = ["battlelevels kills"], requirements.BattleLevelsKillsRequirement
    BATTLE_LEVELS_TOP_KILLSTREAK_REQUIREMENT = ["battlelevels top killstreak"], requirements.BattleLevelsTopKillStreakRequirement
    BATTLE_LEVELS_SCORE_REQUIREMENT = ["battlelevels score"], requirements.BattleLevelsScoreRequirement
    BATTLE_LEVELS_LEVEL_REQUIREMENT = ["battlelevels level"], requirements.BattleLevelsLevelRequirement
    BLOCKS_BROKEN_REQUIREMENT = ["blocks broken"], requirements.BlocksBrokenRequirement
    BLOCKS_MOVED_REQUIREMENT = ["blocks moved"], requirements.BlocksMovedRequirement
    BLOCKS_PLACED_REQUIREMENT = ["blocks placed"], requirements.BlocksPlacedRequirement
    CAKE_SLICES_EATEN_REQUIREMENT = ["cake slices eaten"], requirements.CakeSlicesEatenRequirement
    DAMAGE_TAKEN_REQUIREMENT = ["damage taken"], requirements.DamageTakenRequirement
    ESSENTIALS_GEOIP_REQUIREMENT = ["essentials geoip location"], requirements.EssentialsGeoIPRequirement
    EXP_REQUIREMENT = ["exp"], requirements.ExpRequirement
    FACTION_POWER_REQUIREMENT = ["faction power"], requirements.FactionPowerRequirement
    FISH_CAUGHT_REQUIREMENT = ["fish caught"], requirements.FishCaughtRequirement
    FOOD_EATEN_REQUIREMENT = ["food eaten"], requirements.FoodEatenRequirement
    GAME_MODE_REQUIREMENT = ["gamemode"], requirements.GamemodeRequirement
    GLOBAL_TIME_REQUIREMENT = ["global time"], requirements.GlobalTimeRequirement
    GRIEF_PREVENTION_BONUS_BLOCKS_REQUIREMENT = ["grief prevention bonus blocks"], requirements.GriefPreventionBonusBlocksRequirement
    GRIEF_PREVENTION_CLAIMED_BLOCKS_REQUIREMENT = ["grief prevention claimed blocks"], requirements.GriefPreventionClaimedBlocksRequirement
    GRIEF_PREVENTION_CLAIMS_COUNT_REQUIREMENT = ["grief prevention claims"], requirements.GriefPreventionClaimsCountRequirement
    GRIEF_PREVENTION_REMAINING_BLOCKS_REQUIREMENT = ["grief prevention remaining blocks"], requirements.GriefPreventionRemainingBlocksRequirement
    HAS_ITEM_REQUIREMENT = ["has item"], requirements.HasItemRequirement
    IN_BIOME_REQUIREMENT = ["in biome"], requirements.InBiomeRequirement
    ITEM_THROWN_REQUIREMENT = ["item thrown"], requirements.ItemThrownRequirement
    ITEMS_CRAFTED_REQUIREMENT = ["items crafted"], requirements.ItemsCraftedRequirement
    ITEMS_ENCHANTED_REQUIREMENT = ["items enchanted"], requirements.ItemsEnchantedRequirement
    JAVASCRIPT_REQUIREMENT = ["javascript"], requirements.JavaScriptRequirement
    JOBS_CURRENT_POINTS_REQUIREMENT = ["jobs current points"], requirements.JobsCurrentPointsRequirement
    JOBS_LEVEL_REQUIREMENT = ["jobs level"], requirements.JobsLevelRequirement
    JOBS_EXPERIENCE_REQUIREMENT = ["jobs experience"], requirements.JobsExperienceRequirement
    JOBS_TOTAL_POINTS_REQUIREMENT = ["jobs total points"], requirements.JobsTotalPointsRequirement
    LOCATION_REQUIREMENT = ["location"], requirements.LocationRequirement
    MCMMO_SKILL_LEVEL_REQUIREMENT = ["mcmmo skill level"], requirements.McMMOSkillLevelRequirement
    MCMMO_POWER_LEVEL_REQUIREMENT = ["mcmmo power level"], requirements.McMMOPowerLevelRequirement
    MCRPG_POWER_LEVEL_REQUIREMENT = ["mcrpg power level"], requirements.McRPGPowerLevelRequirement
    MCRPG_SKILL_LEVEL_REQUIREMENT = ["mcrpg skill level"], requirements.McRPGSkillLevelRequirement
    MOB_KILLS_REQUIREMENT = ["mobs killed"], requirements.MobKillsRequirement
    MONEY_REQUIREMENT = ["money"], requirements.MoneyRequirement
    PERMISSION_REQUIREMENT = ["permission"], requirements.PermissionRequirement
    PLANTS_POTTED_REQUIREMENT = ["plants potted"], requirements.PlantsPottedRequirement
    PLAYER_KILLS_REQUIREMENT = ["players killed"], requirements.PlayerKillsRequirement
    PLAYER_POINTS_POINTS_REQUIREMENT = ["playerpoints points"], requirements.PlayerPointsPointsRequirement
    QUESTS_ACTIVE_QUESTS_REQUIREMENT = ["quests active quests"], requirements.QuestsActiveQuestsRequirement
    QUESTS_COMPLETE_SPECIFIC_QUEST_REQUIREMENT = ["quests complete quest"], requirements.QuestsCompleteSpecificQuestRequirement
    QUEST_COMPLETED_QUESTS_REQUIREMENT = ["quests completed quests"], requirements.QuestsCompletedQuestsRequirement
    QUESTS_QUEST_POINTS_REQUIREMENT = ["quests quest points"], requirements.QuestsQuestPointsRequirement
    RPGME_COMBAT_LEVEL_REQUIREMENT = ["rpgme combat level"], requirements.RPGMeCombatLevelRequirement
    RPGME_SKILL_LEVEL_REQUIREMENT = ["rpgme skill level"], requirements.RPGMeSkillLevelRequirement
    SAVAGEFACTIONS_POWER_REQUIREMENT = ["savagefactions faction power"], requirements.SavageFactionsPowerRequirement
    TIME_DAILY_REQUIREMENT = ["daily time"], requirements.TimeDailyRequirement
    TIME_MONTHLY_REQUIREMENT = ["monthly time"], requirements.TimeMonthlyRequirement
    TIME_REQUIREMENT = ["time"], requirements.TimeRequirement
    TIME_WEEKLY_REQUIREMENT = ["weekly time"], requirements.TimeWeeklyRequirement
    TIMES_DIED_REQUIREMENT = ["times died"], requirements.TimesDiedRequirement
    TIMES_SHORN_REQUIREMENT = ["times sheared"], requirements.TimesShornRequirement
    TOTAL_TIME_REQUIREMENT = ["total time"], requirements.TotalTimeRequirement
    TOTAL_VOTES_REQUIREMENT = ["votes"], requirements.TotalVotesRequirement
    TOWNY_HAS_A_NATION_REQUIREMENT = ["towny has nation"], requirements.TownyHasANationRequirement
    TOWNY_HAS_A_TOWN_REQUIREMENT = ["towny has town"], requirements.TownyHasATownRequirement
    TOWNY_IS_KING_REQUIREMENT = ["towny is king"], requirements.TownyIsKingRequirement
    TOWNY_IS_MAYOR_REQUIREMENT = ["towny is mayor"], requirements.TownyIsMayorRequirement
    TOWNY_NUMBER_OF_TOWN_BLOCKS_REQUIREMENT = ["towny town blocks"], requirements.TownyNumberOfTownBlocksRequirement
    TRADED_WITH_VILLAGERS_REQUIREMENT = ["traded with villagers"], requirements.TradedWithVillagersRequirement
    UHCSTATS_DEATHS_REQUIREMENT = ["uhcstats deaths"], requirements.UHCStatsDeathsRequirement
    UHCSTATS_KILLS_REQUIREMENT = ["uhcstats kills"], requirements.UHCStatsKillsRequirement
    UHCSTATS_WINS_REQUIREMENT = ["uhcstats wins"], requirements.UHCStatsWinsRequirement
    WORLDGUARD_REGION_REQUIREMENT = ["worldguard region"], requirements.WorldGuardRegionRequirement
    WORLD_REQUIREMENT = ["world"], requirements.WorldRequirement
