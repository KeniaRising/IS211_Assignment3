import argparse
import urllib.request
import csv
import re 
from datetime import datetime   


parser = argparse.ArgumentParser()
parser.add_argument("--url", required =True, help="URL of the web log file")

args = parser.parse_args()

urllib.request.urlretrieve(args.url, "weblog.csv")

print("Web log file downloaded successfully.")

total_requests = 0
images_requested = 0

firefox_count = 0
chrome_count = 0
ie_count = 0
safari_count = 0
hours_counts = {hour: 0 for hour in range(24)} 

image_pattern = re.compile(r".*\.(jpg|jpeg|png|gif)$", re.IGNORECASE)
browser_pattern = re.compile(r"(Firefox|Chrome|MSIE|Safari)", re.IGNORECASE) 

with open("weblog.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        total_requests += 1
        date_time = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        hourscounts[date_time.hour] += 1    
        
        if image_pattern.search(row[0]):
            images_requested += 1

        browser_match = browser_pattern.search(row[2])

        if browser_match:
            browser = browser_match.group(1).lower()

            if browser == "firefox":
                firefox_count += 1
            elif browser == "chrome":
                chrome_count += 1              
            elif browser == "msie":     
                ie_count += 1
            elif browser == "safari":
                safari_count += 1 
  

image_percentage = (images_requested / total_requests) * 100 

print(f"Image requests account for {image_percentage:.1f}% of total requests.")

print("Firefox:", firefox_count)
print("Chrome:", chrome_count)
print("Internet Explorer:", ie_count)
print("Safari:", safari_count)

browser_counts = {
    "Firefox": firefox_count,
    "Chrome": chrome_count,
    "Internet Explorer": ie_count,
    "Safari": safari_count
}   


most_popular_browser = max(browser_counts, key=browser_counts.get)

print(f"Most popular browser: {most_popular_browser}") 
print("\nHits by hour:") 
for hour, count in sorted(hourscounts.items(), key=lambda item:item[1], reverse=True):
    print(f"Hour {hour:02d}: {count} hits")
