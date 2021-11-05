def test():
    input = {
        "sid": "EQ1",
        "client": "310",
        "hash": "GL_JEEQ1310IOM 01000409232021",
        "bukrs": "IOM",
        "rem_id": "GL_JE",
        "timestamp": "20210901123655",
        "valueatrisk": "100000.00",
        "param1": "Company Code:IOM (IOM)",
        "param2": "Document number:100040991",
        "param3": "Posting date:03.05.2021",
        "param4": "User:LLUALHATI (Lou Russell LUALHATI)",
        "param5": "0",
        "param6": "Debit account N°:199100",
        "param7": "Credit account N°:192172",
        "param8": "Amount in USD:100,000.00",
        "param9": "",
        "field1": "CH10,TR10",
        "field2": "PH98",
    }

    expected_result = {
        "system_id": "EQ1",
        "client": "310",
        "alert_id": "GL_JEEQ1310IOM 01000409232021",
        "company_code": "IOM",
        "alert_type": "GL_JE",
        "created_date": "20210901123655",
        "value_at_risk_in_usd": "100000.00",
        "company_code": "IOM (IOM)",
        "document_number": "100040991",
        "posting_date": "03.05.2021",
        "user": "LLUALHATI (Lou Russell LUALHATI)",
        "param5": "0",
        "debit_account_numbers": "199100",
        "credit_account_numbers": "192172",
        "amount_in_txn_currency": "100,000.00",
        "txn_currency": "USD",
        "business_areas_impacted": "CH10,TR10",
        "mission_refkey1": "PH98",
    }

    assert clean_and_format_json(input) == expected_result


def clean_and_format_json(input_json):
    # removeKeysWithEmptyStringsAsValues should remove keys with empty values
    # extractKeyValuePairsInsideParams should extract key, value pairs inside params with a colon separator
    # convertToSnakeCase should convert to lowercase and replace spaces with underscores
    # replaceKeys should replace the keys with the substitutions provided in the YAML mapping file
    # splitCurrencyField should extract the currency and the amount into 2 different fields
    return input_json
