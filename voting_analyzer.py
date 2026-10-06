from dataclasses import dataclass
from itertools import permutations
from typing import Callable, Dict, Tuple

@dataclass(frozen=True)
class Voter:
    name: str
    weight: int

@dataclass(frozen=True)
class VotingSystem:
    name: str
    quota: int
    voters: Tuple[Voter, ...]

def evaluate_weighted_quota(system: VotingSystem, coalition: Tuple[Voter, ...]) -> bool:
    total_weight = sum(v.weight for v in coalition)
    return total_weight >= system.quota

# Dictionary dispatch replacing if-elif chains
VOTING_RULES: Dict[str, Callable[[VotingSystem, Tuple[Voter, ...]], bool]] = {
    "weighted_quota": evaluate_weighted_quota,
}

def calculate_shapley_shubik(system: VotingSystem, rule_name: str = "weighted_quota") -> Dict[str, float]:
    evaluator = VOTING_RULES[rule_name]
    voters = system.voters
    pivotal_counts = {v.name: 0 for v in voters}
    total_permutations = 0

    for perm in permutations(voters):
        total_permutations += 1
        current_coalition: List[Voter] = []
        for voter in perm:
            winning_before = evaluator(system, tuple(current_coalition))
            current_coalition.append(voter)
            winning_after = evaluator(system, tuple(current_coalition))
            if not winning_before and winning_after:
                pivotal_counts[voter.name] += 1
                break

    return {name: count / total_permutations for name, count in pivotal_counts.items()}

if __name__ == "__main__":
    # Example usage demonstrating module isolation
    sample_system = VotingSystem(
        name="EEC Council (Sample)",
        quota=8,
        voters=(
            Voter("France", 4),
            Voter("Germany", 4),
            Voter("Italy", 3),
            Voter("Benelux", 2)
        )
    )
    power_indices = calculate_shapley_shubik(sample_system)
    for voter_name, power in power_indices.items():
        print(f"{voter_name}: {power:.4f}")
