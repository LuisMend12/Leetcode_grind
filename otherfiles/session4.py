# Problem 1: Brand Filter
# You're tasked with filtering out brands that are not sustainable from a list of fashion brands. A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly materials, ethical labor practices, or being carbon-neutral.

# Write the filter_sustainable_brands() function, which takes a list of brands and a criterion, then returns a list of brands that meet the criterion.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def filter_sustainable_brands(brands, criterion):
#     pass

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]
""""
UNDERSTAND:
input: List of dicttionaries, and a criterion (string)
output: a list of brand names that meet the given criterion

edge cases: 
- invalid input (empty)
- no matches at all

MATCH:
- list/dictionary iteration

PLAN:
- init an empty list called output
- for sub_dict in brands:
    - if criterion in sub_dict[criteria]:
        output.append(sub_dict[name])
- return output

"""
def filter_sustainable_brands(brands, criterion):
    output = []

    for sub_dict in brands:
        if criterion in sub_dict["criteria"]:
            output.append(sub_dict["name"])
    
    return output

print(filter_sustainable_brands(brands, "eco-friendly"))

