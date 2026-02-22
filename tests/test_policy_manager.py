from policy_manager.engine import PolicyEngine
from policy_manager.deployer import PolicyDeployer


def test_policy_engine_returns_false_when_policy_missing():
    engine = PolicyEngine()
    assert engine.evaluate({"resource": "db"}, "missing") is False


def test_policy_engine_returns_true_for_existing_policy():
    engine = PolicyEngine()
    engine.add_policy("baseline", {"allow": True})
    assert engine.evaluate({"resource": "db"}, "baseline") is True


def test_policy_deployer_returns_true():
    deployer = PolicyDeployer()
    assert deployer.deploy({"id": "p1"}, "aws") is True
