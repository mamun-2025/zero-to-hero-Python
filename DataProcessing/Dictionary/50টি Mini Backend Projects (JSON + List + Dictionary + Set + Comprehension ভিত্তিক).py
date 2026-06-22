

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


