def simulate_battle():
    return 12


_map = {
    "The North": {
        "value": 4,
        "territories": {
            "Castle Black": ["Dreadfort"],
            "Dreadfort": ["Castle Black", "Winterfell", "White Harbor"],
            "Winterfell": ["Bear Island", "Dreadfort", "White Harbor"],
            "Bear Island": ["Winterfell"],
            "White Harbor": ["Greywater Watch", "Winterfell", "Dreadfort"],
            "Greywater Watch": ["White Harbor", "The Twins"],
        }
    },
    "King's Lands": {
        "value": 5,
        "territories": {
            "The Twins": ["Iron Islands", "Greywater Watch", "The Vale", "Riverrun"],
            "The Vale": ["The Twins", "Riverrun", "King's Landing"],
            "Iron Islands": ["The Twins", "Lannisport", "Riverrun"],
            "Riverrun": ["Iron Islands", "The Twins", "The Vale", "Lannisport", "King's Landing"],
            "Lannisport": ["Iron Islands", "Riverrun", "Old Oak", "King's Landing"],
            "King's Landing": ["The Vale", "Riverrun", "Lannisport", "Summerhall", "High Garden"],
        }
    },
    "The South": {
        "value": 4,
        "territories": {
            "Summerhall": ["King's Landing", "High Garden", "Old Oak"],
            "Old Oak": ["Lannisport", "Summerhall", "High Garden"],
            "High Garden": ["King's Landing", "Summerhall", "Old Oak", "Old Town"],
            "Old Town": ["High Garden", "Dorne"],
            "Dorne": ["Old Town", "Tyrosh"],
        }
    },
    "The Free Cities": {
        "value": 5,
        "territories": {
            "Tyrosh": ["Dorne", "Myr"],
            "Myr": ["Tyrosh", "Pentos", "Volantis", "Qohor"],
            "Pentos": ["Myr", "Norvos", "Braavos"],
            "Braavos": ["Pentos", "Norvos"],
            "Norvos": ["Pentos", "Braavos", "Qohor"],
            "Qohor": ["Norvos", "Myr", "Forest of Qohor", "Volantis"],
            "Volantis": ["Myr", "Qohor", "Mantarys"],
        }
    },
    "The Dothraki Sea": {
        "value": 3,
        "territories": {
            "Forest of Qohor": ["Qohor", "Vaes Dothrak"],
            "Vaes Dothrak": ["Forest of Qohor", "Meeren", "Lhazar"],
            "Lhazar": ["Vaes Dothrak", "Meeren"]
        }
    },
    "The Shadow Lands": {
        "value": 4,
        "territories": {
            "Mantarys": ["Volantis", "Elyria"],
            "Elyria": ["Mantarys", "Meeren", "Valyria", "Astapor"],
            "Valyria": ["Elyria", "Astapor"],
            "Astaport": ["Valyria", "Meeren", "Elyria"],
            "Meeren": ["Mantarys", "Astapor", "Vaes Dothrak", "Lhazar"],
        }
    },
}
