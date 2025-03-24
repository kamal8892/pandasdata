import json
from collections import defaultdict

# This is my load json file data code 
with open("locations.json", "r") as location_data_file_paths:
    data_locations = json.load(location_data_file_paths)


# This is my meta data load json file code
with open("metadata.json", "r") as meta_data_files_paths:
    data_metadata = json.load(meta_data_files_paths)


location_dict_data = {loc["id"]: loc for loc in data_locations}


merged_data_list = []
for meta in data_metadata:
    loc_id = meta["id"]
    if loc_id in location_dict_data:
        merged_data_list.append({**location_dict_data[loc_id], **meta})



type_count = defaultdict(int)
rating_sum = defaultdict(float)
rating_count = defaultdict(int)

for data in merged_data_list:
    loc_type = data["type"]
    type_count[loc_type] += 1
    rating_sum[loc_type] += data["rating"]
    rating_count[loc_type] += 1


average_rating_data = {
    t: rating_sum[t] / rating_count[t] for t in rating_sum
}


most_reviewed_location_data = max(merged_data_list, key=lambda x: x["reviews"])


incomplete_data = [data for data in merged_data_list if not all(k in data for k in ["id", "latitude", "longitude", "type", "rating", "reviews"])]


print("Location count per type data:", dict(type_count))
print("Average rating per type data:", average_rating_data)
print("Most reviewed location data:", most_reviewed_location_data)
print("Incomplete data entries data:", incomplete_data)
