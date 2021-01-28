import data.requirement


class InGroupRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be in group {0}."


class ASkyBlockLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least an (skyblock) island level of {0}."


class AcidIslandLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least an (acid) island level of {0}."


class AdvancementRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Obtain at least {0} advancements."


class AnimalsBredRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Breed at least {0} animals."


class AureliumSkillsManaRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} mana."


class AureliumSkillsSkillRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Reach level {0} in {1}."


class AureliumSkillsStatRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Reach level {0} in {1}."


class AureliumSkillsXPRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have {0} xp in {1}."


class AutorankActivePathsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} active paths."


class AutorankCompletedPathsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least completed {0} paths."


class BattleLevelsKDRRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least a KDR of {0} in BattleLevels."


class BattleLevelsKillStreakRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Kill at least {0} players in a row in BattleLevels."


class BattleLevelsKillsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Killed at least {0} players in BattleLevels."


class BattleLevelsLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least a level of {0} in BattleLevels."


class BattleLevelsScoreRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least a score of {0} in BattleLevels."


class BattleLevelsTopKillStreakRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Kill at least {0} players in a row in BattleLevels."


class BlocksBrokenRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Break at least {0}."


class BlocksMovedRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Travel at least {0} {1}."


class BlocksPlacedRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Place at least {0}."


class CakeSlicesEatenRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Eat at least {0} slices of cake."


class DamageTakenRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Take at least {0} damage."


class EssentialsGeoIPRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be from area {0}."


class ExpRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least level {0} in exp."


class FactionPowerRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} power in your faction."


class FishCaughtRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Catch at least {0} fish."


class FoodEatenRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Eat at least {0}."


class GamemodeRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be in gamemode {0}."


class GlobalTimeRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Play for at least {0} on any of the servers."


class GriefPreventionBonusBlocksRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} bonus blocks in GriefPrevention."


class GriefPreventionClaimedBlocksRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} claimed blocks in GriefPrevention."


class GriefPreventionClaimsCountRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} claims in GriefPrevention."


class GriefPreventionRemainingBlocksRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} remaining blocks to use in claims in GriefPrevention."


class HasItemRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Obtain {0}."


class InBiomeRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be in biome {0}."


class ItemThrownRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Throw at least {0} {1}."


class ItemsCraftedRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Craft at least {0} item(s)."


class ItemsEnchantedRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Enchant at least {0} items."


class JavaScriptRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Meet Javascript rule"


class JobsCurrentPointsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} points in Jobs."


class JobsExperienceRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} experience in the job '{1}'."


class JobsLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least level {0} in the job '{1}'."


class JobsTotalPointsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} points in total in Jobs."


class LocationRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be at {0}."


class McMMOPowerLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least power level {0}."


class McMMOSkillLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least level {0} in {1}."


class McRPGPowerLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least power level {0}."


class McRPGSkillLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least level {0} in {1}."


class MobKillsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Kill at least {0}."


class MoneyRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0}."


class PermissionRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have permission {0}."


class PlantsPottedRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Pot at least {0} plants."


class PlayerKillsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Kill at least {0} player(s)."


class PlayerPointsPointsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Obtain at least {0} player points."


class QuestsActiveQuestsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have {0} quests active at the same time."


class QuestsCompleteSpecificQuestRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Complete the quest '{0}'."


class QuestsCompletedQuestsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Complete at least {0} quests."


class QuestsQuestPointsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Obtain at least {0} quest points."


class RPGMeCombatLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least a combat level of {0} in RPGme."


class RPGMeSkillLevelRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least level {0} in {1} in RPGme."


class SavageFactionsPowerRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Have at least {0} power in your faction."


class TimeDailyRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Play for at least {0} in a single day."


class TimeMonthlyRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Play for at least {0} in a month."


class TimeRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Play for at least {0}."


class TimeWeeklyRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Play for at least {0} in a week."


class TimesDiedRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Die at least {0} times."


class TimesShornRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Shear at least {0} sheep."


class TotalTimeRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be with this server for at least {0}."


class TotalVotesRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Vote at least {0} times."


class TownyHasANationRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Need to be part of a nation."


class TownyHasATownRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Need to be part of a town."


class TownyIsKingRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Need to be king of a nation."


class TownyIsMayorRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Need to be mayor of a town."


class TownyNumberOfTownBlocksRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Need to have at least {0} town blocks."


class TradedWithVillagersRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Trade at least {0} with villagers."


class UHCStatsDeathsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Get at least {0} deaths."


class UHCStatsKillsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Get at least {0} kills."


class UHCStatsWinsRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Get at least {0} wins."


class WorldGuardRegionRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be in region {0}."


class WorldRequirement(data.requirement.Requirement):
    def default_description(self) -> str:
        return "Be in {0}."
