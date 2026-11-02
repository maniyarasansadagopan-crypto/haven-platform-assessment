
"""
B2, part 2 — implement the cost-tagging check.

Checks Terraform plan resources for the required landlord_account_id tag.
"""

import json
import sys

REQUIRED_TAG = "landlord_account_id"


def check_plan(plan_path: str) -> int:
    """
    Returns an exit code:
    0 if every resource being created/changed has landlord_account_id.
    1 if one or more resources are missing the required tag.
    """

    with open(plan_path, "r", encoding="utf-8") as file:
        plan = json.load(file)

    failures = set()

    for resource in plan.get("resource_changes", []):
        change = resource.get("change", {})
        actions = change.get("actions", [])

        # Only check resources being created or updated
        if not any(action in ("create", "update") for action in actions):
            continue

        after = change.get("after") or {}
        tags = after.get("tags") or {}

        # Check the required billing-unit tag
        if not isinstance(tags, dict) or not tags.get(REQUIRED_TAG):
            failures.add(resource.get("address", "<unknown resource>"))

    # Print failures in deterministic order
    if failures:
        print(f"Missing required tag '{REQUIRED_TAG}':")
        for address in sorted(failures):
            print(address)
        return 1

    print(f"All resources have the required tag '{REQUIRED_TAG}'.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/cost_tag_check.py <plan.json>")
        sys.exit(2)

    sys.exit(check_plan(sys.argv[1]))
