import requests

url = "https://endoflife.date/api/v1/products/android/"

def get_min_supported_android_version():
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data from the API.")
        return

    data = response.json()

    supported_versions = []
    for entry in data["result"]["releases"]:
        iseol = entry["isEol"]
        ismaintained = entry["isMaintained"]

        if iseol == False and ismaintained == True :
            supported_versions.append(entry)

    if not supported_versions:
        print("No supported Android versions found")
        return

    # Find the minimum version among supported ones
    min_supported = min(supported_versions, key=lambda x: float(x["name"]))

    print(f"Minimum supported Android version: {min_supported['name']} {min_supported['codename']}")

get_min_supported_android_version()
