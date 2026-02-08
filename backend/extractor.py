import re

def extract_fields(data):
    """
    Extracts all required fields from JSON form or raw ACORD text.
    """
    if isinstance(data, str):
        text = data.lower()

        # Policy Information
        policy_number = re.search(r'policy number[:\s]*([a-z0-9-]+)', text)
        policyholder_name = re.search(r"owner's name and address[:\s]*(.*?)(describe|phone|$)", text, re.DOTALL)
        effective_dates = re.search(r'policy effective dates[:\s]*(.*?)(\n|$)', text)

        # Incident Information
        incident_date = re.search(r'date of loss.*?(\d{1,2}/\d{1,2}/\d{4})', text)
        incident_time = re.search(r'time of loss[:\s]*(\d{1,2}:\d{2}\s*(am|pm)?)', text)
        location = re.search(r'where can damage be seen\?[:\s]*(.*?)(describe|$)', text)
        description = re.search(r'describe damage[:\s]*(.*?)(phone|$)', text, re.DOTALL)

        # Involved Parties
        claimant = policyholder_name.group(1).strip() if policyholder_name else None
        third_parties = re.search(r'other vehicle / property damaged[:\s]*(.*?)(plate|$)', text)
        contact_details = re.findall(r'(phone|email)[:\s]*(.*)', text)

        # Asset Details
        asset_type = re.search(r'type[:\s]*(.*?)(body|$)', text)
        asset_id = re.search(r'vin[:\s]*(.*?)(type|$)', text)
        estimated_damage = re.search(r'estimate amount[:\s]*\$?([\d,]+)', text)

        # Other Mandatory Fields
        claim_type = "vehicle"  # default
        attachments = None
        initial_estimate = int(estimated_damage.group(1).replace(',', '')) if estimated_damage else None

        return {
            "policyNumber": policy_number.group(1) if policy_number else None,
            "policyholderName": policyholder_name.group(1).strip() if policyholder_name else None,
            "effectiveDates": effective_dates.group(1).strip() if effective_dates else None,
            "incidentDate": incident_date.group(1) if incident_date else None,
            "incidentTime": incident_time.group(1) if incident_time else None,
            "location": location.group(1).strip() if location else None,
            "description": description.group(1).strip() if description else "",
            "claimant": claimant,
            "thirdParties": third_parties.group(1).strip() if third_parties else None,
            "contactDetails": contact_details,
            "assetType": asset_type.group(1).strip() if asset_type else None,
            "assetID": asset_id.group(1).strip() if asset_id else None,
            "estimatedDamage": initial_estimate,
            "claimType": claim_type,
            "attachments": attachments,
            "initialEstimate": initial_estimate
        }

    # Fallback: JSON/dict from manual form
    return {
        "policyNumber": data.get("policyNumber"),
        "policyholderName": data.get("policyholderName"),
        "effectiveDates": data.get("effectiveDates"),
        "incidentDate": data.get("incidentDate"),
        "incidentTime": data.get("incidentTime"),
        "location": data.get("location"),
        "description": data.get("description", "").lower(),
        "claimant": data.get("claimant"),
        "thirdParties": data.get("thirdParties"),
        "contactDetails": data.get("contactDetails"),
        "assetType": data.get("assetType"),
        "assetID": data.get("assetID"),
        "estimatedDamage": data.get("estimatedDamage"),
        "claimType": data.get("claimType"),
        "attachments": data.get("attachments"),
        "initialEstimate": data.get("initialEstimate")
    }
