"""
Module: simple_code.py
Description:
    This module defines a function for printing details about team members and
    their favorite genes. It includes error handling, data validation, and
    reusable helper functions for cleaner code.
"""

import re


def get_value(data, key, default="N/A"):
    """
    Safely retrieves a value from a dictionary.

    Args:
        data (dict): The dictionary containing the data.
        key (str): The key to look up.
        default (str): Value to return if the key is missing.

    Returns:
        str: The corresponding value or default.
    """
    return data.get(key, default)


def validate_url(url):
    """
    Validates whether a given string is a valid URL (basic check).

    Args:
        url (str): The URL string to validate.

    Returns:
        str: The URL if valid, otherwise 'Invalid URL'.
    """
    if not url:
        return "N/A"
    pattern = re.compile(r'^(https?://|www\.)[^\s/$.?#].[^\s]*$')
    return url if re.match(pattern, url) else "Invalid URL"


def print_team_details(team_data):
    """
    Prints details of team members including name, Slack username, country, hobby,
    affiliation, LinkedIn, GitHub, and favorite gene sequence.

    Args:
        team_data (dict): Dictionary of team members and their details.

    Raises:
        ValueError: If the provided team_data is not a dictionary.
    """
    if not isinstance(team_data, dict):
        raise ValueError("Expected a dictionary for team_data.")

    print("Team Members and Their Favorite Genes\n" + "-" * 80)

    for name, details in team_data.items():
        if not isinstance(details, dict):
            print(f"Skipping malformed entry for {name}\n")
            continue

        print(f"Name: {name}")
        print(f"Slack Username: {get_value(details, 'Slack_username')}")
        print(f"Country: {get_value(details, 'Country')}")
        print(f"Hobby: {get_value(details, 'Hobby')}")
        print(f"Affiliation: {get_value(details, 'Affiliation')}")
        print(f"LinkedIn: {validate_url(get_value(details, 'LinkedIN_ID'))}")
        print(f"GitHub: {validate_url(get_value(details, 'Github_ID'))}")
        print(f"Favorite Gene Sequence: {get_value(details, 'Fav_gene_sequence')}\n")


# Actual team Data using a Dict
people = {
    "Chioma Nnadi": {
        "Slack_username": "Chioma",
        "Country": "Nigeria",
        "Hobby": "Writing",
        "Affiliation": "None",
        "Fav_gene": "BRCA1",
        "Fav_gene_ID": "672",
        "Fav_gene_sequence": "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC",
        "LinkedIN_ID": "",
        "Github_ID": ""
    },
    "Kashish Arora": {
        "Slack_username": "Kashish",
        "Country": "India",
        "Hobby": "Reading",
        "Affiliation": "University of Glasgow",
        "Fav_gene": "CDKN1A (p21) promoter",
        "Fav_gene_ID": "1026",
        "Fav_gene_sequence": "GAACATGTCCCAACATGTTG",
        "LinkedIN_ID": "www.linkedin.com/in/kashish-a-a6aa90163",
        "Github_ID": ""
    },
    "Keola Merl Joanes": {
        "Slack_username": "Keola",
        "Country": "India",
        "Hobby": "Reading",
        "Affiliation": "PCCAS",
        "Fav_gene": "HBB gene",
        "Fav_gene_ID": "3043",
        "Fav_gene_sequence": "GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA",
        "LinkedIN_ID": "www.linkedin.com/in/keola-joanes-725b6520a",
        "Github_ID": ""
    },
    "Lavinia Dorothea F Joseph": {
        "Slack_username": "Lavinia",
        "Country": "Antigua & Barbuda",
        "Hobby": "Sudoku",
        "Affiliation": "University Mohammed V, Faculty of Medicine and Pharmacy",
        "Fav_gene": "DHh gene",
        "Fav_gene_ID": "50846",
        "Fav_gene_sequence": "GTTCCAGGTAGTGCCTGAAACTACTTTTCTGAAGAAGTATAATTAAAAGTAATCTTGTTTTGAGAA",
        "LinkedIN_ID": "",
        "Github_ID": ""
    },
    "Atairoro Joshua": {
        "Slack_username": "Atairoro Joshua",
        "Country": "Nigeria",
        "Hobby": "Music",
        "Affiliation": "None",
        "Fav_gene": "BRCA1",
        "Fav_gene_ID": "672",
        "Fav_gene_sequence": "ATGGAAGTTGTCATTTTATAAAGTCAGTAGTTTCTTTGGCAGCAATGCCAGGAAAGGCTCTGAGGAA",
        "LinkedIN_ID": "https://www.linkedin.com/in/atairoro-joshua-88a13424b/",
        "Github_ID": "https://github.com/King-AJr"
    },
    "Bezaleel Akinbami": {
        "Slack_username": "B3z",
        "Country": "Nigeria",
        "Hobby": "Gaming",
        "Affiliation": "none",
        "Fav_gene": "None",
        "Fav_gene_ID": "None",
        "Fav_gene_sequence": "None",
        "LinkedIN_ID": "",
        "Github_ID": ""
    },
    "Sharon Addy": {
        "Slack_username": "Sharon Addy",
        "Country": "Ghana",
        "Hobby": "Repairng damaged electronics",
        "Affiliation": "None",
        "Fav_gene": "MIR1-1",
        "Fav_gene_ID": "406904",
        "Fav_gene_sequence": "UGGAAUGUAAAGAAGUAUGUAU",
        "LinkedIN_ID": "",
        "Github_ID": ""
    }
}

if __name__ == "__main__":
    try:
        print_team_details(people)
    except ValueError as e:
        print(f"Error: {e}")
