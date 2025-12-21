"""Multi-cloud policy deployment"""
class PolicyDeployer:
    def deploy(self, policy: Dict, cloud: str) -> bool:
        print(f"Deploying policy to {cloud}")
        return True
