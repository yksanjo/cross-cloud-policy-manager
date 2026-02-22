"""Multi-cloud policy deployment"""
from typing import Dict


class PolicyDeployer:
    def deploy(self, policy: Dict, cloud: str) -> bool:
        print(f"Deploying policy to {cloud}")
        return True
