# Encoding: utf8
# Copyright 2010 Amaç Herdağdelen

from name_gender import NameGender
from web_name_gender import WebNameGender

# Given a guesser and a name, returns the probability that the person is male or female
# A score of -1 means no one in the dataset has this name)
def get_decision(guesser, name):
    m, f = guesser.get_gender_scores(name)
    return [m, f]

# Whole module is case-insensitive.
boys = ["Bob", "Paul", "Ben", "Mary"]
girls = ["Katie", "Teri", "Ann"]
unknown1 = ["Jordan", "Taylor", "Blaire", "Chuck"]
unknown2 = ["Lawrence", "Kelly", "Tracy", "Justice", "Jessie"]

# Give precedence to us_census data.
primary_guesser = NameGender("us_census_1990_males", "us_census_1990_females")
secondary_guesser = NameGender("popular_1960_2010_males","popular_1960_2010_females")

# Given a list of names, calculate the probability that each name is either female or male
# Returns a list of tuples (by order of names given) with the first entry in the tuple being the score of the male, second of female
# Two tuples for each person, one from the primary guesser and one from the secondary
def get_scores(names):
    p = []
    for line in names:
        name = line.strip().lower()
        p.append(get_decision(primary_guesser, name))
        p.append(get_decision(secondary_guesser, name))
    return p

# A group of names is either entirely male or female
# Determine the most likely gender of the group of names
# This is the function that you will be working with
#def group_gender(names):
    
