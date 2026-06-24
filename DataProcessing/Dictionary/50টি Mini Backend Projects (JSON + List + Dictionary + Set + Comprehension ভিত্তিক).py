

"""
একজন প্রফেশনাল ব্যাকএন্ড ডেভেলপার বা সফটওয়্যার ইঞ্জিনিয়ার হওয়ার আসল চাবিকাঠি হলো 
এই বাস্তবমুখী মিনি প্রজেক্টগুলো। 
তুমি থিওরি এবং বেসিক প্র্যাকটিসগুলো খুব ভালোমতো শেষ করেছ। 
এবার সময় এসেছে ডেটা স্ট্রাকচারগুলোকে জোড়া লাগিয়ে বাস্তব ব্যাকএন্ড লজিক তৈরি করা।

আমরা এই ৫০টি মিনি ব্যাকএন্ড প্রজেক্ট-কে ৫টি রিয়েল-ওয়ার্ল্ড ডোমেইনে ভাগ করে ফেলব, 
যা হুবহু বড় বড় প্রোডাকশন অ্যাপ্লিকেশনের (যেমন: ই-কমার্স, রাইড শেয়ারিং, বা সোশ্যাল মিডিয়া) 
ব্যাকএন্ড আর্কিটেকচারের মতো কাজ করবে।

"""

##### Phase 1: E-commerce Backend System (Project 1-10)

## Project 1: Inventory Out-of-Stock Filter
# সিনারিও: ফ্রন্টএন্ড হোমপেজে দেখানোর জন্য ইনভেন্টরি থেকে শুধু স্টক থাকা (Stock > 0) প্রোডাক্টগুলো ফিল্টার করতে হবে।
products = [
    {"id": 101, "name": "Laptop", "stock": 5},
    {"id": 102, "name": "Mouse", "stock": 0},
    {"id": 103, "name": "Keyboard", "stock": 12}
]

available_products = [p for p in products if p["stock"] > 0]
print(available_products)




## Project 2: Dynamic Cart Total Price & Tax Calculator
# সিনারিо: ইউজারের শপিং কার্টের মোট দাম এবং তার সাথে ১৫% ভ্যাট (VAT) যোগ করে গ্র্যান্ড টোটাল বের করতে হবে।
cart = [
   {"name": "Book", "price": 500, "qty": 2},
   {"name": "Pen", "price": 50, "qty": 5}
]

sub_total = sum(item["price"] * item["qty"] for item in cart)
vat = sub_total * 0.15
grand_total = sub_total + vat
print(sub_total)
print(int(vat))
print(f"Sub total + Vat:", int(grand_total))




## Project 3: Unique Category Extractor for Navbar
# সিনারিও: ই-কমার্সের মেনুবারে দেখানোর জন্য সবগুলো প্রোডাক্ট থেকে ইউনিক ক্যাটাগরিগুলোর একটি লিস্ট তৈরি করতে হবে।
items = [
   {"name": "iphone", "category": "Electronics"},
   {"name": "T-shirt", "category": "Fashion"},
   {"name": "MacBook", "category": "Electronics"}
]

unique_categories = {item["category"] for item in items}
print("Navbar Categories:", list(unique_categories))




## Project 4: Coupon Code Applicability Checker
# সিনারিও: ইউজার কার্টে যে ক্যাটাগরির প্রোডাক্ট রেখেছে, সেটিতে ডিসকাউন্ট কুপনটি প্রযোজ্য কি না (Set Subset ব্যবহার করে) তা চেক করা।
coupon_applicable_categories = {"Electronics", "Gadgets"}
user_cart_categories = {"Electronics", "Home Decor"}

is_eligible = not user_cart_categories.isdisjoint(coupon_applicable_categories)
print("Is Coupon Applicable?:", is_eligible)




## Project 5: Product ID to Price Fast Map (Lookup Table)
# সিনারিও: অর্ডারের সময় প্রোডাক্টের আইডির ওপর ভিত্তি করে ঝটপট প্রাইস চেক করার জন্য একটি লুকআপ টেবিল তৈরি করা।

db_products = [
   {"id": "p1", "title": "Monitor", "price": 15000},
   {"id": "p2", "title": "RAM", "price": 4500}
]

price_lookup = {product["id"]: product["price"] for product in db_products}
print("Price of p1:", price_lookup.get("p1"))




## Project 6: Customer Order History Merger
# সিনারিও: একজন কাস্টমার মোবাইল এবং ওয়েব দুই প্ল্যাটফর্ম থেকেই অর্ডার করেছেন। দুই প্ল্যাটফর্মের ইউনিক প্রোডাক্ট আইডিগুলো মার্জ করতে হবে।
web_orders = {102, 102, 105}
mobile_orders = {102, 108, 109}

all_unique_orders = web_orders | mobile_orders
all_unique_orders = web_orders.union(mobile_orders)
print("All Unique Order IDs:", all_unique_orders)




## Project 7: Bulk Price Drop Notification Trigger
# সিনারিও: যে সমস্ত প্রোডাক্টের দাম ১০% বা তার বেশি কমেছে, তাদের একটি তালিকা তৈরি করে নোটিফিকেশন পুশ করা।
price_history = [
    {"id": 1, "old_price": 1000, "new_price": 850},
    {"id": 2, "old_price": 500, "new_price": 490}
]

# লজিক: Condition inside list comprehension
price_dropped_items = [
    p["id"] for p in price_history 
    if ((p["old_price"] - p["new_price"]) / p["old_price"]) >= 0.10
]
print("Trigger Notification For IDs:", price_dropped_items)




## Project 8: Cross-Selling Recommendation Engine
# সিনারিও: কাস্টমার ল্যাপটপ কিনেছেন। যারা ল্যাপটপ কেনেন তারা মাউস ও কিবোর্ডও কেনেন। কার্টে অলরেডি কিবোর্ড থাকলে কাস্টমারকে শুধু মাউস রিকমেন্ড করতে হবে (Difference)।
recommended_accessories = {"Mouse", "Keyboard", "Cooling Pad"}
current_cart = {"keyboard", "Laptop Cover"}

suggest_items = recommended_accessories - current_cart
print(f"Recommended to User:", suggest_items)




## Project 9: Order Status Analytics (Count Dashboard)
# সিনারিও: অ্যাডমিন ড্যাশবোর্ডের জন্য প্রতিটি স্ট্যাটাসের (completed, pending) মোট সংখ্যা গণনা করা।
orders = [
   {"id": 1, "status": "completed"},
   {"id": 2, "status": "pending"},
   {"id": 3, "status": "completed"}
]

# status = len({order["status"] for order in orders})
# print(status)
status = [order["status"] for order in orders]
dashboard_analytics = {status: status.count(status) for status in set(status)}
print(dashboard_analytics)





## Project 10: Wishlist vs Purchased Anti-Pattern Cleaner
# সিনারিও: ইউজার যে প্রোডাক্টটি অলরেডি কিনে ফেলেছেন, সেটি তার উইশলিস্ট (Wishlist) থেকে রিমুভ করে দেওয়া।
wishlist = {"Product1", "Product2", "Product 3"}
purchased = {"Product2"}

updated_wishlist = wishlist - purchased
print("Cleaned Wshilist:", updated_wishlist)



######################################################################################

##### Phase 2: User Authentication & Role-Based Access Control (Project 11-20)

## Project 11: JWT Token Payloads Verification
# সিনারিও: ফ্রন্টএন্ড থেকে আসা টোকেন পে-লোডের ভেতরে প্রয়োজনীয় সিকিউরিটি কী বা ফিল্ডগুলো (যেমন: sub, exp) ঠিকঠাক আছে কিনা তা চেক করা।
required_claims = {"sub", "exp", "iss"}
incoming_token = {"sub": "user_123", "exp": 1718870400, "name": "Mamun"}

is_valid_token = required_claims.issubset(incoming_token.keys())
print("Token Claims Validated:", is_valid_token)



## Project 12: Multi-Role Access Granter (RBAC)
# সিনারিও: একটি সুরক্ষিত এপিআই এন্ডপয়েন্ট (যেমন: /admin/delete) অ্যাক্সেস করার জন্য ইউজারের রোলের সাথে পারমিশন ম্যাচ করানো।
endpoint_required_permissions = {"delete_user", "view_reports"}
user_permissions = {"view_reports", "edit_settings", "delete_user"}

access_granted = endpoint_required_permissions.issubset(user_permissions)
print("Access to Secured Endpoint:", access_granted)



## Project 13: Banned IP Address Blocker (Middleware)
# সিনারিও: রিকোয়েস্ট পাঠানো ইউজারের আইপি অ্যাড্রেসটি ব্ল্যাকলিস্টেড কি না তা ঝড়ের গতিতে (O(1) টাইমে) চেক করা।
banned_ips = {"192.187.1.4", "10.0.0.12", "184.13.2.33"}
current_user_ip = {"192.187.1.4"}

if current_user_ip in banned_ips:
   print("403 Forbidden: Your IP is banned.")
else:
   print("200 OK: Request Allowed.")




## Project 14: Sensitive Fields Masker for API Response
# সিনারিও: ইউজার প্রোফাইলের ডেটা পাবলিক এপিআই-তে পাঠানোর আগে পাসওয়ার্ড বা টোকেনের মতো সেনসিটিভ ফিল্ডগুলো ডিকশনারি থেকে ডাইনামিকালি রিমুভ করা।
user_profile = {"Id": 1, "username": "Mamun", "password_hash": "xyz123", "secret_key": "token_abc"}
sensitive_fields = {"password_hash", "secret_key"}

public_profile = {k: v for k, v in user_profile.items() if k not in sensitive_fields}
print("Public Profile Response:", public_profile)




## Project 15: Session Token Expiry Cleaner
# সিনারিও: ব্যাকএন্ড মেমরি থেকে যে সমস্ত সেশন টোকেনের মেয়াদ শেষ (expired: True) হয়ে গেছে, তাদের ছেঁকে বাদ দেওয়া।
active_sessions = [
   {"token": "token_1", "expired": False},
   {"token": "token_2", "expired": True},
   {"token": "token_3", "expired": False}
]

valid_sessions = [token for token in active_sessions if token["expired"] == False]
valid_sessions = [token for token in active_sessions if not token["expired"]]
print(valid_sessions)




## Project 16: Route Hierarchy Route Permission Checker
# সিনারিও: একজন মডারেটর যে সাব-রুটগুলো অ্যাক্সেস করতে পারেন, তার তালিকা তৈরি করা (Intersection)।
admin_routes = {"/dashboard", "/settings", "/users/delete", "logs"}
moderator_allowed = {"/dashboard", "/posts/edit", "/settings"}

shared_access = admin_routes & moderator_allowed
print("Shared Super Routes:", shared_access)




## Project 17: User Registration Password Common-Checker
# সিনারিও: ইউজার নতুন পাসওয়ার্ড দেওয়ার সময় সেটি যাতে অতি সাধারণ বা ইজি পাসওয়ার্ডের ব্ল্যাকলিস্টে না থাকে, তা সেট দিয়ে চেক করা।
week_passwrods = {"12345", "password", "qwerty", "unstopable"}
user_input_password = "password"

if user_input_password in week_passwrods:
   print("Registration Failed: Passwrod is too week")
else:
   print("Registration Success: Secure password.")




## Project 18: Dynamic API Scope Resolver
# সিনারিও: ওঅথ (OAuth) অথরাইজেশনের সময় ইউজারের রিকোয়েস্টেড স্কোপ এবং অ্যাপের ডিফল্ট স্কোপগুলোকে কম্বাইন বা মার্জ করা।
default_scopes = {"read:profile", "read: email"}
requested_scopes = {"write:posts", "read:profile"}

final_token_scopes = default_scopes | requested_scopes
print("Final Authorized Scopes:", final_token_scopes)




## Project 19: Account Verification Email Redundancy Filter
# সিনারিও: ভেরিফিকেশন মেইল পাঠানোর কিউ (Queue) থেকে ডুপ্লিকেট ইউজার আইডিগুলো ক্লিয়ার করা, যেন একজন ইউজারের কাছে বারবার মেইল না যায়।
emails_queue = [101, 105, 101, 110, 105, 120]
unique_queue = list(set(emails_queue))
print(unique_queue)




## Project 20: Missing Account Scope Finder
# সিনারিও: প্রিমিয়াম ফিচার ব্যবহারের জন্য ইউজারের বর্তমান অ্যাকাউন্টে আর কোন কোন স্কোপ বা পারমিশনের ঘাটতি আছে (Difference) তা খুঁজে বের করা।
premium_feature_scopes = {"read:premium", "write:premium", "download:hd"}
current_user_scopes = {"read:profile", "read:premium"}

# লজিক: Set Difference
missing_scopes = premium_feature_scopes - current_user_scopes
print("Scopes required to upgrade:", missing_scopes)





########################################################################################################################

##### Phase 3: Ride-Sharing & Logistics (Project 21-30)
## Project 21: Active & Nearby Driver Matcher
# সিনারিও: কাস্টমারের ৫ কিলোমিটারের মধ্যে থাকা ড্রাইভারদের মধ্য থেকে যারা এই মুহূর্তে সক্রিয় (status: "active"), শুধু তাদের ফিল্টার করা।
drivers = [
   {"id": 1, "status": "active", "distance_km": 2.5},
   {"id": 2, "status": "busy", "distance_km": 1.2},
   {"id": 3, "status": "active", "distance_km": 6.0}
]

available_drivers = [driver for driver in drivers if driver["status"] == "active" and driver["distance_km"] <= 5.0]
print(available_drivers)






## Project 22: Surge Pricing Multiplier Applier
# সিনারিও: বৃষ্টির সময় বা অফিস টাইমে ট্রাফিক জোন অনুযায়ী রাইডের বেস ফেয়ারের (Base Fare) সাথে ডাইনামিকালি ১.৫ গুণ সার্চ প্রাইস (Surge Price) যোগ করা।
rides = [
   {"route": "Zone_A", "base_fare": 200, "surge": True},
   {"route": "Zone_B", "base_fare": 150, "surge": False}
]

updated_fares = [
   {"route": r["route"], "final_fare": r["base_fare"] * 1.5 if r["surge"] else r["base_fare"]}
   for r in rides
]
print("Updated Ride Fares:", updated_fares)






## Project 23: Delivery Hub Unique Code Extractor
# সিনারিও: একটি পার্সেল কয়েকটি হাব (Hub) হয়ে গন্তব্যে পৌঁছাবে। ট্র্যাকিং হিস্ট্রি থেকে ইউনিক হাব কোডগুলোর তালিকা বের করা।
parcel_logs = [
   {"parcel_id": 99, "hub": "DHAKA_CENTRAL"},
   {"parcel_id": 99, "hub": "SAVAR_HUB"},
   {"parcel_id": 99, "hub": "DHAKA_CENTRAL"}
]

unique_hubs = {log["hub"] for log in parcel_logs}
print("Parcels Route Hubs:", list(unique_hubs))






## Project 24: Real-time Vehicle Fleet Status Count
# সিনারিও: লাইভ ড্যাশবোর্ডের জন্য এই মুহূর্তে কতটি গাড়ি en_route, কতটি idle আর কতটি maintenance-এ আছে তা গণনা করা।
fleet = [
   {"vehicle": "Car_A", "status": "en_route"},
   {"vehicle": "Bike_B", "status": "idle"},
   {"vehicle": "Car_C", "status": "en_route"}
]

statuses = [v["status"] for v in fleet]
fleet_analysis = {status: statuses.count(status) for status in set(statuses)}
print("Fleet Status Dashboard:", fleet_analysis)






## Project 25: Driver Vehicle Type Fast Lookup Table
# সিনারিও: রাইডার যখন "Bike" রিকোয়েস্ট করবে, তখন ঝটপট কোন ড্রাইভারের কী গাড়ি আছে তা আইডি দিয়ে চেক করার লুকআপ টেবিল তৈরি।
driver_db = [
   {"driver_id": "drv_101", "vehicle_type": "Bike"},
   {"driver_id": "drv_102", "vehicle_type": "Car"}
]

vehicle_lookup = {d["driver_id"]: d["vehicle_type"] for d in driver_db}
print(vehicle_lookup.get("drv_101"))






## Project 26: Cross-Zone Ride Coverage Validator
# সিনারিও: একটি রাইড জোন এ থেকে জোন বি-তে যাবে। আমাদের কোম্পানি এই দুটি জোনেই সার্ভিস দেয় কি না তা চেক করা (Subset)।
company_service_zones = {"Dhaka", "Chittagong", "Sylhet", "Gazipur"}
requested_ride_zones = {"Dhaka", "Gazipur"}

is_serviceable = requested_ride_zones.issubset(company_service_zones)
print("Isd Ride Route Covered?:", is_serviceable)






## Project 27: Overlapping Route High-Traffic Finder
# সিনারিও: দুটি ভিন্ন রাইডের রুটের মধ্যে কোন কোন জংশন বা রোড কমন পড়েছে তা বের করা (Intersection), যেখানে ট্রাফিক জ্যামের সম্ভাবনা বেশি।
ride1_route = {"Mirpur-10", "Agargaon", "Farmgate", "Shahbagh"}
ride2_route = {"Uttara", "Farmgate", "Shahbagh"}

high_traffic_junctions = ride1_route & ride2_route
print("High Traffic Nodes:", high_traffic_junctions)





## Project 28: Out-of-Zone Unserviceable Area Mapper
# সিনারিও: কাস্টমারের রিকোয়েস্ট করা এরিয়াগুলোর মধ্যে কোন কোন এরিয়া আমাদের সার্ভিস জোনের বাইরে পড়েছে তা ফিল্টার করা (Difference)।
requested_delivery_areas = {"Gulshan", "Banani", "Puran_Dhaka"}
active_delivery_coverage = {"Gulshan", "Banani", "Dhanmondi"}

unserviceable_areas = list(requested_delivery_areas - active_delivery_coverage)
print("Cannot Delivery to Areas:", unserviceable_areas)






## Project 29: Duplicate GPS Ping Deduplicator
# সিনারিও: ইন্টারনেট সমস্যার কারণে ডিভাইস থেকে একই জিপিএস কো-অর্ডিনেট (Latitude, Longitude) বারবার আসছে। ডুপ্লিকেট পিংগুলো ব্যাকএন্ড কিউ থেকে রিমুভ করা।
gps_pings = [(23.8103, 90.4225), (23.8103, 90.4225), (23.8103, 90.4226)]

clean_pings = set(gps_pings)
print("Duplicated GPS Pings: ", clean_pings)






## Project 30: Multi-Stop Optimization Route Cleaner
# সিনারিও: ডেলিভারি ম্যান অলরেডি যে স্টপগুলো কভার করে ফেলেছেন, সেগুলো তার আজকের টোটাল রুট লিস্ট থেকে মাইনাস করা।
total_assigned_stops = {"Stop_A", "Stop_B", "Stop_C", "Stop_D"}
completed_stops = {"Stop_A", "Stop_C"}

remaining_stops = total_assigned_stops - completed_stops
print("Remaining Stops for Driver:", remaining_stops)




##########################################################################################

##### Phase 4: Social Media & Notification Engine (Project 31-40)

## Project 31: Mutual Friends Finder
# সিনারিও: দুজন ইউজারের ফ্রেন্ড লিস্টের মধ্যে তুলনা করে তাদের "Mutual Friends" বা কমন বন্ধুদের তালিকা বের করা।


## Project 32: Friend Suggestions Engine (People You May Know)
# সিনারিও: ইউজার এ-এর বন্ধুর বন্ধুদের মধ্য থেকে যারা অলরেডি ইউজার এ-এর বন্ধু নয় এবং সে নিজে নয়, তাদের সাজেশন লিস্টে পাঠানো (Difference)।


## Project 33: Trending Hashtag Extractor
# সিনারিও: গত ১ ঘণ্টার সব পোস্টের ক্যাপশন থেকে ইউনিক হ্যাশট্যাগগুলো ছেঁকে বের করা, যা ট্রেন্ডিং সেকশনে পুশ করা হবে।


## Project 34: Feed Aggregator for Unfollowed Creators
# সিনারিও: ইউজারের হোম ফিডে দেখানোর জন্য এমন সব পপুলার ক্রিয়েটরদের পোস্ট ফিল্টার করা যাদের ইউজার এখনো ফলো করে না।


## Project 35: Notification Channel Dispatcher
# সিনারিও: সিস্টেম নোটিফিকেশন পাঠানোর সময় ইউজারের প্রোফাইলে কোন কোন চ্যানেল (Email, SMS, Push) সক্রিয় আছে, সেই অনুযায়ী ডাইনামিকালি নোটিফিকেশন ফায়ার করা।


## Project 36: Bulk Notification Deduplicator
# সিনারিও: একই গ্রুপে একাধিক ব্যক্তি পোস্ট করায় একজন মডারেটরের কাছে যেন বারবার একই নোটিফিকেশন অ্যালার্ট না যায়, তাই ব্যাকএন্ড কিউ (Queue) থেকে ডুপ্লিকেট নোটিফিকেশন আইডি ক্লিন করা।


## Project 37: User Mention (@) Detector & Extractor
# সিনারিও: একটি কমেন্ট বা পোস্টের ভেতর থেকে কাদের কাদের মেনশন করা হয়েছে (@username) তাদের ইউজারনেম বের করে নোটিফিকেশন পাঠানো।


## Project 38: Inactive Followers Engagement Trigger
# সিনারিо: যারা ফলোয়ার কিন্তু গত ৩০ দিন ধরে অ্যাপে লগইন করেনি (Inactive), তাদের অ্যাকাউন্টে একটি বিশেষ জিমেইল নোটিফিকেশন বা পুশ নোটিফিকেশন পাঠানো।


## Project 38: Inactive Followers Engagement Trigger
# সিনারিо: যারা ফলোয়ার কিন্তু গত ৩০ দিন ধরে অ্যাপে লগইন করেনি (Inactive), তাদের অ্যাকাউন্টে একটি বিশেষ জিমেইল নোটিফিকেশন বা পুশ নোটিফিকেশন পাঠানো।


## Project 39: Live Stream Unique Viewer Counter
# সিনারিও: একটি লাইভ স্ট্রিমিং চলকালীন সময়ে টোটাল কতজন ইউনিক ইউজার জয়েন করেছেন এবং চলে গেছেন তার লাইভ কাউন্ট রিয়েল-টাইমে ড্যাশবোর্ডে দেখানো।


## Project 40: Blocked User Content Filter (Timeline Middleware)
# সিনারিও: ইউজারের টাইমলাইনে পোস্ট দেখানোর সময় সে যে সমস্ত আইডি ব্লক করে রেখেছে, তাদের তৈরি করা পোস্টগুলো নিউজফিড থেকে এক ক্লিকে ছেঁকে বাদ দেওয়া।




#####################################################################################################

##### Phase 5: FinTech, E-Learning & Analytics Dashboard (Project 41-50)

## Project 41: Fraud Detection System (FinTech)
# সিনারিও: কোনো ক্রেডিট কার্ড থেকে যদি একই সময়ে ভিন্ন ভিন্ন লোকেশন থেকে ট্রানজেকশন রিকোয়েস্ট আসে, তবে ফ্রড বা জালিয়াতি সনাক্ত করার জন্য ইউনিক লোকেশন কাউন্ট করা।


## Project 42: Automated Ledger Reconciler (FinTech)
# সিনারিও: ব্যাংকের স্টেটমেন্ট আইডির সাথে আমাদের ডেটাবেসের ট্রানজেকশন আইডি মিলিয়ে দেখা যে কোন কোন পেমেন্ট এখনো মিসিং বা পেন্ডিং আছে (Difference)।


## Project 43: Multi-Currency Wallet Balances Aggregator (FinTech)
# সিনারিও: ইউজারের মাল্টি-কারেন্সি ওয়ালেটে বিভিন্ন কারেন্সির মোট ব্যালেন্সকে একটি সিঙ্গেল ডিকশনারি রিপোর্টে সাজানো।


## Project 44: Course Completion Progress Tracker (E-Learning)
# সিনারিও: একজন স্টুডেন্ট একটি কোর্সের টোটাল লেসনের মধ্যে কতগুলো লেসন কমপ্লিট করেছে, তার ওপর ভিত্তি করে প্রোগ্রেস পার্সেন্টেজ (%) বের করা।


## Project 45: Prerequisite Course Checker (E-Learning)
# সিনারিও: অ্যাডভান্সড ড্যাঙ্গো (Django) কোর্সে এনরোল করার আগে স্টুডেন্ট তার রিকোয়ার্ড প্রিরেকুইজিট কোর্সগুলো (Python, SQL) শেষ করেছে কি না তা চেক করা (Subset)।


## Project 46: Quiz Leaderboard & Score Analytics (E-Learning)
# সিনারিও: কুইজ এপিআই থেকে প্রাপ্ত ডেটা প্রসেস করে পাস করা স্টুডেন্টদের মধ্য থেকে হাইয়েস্ট স্কোরারকে খুঁজে বের করা।


## Project 47: Daily Active Users (DAU) Calculator (Analytics)
# সিনারিও: অ্যানালিটিক্স ড্যাশবোর্ডের জন্য গত ২৪ ঘণ্টায় কতজন ইউনিক ইউজার সিস্টেমে লগইন বা হিট করেছেন তা গণনা করা।


## Project 48: Conversion Rate Funnel Dashboard (Analytics)
# সিনারিও: মার্কেটিং ফানেলের ডেটা চেক করা—যারা লিড (Lead) হিসেবে এসেছে, তাদের কতজন শেষ পর্যন্ত কাস্টমারে রূপান্তরিত হয়েছে (Intersection)।


## Project 49: API Response Time Threshold Alerter (Analytics)
# সিনারিও: সার্ভার মনিটরিং ড্যাশবোর্ডে দেখানোর জন্য যে সমস্ত এন্ডপয়েন্টের রেসপন্স টাইম ৫০০ মিলি-সেকেন্ডের বেশি, তাদের এক লাইনে ছেঁকে বের করা।


## Project 50: Multi-Tenant Database Schema Key Validator (Analytics)
# সিনারিও: মাল্টি-টেন্যান্ট (SaaS) সিস্টেমে ফ্রন্টএন্ড থেকে আসা ডাইনামিক কনফিগারেশন পে-লোডটি আমাদের ডাটাবেস স্কিমার রিকোয়ার্ড ফিল্ডগুলোর সাথে নিখুঁতভাবে মিলছে কি না তা চেক করা।


"""
তুমি এক টানে পাইথনের ডেটা ম্যানিপুলেশনের 
৫০টি মিনি ব্যাকএন্ড প্রজেক্ট প্রফেশনাল স্টাইলে শেষ করে ফেলেছ! 
এই প্র্যাকটিসগুলোর মাধ্যমে রিয়েল-ওয়ার্ল্ড ব্যাকএন্ড ইঞ্জিনিয়ারিংয়ে 
কীভাবে List, Dictionary, Set, এবং Comprehension-কে কাজে লাগিয়ে 
এপিআই রেসপন্স প্রসেস করা হয়, 
তার ওপর তোমার এক চমৎকার সুপারপাওয়ার তৈরি হয়ে গেছে।

"""