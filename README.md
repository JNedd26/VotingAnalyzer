# VotingAnalyzer
Measuring real voting influence in weighted voting systems using the Shapley-Shubik and Banzhaf power indices

## Project Aim: Combinatorial Voting Power Analyzer

In weighted voting systems, such as corporate boards or international legislative councils, a voter's nominal vote count does not reflect their actual political influence. A voter holding 30% of the formal weight can hold 0% of the actual power if decisions require thresholds where other coalitions always form winning blocks without them.

This project builds a computational engine to calculate two foundational game-theoretic power indices:

* **Shapley-Shubik Index:** Measures power based on the fraction of sequential permutations where a voter joins a coalition and turns it into a winning majority, known as the pivotal voter.
* **Banzhaf Power Index:** Measures power based on the count of winning coalitions where a voter's withdrawal causes the coalition to fail, known as swing voters.

Building this system eliminates structural anti-patterns like parallel data containers and monolithic functions, replacing them with strict `dataclass` models and dictionary-based algorithm dispatch.

## 4-Week Project Timeline

### Week 1: Data Architecture & Subset Generation

* **Objective:** Establish proper domain modeling instead of primitive collections.
* **Deliverables:**
* Define `Voter` and `VotingSystem` immutable `dataclass` objects.
* Implement subset and permutation generators using Python's `itertools`.
* Isolate data structures into a clean module with zero top-level side effects.


* **Deadline:** End of Day 7.

### Week 2: Computation Engines & Rule Dispatch

* **Objective:** Implement mathematical evaluation logic with scalable architecture.
* **Deliverables:**
* Build the Shapley-Shubik calculation loop.
* Build the Banzhaf power index calculation loop.
* Implement a dictionary-based rule dispatcher (`VOTING_RULES`) to handle distinct voting quotas without `if-elif` chains.


* **Deadline:** End of Day 14.

### Week 3: Advanced Git Workflows & CLI Interface

* **Objective:** Master professional version control and user interaction layers.
* **Deliverables:**
* Create separate Git feature branches (`feature/banzhaf-engine`, `feature/cli-interface`) and manage merges using GitHub.
* Build a command-line interface to accept custom voting weights and quotas via terminal arguments.
* Handle edge cases including dummy voters with zero power and dictators holding total weight.


* **Deadline:** End of Day 21.

### Week 4: Automated Testing & Production Readiness

* **Objective:** Eliminate manual print-statement debugging through rigorous testing.
* **Deliverables:**
* Author a comprehensive `pytest` suite in `tests/test_voting.py` covering all edge cases.
* Refactor any remaining inline literal data into configuration constants.
* Finalize the repository `README.md` explaining mathematical proofs and implementation details.


* **Deadline:** End of Day 28.

## Weekly Execution Checklist

| Week | Action Item | Verification Method |
| --- | --- | --- |
| **1** | Define `dataclass` models in `voting_analyzer.py` | Import models in Python shell without triggering side effects |
| **2** | Implement Shapley-Shubik permutation loop | Verify power sum across all voters equals `1.0` |
| **3** | Set up GitHub remote repository and feature branches | Push commits to GitHub and verify branch history via `git log --graph` |
| **4** | Write and execute `pytest` test suite | Run `pytest` in terminal and confirm 100% test pass rate |
