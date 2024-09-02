import csv
from collections import defaultdict

def load_company_relations(file_path):
    company_relations = defaultdict(list)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for company_id, name, parent_id in reader:
            if parent_id:
                company_relations[parent_id].append(company_id)
    return company_relations

def load_land_ownership(file_path):
    land_ownership = defaultdict(list)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for land_id, company_id in reader:
            land_ownership[company_id].append(land_id)
    return land_ownership

def get_total_land(company_id, company_relations, land_ownership):
    visited = set()
    total_land = set()

    def dfs(company_id):
        if company_id in visited:
            return
        visited.add(company_id)
        # Add the land directly owned by this company
        if company_id in land_ownership:
            total_land.update(land_ownership[company_id])
        # Recurse for all child companies
        for child_company in company_relations.get(company_id, []):
            dfs(child_company)

    dfs(company_id)
    return len(total_land)

if __name__ == "__main__":
    company_relations = load_company_relations('company_relations.csv')
    land_ownership = load_land_ownership('land_ownership.csv')
    
    company_id = "R764915829891"  # Example company ID
    total_land = get_total_land(company_id, company_relations, land_ownership)
    print(f"Total land owned by company {company_id}: {total_land} parcels")
