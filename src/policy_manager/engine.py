"""Policy evaluation engine"""
from typing import Dict, List

class PolicyEngine:
    def __init__(self):
        self.policies = {}
        
    def add_policy(self, name: str, policy: Dict):
        self.policies[name] = policy
        
    def evaluate(self, resource: Dict, policy_name: str) -> bool:
        policy = self.policies.get(policy_name)
        if not policy:
            return False
        # Simple evaluation logic
        return True
