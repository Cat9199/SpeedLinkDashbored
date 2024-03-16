
import requests
def asyncsys(awb):
    reqUrl = f"https://vsoftapi.com-eg.net/api/ClientUsers/V6/GetShipmentDetails/{awb}"

    headersList = {
        "CompanyID": "191307",
        "AccessToken": "0953BF41-4215-46DB-9E80-C5497AFC6B6F",
        "Language": "en"
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload, headers=headersList)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if any shipment has "StatusName" as "Shipment Delivered" and "Reason" as "Collected"
        for shipment in data["shipmentInfo"]:
            status_name = shipment.get("StatusName")
            reason = shipment.get("Reason").strip()  # Remove leading/trailing whitespace

            if status_name == "Shipment Delivered" and reason == "Collected":
                return "ok"
            
            # Check for the additional condition "Returned To Shipper" with reason "لغى الاوردر"
            elif status_name == "Returned To Shipper":
                return "e1"
    
    # If the criteria are not met or there is an issue with the request, return "no"
    return "no"
