"""
A client wants to analyze their ads to determine the effectiveness of their campaigns. You are given three datasets:

Ad Click Logs
Each entry contains:

IP address of the user who clicked the ad.
Timestamp of the click.
Ad text.
ad_clicks = [
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens"
]

User Purchase Data
A list of user IDs corresponding to users who completed a purchase.

completed_purchase_user_ids = [
    "3123122444",
    "234111110",
    "8321125440",
    "99911063"
]

User IP Address Mapping
A list of user IDs mapped to their corresponding IP addresses.

all_user_ips = [
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]

"""

from collections import defaultdict

ad_clicks = [
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens"
]

completed_purchase_user_ids = [
    "3123122444",
    "234111110",
    "8321125440",
    "99911063"
]

all_user_ips = [
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]


def ad_conversion_rate(ad_clicks, completed_purchase_user_ids, all_user_ips):
    ad_clicks_dict = defaultdict(list)
    for clicks in ad_clicks:
        items = clicks.split(",")
        ip_address, click_time, ad_text = items[0], items[1], items[2]
        ad_clicks_dict[ad_text].append(ip_address)

    all_user_ips_dict = defaultdict(list)
    for items in all_user_ips:
        user_id, ip_address = items.split(",")
        all_user_ips_dict[user_id].append(ip_address)

    purchased_ip_addresses = []
    for user in completed_purchase_user_ids:
        if user in all_user_ips_dict:
            purchased_ip_addresses.append(all_user_ips_dict[user])

    final_output = {}

    for ip_ad in purchased_ip_addresses:
        for key, val in ad_clicks_dict.items():
            if ip_ad[0] in val:
                if key not in final_output:
                    final_output[key] = (1, len(val))
                else:
                    count = final_output[key]
                    final_output[key] = (count[0] + 1, count[1])
            else:
                final_output[key] = (0, len(val))

    return final_output

print(ad_conversion_rate(ad_clicks,completed_purchase_user_ids,all_user_ips))