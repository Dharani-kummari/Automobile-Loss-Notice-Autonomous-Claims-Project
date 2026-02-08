
def validate_fields(fields):
    mandatory = [
        "policyNumber",
        "policyholderName",
        "incidentDate",
        "claimType",
        "estimatedDamage"
    ]

    missing = [f for f in mandatory if not fields.get(f)]
    return missing

