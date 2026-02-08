def route_claim(fields, missing_fields):
    description = fields.get("description", "").lower()

    if missing_fields:
        return "Manual Review", "Mandatory fields are missing"

    if any(word in description for word in ["fraud", "staged", "inconsistent"]):
        return "Investigation Flag", "Fraud-related keywords detected"

    if fields.get("claimType") == "injury":
        return "Specialist Queue", "Injury-related claim"

    if fields.get("estimatedDamage", 0) < 25000:
        return "Fast-track", "Low estimated damage"

    return "Manual Review", "Default routing applied"
